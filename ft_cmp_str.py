from ft_len import ft_len


def ft_cmp_str(st1, st2, x):
    res = ''
    for i in range(ft_len(st1)):
        if i == x - 1:
            res += st2
        res += st1[i]
    return res
