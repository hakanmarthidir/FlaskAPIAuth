import datetime
from functools import wraps
import jwt
from flask import request, abort
from werkzeug.security import check_password_hash
from app import api
from app.models import User


@api.route("/register", methods=['POST'])
def register():
    username = request.json['username']
    password = request.json['password']
    age = request.json['age']
    user = User(username, password, age)
    user.save()
    return 'OK', 200


@api.route("/login", methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    count = User.query.filter_by(name=username).count()

    if count == 0:
        abort(400, message='User is not found.')

    user = User.query.filter_by(name=username).first()

    if not check_password_hash(user.password, password):
        abort(400, message='Password is incorrect.')

    exp = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    payload = {
        'exp': exp,
        'iat': datetime.datetime.utcnow(),
        'uid': user.id,
        'unm': user.name,
        'uag': user.age
    }
    encoded = jwt.encode(payload, 'my secret', algorithm='HS256')
    return encoded.decode('utf-8')


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        header = request.headers.get('Authorization')
        token = header
        try:
            decoded = jwt.decode(token, 'my secret', algorithms='HS256')
            username = decoded['unm']
            count = User.query.filter_by(name=username).count()
            if count == 0:
                abort(400, message='User is not found.')
        except jwt.DecodeError:
            abort(400, message='DecodeError')
        except jwt.ExpiredSignatureError:
            abort(400, message='ExpiredSignatureError')
        except:
            abort(400, message='Problem.')

        return f(*args, **kwargs)

    return wrap
