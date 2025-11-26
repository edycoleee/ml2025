from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)
model = load_model("xor_model.h5")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    x1 = data['x1']
    x2 = data['x2']
    
    # Bentuk input ke model
    input_data = np.array([[x1, x2]])
    prediction = model.predict(input_data)
    
    # Konversi ke nilai 0/1
    result = int(round(prediction[0][0]))
    
    return jsonify({
        "x1": x1,
        "x2": x2,
        "prediction": result
    })

if __name__ == '__main__':
    app.run(debug=True)
