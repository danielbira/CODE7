from app import app
from app.routes import *
from app.models import usuario


if __name__ == '__main__':
    app.run(port=8080, debug=True) 