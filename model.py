import joblib
import pandas as pd
from sklearn.linear_model import ElasticNet

# Dataset URL
url = "https://raw.githubusercontent.com/amankharwal/Website-data/master/CarPrice.csv"
df = pd.read_csv(url)

# Select features & target
X = df[['carwidth', 'curbweight', 'enginesize', 'horsepower', 'citympg']]
y = df['price']

# Train Elastic Net model
model = ElasticNet(alpha=0.1, l1_ratio=0.5)
model.fit(X, y)

# Save model
joblib.dump(model, "elasticnet_carprice_model.pkl")
print("✅ Model trained and saved as elasticnet_carprice_model.pkl")
