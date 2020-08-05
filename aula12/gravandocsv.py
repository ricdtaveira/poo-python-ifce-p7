import csv

#path do arquivo csv
arquivo= r'E:\Desenvolvimento\poo-python-ifce-p7\aula12\outros.txt'

with open(arquivo, mode='w') as employee_file:
    # Cada coluna será delimitadada por virgula(,)
    # Cada coluna será envolvida por aspas dupla (")
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

    employee_writer.writerow(['Maria Emanuela', 'Informatica', 'Novembro'])
    employee_writer.writerow(['Erica Rafaela', 'Recursos Humanos', 'Dezembro'])