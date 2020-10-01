from ft_len import ft_len


def ft_slice_str(st, start, end):
    if end > ft_len(st):
        end = ft_len(st)
    res = ' '
    for i in range(start - 1, end):
        res += st[i]
    return res
