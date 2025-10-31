from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from api.routers import all_routers
from db.db import create_tables
from Models.users import UsersOrm
from Models.records import Records




@asynccontextmanager
async def lifespan(app: FastAPI):
    # Убедимся, что таблицы созданы ДО запуска сервера
    print("🔄 Starting table creation...")
    await create_tables()
    print("✅ Database tables created!")

    # Дадим время для завершения создания таблиц
    from sqlalchemy.testing import asyncio
    await asyncio.sleep(1)

    yield

    print("🛑 Application shutdown")
app = FastAPI(
    title="Упрощенный аналог Jira/Asana"
)

for router in all_routers:
    app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)