# Battery-Capacity-Prediction-Using-Regression

## 1. Introduction
The Electric Vehicle (EV) Battery Capacity Prediction Model is designed to estimate the capacity of lithium-ion battery. This predictive capability is crucial for optimizing battery performance, ensuring efficient energy use, and enhancing the overall user experience of EVs.
## 2. Objective
The primary objective of the model is to predict capacity of the battery based on various trip-related parameters. This helps in predicting remaining useful battery life which provides insights into battery performance, planning optimal routes, and making informed decisions on battery management. 
## 3. Dataset Description
The dataset was obtained from NASA. The model is trained on a dataset containing the following features of Lithium-ion battery:
•	Voltage 
•	Current 
•	Temperature
•	Current Load
•	Voltage Load
•	Time
## 4. Data Preprocessing
The preprocessing steps include:
•	Handling Missing Values: Dropping or imputing missing values.
•	Histogram: Plotting histogram to visualize the distribution of values
•	Heat-map: Plotting heatmap to visualize correlation between various factors
## 5. Model Selection
We selected multiple regression models such as Extra Trees Regressor, Random Forest Regressor, Extreme Gradient Boosting, Gradient Boosting Regressor, Light Gradient Boosting Machine, Decision Tree Regressor, AdaBoost Regressor, Bayesian Ridge, Least Angle Regression, Ridge Regression, Linear Regression, Huber Regressor, K Neighbors Regressor, Elastic Net, Lasso Regression, Lasso Least Angle Regression, Passive Aggressive Regressor, Orthogonal Matching Pursuit and Dummy Regressor.
## 6. Model Training
The model is trained on 80% of the dataset, with the remaining 20% used for testing. The training involves fitting the model to the pre-processed features and the target variable (capacity).
## 7. Evaluation
We evaluated the models based on MAE(Mean Absolute Error), MSE(Mean Squared Error), RMSE(Root Mean Squared Error), R2(R squared value), RMSLE(Root Mean Squared Logarithmic Error), MAPE(Mean Absolute Percentage Error) and TT(Training Time in seconds).

## 8. Model Deployment
Using Pycaret, we deployed all the regression models on our dataset. We listed the model performance and found that ExtraTreeRegressor was the best model with 0.0059 MAE, 0.0001 MASE, 0.0086 RMSE, 0.9981 R2, 0.0033 RMSLE and 0.0037 MAPE. We further selected only 4 features, namely cycles, voltage_battery, temp_battery and time. We then deployed the model to a web application which accepts these values and predicts the value of capacity.

## 9. Conclusion
The EV Battery Usage Prediction Model is a powerful tool for optimizing battery performance in electric vehicles. By leveraging historical trip data and advanced machine learning techniques, the model provides accurate predictions of battery capacity, which can help users estimate the remaining useful life and make informed decisions on route planning and battery management.


