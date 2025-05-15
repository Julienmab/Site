
from flask import Flask, render_template

app = Flask(__name__)

# Route pour la page d'accueil
@app.route('/')
def home():
    return render_template('index.html')

# Route pour la page des services
@app.route('/service')
def service():
    return render_template('service.html')

# Route pour la page de contact
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8808)  # Permet d'accepter les connexions externes
