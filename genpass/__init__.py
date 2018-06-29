#!/usr/bin/python

# -*- coding: utf-8 -*-

import string
import random

def gen(*length):
    if len(length) >= 1:
        print(''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(length[0])))
    else:
        print(''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(10)))

