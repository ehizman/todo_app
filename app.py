from todo.views import *
from todo.models import *
from todo import app

db.create_all()
if __name__ == '__main__':
    app.run(debug=True, port=5004)
