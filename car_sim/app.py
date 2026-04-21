from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for sessions

# -----------------------
# Fake Database (in-memory)
# -----------------------
users = {}  # username: password
configs = []  # list of car configurations


# -----------------------
# Classes
# -----------------------
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class CarConfig:
    def __init__(self, body_kit, spoiler, wheels, color, ride_height, wing_angle, owner):
        self.body_kit = body_kit
        self.spoiler = spoiler
        self.wheels = wheels
        self.color = color
        self.ride_height = ride_height
        self.wing_angle = wing_angle
        self.owner = owner


# -----------------------
# Home Page
# -----------------------
@app.route("/")
def home():
    return render_template("index.html", message="Hello from Flask!")


# -----------------------
# Car Configurator Page
# -----------------------
@app.route("/configurator", methods=["GET", "POST"])
def configurator():
    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        config = CarConfig(
            body_kit=request.form.get("body_kit"),
            spoiler=request.form.get("spoiler"),
            wheels=request.form.get("wheels"),
            color=request.form.get("color"),
            ride_height=request.form.get("ride_height"),
            wing_angle=request.form.get("wing_angle"),
            owner=session["user"]
        )

        configs.append(config)

        return redirect(url_for("results"))

    return render_template("configurator.html")


# -----------------------
# Wind Tunnel Page
# -----------------------
@app.route("/windtunnel")
def windtunnel():
    return render_template("windtunnel.html")


# -----------------------
# Results Page
# -----------------------
@app.route("/results")
def results():
    if "user" not in session:
        return redirect(url_for("login"))

    user_configs = [c for c in configs if c.owner == session["user"]]

    return render_template("results.html", configs=user_configs)


# -----------------------
# Login
# -----------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in users and users[username] == password:
            session["user"] = username
            return redirect(url_for("home"))
        else:
            return render_template("login.html", error="Invalid login")

    return render_template("login.html")


# -----------------------
# Register
# -----------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in users:
            return render_template("register.html", error="User already exists")

        users[username] = password
        return redirect(url_for("login"))

    return render_template("register.html")


# -----------------------
# Logout
# -----------------------
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))


# -----------------------
# Run App
# -----------------------
if __name__ == "__main__":
    app.run(debug=True)
