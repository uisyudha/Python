# Import lib flask
from flask import Flask

# Inisialisasi object flask
app = Flask(__name__)

# Definisi route URL dan fungsi yang menghandle
@app.route('/', methods=['GET'])
def helloWordl():
    return "Hello World"

app.run(debug=True, port=9998)


