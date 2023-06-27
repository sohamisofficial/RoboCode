from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/about")
def about():
    name="Soham"
    return render_template('about.html', name = name)

app.run(debug=False,host='0.0.0.0')
