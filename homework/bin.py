users = [["Scott", "Scott", 21, "captain", "research engineer",
          "module_1", "scott_chief@mars.org"],
         ["Enemy", "Bolotov", 22, "captain2", "founder",
          "rodon 3", "enemy@gmail.com"],
         ["Alex", "Bolotov", 23, "captain3", "founder2",
          "dompf 3", "alex@algebra.org"],
         ["Readl", "Bolotov3", 24, "captain4", "iskatel",
          "lenina 28", "readl@.com"]]
db_sess = db_session.create_session()
for user_anwser in users:
    user = User()
    user.surname = user_anwser[0]
    user.name = user_anwser[1]
    user.age = user_anwser[2]
    user.position = user_anwser[3]
    user.speciality = user_anwser[4]
    user.address = user_anwser[5]
    user.email = user_anwser[6]
    db_sess.add(user)

job = Jobs()
job.team_leader = 1
job.job = "deployment of residential modules 1 and 2"
job.work_size = 15
job.collaborators = "2, 3"
job.is_finished = False
db_sess.add(job)

db_sess.commit()
