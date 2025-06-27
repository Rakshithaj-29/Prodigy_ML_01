from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Load and train model
data = pd.read_csv(r"D:\DAA\rakshitha\prodigy_infotech\train.csv")
data = data.dropna(subset=['GrLivArea', 'BedroomAbvGr', 'FullBath', 'SalePrice'])

X = data[['GrLivArea', 'BedroomAbvGr', 'FullBath']]
y = data['SalePrice']

model = LinearRegression()
model.fit(X, y)

@app.route('/')
def home():
    return render_template("index.html", prediction=None)


@app.route('/predict', methods=["POST"])
def predict():
    try:
        area = float(request.form['area'])
        bedrooms = int(request.form['bedrooms'])
        bathrooms = int(request.form['bathrooms'])

        input_data = np.array([[area, bedrooms, bathrooms]])
        prediction = model.predict(input_data)[0]
        prediction = f"${prediction:,.2f}"

        return render_template(r"index.html", prediction=prediction)
    except:
        return render_template(r"index.html", prediction="Invalid input")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

