# Stubs for pyspark.mllib.classification (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from pyspark.mllib.regression import LinearModel, StreamingLinearAlgorithm
from pyspark.mllib.util import Saveable, Loader

class LinearClassificationModel(LinearModel):
    def __init__(self, weights, intercept) -> None: ...
    def setThreshold(self, value): ...
    @property
    def threshold(self): ...
    def clearThreshold(self): ...
    def predict(self, test): ...

class LogisticRegressionModel(LinearClassificationModel):
    def __init__(self, weights, intercept, numFeatures, numClasses) -> None: ...
    @property
    def numFeatures(self): ...
    @property
    def numClasses(self): ...
    def predict(self, x): ...
    def save(self, sc, path): ...
    @classmethod
    def load(cls, sc, path): ...

class LogisticRegressionWithSGD:
    @classmethod
    def train(cls, data, iterations: int = ..., step: float = ..., miniBatchFraction: float = ..., initialWeights: Optional[Any] = ..., regParam: float = ..., regType: str = ..., intercept: bool = ..., validateData: bool = ..., convergenceTol: float = ...): ...

class LogisticRegressionWithLBFGS:
    @classmethod
    def train(cls, data, iterations: int = ..., initialWeights: Optional[Any] = ..., regParam: float = ..., regType: str = ..., intercept: bool = ..., corrections: int = ..., tolerance: float = ..., validateData: bool = ..., numClasses: int = ...): ...

class SVMModel(LinearClassificationModel):
    def __init__(self, weights, intercept) -> None: ...
    def predict(self, x): ...
    def save(self, sc, path): ...
    @classmethod
    def load(cls, sc, path): ...

class SVMWithSGD:
    @classmethod
    def train(cls, data, iterations: int = ..., step: float = ..., regParam: float = ..., miniBatchFraction: float = ..., initialWeights: Optional[Any] = ..., regType: str = ..., intercept: bool = ..., validateData: bool = ..., convergenceTol: float = ...): ...

class NaiveBayesModel(Saveable, Loader):
    labels = ...  # type: Any
    pi = ...  # type: Any
    theta = ...  # type: Any
    def __init__(self, labels, pi, theta) -> None: ...
    def predict(self, x): ...
    def save(self, sc, path): ...
    @classmethod
    def load(cls, sc, path): ...

class NaiveBayes:
    @classmethod
    def train(cls, data, lambda_: float = ...): ...

class StreamingLogisticRegressionWithSGD(StreamingLinearAlgorithm):
    stepSize = ...  # type: Any
    numIterations = ...  # type: Any
    regParam = ...  # type: Any
    miniBatchFraction = ...  # type: Any
    convergenceTol = ...  # type: Any
    def __init__(self, stepSize: float = ..., numIterations: int = ..., miniBatchFraction: float = ..., regParam: float = ..., convergenceTol: float = ...) -> None: ...
    def setInitialWeights(self, initialWeights): ...
    def trainOn(self, dstream): ...
