#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class description_cleaning:
    import numpy as np
    import os
    import re
    import csv
    import pandas as pd
    import collections
    import nltk
    def clean_description(file_name):
        with open(file_name) as f:
            line = f.readlines()
            line = "".join(line)
            product = line.split('Sign In')
        product = product[1:]
        descriptions = []
        for i in product:
            i = i.split('*****************************************************************')[4]
            descriptions.append(i)
            uni_description = sorted(set(descriptions),key=descriptions.index)
    def write_cleaned_description(file_name):        
        with open(file_name, 'w') as f:
        for d in uni_description:
            f.write(d)
            f.write('\n')
            f.write("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            f.write('\n')

