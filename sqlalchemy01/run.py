
from my_app import db
from my_app.models.categoriaTable import Categoria
from my_app.models.postTable import Post
from my_app.models.userTable import Usuario
 
 
def main():
    ## Criação do Banco de Dados
    db.create_all()

    ## Instanciar objetos (Criar)
    admin = Usuario(username='admin', email='admin@example.com')
    guest = Usuario(username='guest', email='guest@example.com')
    joao  = Usuario(username='João',  email='joao@example.com')

    ##Persistir os objetos no Banco de Dados (Insert)
    db.session.add(admin)
    db.session.add(guest)
    db.session.add(joao)
    db.session.commit()

    ##Executar um Select *
    print("Select User *")
    print(Usuario.query.all())

    ##Executar um Select com um filtro
    print("Select Usuario com filtro")
    print(Usuario.query.filter_by(username='admin').first())
    
    ## Criar uma Categoria
    py = Categoria(name='Python')

    ## Criar um Post e associar a categoria py
    Post(title='Hello Python!', body='Python is pretty cool', categoria=py)

    ## Cria um Post p
    p = Post(title='Snakes', body='Ssssssss')

    ## Associa o p ao conjunto de Posts da Categoria py
    py.posts.append(p)
    db.session.add(py)
    db.session.commit()

    ##Executar um Select com um filtro
    print("Select Posts filtro")
    print(Post.query.filter_by(categoria_id=1).all())

    ## print(py.posts)
    print("Select * Categoria")
    posts = Categoria.query.all()
    print(posts)

if __name__ == '__main__':
    main()