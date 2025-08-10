# 🚗 Elastic Net Car Price Predictor

This project predicts car prices using an Elastic Net Regression model trained on a car specifications dataset. The web interface is built with Flask, allowing users to input car attributes and instantly receive a predicted price.

---

## 📌 About
**Elastic Net Regression** is a linear model that combines L1 (Lasso) and L2 (Ridge) regularization. It performs feature selection, handles multicollinearity, and works well with many predictors. The mix of L1 and L2 is controlled by the `l1_ratio` parameter.

---

## 📂 Dataset
We use the [Car Price dataset](https://raw.githubusercontent.com/amankharwal/Website-data/master/CarPrice.csv) containing specifications like dimensions, weight, engine details, and fuel efficiency to predict the car price.

**Selected Features:**
- `carwidth` — Width of the car in inches
- `curbweight` — Weight of the car without passengers or cargo
- `enginesize` — Size of the engine in cubic centimeters
- `horsepower` — Horsepower of the car’s engine
- `citympg` — Miles per gallon in city driving

---

## ⚙️ Installation & Usage

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/elasticnet-car-price-predictor.git
cd elasticnet-car-price-predictor
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Train the model
```bash
python model.py
```

### 4️⃣ Run the Flask app
```bash
python app.py
```
The app will start at **http://127.0.0.1:5001/**.

---

## 🖥️ User Interface
The UI is built using HTML and CSS with a clean, interactive design. Users can enter the car’s attributes in the form, and the app predicts the price instantly.

---

## 📦 Project Structure
```
├── model.py                  # Trains and saves the Elastic Net model
├── app.py                    # Flask application for the web UI
├── templates/
│   └── index.html            # HTML form for user input
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

---

## 📸 Screenshot
![App Screenshot](screenshot.png)