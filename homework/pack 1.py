# from flask import Flask
# from data.db_session import *
# from homework.data.users import User
# from homework.data.works import Jobs

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    global_init(f"{input()}")

    db_sess = create_session()
    for user in db_sess.query(User).filter(User.address == "module_1", User.speciality.notlike('%engineer%'),
                                           User.position.notlike("%engineer%")):
        print(user.id)

    # app.run()


main()
