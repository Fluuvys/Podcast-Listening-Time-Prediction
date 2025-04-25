def check_div(str_current, str_target):
    n_current = len(str_current)
    n_target = len(str_target)
    if(n_target % n_current !=0):
        return False
    for i in range(n_target // n_current):
        if(str_current != str_target[i*n_current: i*n_current + n_current]):
            return False
    return True
print(check_div("AB","ABCABC"))