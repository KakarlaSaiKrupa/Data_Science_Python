import numpy as np
import pandas as pd
import sklearn
import sys
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
import warnings
warnings.filterwarnings('ignore')

class TRAINING:
  def __init__(self, location):
    try:
      self.df=pd.read_csv(location)
      self.df = self.df.drop(['date','waterfront', 'view', 'condition','yr_renovated','street', 'city',
       'statezip'],axis =1)
      self.df['country'] = self.df['country'].map({'USA':0}).astype(int)
      self.X = self.df.iloc[:, 1:]  # independent
      self.y = self.df.iloc[:,0]  # dependent
      self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
    except Exception as e:
      error_type, error_msg, error_line = sys.exc_info()
      print(f'Error from line {error_line.tb_lineno} -> type {error_type} -> Error msg -> {error_msg}')

  def data_training(self):
    try:
      self.reg = LinearRegression()
      self.reg.fit(self.X_train, self.y_train)  # training
    except Exception as e:
      error_type, error_msg, error_line = sys.exc_info()
      print(f'Error from line {error_line.tb_lineno} -> type {error_type} -> Error msg -> {error_msg}')

  def train_performance(self):
    try:
      self.y_train_pred = self.reg.predict(self.X_train)
      Training_data_performance = pd.DataFrame()
      Training_data_performance = self.X_train.copy()
      Training_data_performance['Actual_Y_train'] = self.y_train.copy()
      Training_data_performance['Y_train_predictions'] = self.y_train_pred
      print(f' Train Accuracy : -> {r2_score(self.y_train, self.y_train_pred)}')
      count = 0
      for i in Training_data_performance.index:
          count = count + (Training_data_performance['Actual_Y_train'][i] - Training_data_performance['Y_train_predictions'][i])**2
          mse = count / len(Training_data_performance)
      print(f'Mean Squared Error: {mse}')
      count = 0
      for i in Training_data_performance.index:
          count = count + (Training_data_performance['Actual_Y_train'][i] - Training_data_performance['Y_train_predictions'][i])**2
          mse = count / len(Training_data_performance)
          rmse = (mse)**0.5  # square root of mse
      print(f'Root Mean Squared Error: {rmse}')
      count = 0
      for i in Training_data_performance.index:
        count += abs(Training_data_performance['Actual_Y_train'][i] - Training_data_performance['Y_train_predictions'][i])
        mae = count / len(Training_data_performance)
      print(f'Mean Absolute Error: {mae}')
      print('----------------------------------------------------')
    except Exception as e:
      error_type, error_msg, error_line = sys.exc_info()
      print(f'Error from line {error_line.tb_lineno} -> type {error_type} -> Error msg -> {error_msg}')

  def testing(self):
    try:
      self.y_test_pred = self.reg.predict(self.X_test)
      Testing_data_performance = pd.DataFrame()
      Testing_data_performance = self.X_test.copy()
      Testing_data_performance['Actual_Y_test'] = self.y_test.copy()
      Testing_data_performance['Y_test_predictions'] = self.y_test_pred
      print(f' Test Accuracy : -> {r2_score(self.y_test, self.y_test_pred)}')
      count = 0
      for i in Testing_data_performance.index:
        count = count + (Testing_data_performance['Actual_Y_test'][i] - Testing_data_performance['Y_test_predictions'][i])**2
        mse = count / len(Testing_data_performance)
      print(f'Mean Squared Error: {mse}')
      count = 0
      for i in Testing_data_performance.index:
        count = count + (Testing_data_performance['Actual_Y_test'][i] - Testing_data_performance['Y_test_predictions'][i])**2
        mse = count / len(Testing_data_performance)
        rmse = (mse)**0.5  # square root of mse
      print(f'Root Mean Squared Error: {rmse}')
      count = 0
      for i in Testing_data_performance.index:
        count += abs(Testing_data_performance['Actual_Y_test'][i] - Testing_data_performance['Y_test_predictions'][i])
        mae = count / len(Testing_data_performance)
      print(f'Mean Absolute Error: {mae}')
    except Exception as e:
      error_type, error_msg, error_line = sys.exc_info()
      print(f'Error from line {error_line.tb_lineno} -> type {error_type} -> Error msg -> {error_msg}')

  def ridge(self):
    try:
      self.reg_ridge = Ridge()
      self.reg_ridge.fit(self.X_train,self.y_train)
      f = pd.DataFrame()
      f['independent_columns'] = self.X_train.columns
      f['Model_M_values'] = self.reg.coef_  # corrected reference to reg
      f['Ridge_m_values'] = self.reg_ridge.coef_  # corrected reference to reg_ridge
      print(f)
    except Exception as e:
      error_type, error_msg, error_line = sys.exc_info()
      print(f'Error from line {error_line.tb_lineno} -> type {error_type} -> Error msg -> {error_msg}')

  def lasso(self):
    try:
      self.reg_lasso = Lasso()
      self.reg_lasso.fit(self.X_train, self.y_train)
      print('---------------------------------------------------')
      print(f'model train accuracy: {self.reg.score(self.X_train, self.y_train)}')  # corrected reference to reg
      print(f'model test accuracy: {self.reg.score(self.X_test, self.y_test)}')
      print('---------------------------------------------------')

      print(f'Ridge model train accuracy: {self.reg_ridge.score(self.X_train, self.y_train)}')
      print(f'Ridge model test accuracy: {self.reg_ridge.score(self.X_test, self.y_test)}')
      print('---------------------------------------------------')

      print(f'Lasso model train accuracy: {self.reg_lasso.score(self.X_train, self.y_train)}')
      print(f'Lasso model test accuracy: {self.reg_lasso.score(self.X_test, self.y_test)}')
      print('----------------------------------------------------')
      f = pd.DataFrame()
      f['independent_columns'] = self.X_train.columns
      f['Model_M_values'] = self.reg.coef_  # corrected reference to reg
      f['Ridge_m_values'] = self.reg_ridge.coef_  # corrected reference to reg_ridge
      f['Lasso_m_values'] = self.reg_lasso.coef_  # corrected reference to reg_lasso
      print(f)
    except Exception as e:
      error_type, error_msg, error_line = sys.exc_info()
      print(f'Error from line {error_line.tb_lineno} -> type {error_type} -> Error msg -> {error_msg}')

if __name__ == "__main__":
    try:
        obj = TRAINING('C:\\Users\\u\\Downloads\\House_Project\\House_Price_Pred\\House_price_prediction.csv') #constructor will be called
        obj.data_training()
        obj.train_performance()
        obj.testing()
        obj.ridge()
        obj.lasso()
    except Exception as e:
        error_type, error_msg, error_line = sys.exc_info()
        print(f'Error from line {error_line.tb_lineno} -> type {error_type} -> Error msg -> {error_msg}')
