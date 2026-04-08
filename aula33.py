"""
https://docs.python.org/pt-br/3.14/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = 'Matheus Soares'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(string)
print(outra_variavel)
print(string.capitalize())
print(string.zfill(20))