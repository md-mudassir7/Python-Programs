#!/usr/bin/env python
import os
def parent_child():
    n=os.fork()
    if n>0:
        print("parent process and id is:",os.getpid())
    else:
        print("child process and id is:",os.getpid())        
parent_child()
