from flask import Flask, render_template, request, redirect, url_for
import csv
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')  


@app.route('/service')
def service():
    return render_template('service.html')  


@app.route('/contact')
def contact():
    return render_template('contact.html')  


@app.route('/notedefrais', methods=['GET', 'POST'])
def notedefrais():
    if request.method == 'POST':
       
        nom = request.form['nom']
        prenom = request.form['prenom']
        email = request.form['email']
        date_deplacement = request.form['date_deplacement']
        lieu = request.form['lieu']
        distance = request.form['distance']
        type_vehicule = request.form['type_vehicule']
        repas = request.form['repas']
        
        
        with open('frais_de_deplacement.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            
            writer.writerow([nom, prenom, email, date_deplacement, lieu, distance, type_vehicule, repas])
        
       
        return redirect(url_for('merci'))

    return render_template('formulaire.html')  


@app.route('/merci')
def merci():
    return "Merci pour votre soumission !"

if __name__ == "__main__":
    app.run(debug=True)
