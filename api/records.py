from fastapi import APIRouter
from api.dependencies import UOWDep
from schemas.records import RecordSchemaAdd
from services.records import RecordsServices

router = APIRouter(
    prefix="/records",
    tags=["Records"],
)

@router.post("")
async def add_records(
    task: RecordSchemaAdd,
    uow: UOWDep,
):
    records_id = await RecordsServices().add_record(uow, task)
    return {"records_id": records_id}


@router.get("")
async def get_records(
    uow: UOWDep,
):
    records = await RecordsServices().get_records(uow)
    return records