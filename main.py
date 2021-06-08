from flask import request, render_template, Flask

app = Flask(__name__)
FIELDS = ['Hello', 'World', 'Goodbye']

@app.route('/')
def index():
    return render_template('index.html', fields=FIELDS)

if __name__ == '__main__':
    app.secret_key = b'nick1234'
    app.run('localhost', 8080)