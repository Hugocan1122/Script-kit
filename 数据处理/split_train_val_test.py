import os
import numpy as np
import random
import shutil
import argparse


def split_dataset(simple=False, **kwargs):
    current_dir = os.getcwd()
    images_folder = os.path.join(current_dir, "images")
    files_list = [os.path.join(images_folder, file) for file in os.listdir(images_folder)]

    if simple:
        np.savetxt("train_data.txt", files_list, fmt="%s", newline="\n")
        np.savetxt("val_data.txt", files_list, fmt="%s", newline="\n")

    else:
        train_ratio = 0.8
        val_ratio = 0.1
        # test_ratio = 0.1

        random.shuffle(files_list)  # shuffle the file list to split it into train, val, test
        train_index = int(len(files_list) * train_ratio)
        val_index = int(len(files_list) * val_ratio)
        print("train_index:", train_index)

        train_files_list = files_list[:train_index]
        val_files_list = files_list[train_index:train_index + val_index]
        test_files_list = files_list[train_index + val_index:]

        # create test_image folder and move images in to test it
        test_img_folder = os.path.join(current_dir, "test_img")

        if not os.path.exists(test_img_folder):
            os.mkdir(test_img_folder)

        for name in test_files_list:
            test_name = os.path.join(test_img_folder, name.split('/')[-1])
            shutil.copyfile(name, test_name)

        np.savetxt("train_data.txt", train_files_list, fmt="%s", newline="\n")
        np.savetxt("val_data.txt", val_files_list, fmt="%s", newline="\n")
        np.savetxt("test_data.txt", test_files_list, fmt="%s", newline="\n")

    print("work done")


def split_classify_dataset(**kwargs):
    current_dir = os.getcwd()
    images_folder = os.path.join(current_dir, "yaozhentanhuang")

    for folder_name in os.listdir(images_folder):

        subfolder = os.path.join(images_folder, folder_name)

        files_list = [os.path.join(subfolder, file) for file in os.listdir(subfolder)]

        train_ratio = 0.8
        val_ratio = 0.1
        test_ratio = 0.1

        random.shuffle(files_list)  # shuffle the file list to split it into train, val, test
        train_index = int(len(files_list) * train_ratio)
        val_index = int(len(files_list) * val_ratio)
        print("train_index:", train_index)

        train_files_list = files_list[:train_index]
        val_files_list = files_list[train_index:train_index + val_index]
        test_files_list = files_list[train_index + val_index:]

        train_img_folder = os.path.join(current_dir, f"images_yaozhentanhuang/train/{folder_name}")

        if not os.path.exists(train_img_folder):
            os.mkdir(train_img_folder)

        for name in train_files_list:
            train_name = os.path.join(train_img_folder, name.split('/')[-1])
            shutil.copyfile(name, train_name)

        test_img_folder = os.path.join(current_dir, f"images_yaozhentanhuang/test/{folder_name}")

        if not os.path.exists(test_img_folder):
            os.mkdir(test_img_folder)

        for name in test_files_list:
            test_name = os.path.join(test_img_folder, name.split('/')[-1])
            shutil.copyfile(name, test_name)

        val_img_folder = os.path.join(current_dir, f"images_yaozhentanhuang/val/{folder_name}")

        if not os.path.exists(val_img_folder):
            os.mkdir(val_img_folder)

        for name in val_files_list:
            val_name = os.path.join(val_img_folder, name.split('/')[-1])
            shutil.copyfile(name, val_name)

    print("work done")


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument("--simple", action="store_true", help="use whole dataset as train&val")
    parser.add_argument("--classify", action="store_true")
    opt = parser.parse_args()
    return opt


def main():
    opt = parse_opt()
    if vars(opt)["classify"]:
        split_classify_dataset(**vars(opt))
    else:
        split_dataset(**vars(opt))


if __name__ == "__main__":
    main()