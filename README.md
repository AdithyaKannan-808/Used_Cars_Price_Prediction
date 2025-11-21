#  Used Car Price Prediction & Market Insights (Python, Machine Learning)

This project predicts the **resale price of used cars** using machine learning, combining data cleaning, EDA, feature engineering, model training, model evaluation, and market interpretation. It uses a Random Forest model to estimate fair prices based on car age, mileage, fuel type, transmission, seller type, and ownership history.

---

##  Project Structure

Used-Car-Price-Prediction/
│

├── data/

│ ├── raw/

│ │ └── CAR DETAILS FROM CAR DEKHO.csv

│ └── processed/

│ └── used_car_cleaned.csv

│

├── notebooks/

│ └── Predicting_car_price.ipynb

│

├── src/

│ ├── train_model.py

│ └── predict.py

│

├── outputs/

│ ├── model_predictions.csv

│ ├── test_predictions.csv

│ └── feature_importance.csv

│

├── images/

│ ├── price_distribution.png

│ ├── car_age_distribution.png

│ ├── feature_importance.png

│ └── residuals_plot.png

│

├── docs/

├── project_overview.md

├── modeling_process.md

└── insights_summary.md

└── README.md


---

##  Dataset Summary

- **Source:** CarDekho used-car dataset  
- **Total records:** 4,340 → **3,577 after removing duplicates**  
- Key features:
  - `car_age` (derived from year)
  - `km_driven`
  - `fuel`, `seller_type`, `transmission`
  - `owner`
  - `selling_price` (target)

---

##  EDA Highlights

- Prices are right-skewed; most cars fall under ₹10 lakh  
- Newer cars have significantly higher resale value  
- Automatic cars sell for more than manual  
- Higher mileage reduces price (negative correlation)  
- Diesel & petrol dominate the higher price bands  

---

##  Modelling Overview

Two models were evaluated:

| Model | R² | MAE | RMSE |
|-------|----|------|------|
| Linear Regression | 0.32 | 2.21L | 4.9L |
| **Random Forest (Final)** | **0.45** | **1.94L** | **4.2L** |

**Most important predictors:**  
- Car age  
- Kilometres driven  
- Transmission  
- Fuel type  

---

##  Business Value

- **Buyers:** Estimate fair value before negotiation  
- **Dealers:** Identify mispriced vehicles and optimize stock  
- **Platforms (Cars24/OLX):** Enable AI-based dynamic pricing  

This project shows complete ML workflow skills — from raw data to deploy-ready insights.

