import os
import pickle
import numpy as np
from src.render.renderer import get_renderer
import argparse
os.environ['PYOPENGL_PLATFORM'] = 'egl'


def sendMessage(pipe_R2S, message):
    with open(pipe_R2S, 'wb') as pipe_r2s:
        data = {
            'message': message
        }
        serialized_data = pickle.dumps(data)
        pipe_r2s.write(serialized_data)

def main(args):
    pipe_S2R = f'./pipe/my_S2R_pipe{args.pipeID}'
    pipe_R2S = f'./pipe/my_R2S_pipe{args.pipeID}'
    # 检查管道文件是否存在，如果不存在，则创建
    if not os.path.exists(pipe_S2R):
        os.mkfifo(pipe_S2R)
        print(f'Created pipe: {pipe_S2R}')

    if not os.path.exists(pipe_R2S):
        os.mkfifo(pipe_R2S)
        print(f'Created pipe: {pipe_R2S}')

    with open(pipe_S2R, 'rb') as pipe_s2r:
        while True:
            # 读取序列化的数据
            serialized_data = pipe_s2r.read()
            # 如果读取到数据，反序列化
            if serialized_data:
                data = pickle.loads(serialized_data)
                function = data['function']
                if function == 'create renderer':
                    WIDTH = data['WIDTH']
                    HEIGHT = data['HEIGHT']
                    renderer = get_renderer(WIDTH, HEIGHT)
                    message = f"SUCCESS {function}: WIDTH:{WIDTH}, HEIGHT:{HEIGHT}."
                    print(message)
                    sendMessage(pipe_R2S,message)
                elif function == 'set human':
                    human_list = data['human_list']
                    renderer.newHumans(human_list)
                    message = f"SUCCESS {function}: {len(human_list)} humans of Scan {data['scanID']}."
                    print(message)
                    sendMessage(pipe_R2S,message)
                elif function == 'set agent':
                    VFOV = data['VFOV']
                    location = data['location']
                    heading = data['heading']
                    elevation = data['elevation']
                    renderer.newAgent(VFOV, location, heading, elevation)
                    message = f"SUCCESS {function}: VFOV:{VFOV}, \
                            location:({location[0]},{location[1]},{location[2]}),\
                            heading:{heading},\
                            elevation,{elevation}"
                    print(message)
                    sendMessage(pipe_R2S,message)
                elif function == 'move agent':
                    VFOV = data['VFOV']
                    location = data['location']
                    heading = data['heading']
                    elevation = data['elevation']
                    renderer.moveAgent(VFOV, location, heading, elevation)
                    message = f"SUCCESS {function}: VFOV:{VFOV}, \
                            location:({location[0]},{location[1]},{location[2]}),\
                            heading:{heading},\
                            elevation,{elevation}"
                    print(message)
                    sendMessage(pipe_R2S,message)               
                elif function == 'rendering scene':
                    background = data['background']
                    background_depth = data['background_depth']
                    message = f"SUCCESS {function}: {np.sum(background)},{background.shape}"
                    print(message)
                    sendMessage(pipe_R2S,message)
                elif function == 'get state':
                    frame_num = data['frame_num']
                    rgb,_ = renderer.render_agent(frame_num, background, background_depth)
                    message = f"SUCCESS {function}: frame_num {frame_num}"
                    #print(message)
                    #sendMessage(pipe_R2S,message) 
                    with open(pipe_R2S, 'wb') as pipe_r2s:
                        data = {
                            'function': 'get state',
                            'frame_num': frame_num,
                            'rgb': rgb
                        }
                        serialized_data = pickle.dumps(data)
                        pipe_r2s.write(serialized_data)
                elif function == 'get human state':
                    frame_num = data['frame_num']
                    human_loc = renderer.getHumanLocation(frame_num)
                    message = f"SUCCESS {function}: frame_num {frame_num}"
                    with open(pipe_R2S, 'wb') as pipe_r2s:
                        data = {
                            'function': 'get human state',
                            'frame_num': frame_num,
                            'human_state': human_loc
                        }
                        serialized_data = pickle.dumps(data)
                        pipe_r2s.write(serialized_data)   
                else:
                    print(data)
    print("Render Process Message: FINISH")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--pipeID', type=int, required=True, help='ID for the pipe to be created')
    args = parser.parse_args()
    main(args)