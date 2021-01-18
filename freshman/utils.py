import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def underride(d, **options):
    """Add key-value pairs to d only if key is not in d.

    d: dictionary
    options: keyword args to add to d
    """
    for key, val in options.items():
        d.setdefault(key, val)

    return d


def decorate(**options):
    """Decorate the current axes.
    
    Call decorate with keyword arguments like
    decorate(title='Title',
             xlabel='x',
             ylabel='y')
             
    The keyword arguments can be any of the axis properties
    https://matplotlib.org/api/axes_api.html
    """
    ax = plt.gca()
    ax.set(**options)
    
    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(handles, labels)

    plt.tight_layout()
    
    
def savefig(root, **options):
    """Save the current figure.
    
    root: string filename root
    options: passed to plt.savefig
    """
    format = options.pop('format', None)
    if format:
        formats = [format]
    else:
        formats = ['png']

    for format in formats:
        fname = f'figs/{root}.{format}'
        plt.savefig(fname, **options)

