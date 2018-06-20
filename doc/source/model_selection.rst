.. _model_selection:

The model_selection package
---------------------------

Amaze provides various tools to run cross-validation procedures and search
the best parameters for a prediction algorithm. The tools presented here are
all heavily inspired from the excellent `scikit learn
<http://scikit-learn.org/stable/modules/classes.html#module-sklearn.model_selection>`_
library.


.. _cross_validation_iterators_api:

Cross validation iterators
==========================

.. automodule:: amaze.model_selection.split
    :members:
    :exclude-members: get_cv, get_rng

Cross validation
================

.. autofunction:: amaze.model_selection.validation.cross_validate

Parameter search
================

.. autoclass:: amaze.model_selection.search.GridSearchCV
    :members:
    :inherited-members:

.. autoclass:: amaze.model_selection.search.RandomizedSearchCV
    :members:
    :inherited-members:

