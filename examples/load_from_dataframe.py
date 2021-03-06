"""
This module descibes how to load a dataset from a pandas dataframe.
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import pandas as pd

from amaze import NormalPredictor
from amaze import Dataset
from amaze.model_selection import cross_validate


# Creation of the dataframe. Column names are irrelevant.
ratings_dict = {'itemID': [1, 1, 1, 2, 2],
                'userID': [9, 32, 2, 45, 'user_foo'],
                'rating': [3, 2, 4, 3, 1]}
df = pd.DataFrame(ratings_dict)

# The columns must correspond to user id, item id and ratings (in that order).
data = Dataset.load_from_df(df[['userID', 'itemID', 'rating']],
                            rating_scale=(1, 5))

# We can now use this dataset as we please, e.g. calling cross_validate
cross_validate(NormalPredictor(), data, cv=2)
