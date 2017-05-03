from pyretic.lib.corelib import *

IP1 = "10.0.0.1"
IP2 = "10.0.0.2"

route = (match(dstip=IP1) >> fwd(1)) + (match(dstip=IP2) >> fwd(2))

def main():
    return route
