from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html')

get_fernet(user_key):
key_bytes = user_key.encode()
return Fernet(key_bytes)
except Exception as e:
return None

@app.route('/encrypt', methods ['GET'])
def encryptage():
    valeur = request.args.get('valeur')
    user_key = request.args.get('key')
  if not valeur or not user_key:
    return "Erreur: veuillez donner à la fois la 'valeur' et la 'Key'"
  
  f = get_fernet(user_key)
if not f:
  return "Erreur: clé invalide.Assurrez vous d'utiliser une clé Fernet valide (32 url-safe base64-encoded bytes)."
  
@app.route('/decrypt', methods=['GET'])
def decryptage(token):
    token_bytes = token.encode()  # Conversion str -> bytes
    token = request.args.get('token')
    user_key = request.args.get('key')
  if not token or not user_key:
    return "Erreur: veuillez donner à la fois la 'token' et la 'Key'"
    
     f = get_fernet(user_key)
if not f:
  return "Erreur: clé invalide.Assurrez vous d'utiliser une clé Fernet valide (32 url-safe base64-encoded bytes)."

try:
  token_bytes = token.encode()
  valeur = f.decrypt(token_bytes)
  return f"Valeur décryptée : {valeur.decode()}
  except InvalidToken:
  return "Erreur: échec du décryptage.clé ou token invalide."
    except Exception as e:
    return return f"Erreur lors du décryptage: {str(e)}"
                                                                                                                                                
if __name__ == "__main__":
  app.run(debug=True)
