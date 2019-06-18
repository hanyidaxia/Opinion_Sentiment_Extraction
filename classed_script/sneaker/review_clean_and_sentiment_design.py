#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class get_clean_reviews():
    import sys
    import numpy as np
    import os
    import collections
    import re
    
    def clean_review(file_name):
        reviews = []
        clean_review = []
        with open (file_name, "r", encoding = "UTF-8") as f:
            line = f.readlines()
            line = "".join(line)
            products = line.split('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
            while "" in products:
                products.remove("")
            for p in products:
                temp = p.split("****************************************************************************************")
            for i in temp:
                reviews.append(i)
            for i in reviews:
                if i not in ['\n\n', '\n']:
                    name = i.split('+-++++++++++++++++++++++++++++++')[0]
                    star = i.split('+-++++++++++++++++++++++++++++++')[1]
                    star = star.split("+++++++++++++++++++++++++++++++")[0]
                    star = star.split("alt=")
                    if len(star) >= 3:
                        star = star[2]
                        star = star.split("title=")[0]
                        star = star.split("><\\/div>")[0]
                    else:
                        star = star[1]
                        star = star.split("title=")[0]
                        star = star.split("><\\/div>")[0]
                    title = i.split('+++++++++++++++++++++++++++++++')[1]
                    title = title.split('-+-+++++++++++++++++++++++++++++++++++++++')[0]
                    title = title.split("BVRRValue BVRRReviewTitle")[1]
                    title = title.split("<\/span><span class=")[0]
                    text = i.split('-+-+++++++++++++++++++++++++++++++++++++++')[1]
                    if "BVRRReviewText" in text:
                        text = text.split("BVRRReviewText")[1]
                        text = text.split("<\/span>")[0]
                    j = name + star + title + text
                    clean_review.append(j)
        return clean_review
    
    def write_clean_review(file_name):
        with open(file_name, 'w', encoding = "UTF-8") as f:
            for details in clean_review:
                f.write(details)


# In[54]:


product_reviews = {}

for review in clean_review:
    p_name = review.split('\\')[0]
    p_review = review.split('\\')[-1]
    if p_name not in product_reviews:
        product_reviews[p_name] = [p_review]
    else:
        product_reviews[p_name].append(p_review)


# In[55]:


import json
with open('H:/Data/reviews.json', 'w') as f:
    json.dump(product_reviews, f)


# In[56]:


dan_reviews = []
for i in clean_review:
    d_review = i.split('\\')[-1]
    dan_reviews.append(d_review)


# In[57]:


import nltk


# Deep cleaning for the reviews, eliminate all the duplicated review

# In[58]:


c_reviews = []
for line in dan_reviews:
    line = line.strip()
    line = line.strip('\">')
    line = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+", " ",line)
    line = line.rstrip(' ')
    c_reviews.append(line)


# In[59]:


ch_reviews = sorted(set(c_reviews),key=c_reviews.index)


# In[60]:


r_tokens = []
for review in ch_reviews:
    tokens = nltk.word_tokenize(review)
    r_tokens.append(tokens)


# In[62]:


POS_tags = []
for tokens in r_tokens:
    POS_tags.append(nltk.pos_tag(tokens)) 


# In[63]:


attribute_lexicon = ['nike', 'addidas', 'puma', 'reebok', 'under armour', 'asics', 'brooks', 'champion', 'converse', 'jordan', 'fila', 'lacoste', 'mizuno', 'new balance', 'snkr', 'skechers', 'timberland', 'saucony', 'k-swiss', 'air', 'design', 'color', 'combination', 'sensor', 'surface', 'midsole', 'durable', 'explosive', 'speedy', 'powerful', 'intelligent', 'eyelet', 'heel', 'heel cup', 'quarter', 'sole', 'toe cap', 'tongue', 'topline', 'top piece', 'upper', 'vamp', 'welt', 'collar', 'foxing', 'heel counter', 'heel tab', 'inner sole', 'lace guard', 'midsole', 'outsole', 'padding', 'sock liner', 'aglets', 'beaters', 'bespoke', 'colorway', 'deadstock', 'deubré', 'flip-flop', 'grails', 'high top', 'hypebeast', 'hyperstrike', 'jumpman', 'lows', 'mids', 'nib', 'ndc', 'ogs', 'on ice', 'player edition', 'player exclusives', 'quickstrike', 'reseller', 'Retro', 'tonal', 'upper', 'updown', 'vnds', 'zigtech', 'red', 'yellow', 'blue', 'leather', 'thick', 'light', 'heavy', 'hard', 'soft', 'materials', 'big', 'small', 'adjustable', 'adorable', 'anatomic', 'anatomically designed', 'anti-fatigue', 'antimicrobial', 'athletic', 'beveled', 'bold', 'boys', 'breathable', 'breezy', 'canvas', 'casual', 'chic', 'classic', 'closed-toe', 'comfortable', 'comfy', 'contemporary', 'cooler', 'cushioned', 'cut-out', 'cute', 'cutting-edge', 'dainty', 'dapper', 'decorative', 'dependable', 'designer', 'detailed', 'distressed', 'dress', 'drier', 'kids', 'latest', 'lightweight', 'long-lasting', 'machine washable', 'masculine', 'memory foam-lined', 'mens', 'moisture-wicking', 'non-marking', 'non-slip', 'odor-absorbing', 'odor-resistant', 'open-toe', 'optimal', 'over-the-knee', 'overlay', 'padded', 'patchwork', 'patent', 'pleated', 'plush', 'professional', 'protective', 'pull-on', 'reflective', 'reliable', 'remodeled', 'revolutionary', 'rocker-style', 'ruched', 'rugged', 'sassy', 'savvy', 'easy-to-maintain', 'eco-friendly', 'edgy', 'efficient', 'elegant', 'embroidered', 'engineered', 'environmentally-friendly', 'ergonomic', 'everyday', 'exceptional', 'exciting', 'fabric-lined', 'fancy', 'fashionable', 'favorite', 'feminine', 'finely detailed', 'flattering', 'flexible', 'flirty', 'foot-friendly', 'forefoot', 'form-fitting', 'girls', 'gusseted', 'high-heeled', 'high-performance', 'hot', 'imported', 'injection-molded', 'innovative', 'insole', 'insulated', 'shock-absorbent', 'shock-absorbing', 'simple', 'sleek', 'slip-on', 'slip-resistant', 'slouched', 'smooth', 'sophisticated', 'stable', 'state-of-the-art', 'strapless', 'strappy', 'structural', 'stunning', 'stylish', 'suede', 'superior', 'supple', 'supportive', 'synthetic', 'textured', 'toning', 'top-of-the-line', 'treaded', 'trendy', 'underfoot', 'unique', 'versatile', 'water-resistant', 'waterproof', 'wear-anywhere', 'womens', 'eva insert', 'accent', 'accents', 'all-day comfort', 'ankle', 'ankle strap', 'apparel', 'arch', 'arch bridge', 'arch support', 'best fit', 'beveled heel', 'block heel', 'brand', 'breathability', 'buckle', 'calf', 'calf space', 'canvas', 'clasp', 'closure', 'comfort', 'coziness', 'cushioning', 'cut-out upper', 'design', 'design elements', 'detailing', 'durability', 'easy on/off', 'efficiency', 'elastic', 'embellishment', 'mesh fabric', 'midsole', 'motion control', 'movement', 'name brand', 'nubuck', 'orthotics', 'outdoor wear', 'outsole', 'over-pronator', 'padding', 'padding', 'pair', 'pair of shoes', 'panel', 'patent leather', 'peep toe', 'perfect fit', 'personal style', 'platform', 'pointed toe', 'posture', 'propulsion', 'quality', 'rearfoot', 'rearfoot stability', 'removable insole', 'rocker bottom', 'sandal', 'season', 'shearling', 'shock', 'shoe', 'ensemble', 'fabric', 'fall', 'fashion', 'fit', 'flair', 'foot', 'foot environment', 'footbed', 'footing', 'full-grain leather', 'gait', 'give', 'grip', 'heel', 'heel cup', 'heel strike', 'hidden zipper', 'impact', 'indoor wear', 'innovation', 'insert', 'insole', 'instep', 'laces', 'leather', 'leather upper', 'leg', 'lifestyle', 'lining', 'lining', 'low back', 'side zip entry', 'skid-resistant', 'sole', 'spring', 'square toe', 'stability', 'steel shank', 'steel toe', 'stitching', 'strap', 'strap closure', 'stride', 'strike points', 'style', 'styling', 'summer', 'support', 'technology', 'toe-off', 'toes', 'tongue', 'traction', 'tread', 'tricot lining', 'trim', 'underfoot protection', 'upper', 'ventilation system', 'wardrobe', 'warmth', 'width', 'winter', 'zipper']


# In[64]:


POS_tags[0:5]


# In[151]:


window = 5
output = []

# Iterating through all POS tags
for pairs in POS_tags:
    t = 0
    for element in pairs:
        l = len(pairs)
        # joining the terms with ,
        element = ",".join(element)
        word = element.strip("(\'").split(',')[0]
        t += 1
        if word in attribute_lexicon:
            if t >= 5 and t <= l-5:
                n_window = pairs[t-5:t+5]
            if t >= 5 and t > l-5:
                n_window = pairs[t-5:-1]
            if t < 5 and t <= l-5:
                n_window = pairs[0:t+5]
            if t < 5 and t > l-5:
                n_window = pairs[0:-1]
        for n_element in n_window:
            n_element = ",".join(n_element)
            n_tag = n_element.strip(")\'").split(",")[1]
            if n_tag in ['NN', 'NNS', 'JJ', 'RB']:
                # under construction
                # 
                
            
                


# ## Build sentiment lexicon 

# In[1]:


import senticnet


# In[2]:


from senticnet.senticnet import SenticNet

sn = SenticNet()
concept_info = sn.concept('love')
polarity_value = sn.polarity_value('love')
polarity_intense = sn.polarity_intense('love')
moodtags = sn.moodtags('love')
semantics = sn.semantics('love')
sentics = sn.sentics('love')


# In[3]:


print(polarity_value, polarity_intense, moodtags, semantics, sentics)


# In[34]:


baoli_lexicon = []
with open("H:/Google_download/opinion-lexicon-English/positive-words.txt") as f:
    positive = f.readlines()
    positive = "".join(positive).split('\n')
    positive = positive[30:]
with open("H:/Google_download/opinion-lexicon-English/negative-words.txt") as n_f:
    negative = n_f.readlines()
    negative = "".join(negative).split('\n')
baoli_lexicon = positive + negative


# In[43]:


sentiment_lexicon = {}
for i in range(0,len(baoli_lexicon)):
    sentiment_lexicon[i] = baoli_lexicon[i] 


# In[45]:


sentiment_lexicon


# In[67]:


manu = np.load("H:/Data/jade.npy")
print(manu)


# In[75]:


with open("H:/Data/manu.txt", "w") as f:
    for i in manu:
        i = "".join(str(i))
        f.write(i)
        f.write('\n')


# In[ ]:




