"""
Convenience functions
"""

def is_num(s):
    try:
        v = float(s)
        return True
    except:
        return False