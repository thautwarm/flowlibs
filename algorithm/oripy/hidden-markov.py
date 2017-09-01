#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 10:38:50 2017

@author: misakawa
"""

from collections import defaultdict
# Σ :: status -> observation -> probability     -
# Φ :: status -> status      -> probability
class HMM:
    __slots__ = []
    def __new__(self, Σ, Φ, F):
        return (Σ, Φ, F)

def cal_status_transfrom(Seqs, gram, decide_status, gap = 1):	
    Σ  = defaultdict(lambda :defaultdict(float))  
    Φ  = defaultdict(lambda :defaultdict(float))  
    for Seq in Seqs:
        last         = None
        for i in range(0, len(Seq) - gram +1, gap):
            seq                     = Seq[i:i+gram]
            observation             = "".join(map(lambda x:x[0], seq))
            status                  = decide_status(list(map(lambda x:x[0], seq))) 
            Σ[status][observation]  += 1
            Φ[last][status]         += 1
            last                    = status

    def normalize(X):
        for X1 in X:
            count = sum(X[X1].values())
            for X2 in X[X1]:
                X[X1][X2] /= count
    normalize(Σ)
    normalize(Φ)

    def F(seq):
        for i in range(0, len(seq) - gram +1, gap):
            yield seq[i:i+gram]
    return HMM(Σ, Φ, F)


def forward(Σ, Φ, F):
    def _f(seq):
        # initial 
        prob = [dict()]
        observations = F(seq)
        observation = next(observations)
        for status in Σ:
            try:
                prob[-1][status] = Σ[status][observation]
            except:
                assert status == None
        prob.append(dict())

        # forward
        for observation in observations:
            for status in Σ:
                prob[-1][status] = \
                    sum( ( prob[-2][ϕ]*Φ[ϕ][status] for ϕ in Φ if ϕ is not None) )*Σ[status][observation]
            prob.append(dict())
        prob.pop()
        return prob
        
    return _f











