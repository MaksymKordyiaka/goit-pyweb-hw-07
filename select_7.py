from sqlalchemy import func

from connect_db import session
from models import Student, Group, Subject, Grade

results = session.query(Student.last_name, func.round(Grade.grade_value, 2))\
    .join(Group, Student.group_id == Group.group_id)\
    .join(Grade)\
    .join(Subject, Grade.subject_id == Subject.subject_id)\
    .filter(Group.group_id == 2)\
    .filter(Subject.subject_id == 3)\
    .all()

for result in results:
    print(result)