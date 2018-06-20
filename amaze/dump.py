"""
The :mod:`dump <amaze.dump>` module defines the :func:`dump` function.
"""

import pickle


def dump(file_name, predictions=None, algo=None, verbose=0):
    """A basic wrapper around Pickle to serialize a list of prediction and/or
    an algorithm on drive.

    What is dumped is a dictionary with keys ``'predictions'`` and ``'algo'``.

    Args:
        file_name(str): The name (with full path) specifying where to dump the
            predictions.
        predictions(list of :obj:`Prediction\
            <amaze.prediction_algorithms.predictions.Prediction>`): The
            predictions to dump.
        algo(:class:`Algorithm\
            <amaze.prediction_algorithms.algo_base.AlgoBase>`, optional):
            The algorithm to dump.
        verbose(int): Level of verbosity. If ``1``, then a message indicates
            that the dumping went successfully. Default is ``0``.
    """

    dump_obj = {'predictions': predictions,
                'algo': algo
                }
    pickle.dump(dump_obj, open(file_name, 'wb'),
                protocol=pickle.HIGHEST_PROTOCOL)

    if verbose:
        print('The dump has been saved as file', file_name)


def load(file_name):
    """A basic wrapper around Pickle to deserialize a list of prediction and/or
    an algorithm that were dumped on drive using :func:`dump()
    <amaze.dump.dump>`.

    Args:
        file_name(str): The path of the file from which the algorithm is
            to be loaded

    Returns:
        A tuple ``(predictions, algo)`` where ``predictions`` is a list of
        :class:`Prediction
        <amaze.prediction_algorithms.predictions.Prediction>` objects and
        ``algo`` is an :class:`Algorithm
        <amaze.prediction_algorithms.algo_base.AlgoBase>` object. Depending
        on what was dumped, some of these may be ``None``.

    """

    dump_obj = pickle.load(open(file_name, 'rb'))

    return dump_obj['predictions'], dump_obj['algo']
