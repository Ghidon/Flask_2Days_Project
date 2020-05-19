from flask import Flask, json, request
from Instruments import Instruments
from Users import User


app = Flask(__name__)

data = {}
instruments = {}
users = {}


@app.route("/instruments")
def show_instruments():

    response = app.response_class(
        response=json.dumps(instruments),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/users")
def show_users():
    response = app.response_class(
        response=json.dumps(users),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/instruments/<instrument_name>', methods=['POST'])
def add_instrument(instrument_name):
    value = Instruments.create_id()
    new_instrument = Instruments(instrument_name, value)
    instrument_dict = {value: new_instrument.__dict__}
    instruments.update(instrument_dict)
    response = app.response_class(
        response=json.dumps(instruments),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/users/<user_name>', methods=['POST'])
def add_user(user_name):
    value = User.create_id()
    new_user = User(user_name, value, {})
    id_for_dict = {value: new_user.__dict__}
    users.update(id_for_dict)
    response = app.response_class(
        response=json.dumps(users),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/instruments/<instrument_id>')
def get_instrument_by_id(instrument_id):
    instrument_list = []
    for i in instruments.values():
        if i['instrument_id'] == instrument_id:
            instrument_list.append(i)

    response = app.response_class(
        response=json.dumps(instrument_list),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/users/<user_id>')
def get_user_by_id(user_id):
    user_list = []
    for i in users.values():
        if i["user_id"] == user_id:
            user_list.append(i)

    response = app.response_class(
        response=json.dumps(user_list),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/instruments/<instrument_id>/users/<user_id>', methods=['POST'])
def assign_instrument_to_user(instrument_id, user_id):
    for i in users.values():
        if instrument_id not in i['assigned_instruments']:
            if i['user_id'] == user_id:
                for item in instruments.values():
                    if item['instrument_id'] == instrument_id:
                        instrument_with_id = {item['instrument_id']: item}
                        i['assigned_instruments'].update(instrument_with_id)
        else:
            return 'This instrument is already assigned'

    response = app.response_class(
        response=json.dumps(users),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/users/<user_id>/instruments')
def get_instruments_by_user_id(user_id):
    response = app.response_class(
        response=json.dumps(users[user_id]['instruments']),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/instruments/<instrument_id>/video/<youtube>', methods=['POST'])
def add_video_to_instrument(instrument_id, youtube):
    for i in instruments.values():
        if i['instrument_id'] == instrument_id:
            i['youtube'] = 'https://youtu.be/' + youtube
            return 'https://youtu.be/{} has been added to {}'.format(youtube, i['instrument_name'])
        else:
            return 'There is no such instrument'


if __name__ == '__main__':
    app.run()


if __name__ == '__main__':
    app.run(debug=True)
