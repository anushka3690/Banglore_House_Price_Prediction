# Bangalore House Price Prediction

A machine learning project that predicts house prices in Bangalore based on various features like location, number of bedrooms (BHK), total square feet, and number of bathrooms.

## 🏠 Project Overview

This project uses machine learning algorithms to predict house prices in Bangalore. It includes data preprocessing, feature engineering, outlier removal, and model comparison to achieve the best prediction accuracy.

## 📊 Dataset

The project uses the `Bengaluru_House_Data.csv` dataset containing information about:
- Area type
- Availability
- Location
- Size (BHK)
- Society
- Total square feet
- Bathrooms
- Balcony
- Price

## 🔧 Data Preprocessing

### Data Cleaning Steps:
1. **Column Removal**: Dropped irrelevant columns (`area_type`, `availability`, `society`, `balcony`)
2. **Missing Value Handling**:
   - Location: Filled with 'Sarjapur Road'
   - Size: Filled with '2 BHK'
   - Bathrooms: Filled with median value
3. **Feature Engineering**:
   - Extracted numerical values from size column (removed 'BHK' text)
   - Converted range values in `total_sqft` to average values
   - Created `price_per_sqft` feature
4. **Location Grouping**: Locations with ≤10 occurrences grouped as 'other'

### Outlier Removal:
1. **Size-based filtering**: Removed properties with <300 sqft per BHK
2. **Price-based filtering**: Used standard deviation method to remove price outliers
3. **BHK comparison**: Removed properties where higher BHK has lower price than lower BHK in same location

## 🤖 Models Implemented

Three regression models were compared:

### 1. Linear Regression
- Basic linear regression without regularization
- R² Score: 0.82337

### 2. Lasso Regression
- L1 regularization to prevent overfitting
- R² Score: 0.81282

### 3. Ridge Regression
- L2 regularization for better generalization
- R² Score: 0.82341
- **Selected as final model**

### Model Performance:
- Ridge Regression was selected as the final model due to its superior performance and regularization benefits
- The model effectively captures the relationship between property features and prices in Bangalore's real estate market

## 🛠️ Technologies Used

- **Python 3.x**
- **Libraries**:
  - `pandas` - Data manipulation
  - `numpy` - Numerical operations
  - `scikit-learn` - Machine learning algorithms
  - `pickle` - Model serialization

## 🎯 Conclusion

This project successfully demonstrates the application of machine learning techniques for real estate price prediction in Bangalore. Through comprehensive data preprocessing, feature engineering, and outlier removal, we achieved a robust model capable of accurately predicting house prices. The Ridge regression model proved most effective, balancing bias and variance while preventing overfitting. This solution provides valuable insights into Bangalore's housing market and can serve as a foundation for real estate decision-making tools.