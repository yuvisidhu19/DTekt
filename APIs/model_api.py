import tensorflow as tf
import tensorflow_text as text
import tensorflow_hub as hub
from flask import Flask, request
app = Flask(__name__)
@app.route('/', methods = ['POST'])
def model():
    test = request.get_json()
    test = test['name']
    #print(test, flush=True)
    prediction1 = real_fake_model.predict(test)
    prediction2 = pos_neg_model.predict(test)

    real = 0
    fake = 0
    for i in prediction1:
        if i >= 0.5:
            real += 1
        else:
            fake += 1

    pos = 0
    neg = 0
    for i in prediction2:
        if i >= 0.5:
            pos += 1
        else:
            neg += 1

    # realness = real/(fake + real)
    # positiveness = pos/(neg + pos)
    # answer = (realness*0.8 + positiveness*0.2) / 2
    fakeness = fake/(fake + real)
    negativeness = neg/(neg + pos)
    answer = negativeness
    if fakeness >= 0.35:
        answer = min(negativeness + 0.15, 1.00)
    # print('fakeness: ', fakeness, flush=True)
    # print('negativeness', negativeness, flush=True)

    return {'val': round((1 - answer)*100, 2)}

if __name__ == '__main__':
    model_dir = 'real_fake_model'   #train this model from models.ipynb
    real_fake_model = tf.keras.models.load_model(model_dir)
    model_dir = 'pos_neg_model'   #train this model from models.ipynb
    pos_neg_model = tf.keras.models.load_model(model_dir)
    app.run(port = 7000)
