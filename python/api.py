import flask
import sys
import pandas as pd
import tensorflow as tf

try:
    import config
except ImportError:
    import python.config as config
try:
    from ml import Predictor
except ImportError:
    from python.ml import Predictor

app = flask.Flask(__name__)
predictor = Predictor(config=config)
graph = tf.get_default_graph()


def sendResponse(responseObj):
    response = flask.jsonify(responseObj)
    # TODO: Add respose.headers if needed
    return response


@app.route("/predict", methods=["GET"])
def predict():
    id = flask.request.args.get('id')
    label = flask.request.args.get('label')

    data = {"success": False}
    with graph.as_default():
        y_pred = predictor(id, label)
    data['probabilities'] = pd.Series(y_pred).to_json(orient='index')
    data["success"] = True

    return sendResponse(data)


if __name__ == '__main__':

    app.run(debug=True)

    # example: http://localhost:5000/predict?id=ISIC_0000198&label=benign
