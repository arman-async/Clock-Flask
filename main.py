from flask import Flask

app = Flask(__name__)

from app.routes import *

if __name__ == '__main__':
    from app.routes import *

    app.run(debug=True)