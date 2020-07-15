import os
import sys

RUNNING = True

PICDIR = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pics')
LIBDIR = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'libs')

if os.path.exists(LIBDIR):
    sys.path.append(LIBDIR)

print("Common init.")
