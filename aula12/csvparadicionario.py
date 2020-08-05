import csv

#path do arquivo csv
arquivo= r'E:\Desenvolvimento\poo-python-ifce-p7\aula12\funcionarios.txt'


with open(arquivo, mode='r') as csv_file:
    
    # Cria um objeto csv_reader que funciona como um
    # uma coleção de dicionários. 
    # Cada objeto row lido de csv_reader possui uma linha.
    # Cada linha será um conjunto chave e valor.
    # chave é o nome da colulaself.
    # valor é o valor contido na coluna.
    # 
    csv_reader = csv.DictReader(csv_file)
    
    
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Nome das colunas {", ".join(row)}')
            line_count += 1
        print(f'\t{row["Nome"]} trabalha do departamento {row["Departamento"]}, nasceu no mes de {row["Mes"]}.')
        line_count += 1
    print(f'Processadas {line_count} linhas.')