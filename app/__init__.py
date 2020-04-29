#import bibliotek
from flask import Flask
#utwotrzenie instancji (obiektu) klasy Flask reprezentującej aplikację
app = Flask(__name__)

#from app import routes
from app import views

if __name__ == "__main__":
    app.run(debug=True)
