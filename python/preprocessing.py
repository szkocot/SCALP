import os
from PIL import Image
import numpy as np
import python.config


class Preprocessor():

    def __init__(self, config):
        self.img_mean = config.img_mean
        self.img_std = config.img_std
        self.img_target_size = config.img_target_size

    def load_image_and_resize(self, file_path, img_type):
        img = np.array(Image.open(file_path).resize(
            reversed(self.img_target_size)))
        if img_type is 'img':
            return img
        elif img_type is 'mask':
            return img == 255
        else:
            raise ValueError('img_type should be either img or mask')

    def mask_img(self, img, mask):
        return img*np.stack((mask, mask, mask), axis=2)

    def standardize_img(self, img):
        img = img[:, :, :3]
        for i in range(3):
            img[:, :, i] = (img[:, :, i] - self.img_mean[i])/self.img_std[i]
        return img

    def prepare_img(self, img_path, mask_path):
        img = self.load_image_and_resize(img_path, 'img')
        mask = self.load_image_and_resize(mask_path, 'mask')

        img_masked = self.mask_img(img, mask)

        return self.standardize_img(img_masked)
