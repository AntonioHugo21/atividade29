# Crie um programa que receba uma lista com os nomes dos alunos presentes em uma aula e exiba quantos alunos estão presentes e a lista dos nomes. Se o total de alunos presentes for menor que 5, exiba uma mensagem sugerindo uma revisão da lista de chamada.

# Exemplo de entrada:
# Alunos presentes: ['Ana', 'Bruno', 'Carlos', 'Daniela']

# Exemplo de saída:
# Alunos presentes: 4
# Lista de alunos presentes: Ana, Bruno, Carlos, Daniela
# Aviso: Poucos alunos presentes. Revisar lista de chamada.


nomes_alunos = []

while True:
    nome = input('Digite um nome (ou pressione Enter para encerrar): ')      
    if nome == "":
        break

    nomes_alunos.append(nome)

alunos_presentes = len(nomes_alunos)

print(f'A quantidade de alunos presentes é = {alunos_presentes}')
print(f'Os alunos presentes são: {", ".join(nomes_alunos)}')

if alunos_presentes < 5:
        print('Aviso: Poucos alunos presentes. Revisar lista de chamada.') 


