from ft_len import ft_len


def ft_slice_str(st, start, end=0):
    if end == 0:
        end = ft_len(st)
    res = ''
    for i in range(start, end):
        res += st[i]
    return res
