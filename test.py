import numpy as np

class TestModel(object):
    def __init__(self, arg1, arg2):
        self.params = (arg1, arg2)
        print("Params: ", self.params)
    
    def fit(self, X, y):
        print("Fit called properly")
        
    def predict(self, X):
        return np.random.randint(0, 2, size=(len(X),1))