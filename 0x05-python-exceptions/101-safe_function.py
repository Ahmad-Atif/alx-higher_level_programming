#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except (ValueError, TypeError, IndexError, ZeroDivisionError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None