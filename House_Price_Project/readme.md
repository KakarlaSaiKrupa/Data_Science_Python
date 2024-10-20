# Multiple Linear Regression on House_Price_Prediction
### Multiple Linear Regression Using OOP
    This Python script demonstrates how to implement Multiple Linear Regression using Object-Oriented Programming (OOP). The script includes data preprocessing, model training, evaluation metrics, and additional regularization techniques like Ridge and Lasso.

1. Importing Required Libraries

The script begins by importing the necessary libraries:
        - numpy
        - pandas for handling arrays and data manipulation.
        - sklearn for machine learning algorithms, 
          such as  LinearRegression ,Ridge, and Lasso.
        - sys for handling errors and exceptions in the program.

    import numpy as np
    import pandas as pd
    import sklearn
    import sys
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import r2_score, mean_squared_error
    from sklearn.linear_model import Ridge, Lasso


2. Defining the TRAINING Class

The TRAINING class encapsulates the entire regression process, including data preparation, model training, evaluation, and testing. Here's a breakdown of the key methods:

    __init__(self, location) Constructor

This method initializes the class by loading the dataset and splitting it into features (X) and target labels (y). It also performs a train-test split:
     
    pd.read_csv(location) loads the CSV file containing the dataset.

The script drops unnecessary columns and encodes categorical data (like 'USA').
It splits the dataset into training and testing sets using train_test_split.

    class TRAINING:
      def __init__(self, location):
    try:
      self.df = pd.read_csv(location)
      self.df = self.df.drop(['date', 'waterfront', 'view', 'condition', 'yr_renovated', 'street', 'city', 'statezip'], axis=1)
      self.df['country'] = self.df['country'].map({'USA': 0}).astype(int)
      self.X = self.df.iloc[:, 1:]
      self.y = self.df.iloc[:, 0]
      self.X_train, self.X_test, self.y_train, self.y_test =    train_test_split(self.X, self.y, test_size=0.2, random_state=42)
    except Exception as e:
      error_type, error_msg, error_line = sys.exc_info()
      print(f'Error from line {error_line.tb_lineno} -> type {error_type} -> Error msg -> {error_msg}')

- data_training(self)
This method trains the Linear Regression model on the training data: LinearRegression() initializes the linear regression model.
self.reg.fit(self.X_train, self.y_train) fits the model on the training data.

    def data_training(self):
    try:
    self.reg = LinearRegression()
    self.reg.fit(self.X_train, self.y_train)
    except Exception as e:
      error_type, error_msg, error_line = sys.exc_info()
      print(f'Error from line {error_line.tb_lineno} -> type {error_type} -> Error msg -> {error_msg}')


- train_performance(self)
This method evaluates the performance of the trained model using the training dataset: Predictions are generated using self.reg.predict(self.X_train). The accuracy (R² score), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and Mean Absolute Error (MAE) are calculated and displayed.

    def train_performance(self):
     try:
    self.y_train_pred = self.reg.predict(self.X_train)
    Training_data_performance = pd.DataFrame(self.X_train.copy())
    Training_data_performance['Actual_Y_train'] = self.y_train.copy()
    Training_data_performance['Y_train_predictions'] = self.y_train_pred
    print(f'Train Accuracy: {r2_score(self.y_train, self.y_train_pred)}')
    mse = mean_squared_error(self.y_train, self.y_train_pred)
    rmse = mse ** 0.5
    mae = np.mean(np.abs(self.y_train - self.y_train_pred))
    print(f'Mean Squared Error: {mse}')
    print(f'Root Mean Squared Error: {rmse}')
    print(f'Mean Absolute Error: {mae}')
    except Exception as e:
      error_type, error_msg, error_line = sys.exc_info()
      print(f'Error from line {error_line.tb_lineno} -> type {error_type} -> Error msg -> {error_msg}')

- testing(self)
This method evaluates the performance of the trained model using the test dataset: Similar to train_performance, it calculates the R², MSE, RMSE, and MAE for the test set.

    def testing(self):
    try:
      self.y_test_pred = self.reg.predict(self.X_test)
      print(f'Test Accuracy: {r2_score(self.y_test, self.y_test_pred)}')
      mse = mean_squared_error(self.y_test, self.y_test_pred)
      rmse = mse ** 0.5
      mae = np.mean(np.abs(self.y_test - self.y_test_pred))
      print(f'Mean Squared Error: {mse}')
      print(f'Root Mean Squared Error: {rmse}')
      print(f'Mean Absolute Error: {mae}')
    except Exception as e:
      error_type, error_msg, error_line = sys.exc_info()
      print(f'Error from line {error_line.tb_lineno} -> type {error_type} -> Error msg -> {error_msg}')

- ridge(self) and lasso(self)
These methods apply Ridge and Lasso regression techniques for regularization: In ridge(self), the Ridge() model is used to reduce overfitting by adding a regularization term. In lasso(self),the Lasso() model adds regularization and also performs feature selection by shrinking less important features to zero.

    def ridge(self):
    try:
      self.reg_ridge = Ridge()
      self.reg_ridge.fit(self.X_train, self.y_train)
      print(f'Ridge coefficients: {self.reg_ridge.coef_}')
    except Exception as e:
    error_type, error_msg, error_line = sys.exc_info()
    print(f'Error from line {error_line.tb_lineno} -> type {error_type} -> Error msg -> {error_msg}')

    def lasso(self):
    try:
     self.reg_lasso = Lasso()
     self.reg_lasso.fit(self.X_train, self.y_train)
     print(f'Lasso coefficients: {self.reg_lasso.coef_}')
    except Exception as e:
     error_type, error_msg, error_line = sys.exc_info()
     print(f'Error from line {error_line.tb_lineno} -> type {error_type} -> Error msg -> {error_msg}')

- Main Block
In the main block, an instance of the TRAINING class is created, and all methods are executed in sequence to load the dataset, train the model, and evaluate its performance:

    if __name__ == "__main__":
       try:
          obj = TRAINING('/content/House_price_prediction.csv')
          obj.data_training()
          obj.train_performance()
          obj.testing()
          obj.ridge()
          obj.lasso()
    except Exception as e:
      error_type, error_msg, error_line = sys.exc_info()
      print(f'Error from line {error_line.tb_lineno} -> type {error_type} -> Error msg -> {error_msg}')

