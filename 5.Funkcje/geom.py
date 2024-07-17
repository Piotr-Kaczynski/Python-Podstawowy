def element_ciagu_geo(a1=2, q=2, wyraz=2):
    # policz dany wyraz ciągu
    return q**(wyraz-1)*a1


def iloraz_ciagu(wyraz, nast_wyraz):
    return nast_wyraz / wyraz


def suma_nWyrazow(a1=2, q=2, n=2):
    if q==1:
        return n*a1
    else:
        return a1*(1-q**n) / (1-q)
