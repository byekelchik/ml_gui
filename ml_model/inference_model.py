from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import *

class model_prediction():
    def __init__(self, inference_data, problem_type) -> None:
        self.inference_data = inference_data
        self.problem_type = problem_type
    
    def perform_inference(self, trained_model_object):
        """
        Take a model object and performs inference.
        **NEED to build a check in that makes sure the inference data is same shape as model object input
        """
        predictions = trained_model_object.predict(self.inference_data)
        return predictions

    def calc_performance(self,test_data):
        """
        Need to make sure that inference data and test_data is the same length
        Return model performance metrics given what type of 
        """
        if self.problem_type.lower() == 'regression':
            r2 = r2_score(self.inference_data, test_data)
            mae = mean_squared_error(self.inference_data, test_data)
            mse = mean_squared_error(self.inference_data, test_data)
            return r2, mae, mse
        elif self.problem_type.lower() == 'classifcation':
            area_under_curve = auc(self.inference_data, test_data)
            conf_matrix = confusion_matrix(self.inference_data, test_data)
            f1 = f1_score(self.inference_data, test_data)
            recall = recall_score(self.inference_data, test_data)
            return area_under_curve, conf_matrix, f1, recall




