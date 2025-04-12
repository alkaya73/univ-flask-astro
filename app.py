from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)
app.secret_key = "key_secret"


@app.route("/")
def home():
    """HTML Index page"""
    return render_template('index.html')

@app.route("/inscription", methods=["GET", "POST"])
def inscription():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        print(f"Nom d'utilisateur : {username}")
        print(f"Email : {email}")

        if password == confirm_password:
            flash("Inscription réussite.", "success")
            return redirect(url_for("home"))
        else:
            flash("Les mots de passe ne correspondent pas.", "danger")
            return redirect(url_for("inscription"))

    return render_template('inscription.html')

def get_accounts():
    with open("comptes.txt", "r") as f:
        return {line.strip().split(":")[0]: line.strip().split(":")[1] for line in f}

@app.route("/connexion", methods=["GET", "POST"])
def connexion():
    """Page de connexion"""
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        print(f"Tentative de connexion avec {email}.")

        comptes = get_accounts()

        if comptes.get(email) == password:
            flash(f"Connexion réussie pour {email}.", "success")
            return redirect(url_for("home"))
        else:
            flash("Erreur de connexion : mail ou mot de passe incorrect.", "danger")
            return redirect(url_for("connexion"))

    return render_template('connexion.html')


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
