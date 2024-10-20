# Multiple Linear Regression on Car_Purchasing
### Multiple Linear Regression using OOP in Python
This script demonstrates how to build a Multiple Linear Regression model using Object-Oriented Programming (OOP) principles in Python. Below is an in-depth explanation of the code and its components.

1. Importing Necessary Libraries
 The first part of the script imports essential libraries required for data handling, model training, and evaluation.

    import numpy as np
    import pandas as pd
    import sklearn
    import sys
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import r2_score
    import warnings
    warnings.filterwarnings('ignore')
- numpy and pandas are used for handling numerical and tabular data.
- train_test_split from sklearn is used to split the data into training and test sets.
- LinearRegression is the linear regression model from sklearn.
- r2_score is used to evaluate model accuracy.
- Warnings are suppressed using warnings.filterwarnings('ignore').

2. Defining the TRAINING Class
This class handles the training and testing of the Multiple Linear Regression model. The __init__ method is called when an object is created from the class, and the data_training, train_performance, and testing methods are responsible for training, evaluating, and testing the model.

2.1 Initialization - __init__()

    class TRAINING:
        def __init__(self, location):
            try:
                self.df = pd.read_csv(location)
                self.df = self.df.drop(['Customer Name', 'Customer e-mail', 'Country'], axis=1)
                self.X = self.df.iloc[:, :-1]
                self.y = self.df.iloc[:, -1]
                self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
            except Exception as e:
                error_type, error_msg, error_line = sys.exc_info()
                print(f'Error from line {error_line.tb_lineno} -> type {error_type} -> Error msg -> {error_msg}')

self.df loads the CSV file using pd.read_csv(), self.df.drop() removes unnecessary columns (Customer Name, Email, and Country).self.X contains the independent variables, while self.y holds the dependent variable (target), train_test_split splits the dataset into 80% training data and 20% testing data.

2.2 Data Training - data_training()

    def data_training(self):
    try:
        self.reg = LinearRegression()
        self.reg.fit(self.X_train, self.y_train)
    except Exception as e:
        error_type, error_msg, error_line = sys.exc_info()
        print(f'Error from line {error_line.tb_lineno} -> type {error_type} -> Error msg -> {error_msg}')

self.reg initializes a Linear Regression model,self.reg.fit() fits the model to the training data.

2.3 Evaluating Training Performance - train_performance()

    def train_performance(self):
    try:
        self.y_train_pred = self.reg.predict(self.X_train)
        Training_data_performance = pd.DataFrame(self.X_train.copy())
        Training_data_performance['Actual_Y_train'] = self.y_train
        Training_data_performance['Y_train_predictions'] = self.y_train_pred
        print(f' Train Accuracy : -> {r2_score(self.y_train, self.y_train_pred)}')

self.reg.predict() generates predictions for the training data.
The predicted and actual values are stored in a DataFrame Training_data_performance. The model's accuracy on the training data is printed using r2_score().

2.4 Testing the Model - testing()

    def testing(self):
    try:
        self.y_test_pred = self.reg.predict(self.X_test)
        Testing_data_performance = pd.DataFrame(self.X_test.copy())
        Testing_data_performance['Actual_Y_test'] = self.y_test
        Testing_data_performance['Y_test_predictions'] = self.y_test_pred
        print(f' Test Accuracy : -> {r2_score(self.y_test, self.y_test_pred)}')

self.reg.predict() generates predictions for the test data.
Both the actual and predicted values are stored in Testing_data_performance, the model's accuracy on the test data is printed using r2_score().

3. Evaluating Errors
The code also calculates Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and Mean Absolute Error (MAE) to evaluate how well the model performs.

### Mean Squared Error (MSE)

    count = 0
    for i in Training_data_performance.index:
        count = count + (Training_data_performance['Actual_Y_train'][i] - Training_data_performance['Y_train_predictions'][i]) ** 2
        mse = count / len(Training_data_performance)
    print(f'Mean Squared Error: {mse}')

### Root Mean Squared Error (RMSE)
    rmse = mse ** 0.5
    print(f'Root Mean Squared Error: {rmse}')

### Mean Absolute Error (MAE)
    count = 0
    for i in Training_data_performance.index:
        count += abs(Training_data_performance['Actual_Y_train'][i] - Training_data_performance['Y_train_predictions'][i])
        mae = count / len(Training_data_performance)
    print(f'Mean Absolute Error: {mae}')

These metrics help quantify the differences between the actual and predicted values.

4. Running the Code


        if __name__ == "__main__":
        try:
            obj = TRAINING('C:\\Users\\u\\Downloads\\REG-ASS\\Assignment\\Car_Purchasing_Data.csv')
            obj.data_training()
            obj.train_performance()
            obj.testing()
        except Exception as e:
            error_type, error_msg, error_line = sys.exc_info()
            print(f'Error from line {error_line.tb_lineno} -> type {error_type} -> Error msg -> {error_msg}')

The main section of the code creates an instance of the TRAINING class and calls the necessary methods to train, evaluate, and test the model.

