import albumentations as A
import cv2
import os
import shutil
from matplotlib import pyplot as plt

# 增广数据集
transform_tfds = A.Compose([  # zyp
    A.Blur(p=0.2),
    A.MedianBlur(p=0.2),
    A.CLAHE(p=0.2),
    A.RandomBrightnessContrast(p=0.2),
    A.RandomGamma(p=0.2)
])


if __name__ == "__main__":
    images_folder_path = r"D:\dataset"

    number_albumentation = 9  # 一张增广多少张

    images = [os.path.join(images_folder_path, image) for image in os.listdir(images_folder_path)]
    images.sort()

    img_types = [".jpg", ".png"]

    for image in images:
        file_name = os.path.basename(image).split(".")[0]
        print(file_name)
        for img_type in img_types:
            image_path = os.path.join(images_folder_path, file_name + img_type)
            if os.path.exists(image_path):
                print(image_path)
                image = cv2.imread(image_path)
                for i in range(number_albumentation):
                    transformed = transform_tfds(image=image)["image"]
                    # plt.imshow(transformed)
                    # plt.show()
                    image_save_path = os.path.join(images_folder_path, file_name + "_" + str(i) + img_type)
                    cv2.imwrite(image_save_path, transformed)
    print("all done")
