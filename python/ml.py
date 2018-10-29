import numpy as np
import keras
try:
    import config
except ImportError:
    import python.config as config
try:
    from preprocessing import Preprocessor
except ImportError:
    from python.preprocessing import Preprocessor
try:
    from utils import id_to_path
except ImportError:
    from python.utils import id_to_path


class Predictor(Preprocessor):

    """Predicts probability for benign and malignant label when image is given.

    Arguments:
        Preprocessor {class} -- image id, label (['benign','malignant','unknown'])

    Returns:
        [np.Array] -- Probabilities for benign, malignant label.
    """

    def __init__(self, config=config):
        super().__init__(config)

        self.model = keras.models.load_model(config.model_path)

    def __call__(self, id, label):

        img_path = id_to_path(id=id, label=label, img_type='img')
        mask_path = id_to_path(id=id, label=label, img_type='mask')

        img = self.prepare_img(img_path, mask_path)

        # resize to N,W,H,C format (N==1)
        img.shape = (1, *img.shape)

        y_pred = self.model.predict(img)

        y_dict = {'benign': y_pred[0][0],
                  'malignant': y_pred[0][1]}

        return y_dict


if __name__ is '__main__':

    predictor = Predictor()
    benign_ids = ['ISIC_0000198',
                  'ISIC_0000335',
                  'ISIC_0001913']

    malignant_ids = ['ISIC_0000019',
                     'ISIC_0000335',
                     'ISIC_0010990']

    print('--Benign--')
    label = 'benign'
    for id in benign_ids:
        y_pred = predictor(id, 'benign')
        print(y_pred)

    print('--Malignant--')
    label = 'malignant'
    for id in malignant_ids:
        y_pred = predictor(id, 'malignant')
        print(y_pred)
