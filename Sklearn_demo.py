# -*- coding: utf-8 -*-
# __author__ = 'xinjiu.qiao'
import numpy as np
from sklearn import preprocessing
import numpy as np
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
print(sigmoid(1))