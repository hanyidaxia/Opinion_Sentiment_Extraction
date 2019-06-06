import nltk
import re
import itertools
from nltk.corpus import treebank
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('treebank')

class Features:
    def __init__(self, product_descriptions):
        self.candidate_attributes = []
        self.product_descriptions = product_descriptions
        self.candidate_feature_POS = [['NNP', 'NN'], 
                                      ['VBG', 'NNS'], ['NNP', 'NN', 'NN'], 
                                      ['NN', 'NNS'], ['NN', 'JJ']]
        self.frequency_counts = None
        self.pos = []
        
    def preprocess(self, sentence):
        sentence = sentence.lower()
        return sentence

    def find_candidate_attributes(self, sentence, show = False, lower = False):
        candidate_tags = []
        candidate_words = []
        if lower:
            sentence = self.preprocess(sentence)
        tokens = nltk.word_tokenize(sentence)
        tags = nltk.pos_tag(tokens)
        self.pos.append(tags)
        if show:
            print(tags)
        for word, tag in tags:
            candidate_tags.append(tag)
            candidate_words.append(word)
        combinations = [candidate_tags[i:j] for i, j in itertools.combinations(range(len(candidate_tags) + 1), 2)]
        terms = [candidate_words[i:j] for i, j in itertools.combinations(range(len(candidate_words) + 1), 2)]
        for tag, word in zip(combinations, terms):
            if tag in self.candidate_feature_POS and tag not in self.candidate_attributes:
                self.candidate_attributes.append(" ".join(w for w in word))
                
    def get_candidate_attributes(self, show = False, num_example_show = 3 ,lower = False):
        i = 0
        for key in self.product_descriptions.keys():
            if i < num_example_show:
                show = True
            category = self.product_descriptions[key]
            for model in category:
                [self.find_candidate_attributes(x, show, lower) for x in model['description'].split(',')]
                show = False
            i += 1   
        return self.candidate_attributes, self.pos
    
    def get_frequent_attributes(self, support = 0.05):
        import collections
        self.frequency_counts = collections.Counter(self.candidate_attributes)
        for key, val in self.frequency_counts.items():
            self.frequency_counts[key] = self.frequency_counts[key]/len(self.candidate_attributes)
        self.frequency_counts = { k:v for k,v in self.frequency_counts.items() if v >= support }
        return self.frequency_counts
    
    
    