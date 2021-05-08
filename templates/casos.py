from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return map_1._repr_html_()

if __name__ == '__main__':
    app.run(debug=True)
