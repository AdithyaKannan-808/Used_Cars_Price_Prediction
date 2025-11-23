import pandas as pd
import joblib

# Load model
model = joblib.load("outputs/model.pkl")

# Load test data
test = pd.read_csv("data/processed/test_data.csv")

# Make predictions
preds = model.predict(test)

# Save predictions
output = pd.DataFrame({"predicted_price": preds})
output.to_csv("outputs/test_predictions.csv", index=False)

print("Predictions saved to outputs/test_predictions.csv")
