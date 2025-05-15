from flask import Flask, request, render_template, redirect, session, url_for
import csv
import random

app = Flask(__name__)

def generate_question():
    questions = [
        {"question": "Combien font 2 + 2 ?", "reponse": "4"},
        {"question": "Quelle est la première lettre du mot 'chat' ?", "reponse": "c"},
        {"question": "Combien font 5 - 3 ?", "reponse": "2"},
        {"question": "Écrivez le mot 'bleu' en minuscules.", "reponse": "bleu"},
        {"question": "Combien de lettres dans le mot 'soleil' ?", "reponse": "6"}
    ]
    return random.choice(questions)


def conteur_ip(ip):
    compteur = 0  # Compteur pour l'IP actuelle

    table_ip = []

    with open('message.csv', 'r', encoding='utf-8') as file_ip:
        csv_reader_ip = csv.reader(file_ip)
        
        for row in csv_reader_ip:
            table_ip.append(row[0])

        for i in range (len(table_ip)-10,len(table_ip)):
            if table_ip[i] == ip:  # Vérifie si la ligne existe et si l'IP correspond
                compteur += 1

    return compteur

@app.route('/', methods =['GET','POST'])
def Accueil_post():
    return render_template('index.html')

@app.route('/Service', methods =['GET','POST'])
def service_post():
    return render_template('service.html')

@app.route('/Contact', methods=['GET', 'POST'])
def contact_post():
    q = generate_question()
    return render_template('contact.html', question=q["question"], reponse=q["reponse"] )

@app.route('/notedefrais', methods=['GET', 'POST'])
def formualire_post():
    q = generate_question()
    return render_template('formulaire.html', question=q["question"], reponse=q["reponse"] )

@app.route('/SaveFormualaire', methods=['POST'])
def saveFormulaire_message():
    ip = request.remote_addr
    if conteur_ip(ip) > 4:
        return redirect('/spam')
    nom = request.form.get('name')
    prenom = request.form.get('prenom')  # Champ honeypot
    email = request.form.get('email')
    date_deplacement = request.form.get('date_deplacement')
    lieu = request.form.get('lieu')
    distance = request.form.get('distance')
    message = request.form.get('message')
    vehicule_type = request.form.get('vehicule_type')
    repas = request.form.get('repas')
    bot = request.form.get('bot')  # Champ honeypot
    question = request.form.get('question')
    question_correct = request.form.get('correct_answer')

    
    # Si un bot remplit le champ "prenom", on ignore la requête
    if bot or question.strip().lower() != question_correct.strip().lower():  
        return redirect('/')

    new_message = [{'ip' : ip, 'name': nom, "email": email, "message": message}]

    # Sauvegarde dans le fichier CSV
    with open('formualaire.csv', mode='a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=new_message[0].keys())
        writer.writerows(new_message)

    
    return redirect('/')


@app.route('/Save', methods=['POST'])
def save_message():
    ip = request.remote_addr
    if conteur_ip(ip) > 4:
        return redirect('/spam')
    nom = request.form.get('name')
    prenom = request.form.get('prenom')  # Champ honeypot
    email = request.form.get('email')
    message = request.form.get('message')
    question = request.form.get('question')
    question_correct = request.form.get('correct_answer')

    
    # Si un bot remplit le champ "prenom", on ignore la requête
    if prenom or question.strip().lower() != question_correct.strip().lower():  
        return redirect('/')

    new_message = [{'ip' : ip, 'name': nom, "email": email, "message": message}]

    # Sauvegarde dans le fichier CSV
    with open('message.csv', mode='a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=new_message[0].keys())
        writer.writerows(new_message)

    
    return redirect('/')


@app.route('/spam')
def erreur403_post():
    return "<h1>Trop de requêtes, accès bloqué.</h1>"


if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 8808, debug=True)
