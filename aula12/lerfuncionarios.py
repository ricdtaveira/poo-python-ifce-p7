import csv

#path do arquivo csv
arquivo= r'E:\Desenvolvimento\poo-python-ifce-p7\aula12\funcionarios.txt'

# Abertura e carga do arquivo csv em um objeto csv_reader
# 
with open(arquivo) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Nomes das Colunas {" - ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} trabalha no departamento {row[1]}, e nasceu no mes {row[2]}.')
            line_count += 1
    print(f'Foram processadas {line_count} linhas.')