import os
import glob
try:
    from config import data_path
except ImportError:
    from python.config import data_path


def id_to_path(id='ISIC_0000000', label='malignant', img_type='img'):
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

    base_dir = os.path.join(data_path, label, img_type)

    return glob.glob(base_dir+'/'+id+'*')[0]
