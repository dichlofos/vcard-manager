#!/usr/bin/env python
# coding: utf-8

import os
import sys


unk_index = 0

with open('unix.vcf') as f:
    for line in f:
        line = line.strip()

        # fix some Android export bugs
        if line == 'ORG:':
            # skip it; delete; delete!
            continue
        if line == 'N:':
            line = 'N:' + str(unk_index)
        if line == 'FN:':
            line = 'FN:' + str(unk_index)
        print line
