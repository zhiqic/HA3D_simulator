import json
import os
import math

# 判断viewpoint是否能看见人物，若能则返回人物信息
# Parameters：
## basic_data_dir :基础目录路径（人物信息所在目录）
## scan_id :viewpoint所在建筑scan ID
## agent_view_id :viewpoint ID
# Return:
## human_heading 人物朝向 弧度
## human_loc 人物坐标[x,y,z]
## motion_path 人物动作的3D网格数据的路径
def get_human_info(basic_data_dir, scan_id, agent_view_id):
    motion_dir = os.path.join(basic_data_dir,"human_motion_meshes")
        # 一共90个建筑场景数据
    with open('human_motion_text.json', 'r') as f:
        human_view_data = json.load(f)
            # 获取建筑场景所有视点信息（视点之间的关系）
    with open('con/pos_info/{}_pos_info.json'.format(scan_id), 'r') as f:
        pos_data = json.load(f)
        #print(len(pos_data))
    with open('con/con_info/{}_con_info.json'.format(scan_id), 'r') as f:
        connection_data = json.load(f)

    human_heading = None
    human_loc = None
    motion_path = None
    for human_view_id in human_view_data[scan_id]:
        # 人物视点编号
        human_motion = human_view_data[scan_id][human_view_id][0]
        human_model_id = human_view_data[scan_id][human_view_id][1]
        try:
            if human_view_id == agent_view_id:
                connection_data[agent_view_id]["visible"].append(agent_view_id)
                #print(f"human_view_id:{agent_view_id}")
            # 判断该视点是否可见目标视点（人物）
            if human_view_id in connection_data[agent_view_id]['visible']:
                print(human_view_id)
                motion_path = os.path.join(motion_dir, human_motion.replace(' ', '_').replace('/', '_'), f"{human_model_id}_obj")
                human_loc = [pos_data[human_view_id][0], pos_data[human_view_id][1], pos_data[human_view_id][2]]
                human_heading = human_view_data[scan_id][human_view_id][2]
        except KeyError:
            pass

    return human_heading, human_loc, motion_path

# 计算数据集中每条路径的可见人物
def get_human_on_path(data_dir_path):
    print(f"**********************{data_dir_path}*****************************")
    with open('human_motion_text.json', 'r') as f:
        human_view_data = json.load(f)
    human_count = 0
    for scan in human_view_data:
        human_count = human_count + len(scan)
    #print(f"human count:{human_count}")
    r2r_data = read_R2R_data(data_dir_path)

    new_r2r_data = []

    

    All_path_num = 0
    Beginning_path_num = 0
    Obstacle_path_num = 0
    Around_path_num = 0
    End_path_num = 0
    
    human_num = 0
    Beginning_num = 0
    Obstacle_num = 0
    Around_num = 0
    End_num = 0
    

    for r2r_data_item in r2r_data:
        human_info = []
        scan_id = r2r_data_item["scan"]
        path = r2r_data_item["path"]
        path_id = r2r_data_item["path_id"]
        with open('con/pos_info/{}_pos_info.json'.format(scan_id), 'r') as f:
            pos_data = json.load(f)
            #print(len(pos_data))
        with open('con/con_info/{}_con_info.json'.format(scan_id), 'r') as f:
            connection_data = json.load(f)
    
        path_visible_points = get_visible_points(path, connection_data)

        for visible_point in path_visible_points:
            if visible_point in human_view_data[scan_id]:
                human_rel_pos = get_rel_pos(visible_point, path, path_id, pos_data)
                human_num += 1
                Beginning_num += int(human_rel_pos == "Beginning")
                Obstacle_num += int(human_rel_pos == "Obstacle")
                Around_num += int(human_rel_pos == "Around")
                End_num += int(human_rel_pos == "End")
                human_info.append({
					"human_viewpoint":visible_point,
					"human_rel_pos":human_rel_pos,
					"human_description":human_view_data[scan_id][visible_point][0]
				})
        # 统计含有每种相对位置的路径数量
        if len(human_info) > 0:
            All_path_num += 1
            Beginning_flag = 0
            Obstacle_flag = 0
            Around_flag = 0
            End_flag = 0
            for item in human_info:
                Beginning_flag = int(item["human_rel_pos"] == "Beginning")
                Obstacle_flag = int(item["human_rel_pos"] == "Obstacle")
                Around_flag = int(item["human_rel_pos"] == "Around")
                End_flag = int(item["human_rel_pos"] == "End")
            
            Beginning_path_num += Beginning_flag
            Obstacle_path_num += Obstacle_flag
            Around_path_num += Around_flag
            End_path_num += End_flag

        r2r_data_item["human"] = human_info
        new_r2r_data.append(r2r_data_item)
    
    print(f"paths with human:{All_path_num} / all paths {len(new_r2r_data)}")
    print(f"Number of paths containing each relative position:")
    print(f"All paths containing relative position:{All_path_num}")
    print(f"Beginning:{Beginning_path_num}")
    print(f"Obstacle:{Obstacle_path_num}")
    print(f"Around:{Around_path_num}")
    print(f"End:{End_path_num}")
    print(f"Number of relative positions of each human species")
    print(f"All relative positions:{human_num}")
    print(f"Beginning:{Beginning_num}")
    print(f"Obstacle:{Obstacle_num}")
    print(f"Around:{Around_num}")
    print(f"End:{End_num}")

    #print(f"Beginning_num:{Beginning_num}, Obstacle_num:{Obstacle_num}, End_num:{End_num}, Around_num:{Around_num}, None_num:{None_num}")
    
    with open(f"{data_dir_path.split('.json')[0]}_human.json", 'w') as f:
        json.dump(new_r2r_data, f, indent=4)
    #return

# 计算人物之于路径的相对位置
def get_rel_pos(human_point, path, path_id, pos_data):
    loc_dsc = [
        "Beginning",
        "Obstacle", 
        "Around",
        "End"
    ]
    min_distance = 1000
    for index, path_point in enumerate(path):
        distance = compute_distance(human_point, path_point, pos_data)
        if distance < min_distance:
            min_distance = distance
            if distance < 1.5 and index == 0:
                human_rel_pos=loc_dsc[0]
            elif distance < 1.5 and index == len(path)-1:
                human_rel_pos=loc_dsc[-1]
            elif distance < 1.5:
                human_rel_pos=loc_dsc[1]
            else:
                human_rel_pos=loc_dsc[2]
    return human_rel_pos

# 加载所有viewpoints
def load_viewpointids():
    GRAPHS = "connectivity/"
    viewpointIds = []
    with open(GRAPHS + "scans.txt") as f:
        scans = [scan.strip() for scan in f.readlines()]
        for scan in scans:
            with open(GRAPHS + scan + "_connectivity.json") as j:
                data = json.load(j)
                for item in data:
                    if item["included"]:
                        viewpointIds.append((scan, item["image_id"]))
    print("Loaded %d viewpoints" % len(viewpointIds))
    return viewpointIds

# 计算两点距离
def compute_distance(viewpointId1, viewpointId2, pos_data):
    x_dis = pos_data[viewpointId1][0] - pos_data[viewpointId2][0]
    y_dis = pos_data[viewpointId1][1] - pos_data[viewpointId2][1]
    z_dis = pos_data[viewpointId1][2] - pos_data[viewpointId2][2]
    squared_sum = x_dis**2 + y_dis**2 + z_dis**2
    return math.sqrt(squared_sum)

# 读取R2R数据
def read_R2R_data(file_path):
    with open(file_path, 'r') as f:
        r2r_data= json.load(f)
    r2r_data_path_num = len(r2r_data)
    print("R2R dataset:")
    print(f"total path:{r2r_data_path_num}")
    print(f"total instructions:{r2r_data_path_num * 3}")
    
    return r2r_data

# 获取路径周围可见的点（包括路径点本身）
def get_visible_points(path, connection_data):
    path_visible_points = []
    try:
        for path_point in path:
            visible_points = connection_data[path_point]['visible']
            for point in visible_points:
                if point not in path_visible_points:
                    path_visible_points.append(point)
    except KeyError:
        pass
        #print(connection_data[path_point])
    return path_visible_points

#计算可以看见人物的viewpoint总数
def count_points_seen_human():
    all_viewpointIds = load_viewpointids()
    viewpoints_counts = len(all_viewpointIds)
    human_visible_counts = 0
    for _, (scanId, viewpointId) in enumerate(all_viewpointIds):
        _, human_loc, _ = get_human_info("./", scanId, viewpointId)
        if human_loc is not None:
            human_visible_counts += 1
    print(f"human visible points {human_visible_counts} / All points {viewpoints_counts}")

# 计算两个列表的重合的元素数量
def count_common_elements(list1, list2):
    # Convert the lists to set
    set1 = set(list1)
    set2 = set(list2)
    
    # Find the intersection of the two sets
    common_elements = set1 & set2
    
    # Return the number of common elements
    return len(common_elements)

# 获取path上的关键点，抵达目标的必经点
def get_crux_on_path(data_file):
    data = read_R2R_data(data_file)
    #遍历每条路径
    for j,data_item in enumerate(data):
        scan_id = data_item["scan"]
        with open('con/con_info/{}_con_info.json'.format(scan_id), 'r') as f:
            connection_data = json.load(f)
        # 初始化并加入起点
        crux_list = [data_item["path"][0]]
        #遍历路径的每个点
        #print(data_item["path"])
        for i,viewpoint in enumerate(data_item["path"]):
            #下一个点
            if len(data_item["path"]) < 2:
                break
            next_viewpoint = data_item["path"][i+1]
            #到达终点
            if next_viewpoint == data_item["path"][-1]:
                crux_list.append(next_viewpoint)
                break
            # 计算本点的可到达点列表
            unobstructed_points = connection_data[viewpoint]['unobstructed']
            # 计算下一点的可到达点列表
            next_unobstructed_points = connection_data[next_viewpoint]['unobstructed']

            #计算重合点>1?（为关键点？）
            if count_common_elements(unobstructed_points, next_unobstructed_points) == 1:
                crux_list.append(next_viewpoint)

        # 写入原来的数据字典
        data[j]["crux_points"] = crux_list
    print(data_file)
    with open(data_file.split(".")[0]+'_crux_'+".json", 'w') as f:
        json.dump(data, f, indent=4)

# 获取每类区域的人物数量
def count_human_of_region():
    region = {}

    with open('human_motion_text.json', 'r') as f:
        human_view_data = json.load(f)
    
    for i, scanId in enumerate(human_view_data):
        print(f"{i}th scan {scanId}")
        for human_viewpointId in human_view_data[scanId]:
            print(f"**Human viewpoint {human_viewpointId}")
            #print(human_view_data[scanId][human_viewpointId])
            human_region = human_view_data[scanId][human_viewpointId][0].split(':')[0]
            try:
                region[human_region] += 1
            except KeyError:
                region[human_region] = 1
    print(region)
    print(len(region))

if __name__ == '__main__':
    #count_points_seen_human()
       
    data_folder = 'tasks/R2R/data'
    #files = [f for f in os.listdir(data_folder) if f.endswith('.json')]
    #for file in files:
        #get_crux_on_path(os.path.join(data_folder,file)) 
    #get_human_on_path(os.path.join(data_folder,"R2R_train.json"))
    #get_human_on_path(os.path.join(data_folder,"R2R_val_seen.json"))
    #get_human_on_path(os.path.join(data_folder,"R2R_val_unseen.json"))
    #get_human_on_path(os.path.join(data_folder,"path.json"))
    count_human_of_region()

    #count_points_seen_human()
    
