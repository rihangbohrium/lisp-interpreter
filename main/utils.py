def is_num(s):
    try:
        v = float(s)
        return True
    except:
        return False

def valid_name(name):
    return isinstance(name, str) and not is_num(name[0]) and name[0] != '$'
