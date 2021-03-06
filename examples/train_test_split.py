"""
This module describes how to use the train_test_split() function.
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from amaze import SVD
from amaze import Dataset
from amaze import accuracy
from amaze.model_selection import train_test_split

# Load the movielens-100k dataset (download it if needed),
data = Dataset.load_builtin('ml-100k')

# sample random trainset and testset
# test set is made of 25% of the ratings.
trainset, testset = train_test_split(data, test_size=.25)

# We'll use the famous SVD algorithm.
algo = SVD()

# Train the algorithm on the trainset, and predict ratings for the testset
algo.fit(trainset)
predictions = algo.test(testset)

# Then compute RMSE
accuracy.rmse(predictions)
