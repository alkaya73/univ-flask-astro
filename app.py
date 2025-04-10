from flask import Flask, render_template, request, redirect, url_for, session, abort


app = Flask(__name__)

@app.route("/")
def home():
    """HTML Index page"""
    return render_template('index.html')

@app.route("/inscription", methods=["GET", "POST"])
def inscription():
    """Page d'inscription"""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        print(f"Nom d'utilisateur : {username}")
        print(f"Mot de passe : {password}")
        
    return render_template('inscription.html')



@app.route("/connexion", methods=["GET", "POST"])
def connexion():
    """Page de connexion"""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        print(f"Tentative de connexion : {username}")
        
        if username == "admin" and password == "admin":
            print(f"Connexion réussie pour {username}")
            session["username"] = username
            return redirect(url_for("home"))
        else:
            print(f"Échec de la connexion pour {username}")
            abort(401)  


    return render_template("connexion.html")


@app.route("/appareils")
def appareils():
    """HTML appareil-photo page"""
    return render_template('appareils.html')

@app.route("/telescopes")
def telescopes():
    """HTML telescope page"""
    return render_template('telescopes.html')

@app.route("/photographies")
def photos():
    """HTML photo page"""
    return render_template('photographies.html')

if __name__ == "__main__":
    app.run(debug=True)
