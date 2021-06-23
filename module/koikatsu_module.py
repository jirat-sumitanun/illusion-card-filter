'''
                text = b"IEND\xaeB`\x82"
                KStudio
                KoiKatuChara
                KoiKatuClothes
                ===============
                KoiKatuCharaSun
                ??not yet release KStudioSun
                ??not yet release KoiKatuClothesSun
'''
import os

def classify_card_type(directory,item):
    with open(os.path.join(directory,item),'rb') as readImage:
        s = readImage.read()
        # wait for full game release
        # if check_is_scene_sunshine(s):
        #     return "scene_sunshine"
        if check_is_scene(s):
            return "scene"
        elif check_is_chara_sunshine(s):
            return "chara_sunshine"
        elif check_is_chara(s):
            return "chara"
        # wait for full game release
        # elif check_is_clothes_sunshine(s):
        #     return "coordinate_sunshine"
        elif check_is_clothes(s):
            #return "clothes"
            return "coordinate"
        else:
            return "other"

# ============= Koikatsu ================

def check_is_scene(card_data):
    if card_data.find(b'KStudio') != -1:
        return True
    return False

def check_is_chara(card_data):
    if card_data.find(b"KoiKatuChara") != -1:
        return True
    return False

def check_is_clothes(card_data):
    if card_data.find(b"KoiKatuClothes") != -1:
        return True
    return False

# ============= Koikatsu Sunshine ================

def check_is_chara_sunshine(card_data):
    if card_data.find(b"KoiKatuCharaSun") != -1:
        return True
    return False

# prototype
# not yet release
def check_is_scene_sunshine(card_data):
    if card_data.find(b"KStudioSun") != -1:
        return True
    return False

# prototype
# not yet release
def check_is_clothes_sunshine(card_data):
    if card_data.find(b"KoiKatuClothesSun") != -1:
        return True
    return False