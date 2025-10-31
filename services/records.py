from schemas.records import RecordSchemaAdd


from schemas.records import RecordSchemaAdd

class RecordsServices:
    def __init__(self):

        pass

    async def add_record(self, uow, record: RecordSchemaAdd) -> int:
        async with uow:
            record_dict = record.model_dump()
            record_id = await uow.records.add_one(record_dict)
            await uow.commit()
            return record_id

    async def get_records(self, uow) -> list:
        async with uow:
            records = await uow.records.find_all()
            return records