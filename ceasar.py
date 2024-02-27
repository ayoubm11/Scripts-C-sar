def encode_cesar(s ,decalage):
    chaine_code = ""
    for element in s:
        if 'A'<= element <= 'Z':
            indice = ord(element) - ord('A')
            indice = (indice + decalage) %26 
            chaine_code = chaine_code + chr(indice + ord('A'))
        elif'a' <=element<='z':
            indice = ord(element) - ord('a')
            indice = (indice + decalage) %26 
            chaine_code = chaine_code + chr(indice + ord('a'))
        else:
            chaine_code=chaine_code + element
    return chaine_code


                    #bonjour mes amies est ce que vous allez bien
c_code = encode_cesar ('hutpuax sky gsoky kyz ik wak buay grrkf hokt' ,2)
print(c_code)

for i in range(26):
    c_clair = encode_cesar(c_code, i)
    print (c_clair)

