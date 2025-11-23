import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load processed data
df = pd.read_csv("data/processed/Cleaned_Car.csv")

# Features and target
X = df.drop("selling_price", axis=1)
y = df["selling_price"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "outputs/model.pkl")

print("Model trained and saved as outputs/model.pkl")
