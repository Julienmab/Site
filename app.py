from flask import Flask, render_template, request, redirect, url_for
import csv
from datetime import datetime

app = Flask(__name__)

# Route pour la page d'accueil
@app.route('/')
def index():
    return render_template('index.html')  # Accueil

# Route pour la page Service
@app.route('/service')
def service():
    return render_template('service.html')  # Page Services

# Route pour la page Contact
@app.route('/contact')
def contact():
    return render_template('contact.html')  # Page Contact

# Route pour la page Note de frais
@app.route('/notedefrais', methods=['GET', 'POST'])
def notedefrais():
    if request.method == 'POST':
        # Récupération des données du formulaire
        nom = request.form['nom']
        prenom = request.form['prenom']
        email = request.form['email']
        date_deplacement = request.form['date_deplacement']
        lieu = request.form['lieu']
        distance = request.form['distance']
        type_vehicule = request.form['type_vehicule']
        repas = request.form['repas']
        
        # Sauvegarde des données dans un fichier CSV
        with open('frais_de_deplacement.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            # Écriture des données en ligne dans le fichier CSV
            writer.writerow([nom, prenom, email, date_deplacement, lieu, distance, type_vehicule, repas])
        
        # Redirection après la soumission du formulaire
        return redirect(url_for('merci'))

    return render_template('formulaire.html')  # Affichage du formulaire de frais

# Route pour afficher une page de remerciement
@app.route('/merci')
def merci():
    return "Merci pour votre soumission !"

if __name__ == "__main__":
    app.run(debug=True)
