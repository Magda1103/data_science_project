from sklearn.base import BaseEstimator, TransformerMixin

class DelayCombiner(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return 1
    def transform(self, X):
        return 1

class FeatureSelector(BaseEstimator, TransformerMixin):
    def __init__(self, features):
        self.features = features
    def fit(self, X, y=None):
        return 1
    def transform(self, X):
        return 1