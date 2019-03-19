import os

from parser import Parser

_DATA_DIR = os.path.join(os.path.abspath(os.path.pardir), 'data')

Parser(_DATA_DIR + '/aliceinwonderland.txt')
