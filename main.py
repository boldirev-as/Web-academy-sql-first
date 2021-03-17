from flask import Flask, render_template
from data import db_session
from data.db_session import create_session
from data.works import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    app.run()


@app.route("/")
def work_log():
    db_sess = create_session()
    return render_template("work_log.html", jobs=db_sess.query(Jobs).all())


if __name__ == '__main__':
    main()
