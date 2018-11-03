# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 20:55:56 2018

@author: roy
"""

import pandas as pd, numpy as np
#data = temp.iloc[:, 1:1682].astype('float')
data = outstanding_shares.iloc[:, 1:1682].astype('float')
def seq(z):
    s1 = 1; s2 = 0; g = {}
    for i in range(len(z)):
        if z[i] > 0:
            g[s1] = s2 + 1 ; s2 = s2 + 1
        else:
            s2 = 0; s1 =s1 + 1
    return list(g.values())

def seq_na(z):
    s1 = 1; s2 = 0; g = {}
    for i in range(len(z)):
        if np.isnan(z[i]) == True:
            g[s1] = s2 + 1 ; s2 = s2 + 1
        else:
            s2 = 0; s1 =s1 + 1
    return list(g.values())

conti_show = [seq(data.iloc[:, x]) for x in range(1681)]
cap = [len(conti_show[x]) for x in range(len(conti_show))]
loc = np.where(np.array(cap)>1)[0]
nan_show_loc = [seq_na(data.iloc[:, loc[x]]) for x in range(len(loc))]

def fill_nan(data, loc):
    import numpy as np, pandas as pd
    x = data.iloc[:, loc].values
    def seq(z):
        s1 = 1; s2 = 0; g = {}
        for i in range(len(z)):
            if z[i] > 0:
                g[s1] = s2 + 1 ; s2 = s2 + 1
            else:
                s2 = 0; s1 =s1 + 1
        return list(g.values())
    
    def seq_na(z):
        s1 = 1; s2 = 0; g = {}
        for i in range(len(z)):
            if np.isnan(z[i]) == True:
                g[s1] = s2 + 1 ; s2 = s2 + 1
            else:
                s2 = 0; s1 =s1 + 1
        return list(g.values())
    
    conti_show = seq(x)
    na_show = seq_na(x)
    conti_cumsum = np.cumsum(conti_show)
    na_cumsum = np.cumsum(na_show)
    if np.isnan(x[0]) == True and len(na_show)>=len(conti_show):
        for i in range(len(conti_show)-1):
            if i == 0: 
                    s = 0 
                    u = 0
            else: 
                    s = 1
                    u = i
            x[conti_cumsum[i]+na_cumsum[i]:na_cumsum[i+1]+conti_cumsum[i]] = x[conti_cumsum[i]+na_cumsum[i]-1]
    elif np.isnan(x[0]) == False and len(na_show)<=len(conti_show):
        for i in range(len(conti_show)-1):
            if i == 0: 
                    s = 0 
                    u = 0
            else: 
                    s = 1
                    u = i
            x[conti_cumsum[i]+na_cumsum[u-1]*s:conti_cumsum[i]+na_cumsum[i]] = x[conti_cumsum[i]+na_cumsum[u-1]*s-1]
    data.iloc[:, loc] = x
    return data.iloc[:, loc]

for i in range(len(loc)):
    fill_nan(data, loc[i])