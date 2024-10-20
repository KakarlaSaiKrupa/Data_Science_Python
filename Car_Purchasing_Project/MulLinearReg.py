'''
In this file we are going to develop and Multiple Linear Regression with Oops concept
'''
import numpy as np
import pandas as pd
import sklearn
import sys
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import warnings
warnings.filterwarnings('ignore')
#from sklearn.metrics import mean_squared_error

class TRAINING:
  def __init__(self, location):
    try:
      self.df=pd.read_csv(location)
      self.df = self.df.drop(['Customer Name','Customer e-mail', 'Country'], axis =1)
      #print(self.df)
      self.X = self.df.iloc[:, :-1]  # independent
      self.y = self.df.iloc[:, -1]  # dependent
      #print(self.X)
      #print(self.y)
      self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
      #print(len(self.X_train), len(self.y_train))
      #print(len(self.X_test), len(self.y_test))
    except Exception as e:
      error_type, error_msg, error_line = sys.exc_info()
      print(f'Error from line {error_line.tb_lineno} -> type {error_type} -> Error msg -> {error_msg}')

  def data_training(self):
    try:
      self.reg = LinearRegression()
      self.reg.fit(self.X_train, self.y_train)
    except Exception as e:
      error_type, error_msg, error_line = sys.exc_info()
      print(f'Error from line {error_line.tb_lineno} -> type {error_type} -> Error msg -> {error_msg}')

  def train_performance(self):
    try:
      self.y_train_pred = self.reg.predict(self.X_train)
      #print(self.y_train_pred)
      Training_data_performance = pd.DataFrame()
      Training_data_performance = self.X_train.copy()
      Training_data_performance['Actual_Y_train'] = self.y_train.copy()
      Training_data_performance['Y_train_predictions'] = self.y_train_pred
      #print(Training_data_performance)
      print(f' Train Accuracy : -> {r2_score(self.y_train, self.y_train_pred)}')
# MEAN SQUARED ERROR - TRAIN LOSS
      count = 0
      for i in Training_data_performance.index:
          count = count + (Training_data_performance['Actual_Y_train'][i] - Training_data_performance['Y_train_predictions'][i]) ** 2
          mse = count / len(Training_data_performance)
      print(f'Mean Squared Error: {mse}')
# ROOT MEAN SQUARED ERROR
      count = 0
      for i in Training_data_performance.index:
          count = count + (Training_data_performance['Actual_Y_train'][i] - Training_data_performance['Y_train_predictions'][i]) ** 2
          mse = count / len(Training_data_performance)
          rmse = (mse) ** 0.5
      print(f'Root Mean Squared Error: {rmse}')
#MEAN ABSOLUTE ERROR
      count = 0
      for i in Training_data_performance.index:
        count += abs(Training_data_performance['Actual_Y_train'][i] - Training_data_performance['Y_train_predictions'][i])
        mae = count / len(Training_data_performance)
      print(f'Mean Absolute Error: {mae}')
    except Exception as e:
      error_type, error_msg, error_line = sys.exc_info()
      print(f'Error from line {error_line.tb_lineno} -> type {error_type} -> Error msg -> {error_msg}')
  def testing(self):
         try:
             self.y_test_pred = self.reg.predict(self.X_test)
             #print(self.y_test_pred)
             #print(self.y_test_pred.shape)
             Testing_data_performance = pd.DataFrame()
             Testing_data_performance = self.X_test.copy()
             Testing_data_performance['Actual_Y_test'] = self.y_test.copy()
             Testing_data_performance['Y_test_predictions'] = self.y_test_pred
             #print(Testing_data_performance)
             print(f' Test Accuracy : -> {r2_score(self.y_test, self.y_test_pred)}')
# MEAN SQUARED ERROR - TEST LOSS
             count = 0
             for i in Testing_data_performance.index:
                 count = count + (Testing_data_performance['Actual_Y_test'][i] - Testing_data_performance['Y_test_predictions'][i]) ** 2
                 mse = count / len(Testing_data_performance)
             print(f'Mean Squared Error: {mse}')
# ROOT MEAN SQUARED ERROR
             count = 0
             for i in Testing_data_performance.index:
                 count = count + (Testing_data_performance['Actual_Y_test'][i] - Testing_data_performance['Y_test_predictions'][i]) ** 2
                 mse = count / len(Testing_data_performance)
                 rmse = (mse) ** 0.5
             print(f'Root Mean Squared Error: {rmse}')
# MEAN ABSOLUTE ERROR
             count = 0
             for i in Testing_data_performance.index:
                 count += abs(Testing_data_performance['Actual_Y_test'][i] - Testing_data_performance['Y_test_predictions'][i])
                 mae = count / len(Testing_data_performance)
             print(f'Mean Absolute Error: {mae}')
         except Exception as e:
             error_type, error_msg, error_line = sys.exc_info()
             print(f'Error from line {error_line.tb_lineno} -> type {error_type} -> Error msg -> {error_msg}')

if __name__ == "__main__":
    try:
        obj = TRAINING('C:\\Users\\u\\Downloads\\REG-ASS\\Assignment\\Car_Purchasing_Data.csv') #constructor will be called
        obj.data_training()
        obj.train_performance()
        obj.testing()

    except Exception as e:
        error_type, error_msg, error_line = sys.exc_info()
        print(f'Error from line {error_line.tb_lineno} -> type {error_type} -> Error msg -> {error_msg}')


