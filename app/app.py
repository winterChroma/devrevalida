from flask import Flask, render_template, request, jsonify
from fastai import *
from fastai.vision import *
from io import BytesIO

classes = ['Abyssinian','Bengal','Birman','Bombay','British_Shorthair','Egyptian_Mau','Maine_Coon','Persian','Ragdoll','Russian_Blue','Siamese','Sphynx','american_bulldog','american_pit_bull_terrier','basset_hound','beagle','boxer','chihuahua','english_cocker_spaniel','english_setter','german_shorthaired','great_pyrenees','havanese','japanese_chin','keeshond','leonberger','miniature_pinscher','newfoundland','pomeranian','pug','saint_bernard','samoyed','scottish_terrier','shiba_inu','staffordshire_bull_terrier','wheaten_terrier','yorkshire_terrier']

model_path = download_url('https://revalida-test.s3-ap-southeast-1.amazonaws.com/resnet50_revalida.pkl','app/models/resnet50_revalida.pkl')
learn = load_learner(Path('app/models'), 'resnet50_revalida.pkl')

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
  prediction = learn.predict(image)[0]
  print(prediction)
  return {'result': str(prediction)}

if __name__ == '__main__':
  app.run(host="0.0.0.0", port = 5000, debug = True)