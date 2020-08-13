#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 18:14:37 2020

@author: matan
"""

import sys
import time

'''functiont to sleep number of minutes in order to limit over liking'''

def sleep_in_min(num_min = 50):
    print('\nsleep for ' + str(num_min) + ' min...')
    for i in range(num_min):
        #flush update
        sys.stderr.write('\r%d/%d min' % (i, num_min))
        sys.stderr.flush()
        time.sleep(60)
        
    sys.stderr.write('\r%d/%d min' % (num_min, num_min))
    sys.stderr.flush()

