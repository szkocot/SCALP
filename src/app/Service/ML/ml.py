import keras
import config,os
from src.app.Service.ML.Preprocessing import Preprocessor
from src.app.Helper.utils import idToPath


class Predictor(Preprocessor):
    """Predicts probability for benign and malignant label when image is given.

    Arguments:
        Preprocessor {class} -- image id, label (['benign','malignant','unknown'])

    Returns:
        [np.Array] -- Probabilities for benign, malignant label.
    """

    def __init__(self):
        super().__init__()
        print(config.PREDICTOR['model_path'])
        print(os.path.abspath(__file__))

        #commented cause of OSError: Unable to open file (file signature not found
        #self.model = keras.models.load_model(config.PREDICTOR['model_path'])

    def __call__(self, img, mask):
        img_ready = self.prepare_img(img, mask)

        # resize to N,W,H,C format (N==1)
        img_ready.shape = (1, *img_ready.shape)

        y_pred = self.model.predict(img_ready)

        y_dict = {'benign': y_pred[0][0],
                  'malignant': y_pred[0][1]}

        return y_dict
