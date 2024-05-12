from sqlalchemy import func

from connect_db import session
from models import Student, Grade, Subject, Group

results = session.query(Group.group_name, func.round(func.avg(Grade.grade_value), 2))\
    .select_from(Grade)\
    .join(Student)\
    .join(Group)\
    .join(Subject)\
    .group_by(Group.group_name)\
    .all()

for result in results:
    print(result)