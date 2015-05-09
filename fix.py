__author__ = 'mammothbane'

import os
from PIL import Image


def recognize_pure(image):
    return False


def recognize_magic(image):
    return False


def recognize_physical(image):
    return False


def recognize_immune_pierce(image):
    return False


def mark_image(image, features):
    out = Image.open(image)

    if features['physical']:
        print('[' + image + '] physical')
    if features['magic']:
        print('[' + image + '] magic')
    if features['pure']:
        print('[' + image + '] pure')
    if features['immune_pierce']:
        print('[' + image + '] immune_pierce')

    return out


def check_and_create_dir(dir_name):
    if not os.path.isdir(dir_name):
        if os.path.exists(dir_name):
            raise Exception("file " + dir_name + "already exists. aborting.")
        os.mkdir(dir_name)


def gen_image(src, original, out):
    features = {'physical': False, 'magic': False, 'pure': False, 'immune_pierce': False}

    if recognize_physical(src):
        features['physical'] = True
    elif recognize_magic(src):
        features['magic'] = True

    if recognize_pure(src):
        features['pure'] = True

    if recognize_immune_pierce(src):
        features['immune_pierce'] = True

    mark_image(original, features).save(out, "PNG")

orig = 'original'
source = 'source'
result = 'result'

for directory in [orig, source, result]:
    check_and_create_dir(directory)

miss = []

for root, dirs, files in os.walk(source):
    for fil in files:
        rel_path = os.path.join(os.path.relpath(root, source), fil)
        orig_path = os.path.join(orig, rel_path)
        res_path = os.path.join(result, rel_path)
        if os.path.isfile(orig_path):
            print('[MATCH]\t' + orig_path)
            if not os.path.isdir(os.path.dirname(res_path)):
                os.makedirs(os.path.dirname(res_path))
            gen_image(os.path.join(root, fil), orig_path, os.path.join(result, rel_path))
        else:
            print('[MISS]\t' + orig_path)
            miss.append(rel_path)

print(miss)