import os

def is_file(f):
    if os.path.exists(f):
        return True
    else:
        if os.path.exists(os.path.abspath(f)):
            return True
    
    return False