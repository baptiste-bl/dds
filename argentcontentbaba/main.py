def donne_des_sous(a: int, b: int) -> int:
    if(a > 10):
        return a + b + 2
    else:
        return a + b

compte_en_banque = donne_des_sous(12,10)
print(compte_en_banque)