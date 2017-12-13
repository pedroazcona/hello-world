# -*- coding: utf-8 -*-
"""
Created on Thu May 18 15:02:41 2017

@author: poaa
"""

import re

def word_counts(path):
    counts_dict = {}
    i=0
    with open(path) as file:
        for line in file:
            for word in re.split('[^a-z]+', line.lower()):
                if not word: continue
                if not word in counts_dict:
                    counts_dict[word] = 1
                else:
                    counts_dict[word] += 1
    sorted_list = sorted([(n, w) for w, n in counts_dict.items()], reverse=True)
    print('The 100 most frequent words:', sorted_list[:100])
    print('Number of distinct words:', len(sorted_list))
    print('Number of words that occur once:', len(list(filter(lambda p: p[0] == 1, sorted_list))))
    j=0
    for s in counts_dict:
        if counts_dict[s]==2:
            j +=1
    print('Number of words that occur once by the elder woman\'s count: '+ str(j))

if __name__ == '__main__':
    word_counts('C:\\Users\\poaa\\Documents\\Python Scripts\\1342.txt')

