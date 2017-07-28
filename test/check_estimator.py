import sys
import os
import sklearn
import sklearn.utils.estimator_checks

sys.path.append(os.pardir)
from SklearnWrapper import SklearnWrapperClassifier, SklearnWrapperRegressor
from examples.mlp import MLP

#estimator = SklearnWrapperClassifier(MLP(10, 10))
#sklearn.utils.estimator_checks.check_estimator(estimator)

print('Classifier test')
sklearn.utils.estimator_checks.check_estimator(SklearnWrapperClassifier)

print('Regressor test')
sklearn.utils.estimator_checks.check_estimator(SklearnWrapperRegressor)
