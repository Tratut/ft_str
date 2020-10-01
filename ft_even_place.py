from ft_len import ft_len


def ft_even_place(st):
    kol = ft_len(st)
    out = ''
    for i in range(kol):
        if i % 2 == 0:
            out += st[i]
    return out
