# !/usr/bin/python
# coding:utf-8

import sys
# import cv2
import os, random, glob
from preprocessing_helper import draw_single_char, CANVAS_SIZE, CHAR_SIZE, draw_example_src_only, draw_single_char_by_font
from PIL import Image, ImageEnhance, ImageFont
import numpy as np
from char_info import get_component


img_folder = sys.argv[1]  # img_folder: crawler
dst_folder_all = sys.argv[2]  # img_all
dst_folder_cns = sys.argv[3]  # img_all_cns
src_font = "preprocess/SimSun.ttf"

def get_char(folder_name):
    char_list = []
    for filename in os.listdir(folder_name):
        if '.png' in filename:
            char = filename[0]
            char_list.append(char)
    return char_list


def select_test_character(intersect_list):
    return random.sample(intersect_list, 1000)


def clear_folder(folder_path: str):
    files = glob.glob(os.path.join(folder_path, '*'))
    for f in files:
        os.remove(f)


# output image file name: [category]_[count].jpg
def generatePairImg(selectedTestChar, save_folder_all, save_folder_cns, folder_list, img_folder):
    train = save_folder_all + '/train/'
    test = save_folder_all + '/test/'
    train_cns = save_folder_cns + '/train/'
    test_cns = save_folder_cns + '/test/'
    if not os.path.exists(train):
        os.makedirs(train)
    else:
        clear_folder(train)
    if not os.path.exists(test):
        os.makedirs(test)
    else:
        clear_folder(test)
    if not os.path.exists(train_cns):
        os.makedirs(train_cns)
    else:
        clear_folder(train_cns)
    if not os.path.exists(test_cns):
        os.makedirs(test_cns)
    else:
        clear_folder(test_cns)

    font = ImageFont.truetype(src_font, CHAR_SIZE)
    count_test = 1
    count_train = 1

    for idx, folder in enumerate(folder_list):
        src_folder = os.path.join(img_folder, folder)
        print(src_folder)
        for path in glob.glob(os.path.join(src_folder, '*.png')):
            filename = path[len(src_folder)+1:]
            substr = str(filename[0])
            component = get_component(substr) # this part is for cns code

            try:
                image = Image.open(path)
                # read calligraphy image and modify size
                calli_img = draw_single_char(image, canvas_size=CANVAS_SIZE, char_size=CHAR_SIZE)
                # Add contrast
                contrast = ImageEnhance.Contrast(calli_img)
                calli_img = contrast.enhance(2.)
                # Add brightness
                brightness = ImageEnhance.Brightness(calli_img)
                calli_img = brightness.enhance(2.)

                #get corresponding font image
                #font_img = draw_single_char_by_font(substr, font, CANVAS_SIZE, CHAR_SIZE)
                #im_AB = np.concatenate([font_img, char_img], 1)
                together = draw_example_src_only(substr, font, calli_img, CANVAS_SIZE, CHAR_SIZE)

                if substr in selectedTestChar:
                    together.save(os.path.join(test, "%d_%d.jpg" %(idx, count_test)))
                    together.save(os.path.join(test_cns, "%s_%d_%d.jpg" %(component, idx, count_test)))
                    count_test += 1
                else:
                    together.save(os.path.join(train, "%d_%d.jpg" %(idx, count_train)))
                    together.save(os.path.join(train_cns, "%s_%d_%d.jpg" %(component, idx, count_train)))
                    count_train += 1

            except OSError:
                with open(save_folder_all + '/error_msg.txt', 'a') as f:
                    f.write("cannot open image file %s \n" %(filename))


folder_list = ['edukai']
test_chars = get_char(os.path.join(img_folder, 'edukai'))

generatePairImg(selectedTestChar=select_test_character(test_chars), save_folder_all=dst_folder_all, save_folder_cns=dst_folder_cns, folder_list=folder_list, img_folder=img_folder)
