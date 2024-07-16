import random
import string

def gerar_senha(tamanho=8):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

while True:
    tamanho_senha = int(input("Digite o tamanho da senha desejada: "))
    nova_senha = gerar_senha(tamanho_senha)
    print(f"A senha gerada é: {nova_senha}")

    pergunta = input('Deseja gerar mais alguma senha? [S/N]: ').upper().strip()
    if pergunta != 'S':
        print('Você parou de gerar novas senhas.')
        break