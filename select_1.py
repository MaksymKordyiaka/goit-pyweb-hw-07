from sqlalchemy import func, desc

from connect_db import session
from models import Student, Grade

results = session.query(Student.last_name, func.round(func.avg(Grade.grade_value), 2).label('avg_grade'))\
    .select_from(Grade)\
    .join(Student)\
    .group_by(Student.student_id)\
    .order_by(desc('avg_grade'))\
    .limit(5).all()

for result in results:
    print(result)


