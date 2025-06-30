from flask import Flask, render_template, request
import joblib


app = Flask(__name__)
model = joblib.load("final_model.pkl")

# trained model load kro

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # input_value = float(request.form['feature']) # form input
     f1 = float(request.form['feature1'])
     f2 = float(request.form['feature2'])
     f3 = float(request.form['feature3'])
     f4 = float(request.form['feature4'])

     input_values = [[f1, f2, f3, f4]]
     prediction = model.predict(input_values) # prediction

     return render_template('result.html',
 prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
