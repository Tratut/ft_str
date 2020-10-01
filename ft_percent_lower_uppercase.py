def ft_percent_lower_uppercase(x):
    b = 'qwertyuioplkjhgfdsazxcvbnm'
    B = 'QWERTYUIOPLKJHGFDSAZXCVBNM'
    rb = 'ёйцукенгшщзхъэждлорпавыфячсмитьбю'
    RB = 'ЁЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ'
    kol_small = 0
    kol_big = 0
    kol_ln = 0
    for i in x:
        if i in b or i in rb:
            kol_small += 1
        if i in B or i in RB:
            kol_big += 1
        kol_ln += 1
    if kol_small / kol_big == 1:
        return 1
    else:
        return kol_small / kol_big * 100
