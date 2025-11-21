#  Modeling Process

This project follows a complete machine learning pipeline:

---

## 1️ Data Cleaning
- Removed duplicate rows  
- Extracted `car_age` from manufacturing year  
- Cleaned inconsistent text fields  
- Removed irrelevant columns (car name)

---

## 2️ Exploratory Data Analysis (EDA)
- Distribution analysis for `selling_price`, `km_driven`, `car_age`  
- Boxplots for fuel and transmission  
- Correlation heatmap  
- Found negative correlation between price and both age/mileage

---

## 3️ Feature Engineering
- Derived feature: `car_age = 2020 - year`
- One-hot encoded categorical variables
- Normalized numeric fields where needed

---

## 4️ Model Training
Models evaluated:
- Linear Regression  
- Random Forest Regressor (final model)

Hyperparameters tuned using default settings for baseline performance.

---

## 5️ Evaluation Metrics
- R² Score  
- Mean Absolute Error (MAE)  
- Root Mean Squared Error (RMSE)

Random Forest selected as best model:
- R² ≈ 0.45  
- MAE ≈ ₹1.94 lakh  
- RMSE ≈ ₹4.2 lakh

---

## 6️ Feature Importance
Top drivers of price:
- car_age  
- km_driven  
- transmission  
- fuel type
