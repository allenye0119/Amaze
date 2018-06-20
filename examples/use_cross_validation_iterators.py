"""
This module descibes how to use cross-validation iterators.
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from amaze import SVD
from amaze import Dataset
from amaze import accuracy
from amaze.model_selection import KFold

# Load the movielens-100k dataset
data = Dataset.load_builtin('ml-100k')

# define a cross-validation iterator
kf = KFold(n_splits=3)

algo = SVD()

for trainset, testset in kf.split(data):

    # train and test algorithm.
    algo.fit(trainset)
    predictions = algo.test(testset)

    # Compute and print Root Mean Squared Error
    accuracy.rmse(predictions, verbose=True)
