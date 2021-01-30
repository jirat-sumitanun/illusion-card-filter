import os,shutil,time

'''
                text = b"IEND\xaeB`\x82"
                KStudio
                KoiKatuChara
                KoiKatuClothes
                AIS_Chara
                StudioNEOV2
                AIS_Clothes
'''
def display_title():
    print('''\n    ***************************************************************************************************
    *                                                                                                 *
    *          Automate filter AI/HS2 character, scene, coordinate                                    *
    *          if not enter directory to work, it will work in the same folder as this script         *
    *                                                                                                 *
    ***************************************************************************************************\n''')

def get_started(directory):
    flag = ''
    create_folder(directory)
    for item in os.listdir(directory):
        if item.endswith('.png'):
            file_in_progress = os.path.join(directory,item)
            flag = classify_image_type(file_in_progress)
            if flag == 'chara':
                dest = os.path.join(directory,'card',item)
            elif flag == 'scene':
                dest = os.path.join(directory,'scene',item)
            elif flag == 'clothes':
                dest = os.path.join(directory,'coordinate',item)
            elif flag == 'other':
                dest = os.path.join(directory,'other',item)
            try:
                shutil.move(file_in_progress,dest)
            except Exception as e:
                print(e,'top')
        #elif not item.endswith('.png') and not os.path.isdir(os.path.join(directory,item)):
        elif item.endswith('.jpg'):
            try:
                #print(os.path.splitext(item))
                file_in_progress = os.path.join(directory,item)
                dest = os.path.join(directory,'other',item)
                shutil.move(file_in_progress,dest)
            except Exception as e:
                print(e,'bottom')

def classify_image_type(file_to_test):
    with open(file_to_test, 'rb') as readImage:
        s = readImage.read()
        v1 = s.find(b"KStudio") # check koikatsu scene
        if v1 != -1:
            return "scene" # koikatsu scene => True
        elif v1 == -1: # Koikatsu scene => False
            v2 = s.find(b"KoiKatuChara") # check koikatsu character card
            v3 = s.find(b"KoiKatuClothes") # check koikatsu coordinate (clothes)
            if v2 != -1:
                return "chara" # koikatsu character card => True
            elif v3 != -1:
                return "clothes" # koikatsu clothes => True
            elif v1 == -1 and v2 == -1 and v3 == -1: # just a picture
                return "other"

def create_folder(directory):
    folder_array = ['card','scene','coordinate','other']
    for item in folder_array:
        path = os.path.join(directory,item)
        if not os.path.isdir(path):
            os.mkdir(path)

def main():
    display_title()
    dir_to_do_work = input('directory: ')
    if dir_to_do_work =='':
        dir_to_do_work = os.getcwd()
    get_started(dir_to_do_work)
if __name__ == "__main__":
    main()