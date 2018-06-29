#!/usr/bin/python

# -*- coding: utf-8 -*-

import string
import random

def gen(*length, model=7):
    passlen = 10
    seedchr = ''

    if len(length) >= 1:
        passlen = length[0]

    if model&1:
        seedchr += string.digits

    if model&2:
        seedchr += string.ascii_lowercase

    if model&4:
        seedchr += string.ascii_uppercase

    if model&8:
        seedchr += string.punctuation

    print(''.join(random.choice(seedchr) for _ in range(passlen)))

