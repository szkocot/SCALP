import os, glob, base64, re
from io import BytesIO
from PIL import Image
import config
import numpy as np
from PIL import Image
import base64
import io

def idToPath(id='ISIC_0000000', label='malignant', img_type='img'):
    """Processes given id, label and img_type with data_path from config to create image path.

    Returns:
        [str] -- image path.
    """

    if label not in ['malignant', 'benign', 'unknown']:
        raise ValueError('label should be either malignant or benign')

    if img_type not in ['img', 'mask', 'segmentation']:
        raise ValueError('img_type should be either img or mask/segmentation')

    # TODO: Use single directory for images.
    if img_type is 'mask':
        img_type = 'segmentation'
    elif img_type is 'img':
        img_type = 'images'

    base_dir = os.path.join(config.PREDICTOR['data_path'], label, img_type)

    return glob.glob(base_dir + '/' + id + '*')[0]

    # todo


def b64ToImg(img_b64):
    image_data = re.sub('^data:image/.+;base64,',
                        '', img_b64)
    image = Image.open(BytesIO(base64.b64decode(image_data)))

    return image


def allowedFile(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in config.ALLOWED_EXTENSIONS

def mask_img(img_path, mask_path):

    img = Image.open(img_path)
    mask = Image.open(mask_path)

    img_transp = Image.new('RGBA', img.size, (0, 0, 0, 0))
    img_transp.paste(img, (0,0), mask=mask)

    return img_transp

def np_img_to_b64(pil_img):

    img_io = io.BytesIO()
    pil_img.save(img_io, 'png', quality=100)
    img_io.seek(0)
    img = base64.b64encode(img_io.getvalue())

    return img.decode('ascii')
