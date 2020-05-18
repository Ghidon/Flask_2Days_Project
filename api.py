from flask import Flask, json
from Instruments import Instruments
from JsonEncoder import MyEncoder
import request

app = Flask(__name__)


@app.route("/instruments")
def show_instruments():
    instruments = []
    violin = Instruments("violin", 1, "Ghidon", "https://www.youtube.com/watch?v=IoPsgJ2I_zo")
    instruments.append(violin)
    piano = Instruments("piano", 2, "Gigi" , "https://www.youtube.com/watch?v=WJ3-F02-F_Y")
    instruments.append(piano)
    guitar = Instruments("guitar", 3, "Maria", "https://www.youtube.com/watch?v=j4OuCMnY43E")
    instruments.append(guitar)

    json_serialized = MyEncoder().encode(instruments)

    response = app.response_class(
        response=json.dumps(json_serialized),
        status=200,
        mimetype='application/json'
    )

    return response


if __name__ == '__main__':
    app.run(debug=True)