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

# simulando banco de dados
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

