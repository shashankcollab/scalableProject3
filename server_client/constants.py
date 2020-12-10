"""
    This file is the constants of the peer to peer network
"""

import socket 
import threading 
import sys
import time
from random import randint
import fileIO

BYTE_SIZE = 1024
HOST = '10.35.70.30'
PORT = 33000
PEER_BYTE_DIFFERENTIATOR = b'\x11' 
RAND_TIME_START = 1
RAND_TIME_END = 2
REQUEST_STRING = "req"
