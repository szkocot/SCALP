import keras
import tensorflow as tf
import config
from src.app.Service.ML.preprocessing import Preprocessor
from src.app.Helper.utils import idToPath


class Predictor(Preprocessor):
    """Predicts probability for benign and malignant label when image is given.

    Arguments:
        Preprocessor {class} -- image path and mask path

    Returns:
        [np.Array] -- Probabilities for benign, malignant label.
    """

    def __init__(self):
        super().__init__()
        self.graph = tf.get_default_graph()
        self.model = keras.models.load_model(config.PREDICTOR['model_path'])

    def __call__(self, img_path, mask_path):

        img = self.load_img(img_path)
        mask = self.load_img(mask_path)

        img_ready = self.prepare_img(img, mask)

        # resize to N,W,H,C format (N==1)
        img_ready.shape = (1, *img_ready.shape)
        with self.graph:
            y_pred = self.model.predict(img_ready)

        y_dict = {'benign': y_pred[0][0],
                  'malignant': y_pred[0][1]}

        return y_dict
