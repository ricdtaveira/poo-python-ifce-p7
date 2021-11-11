from my_app import db, Person, Address

def main():
    ## Criação do Banco de Dados
    db.create_all()

    ## Criar Objetos
    jose = Person(name="José Maria")
    mary = Person(name="Maria Josino")

    end1 = Address(email="jose@google.com.br", person_id=1)
    end2 = Address(email="jose@ifce.edu.br", person_id=1)
    end3 = Address(email="jose@biroska.com.ru", person_id=1)

    end4 = Address(email="maryjo@google.com.br", person_id=2)
    end5 = Address(email="mary.josino@ifce.edu.br", person_id=2)
    end6 = Address(email="maryjo@biroska.com.ru", person_id=2)

    ##Persistir os objetos no Banco de Dados
    db.session.add(jose)
    db.session.add(mary)
    db.session.commit()

    db.session.add(end1)
    db.session.add(end2)
    db.session.add(end3)
    db.session.commit()

    db.session.add(end4)
    db.session.add(end5)
    db.session.add(end6)
    db.session.commit()

    print("\nImprimir Pessoas")
    print("----------------")

    pessoas = Person.query.all()
    for pessoa in pessoas:
        print(pessoa)

    print("\nImprimir Endereços")
    print("------------------")
    address = Address.query.all()
    for addres in address:
        print(addres)

    print("\nImprimir Endereços das Pessoas")
    print("------------------------------")
    pessoas = Person.query.all()
    for pessoa in pessoas:
        print(pessoa.name)
        print(pessoa.addresses)

if __name__ == '__main__':
    main()



