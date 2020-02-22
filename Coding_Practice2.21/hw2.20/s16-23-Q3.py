def Decrypt(CipherChar, Lookup):
    Index = 1
    Found = False
    while Found == False:
        if Lookup[Index] = CipherChar:
            Found = True
        else:
            Index = Index + 1
    OriginalChar = chr(Index)
    return OriginalChar