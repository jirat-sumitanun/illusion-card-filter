import os, shutil
from module.koikatsu_module import classify_card_type
from module.extend_module import create_folder, classify_file_type, move_file, clean_empty_folder

def display_title():
    print('''\n    ***************************************************************************************************
    *                                                                                                 *
    *                     Automate filter Koikatsu character, scene, coordinate                       *
    *          if not type directory to work, it will work in the same folder as this script         *
    *                                                                                                 *
    ***************************************************************************************************\n''')

def get_started(directory):
    create_folder(directory,'koikatsu')
    for item in os.listdir(directory):
        file_type_flag = classify_file_type(directory,item)

        if file_type_flag == "png":
            card_flag = classify_card_type(directory,item)
            if not card_flag == "chara":
                move_file(directory,card_flag,item)
        elif file_type_flag == "mod":
            move_file(directory, file_type_flag, item)
        elif file_type_flag == "plugin":
            move_file(directory, file_type_flag, item)
        elif file_type_flag == "graphic preset":
            move_file(directory, file_type_flag, item)
        elif file_type_flag == "other":
            move_file(directory, file_type_flag, item)

if __name__ == "__main__":
    dir_to_do_work = input('directory: ')
    dir_to_do_work = dir_to_do_work.replace('\"','')
    if dir_to_do_work =='':
        dir_to_do_work = os.getcwd()
    get_started(dir_to_do_work)
    clean_empty_folder(dir_to_do_work,'koikatsu')

