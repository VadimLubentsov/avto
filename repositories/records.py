from Models.records import Records
from utils.repository import SQLAlchemyRepository


class RecordsRepositories(SQLAlchemyRepository):
    model = Records