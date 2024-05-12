from connect_db import session
from models import Student, Group

results = session.query(Student.last_name, Group.group_name)\
    .join(Group, Student.group_id == Group.group_id)\
    .filter(Group.group_id == 1)\
    .all()

for result in results:
    print(result)