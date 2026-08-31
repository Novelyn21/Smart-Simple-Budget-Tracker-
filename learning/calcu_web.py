from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    display_value = "0"
    
    if request.method == "POST":
        current_display = request.form.get("display", "0")
        button_pressed = request.form.get("button", "")

        if button_pressed == "C":
            display_value = "0"
        elif button_pressed == "=":
            try:
                display_value = str(eval(current_display))
            except:
                display_value = "Error"
        else:
            if current_display == "0" or current_display == "Error":
                display_value = button_pressed
            else:
                display_value = current_display + button_pressed

    return render_template("index.html", result=display_value)

if __name__ == "__main__":
    app.run(debug=True)
