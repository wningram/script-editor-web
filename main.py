from types import MethodDescriptorType
from flask import request, render_template, Flask

app = Flask(__name__)
FIELDS = ['Hello', 'World', 'Goodbye']

def process_intellisense_query(query: str):
    if query is None:
        return ''
    for fld in FIELDS:
        if str(fld).lower().startswith(query.lower()):
            return fld
    return query

@app.route('/')
def index():
    return render_template('index.html', fields=FIELDS)

@app.route('/inteliquery', methods=['GET'])
def inteliquery():
    query = request.values.get('query')
    return process_intellisense_query(query)

if __name__ == '__main__':
    app.secret_key = b'nick1234'
    app.run('localhost', 8080)