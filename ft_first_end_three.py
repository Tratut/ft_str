from ft_len import ft_len


def ft_first_end_three(x):
    kol = ft_len(x)
    fd = ''
    if kol < 5:
        for i in range(kol):
            return x[0]
    else:
        fd = fd + x[0] + x[1] + x[2] + x[-3] + x[-2] + x[-1]
        return fd
