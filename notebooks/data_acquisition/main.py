## Adquisición de Datos
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
import tensorflow as tf
%load_ext tensorboard
import tensorboard
tensorboard.__version__
import matplotlib.pyplot as plt
from datetime import datetime
df = pd.read_csv('/content/creditcard.csv', sep=';')
df.head()
