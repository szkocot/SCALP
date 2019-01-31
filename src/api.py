import flask
from flask_restplus import Resource, Api, fields
import tensorflow as tf
from io import BytesIO
import base64
import re
from PIL import Image

try:
    import config
except ImportError:
    import python.config as config
try:
    from src.ml import Predictor
except ImportError:
    from python.ml import Predictor

app = flask.Flask(__name__)
api = Api(app)

predictor = Predictor(config=config)
graph = tf.get_default_graph()

img64_model = api.model(
    'Image and mask', {
        'img_b64': fields.String('base64 image'),
        'mask_b64': fields.String('base64 mask')})

pred_model = api.model(
    'prediction', {
        'benign': fields.Float('probability'),
        'malignant': fields.Float('probability')
    })


@api.route("/predict")
class PredictMalignancy(Resource):

    @api.expect(img64_model)
    @api.marshal_list_with(pred_model)
    def post(self):
        img = self.b64_to_img(api.payload['img_b64'])
        mask = self.b64_to_img(api.payload['mask_b64'])

        with graph.as_default():
            y_pred = predictor(img, mask)

        return y_pred

    def b64_to_img(self, img_b64):
        image_data = re.sub('^data:image/.+;base64,',
                            '', img_b64)
        image = Image.open(BytesIO(base64.b64decode(image_data)))

        return image


def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


if __name__ == '__main__':

    app.run(debug=True)
