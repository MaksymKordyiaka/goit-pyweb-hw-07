from sqlalchemy import func, desc

from connect_db import session
from models import Student, Grade, Subject

results = session.query(Student.last_name, func.round(func.avg(Grade.grade_value), 2).label('avg_grade'))\
    .select_from(Grade)\
    .join(Student)\
    .join(Subject)\
    .filter(Subject.subject_id == 2)\
    .group_by(Student.student_id)\
    .order_by(desc('avg_grade'))\
    .limit(1)

for result in results:
    print(result)
