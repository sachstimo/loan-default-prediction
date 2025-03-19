# Loan Default Prediction System

## Overview
This project predicts the likelihood of loan defaults using machine learning techniques to help financial institutions make more informed investment decisions. By analyzing historical loan data from Lending Club, we've developed a model that predicts which loans are likely to default, allowing for strategic investment decisions that maximize returns while managing risk.

## Project Structure
```
├── DATA/                      # Data files
│   ├── active_loans.parquet   # Current active loans for prediction
│   ├── Loan_Lending_Club.csv  # Historical loan data for training
│   ├── recovery_info.json     # Recovery rates by loan grade
│   └── Variable Definition.xlsx # Detailed field descriptions
├── OUTPUT/                    # Generated output files
│   ├── Metrics/               # Model performance metrics
│   ├── Models/                # Saved model files
│   ├── Plots/                 # Visualizations
│   └── Processing/            # Preprocessing pipeline artifacts
├── business_predictions.ipynb # Analysis of profitability strategies
├── column_descriptions.md     # Documentation of dataset fields
├── loan_processing.py         # Utility functions for data processing
├── model_training.ipynb       # Model development notebook
├── readme.md                  # This documentation
└── requirements.txt           # Project dependencies
```

## Business Problem
Investors in private debt need to be able to assess loan default risk accurately to make profitable investment decisions. This project addresses this challenge by:

1. Predicting which loans are likely to default
2. Calculating optimal discount rates for purchasing loans
3. Evaluating investment strategies across different loan grades (A-G)
4. Determining break-even points for profitability

## Data
The dataset includes historical Lending Club loans with detailed borrower information, loan characteristics, and payment history. Key features include:

- **Borrower Information**: Employment, income, debt-to-income ratio, ...
- **Loan Details**: Amount, term, interest rate, grade, ...
- **Credit History**: FICO scores, delinquencies, credit utilization, ...
- **Payment Information**: Payment amounts, outstanding principal, ...

## Methodology

### 1. Data Preprocessing
- Handle missing values using appropriate strategies for different feature types
- Convert date columns to numerical features
- Process categorical variables using one-hot encoding and ordinal encoding
- Remove highly correlated features to reduce multicollinearity
- Create engineered features such as FICO score changes

### 2. Feature Engineering
- Convert percentage strings to numerical values
- Extract month and year information from dates
- Create loan time-to-maturity calculations
- Generate avg. FICO scores, FICO delta and downgrade indicators

### 3. Model Development
We implemented an ensemble approach combining:
- **XGBoost**: Handles non-linear relationships effectively
- **LightGBM**: Efficient gradient boosting framework

The ensemble is wrapped in a pipeline that includes:
- Imputation for missing values
- SMOTE for handling class imbalance
- Hyperparameter optimization using RandomizedSearchCV
- Model export to re-use in the prediction notebook

### 4. Business Application
The [`business_predictions.ipynb`](business_predictions.ipynb) notebook demonstrates how the model can be applied to make profitable investment decisions by:
- Calculating expected profit at different default probability thresholds
- Determining break-even discount rates for each loan grade
- Recommending optimal investment strategies based on risk tolerance

## Best Results - so far
The model achieves:
- Accuracy: 90.2%
- Precision: 76.0%
- Recall: 76.2%
- F1 Score: 76.1%
- ROC AUC: 94.8%

These metrics indicate that the model is somewhat effective at identifying defaulting loans, but definitely struggles at identifying all of them. This could be due to the quite rigorous feature selection, where a lot of features where removed a priori due to potential data leakage. In a real-life scenario, some of them might still be available even during the prediction phase.

## Key Insights
1. **Grade-based risk assessment**: Higher grade loans (A, B) have significantly lower default probabilities than lower grades (E, F, G)
2. **Profitability across grades**: Even with higher default rates, lower grade loans can be profitable with appropriate discount rates
3. **FICO score importance**: FICO score changes are strong predictors of default risk
4. **Low false negative rate critical**: Misclassifying defaulting loans as safe (false negatives) significantly impacts profitability

## How to Use

### Setup
```bash
# Clone the repository
git clone https://github.com/sachstimo/loan-predictions.git
cd loan-predictions

# Install dependencies
pip install -r requirements.txt
```
### Downloading the Dataset

Download the dataset from [Kaggle](https://www.kaggle.com/datasets/wordsforthewise/lending-club) and save it as `DATA/Loan_Lending_Club.csv`.

### Training a Model
Run the [`model_training.ipynb`](model_training.ipynb) notebook to:
1. Load and preprocess the historical loan data
2. Train the ensemble model
3. Evaluate model performance
4. Save the model and preprocessing pipeline

### Making Predictions
Run the [`business_predictions.ipynb`](business_predictions.ipynb) notebook to:
1. Load active loans for prediction
2. Apply the pre-trained model to predict default probabilities
3. Calculate expected profit / minimum required discount for different investment strategies
4. Visualize results by loan grade

## Requirements
```
pandas>=1.3.0
numpy>=1.20.0
scikit-learn>=1.0.0
matplotlib>=3.4.0
seaborn>=0.11.0
xgboost>=1.4.0
lightgbm>=3.2.0
imbalanced-learn>=0.8.0
joblib>=1.0.0
pyarrow>=5.0.0
```

## Future Improvements
1. Tweak feature engineering approach to improve recall rates for improved default detection
2. Develop a more sophisticated recovery rate model by loan grade

## License
This project is licensed under the MIT License - see the LICENSE file for details.