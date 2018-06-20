"""
This module describes the most basic usage of Amaze: you define a prediction
algorithm, (down)load a dataset and run a cross-validation procedure.
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from amaze import SVD
from amaze import Dataset
from amaze.model_selection import cross_validate


# Load the movielens-100k dataset (download it if needed),
data = Dataset.load_builtin('ml-100k')

# We'll use the famous SVD algorithm.
algo = SVD()

# Run 5-fold cross-validation and print results
cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
