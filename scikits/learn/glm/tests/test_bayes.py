# Author: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#         Fabian Pedregosa <fabian.pedregosa@inria.fr>
#
# License: BSD Style.

import numpy as np

from numpy.testing import assert_array_equal, \
                          assert_array_almost_equal, decorators

from ..bayes import BayesianRidge, ARDRegression

from scikits.learn import datasets

@decorators.skipif(True, "XFailed test")
def test_bayesian_on_diabetes():
    """
    Test BayesianRidge on diabetes
    """
    diabetes = datasets.load_diabetes()
    X, y = diabetes.data, diabetes.target

    clf = BayesianRidge(compute_score=True)

    # Test with more samples than features
    clf.fit(X, y)
    # Test that scores are increasing at each iteration
    assert_array_equal(np.diff(clf.scores_) > 0, True)

    # Test with more features than samples
    X = X[:5,:]
    y = y[:5]
    clf.fit(X, y)
    # Test that scores are increasing at each iteration
    assert_array_equal(np.diff(clf.scores_) > 0, True)


def test_toy_bayesian_ridge_object():
    """
    Test BayesianRidge on toy
    """
    X = np.array([[1], [2], [6], [8], [10]])
    Y = np.array([1, 2, 6, 8, 10])
    clf = BayesianRidge(compute_score=True)
    clf.fit(X, Y)
    X_test = [[1], [3], [4]]
    assert(np.abs(clf.predict(X_test)-[1, 3, 4]).sum() < 1.e-2) # identity


def test_toy_ard_object():
    """
    Test BayesianRegression ARD classifier
    """
    X = np.array([[1], [2], [3]])
    Y = np.array([1, 2, 3])
    clf = ARDRegression(compute_score = True)
    clf.fit(X, Y)
    Test = [[1], [3], [4]]
    assert(np.abs(clf.predict(Test)-[1, 3, 4]).sum() < 1.e-3) # identity
