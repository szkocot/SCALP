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

    def __call__(self, img, mask):

        img_ready = self.prepare_img(img, mask)

        # resize to N,W,H,C format (N==1)
        img_ready.shape = (1, *img_ready.shape)

        y_pred = self.model.predict(img_ready)

        y_dict = {'benign': y_pred[0][0],
                  'malignant': y_pred[0][1]}

        return y_dict
