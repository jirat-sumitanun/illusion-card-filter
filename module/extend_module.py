import os

exclude_image_type = ('.jpg','.jpeg','.gif','.bmp','.jiff','.tiff','.webp','.raw')

def classify_file_type(directory,item):
    if item.endswith('.png'):
        return "png"
    elif item.endswith(exclude_image_type):
        return "other"
    elif item.endswith('.zipmod'):
        return "mod"
    elif item.endswith('.dll'):
        return "plugin"
    elif item.endswith(('.dhh','.preset')):
        return "graphic preset"
    elif os.path.isdir(os.path.join(directory,item)):
        pass

def create_folder(directory,game):
    #folder_array = ['card','scene','coordinate','other']
    if game == "koikatsu":
        folder_array = ['chara_sunshine','scene','scene_sunshine','coordinate','coordinate_sunshine','mod','plugin','other']
    elif game == "ai_hs2":
        folder_array = ['scene','coordinate','mod','plugin','graphic preset','other']

    for item in folder_array:
        path = os.path.join(directory,item)
        if not os.path.isdir(path):
            os.mkdir(path)

def clean_empty_folder(dir_to_do_work,game):
    if game == "koikatsu":
        folder_array = ['chara_sunshine','scene','scene_sunshine','coordinate','coordinate_sunshine','mod','plugin','other']
    elif game == "ai_hs2":
        folder_array = ['scene','coordinate','mod','plugin','graphic preset','other']

    for item in folder_array:
        path = os.path.join(dir_to_do_work, item)
        if len(os.listdir(path)) == 0:
            os.rmdir(path)

def move_file(directory,file_type_folder,item):
    dest = os.path.join(directory, file_type_folder, item)