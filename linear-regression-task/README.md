# 🏠 Linear Regression Task — House Price Prediction

## 📌 Objective
This project demonstrates both simple and multiple linear regression using scikit-learn to predict house prices based on features like area, bedrooms, bathrooms, and more.

---

## 📁 Dataset

- **Source**: [Kaggle Housing Price Prediction Dataset](https://www.kaggle.com/datasets/harishkumardatalab/housing-price-prediction)
- **File**: `house_prices.csv` (placed in the `data/` folder)
- **Columns**:
  - `price` (target)
  - `area`, `bedrooms`, `bathrooms`, `stories`, `parking`
  - Categorical: `mainroad`, `guestroom`, `basement`, `hotwaterheating`, `airconditioning`, `prefarea`, `furnishingstatus`

---

## 🧪 Project Structure
inear-regression-task/ ├── data/ │   └── house_prices.csv ├── src/ │   ├── simple_regression.py │   └── multiple_regression.py ├── plots/ │   └── regression_plot.png ├── requirements.txt └── README.md

---

## 🛠️ Setup Instructions

```bash
# Create virtual environment (optional)
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run simple regression
cd src
python simple_regression.py

# Run multiple regression
python multiple_regression.py




