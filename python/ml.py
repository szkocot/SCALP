import keras
import python.config as config
from python.preprocessing import Preprocessor
from python.utils import id_to_path

class Predictor(Preprocessor):

    def __init__(self, config=config):
        super().__init__(config)

        self.model = keras.models.load_model(config.model_path)

    def __call__(self, id, label):

        img_path = id_to_path(id = id, label = label, img_type = 'img')
        mask_path = id_to_path(id = id, label = label, img_type = 'mask')

        img = self.prepare_img(img_path,mask_path)

        #resize to N,W,H,C format (N==1)
        img.shape = (1,*img.shape)

        return self.model.predict(img)

if __name__ is '__main__':
    P = Predictor()
    print(P('ISIC_0001525','benign'))