import tensorflow as tf
from src.app.Service.ML.ml import Predictor


class Prediction:

    predictor = Predictor()
    graph = tf.get_default_graph()

#//todo rewrite to app flask not api
    # img64_model = api.model(
    #     'Image and mask', {
    #         'img_b64': fields.String('base64 image'),
    #         'mask_b64': fields.String('base64 mask')})
    #
    # pred_model = api.model(
    #     'prediction', {
    #         'benign': fields.Float('probability'),
    #         'malignant': fields.Float('probability')
    #     })
