# Atividade 1
# entrada = input ('Digite um número ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'
    
#     if par_impar:
#         par_impar_texto = 'par'
#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro')

# Atividade 2
# entrada = input('Digite a hora em números inteiros: ')

# try:
#     hora = int(entrada)

#     if hora >= 0 and hora <= 11:
#         print('Bom dia')
#     elif hora >= 12 and hora <= 17:
#         print('Boa tarde')
#     elif hora >= 18 and hora <= 23:
#         print('Boa noite')
#     else: 
#         print('Horário não reconhecido')
# except:
#     print('Por favor, digite apenas números inteiros')

entrada = input('Digite seu nome de usuário: ')
nome_curto = len(entrada) <= 4
nome_normal = len(entrada) >= 5 and len(entrada) <= 6

if nome_curto:
    print("Seu nome é curto")
elif nome_normal:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')