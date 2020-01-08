#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        response = fct(*args)
        return (response)
    except:
        print("Exception: {}".format(sys.exc_info()[0]), file=sys.stderr)
        return (None)
