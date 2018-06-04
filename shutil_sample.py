#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import shutil, os
from pathlib import Path
import send2trash

# TODO hoge.txt exist?

tmpdir = str(Path.home()) + '/work/boringpy_shakyo/'
shutil.copy(str(Path.home()) +  '/hoge.txt', tmpdir)

shutil.move(tmpdir + 'hoge.txt', tmpdir + 'hage.txt')

if (tmpdir + 'hage.txt').endswith('txt'):
    print("### endwith txt")

#os.unlink(tmpdir + 'hage.txt')
send2trash.send2trash(tmpdir + 'hage.txt')


