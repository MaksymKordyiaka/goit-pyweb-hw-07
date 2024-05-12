from connect_db import session
from models import Grade

from sqlalchemy import func

average_grade = session.query(func.round(func.avg(Grade.grade_value), 2)).scalar()
print(average_grade)
