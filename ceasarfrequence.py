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

def donner_frequence(s):
    freq  = {}
    for element in s :
        if element in freq:
            freq[element] += 1
        else :
            freq[element] = 1
    for c, v in freq.items():
        print(c ,v/len(s))

                                        #bonjour mes amies est ce que vous allez bien
c_code = encode_cesar ('ylkglro jbp xjfbp bpq zb nrb slrp xiibw yfbk' ,3)
print(c_code)

#donner_frequence('ylkglro jbp xjfbp bpq zb nrb slrp xiibw yfbk')      