Flask login:
    
    Serve para, fazer login, fazer logout e lembra as sesões de seus usuarios por longos periodos de tempo.
    
ele irá:
    Armazena o id do usuario ativo na sessão flask e deixa o usuario fazer login e sair.
    
    Permite restrigir as exisbiçõesa usuario logados ( ou desconectados )
    
    Lidar com a funcionalidade normalmente-tricky 'lembra de mim'
    
    Ajuda a proteger as sessões dos seus usuarios de serem roubadas por ladrões de biscoitos.
    
Instalação:
    pip install flask-login
    
from flask_login import LoginManager, UserMixin, login_user, logout_user, , current_user

app = Flaks(__name__)

    # Configurando o flaks login
    login_manager = LoginManager() # Iniciando 
    login_manager.init_app(app) # integrando todos os métodos e funcionalidades do login à aplicação.
    login_manager.login_view = 'login' # caso o usuario não esteja logado redirect ele para a pagina de login



   login_managet.login_view = 'login' se o usuario tenta acessar uma rota que ele não tem acessor metodo irá manda ele para a pagina de login


   
   from flask import Flask, request, render_template, url_for, flash, redirect
from flask_login import LoginManager,  UserMixin, login_user, logout_user, login_required, current_user


app = Flask(__name__)
app.secret_key = 'Sua_chave_aqui' # precisamos de uma chave secreta

# Configurando o flaks login
login_manager = LoginManager() # Iniciando 
login_manager.init_app(app) # integrando todos os métodos e funcionalidades do login à aplicação.
login_manager.login_view = 'login' # caso o usuario não esteja logado redirect ele para a pagina de login


# Usuário fictício para demonstração
class User(UserMixin):  #  Permitindo que a class User use metodos do flask login
    def __init__(self, id ):
        self.id = id


# Simulando banco de dados com ID e senha
users = {
    'Gilderlan': {'id': '1', 'password': 'brazil'}
}


# Carrega o usuario
# quais infor voce que mostra no front sobre o user
@login_manager.user_loader
def load_user(user_id):
    for username, user_data in users.items():
      if user_data['id'] == user_id:
        return User(user_id)
    return None 

@app.route('/')
@login_required # Apenas usuarios logados podem acessar a rota home
def home():
    return render_template('home.html', username=current_user.id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username]['password'] == password:
            user = User(users[username]['id'])  # Aqui passamos o ID para o User
            login_user(user)

            flash('Login bem-sucedido!')
            return redirect(url_for('home'))

        else:
            flash('Credencias invalidas. Tente novamente')
    
    return render_template('login.html')



@app.route('/logout')
@login_required
def logout():
    logout_user() # função para deslogar user
    flash('Voce foi desconectado')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)


    

