from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split

class data_preprocessing:
    def __init__(self,data) -> None:
        self.data = data
    
    def scaling_preprocess(self,scaling_type:str):
        """Scales data using min_max or standard scaler"""
        if scaling_type.lower() == 'standard_scaler':
            scaler = StandardScaler()
        elif scaling_type.lower() == 'min_max_scaler':
            scaler = MinMaxScaler()
        scaled_data = scaler.fit_transform(self.data)
        return scaled_data

    def train_test_split_preprocess(self,data,train_size:float):
        """
        Takes in data and train size
        ### Args
        - train_size: percentage of data that is used for training
        ### Returns
        - train_data: train data with length of (data * train_size)
        - test_data: remaining data
        """
        train_data,test_data = train_test_split(self.data,train_size)              
        return train_data,test_data

class model_construction(data_preprocessing):
    """
    Builds and trains various models using user passed hyperparameters and data inherited from data_preprocessing class.
    """
    def __init__(self,data,model_type:str,hp:dict) -> None:
        super().__init__(data) #inherit the data from preprocessing
        self.model_type = model_type
        self.hp = hp
    
    def model_object_creator(self):
        if self.model_type == 'linear_regression':
            model_object = LinearRegression()
        elif self.model_type == 'logistic_regression':
            model_object = LogisticRegression()
        return model_object
    
    def model_train_object(self,training_data):
        model_object = self.model_object(self.model_type)
        trained_object = model_object.train(training_data, self.hp)
        return trained_object
    
    def model_construct_pipeline(self):
        """
        Takes raw data and preprocesses, splits into testing and training, then fits a model
        
        Returns
        - train_object: A trained model object
        """
        scaled_data = self.scaling_preprocess(self.data) #scale the data
        train_data,test_data = self.train_test_split_preprocess(scaled_data) #train test split the data
        model_object = self.model_object_creator(self.model_type) #initialize the model type
        train_object = self.model_train_object(model_object,train_data) #train the model
        return train_object