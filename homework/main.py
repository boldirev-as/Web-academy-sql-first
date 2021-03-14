# from flask import Flask
from data import db_session
from homework.data.users import User
from homework.data.works import Jobs

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init(f"{input()}")

    db_sess = db_session.create_session()
    for user in db_sess.query(User).filter(User.address == "1"):
        print(user)

    # app.run()


if __name__ == '__main__':
    main()
