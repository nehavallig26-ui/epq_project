from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# -----------------------
# Home Page
# -----------------------
@app.route("/")
def home():
    # Original home page content
    return render_template("index.html", message="Hello from Flask!")

# -----------------------
# Car Configurator Page
# -----------------------
@app.route("/configurator", methods=["GET", "POST"])
def configurator():
    if request.method == "POST":
        # Collect user selections from form
        body_kit = request.form.get("body_kit")
        spoiler = request.form.get("spoiler")
        wheels = request.form.get("wheels")
        color = request.form.get("color")
        ride_height = request.form.get("ride_height")
        wing_angle = request.form.get("wing_angle")
        
        # Render configurator page again with user selections
        return render_template(
            "configurator.html",
            body_kit=body_kit,
            spoiler=spoiler,
            wheels=wheels,
            color=color,
            ride_height=ride_height,
            wing_angle=wing_angle
        )
    
    # GET request — show empty form
    return render_template("configurator.html")

# -----------------------
# Future placeholder routes
# -----------------------
@app.route("/windtunnel")
def windtunnel():
    # Placeholder page for wind tunnel simulation
    return render_template("windtunnel.html")

@app.route("/results")
def results():
    # Placeholder page for results display
    return render_template("results.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    # Placeholder login page
    if request.method == "POST":
        # Add login logic here
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    # Placeholder registration page
    if request.method == "POST":
        # Add registration logic here
        return redirect(url_for("login"))
    return render_template("register.html")

# -----------------------
# Run the Flask app
# -----------------------
if __name__ == "__main__":
    app.run(debug=True)
