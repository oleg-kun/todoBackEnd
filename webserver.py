from resources import Entry
from manager import EntryManager
from flask import Flask, request

FOLDER = 'C:/Users/User/PycharmProjects/'

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>aw"


@app.route("/api/entries/")
def get_entries():
    entry_manager = EntryManager(FOLDER)
    entry_manager.load()
    list_of_json = []
    for entry in entry_manager.entries:
        list_of_json.append(entry.json())
    return list_of_json


@app.route('/api/save_entries/', methods=['POST'])
def save_entries():
    entry_manager = EntryManager(FOLDER)
    list_request = request.get_json()
    for entry in list_request:
        entry_from_json = Entry.from_json(entry)
        entry_manager.entries.append(entry_from_json)
    entry_manager.save()
    return {'status': 'success'}


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)