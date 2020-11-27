from flask import Flask, request, render_template
import pickle
from sklearn import svm
app = Flask(__name__)
model = pickle.load(open('SVM_model.pkl', 'rb'))
results = ["It is not a pulsar star :(", "It is a pulsar star!!!"]
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    int_features = [list(map(float, request.form.values()))]
    res = model.predict(int_features)
    return render_template('index.html', prediction_text=results[int(res)])
if __name__ == "__main__":
    app.run(threaded=True, port=5000)
