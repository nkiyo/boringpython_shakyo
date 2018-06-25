#! python3

import sys, pyperclip, subprocess

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

print('address = ' + address)
subprocess.call(["cygstart", 'http://www.google.com/maps/place/' + address])

