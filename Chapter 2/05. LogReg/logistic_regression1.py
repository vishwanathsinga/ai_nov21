import numpy as np
from sklearn import linear_model


class LogisticRegression:

    def __init__(self, lr=0.001, n_iters=1000):
        self.lr = lr 
        self.n_iters = n_iters
        self.weights = None
        self.bias = None


    def _sigmoid(self,x):
        return 1/(1+np.exp(-x))

        


    def fit(self,x,y):
        #init parameters
        n_samples,n_features = x.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        #gradient descent
        for _ in range(self.n_iters):
            linear_model = np.dot(x, self.weights) + self.bias
            y_predicted = self._sigmoid(linear_model)

            dw = (1/n_samples) * np.dot(x.T,(y_predicted - y))
            db = (1/n_samples) * np.sum(y_predicted - y)

            self.weights -= self.lr * dw
            self.bias -= self.db




    def predict(self,x):
        linear_model = np.dot(x, self.weights) + self.bias
        y_predicted = self._sigmoid(linear_model)
        y_predicted_cls = [1 if i > 0.5 else 0 for i in y_predicted]
        return y_predicted_cls







       