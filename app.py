from flask import Flask, render_template, request
from model import predict

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_route():
    temp = float(request.form['temperature'])
    hum = float(request.form['humidity'])
    soil = float(request.form['soil'])

    # simple pest logic
    pest = 2 if hum > 70 else 1 if hum > 60 else 0

    result = predict([temp, hum, soil, pest])

    if result[0] == 1:
        output = "Healthy Crop 🌱"
    else:
        output = "Risk Detected ⚠️"

    # suggestions
    if soil < 30:
        suggestion = "💧 Please irrigate the field"
    elif hum > 70:
        suggestion = "🐛 High pest risk - take action"
    else:
        suggestion = "✅ All conditions are good"

    return render_template('index.html', prediction=output, suggestion=suggestion)

if __name__ == "__main__":
    app.run(debug=True)