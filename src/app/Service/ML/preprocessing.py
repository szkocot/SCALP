import numpy as np
import config
from PIL import Image

class Preprocessor():
    """Preprocesses given image data, so it can be used for CNN prediction.

    Raises:
        ValueError -- Raised when load_image_and_resize method is called with not allowed img type.

    Returns:
        [np.Array] -- Processed image.
    """

    def __init__(self):
        self.img_mean = config.PREDICTOR['img_mean']
        self.img_std = config.PREDICTOR['img_std']
        self.img_target_size = config.PREDICTOR['img_target_size']

    def mask_img(self, img, mask):
        img = self.resize_to_np(img)
        mask = self.resize_to_np(mask)

        img = img[:, :, :3]
        mask = mask == 255

        return img * np.stack((mask, mask, mask), axis=2)

    def standardize_img(self, img):
        for i in range(3):
            img[:, :, i] = (img[:, :, i] - self.img_mean[i]) / self.img_std[i]
        return img

    def prepare_img(self, img, mask):
        img_masked = self.mask_img(img, mask).astype(np.float32)

        return self.standardize_img(img_masked)

    def resize_to_np(self, img):
        return np.array(img.resize(
            reversed(self.img_target_size)))

    def load_img(self,img_path):
        return Image.open(img_path)
