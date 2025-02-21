from cryptography.fernet import Fernet
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/generate_key')
def generate_key():
    key = Fernet.generate_key()
    return f"Votre clé Fernet : {key.decode()}"

# Chiffrement avec clé utilisateur
@app.route('/encrypt')
def encrypt():
    valeur = request.args.get('valeur')
    user_key = request.args.get('key')

    if not valeur or not user_key:
        return "Erreur : Veuillez saisir 'valeur' et 'key'."

    try:
        f = Fernet(user_key)
        token = f.encrypt(valeur.encode())
        return f"Valeur chiffrée : {token.decode()}"
    except Exception as e:
        return f"Erreur : Clé invalide. {str(e)}"

# Déchiffrement avec clé utilisateur
@app.route('/decrypt')
def decrypt():
    token = request.args.get('token')
    user_key = request.args.get('key')

    if not token or not user_key:
        return "Erreur : Veuillez fournir 'token' et 'key'."

    try:
        f = Fernet(user_key)
        valeur = f.decrypt(token.encode())
        return f"Valeur déchiffrée : {valeur.decode()}"
    except InvalidToken:
        return "Erreur : Token invalide ou clé incorrecte."
    except Exception as e:
        return f"Erreur : Clé invalide. {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
