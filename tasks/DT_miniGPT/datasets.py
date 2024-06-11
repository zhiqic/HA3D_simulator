'''
Author: Dylan Li dylan.h.li@outlook.com
Date: 2024-03-17 21:42:00
LastEditors: Dylan Li dylan.h.li@outlook.com
LastEditTime: 2024-03-30 22:46:08
FilePath: /HA3D_simulator/tasks/HA/datasets.py
Description: 

Copyright (c) 2024 by Heng Li, All Rights Reserved. 
'''
import torch
from multiprocessing import Process
import os
import numpy as np
from tqdm import tqdm
from env import HABatch
from agent import RandomAgent, TeacherAgent
import pickle
from transformers import BartTokenizer, BartModel
import sys

from dataclasses import dataclass

@dataclass
class Config:
    # Dataset Path and Name
    HA3D_SIMULATOR_PATH = os.environ.get("HA3D_SIMULATOR_PATH")
    TRAJS_DIR = os.path.join(HA3D_SIMULATOR_PATH, 'tasks/DT_miniGPT/trajs')
    IMAGENET_FEATURES = 'img_features/ResNet-152-imagenet_80_16_mean.tsv'
    features = IMAGENET_FEATURES
    batch_size = 100
    name = 'right_left_mix_teacher' #LINK - should work wit param.py
    
    # Dataset Size 
    max_eposide_length = 30

def setup():
    torch.manual_seed(1)    
    torch.cuda.manual_seed(1)

def train_random(dataset_cfg, train_env, n_iters, log_every=100, val_envs={}):
    """
    Trains a random agent on a given environment for a specified number of iterations.
    
    This function simulates training by having a random agent perform actions within the environment. It is primarily used for baseline comparisons and does not involve any learning or optimization. The function collects trajectories generated by the agent's interactions with the environment.
    
    Parameters:
    - train_env: The training environment where the agent will perform actions.
    - n_iters: The number of iterations to simulate. Each iteration corresponds to a complete trajectory of agent-environment interaction.
    - log_every: The frequency (in iterations) at which to log progress. Default is 100.
    - val_envs: A dictionary of validation environments for evaluating the agent. Default is an empty dictionary. This parameter is not used in the function but included for interface consistency.
    
    Returns:
    - trajs: A list of trajectories. Each trajectory is a list of dictionaries, where each dictionary represents the state of the environment and the agent's action at each step of the interaction.
    """
    
    agent = RandomAgent(train_env, "")
    max_steps = dataset_cfg.max_eposide_length
    print('Random Agent Begins')
    trajs = []

    for _ in tqdm(range(0, n_iters)):
        
        # traj is a list of dictionaries, each of which is a episode, we have a batch of episodes
        traj = agent.rollout(max_steps)
        trajs.extend(traj)
    
    return trajs 

def train_teacher(dataset_cfg, train_env, n_iters, log_every=100, val_envs={}):
    """
    Trains an agent using the teacher forcing method on a given training environment for a specified number of iterations.
    
    This function simulates training by having an agent (initialized as a RandomAgent for simplicity, but typically would be a learning agent) perform actions within the environment based on the teacher forcing strategy. The primary purpose is to generate trajectories that can be used for further analysis or training. The function collects these trajectories by executing the agent's rollout method, which simulates an entire episode of interaction with the environment.
    
    Parameters:
    - train_env: The training environment where the agent will perform actions. This environment should be capable of resetting and providing observations and rewards based on the agent's actions.
    - n_iters: The number of iterations to simulate. Each iteration corresponds to a complete trajectory of agent-environment interaction.
    - log_every: The frequency (in iterations) at which to log progress. Default is 100. This parameter is currently not used but included for future enhancements and consistency with other training functions.
    - val_envs: A dictionary of validation environments for evaluating the agent. Default is an empty dictionary. This parameter is not used in this function but included for interface consistency with other training functions.
    
    Returns:
    - trajs: A list of trajectories. Each trajectory is a list of dictionaries, where each dictionary represents the state of the environment and the agent's action at each step of the interaction. This data structure is useful for analyzing the agent's behavior and for training on the generated data.
    """
    train_env._set_action_level('LLA')
    agent = TeacherAgent(train_env, "")
    max_steps = dataset_cfg.max_eposide_length
    
    print('Teacher Agent (Avoiding human) Begins')
    trajs = []

    for _ in tqdm(range(0, n_iters)):
        # traj is a list of dictionaries, each of which is a episode, we have a batch of episodes

        traj = agent.rollout(max_steps)
        trajs.extend(traj)
    
    train_env._set_action_level('LLA-NA')
    agent = TeacherAgent(train_env, "")
    print('Teacher Agent (shortest path) Begins')
    for _ in tqdm(range(0, n_iters)):
        traj = agent.rollout(max_steps)
        trajs.extend(traj)
    
    return trajs

def train_run(dataset_cfg, agent='random', gpu_id=0, n_iters=0):
    """
    Trains an agent on the training set and saves the generated trajectories.

    This function sets up the training environment, initializes the tokenizer and embedding model, and iterates through the specified number of training iterations. For each iteration, it creates a new training environment, trains the agent (either a random or a teacher agent), and saves the generated trajectories to disk.

    Parameters:
    - iters (int): The number of training iterations to perform.
    - agent (str): The type of agent to train. Can be 'random' or 'teacher'. Default is 'random'.
    - gpu_id (int): The ID of the GPU to use for training. Default is 0.

    Returns:
    None
    """
    trajs_dir = os.path.join(dataset_cfg.TRAJS_DIR)
    if not os.path.exists(trajs_dir):
        os.makedirs(trajs_dir)
    setup()
    device = f'cuda:{gpu_id}' if torch.cuda.is_available() else 'cpu'
    
    tok = BartTokenizer.from_pretrained('facebook/bart-base')
    embedding_model = BartModel.from_pretrained('facebook/bart-base')
    train_env = HABatch(dataset_cfg.features, batch_size=dataset_cfg.batch_size, splits=['train'], tokenizer=tok, text_embedding_model=embedding_model, device=device)
    if agent == 'random':
        trajs = train_random(dataset_cfg, train_env, n_iters)
    elif agent == 'teacher':
        trajs = train_teacher(dataset_cfg, train_env, n_iters)
    with open(os.path.join(trajs_dir, f'train_trajs_{agent}_{dataset_cfg.name}.pkl'), 'wb') as f:
        pickle.dump(trajs, f)

    val_seen_env = HABatch(dataset_cfg.features, batch_size=dataset_cfg.batch_size, splits=['val_seen'], tokenizer=tok, text_embedding_model=embedding_model, device=device)
    if agent == 'random':
        trajs = train_random(dataset_cfg, val_seen_env, int(n_iters*0.3))
    elif agent == 'teacher':
        trajs = train_teacher(dataset_cfg, val_seen_env, int(n_iters*0.3))
    with open(os.path.join(trajs_dir, f'val_seen_trajs_{agent}_{dataset_cfg.name}.pkl'), 'wb') as f:
        pickle.dump(trajs, f)

    val_unseen_env = HABatch(dataset_cfg.features, batch_size=dataset_cfg.batch_size, splits=['val_unseen'], tokenizer=tok, text_embedding_model=embedding_model, device=device)
    if agent == 'random':
        trajs = train_random(dataset_cfg, val_unseen_env, int(n_iters*0.3))
    elif agent == 'teacher':
        trajs = train_teacher(dataset_cfg, val_unseen_env, int(n_iters*0.3))
    with open(os.path.join(trajs_dir, f'val_unseen_trajs_{agent}_{dataset_cfg.name}.pkl'), 'wb') as f:
        pickle.dump(trajs, f)
        
def train_run_quick_test(dataset_cfg, agent='random', gpu_id=0, n_iters=0):
    """
    Trains an agent on the training set and saves the generated trajectories.

    This function sets up the training environment, initializes the tokenizer and embedding model, and iterates through the specified number of training iterations. For each iteration, it creates a new training environment, trains the agent (either a random or a teacher agent), and saves the generated trajectories to disk.

    Parameters:
    - iters (int): The number of training iterations to perform.
    - agent (str): The type of agent to train. Can be 'random' or 'teacher'. Default is 'random'.
    - gpu_id (int): The ID of the GPU to use for training. Default is 0.

    Returns:
    None
    """
    print("debug test")
    trajs_dir = os.path.join(dataset_cfg.TRAJS_DIR)
    if not os.path.exists(trajs_dir):
        os.makedirs(trajs_dir)
    setup()
    device = f'cuda:{gpu_id}' if torch.cuda.is_available() else 'cpu'
    
    tok = BartTokenizer.from_pretrained('facebook/bart-base')
    embedding_model = BartModel.from_pretrained('facebook/bart-base')

    val_seen_env = HABatch(dataset_cfg.features, batch_size=dataset_cfg.batch_size, splits=['val_seen'], tokenizer=tok, text_embedding_model=embedding_model, device=device)
    if agent == 'random':
        trajs = train_random(dataset_cfg, val_seen_env, int(n_iters/14))
    elif agent == 'teacher':
        trajs = train_teacher(dataset_cfg, val_seen_env, int(n_iters/14))
    """         
    with open(os.path.join(trajs_dir, f'val_seen_trajs_{agent}_{dataset_cfg.name}.pkl'), 'wb') as f:
        pickle.dump(trajs, f) 
    """

    

if __name__ == '__main__':
    dataset_cfg = Config()
    # Main entry point for the script. Initializes and starts the training process for the specified agents in parallel.

    if not os.path.exists(dataset_cfg.TRAJS_DIR):
        os.makedirs(dataset_cfg.TRAJS_DIR)
    agents = {'random':450, 'teacher':150}
    processes = []
    for i, agent in enumerate(agents.items()):
        p = Process(target=train_run, args=(dataset_cfg, agent[0], i%3, agent[1]))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
 
    # NOTE: for now we only process teacher agent with single processor for debugging
    #train_run_quick_test(dataset_cfg, agent='teacher', gpu_id=1, n_iters=14)
        
    