from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    area = float(request.form['area'])
    bedrooms = float(request.form['bedrooms'])
    bathrooms = float(request.form['bathrooms'])
    location = float(request.form['location'])

    # simple formula (we will replace with ML model later)
    price = (area * 2000) + (bedrooms * 50000) + (bathrooms * 30000) + (location * 10000)

    return render_template('index.html', prediction=f"Estimated Price: ₹ {price:,.0f}")

if __name__ == "__main__":
   if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
