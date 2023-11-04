import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import requests
import opencc
import os
from matplotlib.font_manager import FontManager
from pyplotz.pyplotz import PyplotZ
from sklearn.preprocessing import LabelEncoder
opencc = opencc.OpenCC('t2s')
sns.set_theme(color_codes=True)
font_manager = FontManager()
font = font_manager.findfont('DejaVu Sans')