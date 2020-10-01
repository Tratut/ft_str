from ft_len import ft_len


def ft_find_str(st1, st2):
    len1 = ft_len(st1)
    len2 = ft_len(st2)
    cop = ''
    if st1 not in st2:
        print(-1)
    else:
        for i in range(len2 - len1):
            for k in range(i, i + len1):
                cop += st2[k]
            if cop == st1:
                return i
            cop = ''
