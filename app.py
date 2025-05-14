from flask import Flask, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'clave-secreta'  # Necesario para sesiones

# Página principal (protegida)
@app.route('/')
def index():
    if 'username' in session:
        return f'¡Hola Mundo SaaS, {session["username"]}!'
    return redirect(url_for('login'))

# Login simple (solo guarda el usuario)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            Usuario: <input type="text" name="username">
            <input type="submit" value="Entrar">
        </form>
    '''

# Logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
