# Battery-Capacity-Prediction-Using-Regression

## 1. Introduction
Electric vehicles (EVs) are transforming transportation with eco-friendly alternatives to gasoline-powered cars. However, battery life and range anxiety remain significant challenges. Accurately predicting battery capacity is crucial for optimizing charging schedules, extending battery lifespan, and enhancing the overall EV user experience.

## 2. Objective
Our machine learning model predicts the remaining capacity of lithium-ion batteries in EVs. By analyzing factors like voltage, current, temperature, and load, the model provides insights into battery health. This helps EV owners make informed decisions on charging schedules, driving habits, and vehicle management, ultimately extending battery life and reducing range anxiety.

## 3. Dataset Description
We used a high-quality dataset from NASA, including parameters like voltage, current, temperature, current load, voltage load, and time. These features are critical for understanding lithium-ion battery behavior under various conditions.

## 4. Data Preprocessing
Preprocessing steps included:
- **Handling Missing Values**: Addressing missing values through imputation or removal.
- **Exploratory Data Analysis (EDA)**: Visualizing feature distributions with histograms and identifying correlations with heatmaps.
These steps ensured data quality and prepared the dataset for accurate battery capacity prediction.

## 5. Model Selection
We explored various regression models, including:
- **Ensemble Methods**: Extra Trees Regressor, Random Forest Regressor, XGBoost, Gradient Boosting Regressor, LightGBM, AdaBoost Regressor.
- **Linear Models**: Linear Regression, Ridge Regression, Lasso Regression, Elastic Net, Bayesian Ridge, Least Angle Regression.
- **Non-linear Models**: Decision Tree Regressor, K-Nearest Neighbors Regressor, Huber Regressor, Passive Aggressive Regressor, Orthogonal Matching Pursuit.
- **Baseline Model**: Dummy Regressor.
This comprehensive exploration helped identify the most suitable algorithm for predicting battery capacity.

## 6. Model Training
We trained the models using an 80/20 train-test split. Each model was fitted to the preprocessed features, with battery capacity as the target variable. This approach enabled the models to learn complex patterns in the data, leading to accurate predictions.

## 7. Evaluation
We evaluated the models using metrics like MAE, MSE, RMSE, R², RMSLE, MAPE, and Training Time. This comprehensive evaluation provided a clear understanding of each model's performance, helping us select the best candidate.

## 8. Model Deployment
Using PyCaret, we deployed various regression models and found that ExtraTreesRegressor performed the best with outstanding metrics. We then identified four key features—cycles, voltage_battery, temp_battery, and time—and deployed the model to a web application. This application allows users to input these values and get real-time battery capacity predictions.

## 9. Conclusion
Our EV Battery Capacity Prediction Model optimizes battery performance by accurately predicting battery capacity. This empowers users to make informed decisions about driving habits and charging schedules, alleviating range anxiety and extending battery life. As battery technology evolves, our model can incorporate additional factors for even more accurate and personalized predictions.

---

# Installation and Usage Tutorial

## Installation and Usage Tutorial

# Clone the Repository
git clone https://github.com/yourusername/Battery-Capacity-Prediction-Using-Regression.git
cd Battery-Capacity-Prediction-Using-Regression

# Create and Activate a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install the Required Packages
pip install -r requirements.txt

# Run the Jupyter Notebook
cd working_directory
jupyter notebook

# Deploy the Model
cd ../app
flask run

# Access the web application
# Open your web browser and go to http://127.0.0.1:5000/
