from flask import Flask, render_template, request

app = Flask(__name__)

alphabet = list("abcdefghijklmnopqrstuvwxyz")

def caesar(text, shift, direction):
    output = ""
    if direction == "decode":
        shift *= -1

    for letter in text:
        if letter in alphabet:
            shifted_index = (alphabet.index(letter) + shift) % 26
            output += alphabet[shifted_index]
        else:
            output += letter
    return output

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        direction = request.form["direction"]
        message = request.form["message"].lower()
        shift = int(request.form["shift"]) % 26
        result = caesar(message, shift, direction)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
