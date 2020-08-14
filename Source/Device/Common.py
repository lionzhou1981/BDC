import os
import sys

RUNNING = True

PICDIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pics')
LIBDIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'libs')
MODDIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'modules')
PAGEDIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pages')

if os.path.exists(LIBDIR):
    sys.path.append(LIBDIR)

if os.path.exists(MODDIR):
    sys.path.append(MODDIR)

print("Common init.")
