#!/usr/bin/env python
# coding: utf-8

# In[2]:


class primitive_rules:

    Rules = [
        ('JJ', 'NN'),
        ('JJ', 'NN','NN'),
        ('NN','NN'),
        ('VBZ', 'NN'),
        ('CD','NNS','IN','NN'),
        ('NN'),
        ('NN','VBZ','NN','NN'),
        ('NN','IN','DT','NNS'),
        ('NN', 'NNS'),
        ('NN','NN','NN'),
        ('VB', 'NN'),
        ('NNS'),
        ('NN', 'VBD'),
        ('JJ','VBD','JJ'),
        ('JJ','RB'),
        ('JJ','JJ','NNS'),
        ('NNS','NN','NN'),
        ('NN','NN','VBD'),
        ('JJ','NNS'),
        ('VBG','NN'),
        ('JJ','JJ'),
        ('NN','JJ'),
        ('JJ'),
        ('NN','CC','JJ'),
        ('NN','CC','NN'),
        ('NN','JJ','NNS'),
        ('NN','NN','NN','NN')
    ]
    with open("H:/Data/Rules.txt", "w") as f:
    Rules = "".join(str(Rules))
    f.write(Rules)

