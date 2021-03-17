# from flask import Flask
from data.db_session import *
from data.department import Department
from data.users import User
from data.works import Jobs

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    global_init(f"{input()}")

    db_sess = create_session()
    users = list()
    for department in db_sess.query(Department).filter(Department.id == 1):
        users.extend(department.members.split(", "))

    work_ours = dict()
    for job in db_sess.query(Jobs).all():
        for member in job.collaborators.split(", "):
            if member in set(users):
                if member in work_ours.keys():
                    work_ours[member] += job.work_size
                else:
                    work_ours[member] = job.work_size

    for user in db_sess.query(User).all():
        if user.id in list(map(int, work_ours.keys())) and \
                work_ours[str(user.id)] > 25:
            print(user.name, user.surname)

    # app.run()


main()
