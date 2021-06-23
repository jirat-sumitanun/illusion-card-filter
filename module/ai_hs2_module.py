'''
                text = b"IEND\xaeB`\x82"
                AIS_Chara
                StudioNEOV2
                AIS_Clothes
'''
import os

def classify_card_type(directory,item):
    with open(os.path.join(directory,item), 'rb') as readImage:
        s = readImage.read()
        if check_is_scene(s):
            return "scene"
        elif check_is_chara(s):
            return "chara"
        elif check_is_clothes(s):
            return "clothes"
        else:
            return "other"

def check_is_scene(card_data):
    if card_data.find(b'StudioNEOV2') != -1:
        return True
    return False

def check_is_chara(card_data):
    if card_data.find(b"AIS_Chara") != -1:
        return True
    return False

def check_is_clothes(card_data):
    if card_data.find(b"AIS_Clothes") != -1:
        return True
    return False