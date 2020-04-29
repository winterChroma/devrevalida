from flask import Flask, render_template, request, jsonify
from fastai import *
from fastai.vision import *
from io import BytesIO

pets_model_path = download_url('https://revalida-test.s3-ap-southeast-1.amazonaws.com/resnet50_revalida.pkl','app/models/resnet50_revalida.pkl')
pets_learn = load_learner(Path('app/models'), 'resnet50_revalida.pkl')

nba_model_path = download_url('https://revalida-test.s3-ap-southeast-1.amazonaws.com/resnet50_revalida_nba.pkl','app/models/resnet50_revalida_nba.pkl')
nba_learn = load_learner(Path('app/models'), 'resnet50_revalida_nba.pkl')

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
  if(request.method == "POST"):
    pass
  else:
    return render_template("index.html")

@app.route('/classify', methods=['POST'])
def classify():
  image = ""
  if request.files:
    image = request.files["inputFile"]

  image = open_image(BytesIO(image.read()))
  if (request.form["classifierSelect"] == "pets"):
    prediction = pets_learn.predict(image)[0]
  elif (request.form["classifierSelect"] == "nba"):
    prediction = nba_learn.predict(image)[0]

  print(prediction)
  return {'result': str(prediction)}

if __name__ == '__main__':
  app.run(host="0.0.0.0", port = 5000, debug = True)