#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import os
from pathlib import Path

for folder, subfolders, filenames in os.walk(str(Path.home()) + '/work'):
    print('The current folder is ' + folder)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folder + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folder + ': ' +  filename)

    print('')

