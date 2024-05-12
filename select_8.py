from sqlalchemy import func

from connect_db import session
from models import Teacher, Subject, Grade

results = session.query(Teacher.last_name, Subject.subject_name, func.round(func.avg(Grade.grade_value), 2))\
    .join(Subject, Teacher.teacher_id == Subject.teacher_id)\
    .join(Grade, Subject.subject_id == Grade.subject_id)\
    .filter(Teacher.teacher_id == 3)\
    .group_by(Teacher.last_name, Subject.subject_name)\
    .all()

for result in results:
    print(result)
