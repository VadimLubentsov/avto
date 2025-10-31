import asyncio
import sys
import os

# Добавляем корневую папку в путь
sys.path.append(os.path.dirname(__file__))


async def main():
    # Импортируем ВСЕ модели
    from Models.users import UsersOrm
    from Models.records import Records

    from db.db import create_tables, engine

    print("🔄 Creating tables...")
    await create_tables()
    print("✅ Tables created!")

    # Проверяем, что таблицы существуют
    from sqlalchemy import text
    async with engine.connect() as conn:
        result = await conn.execute(
            text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"))
        tables = result.fetchall()
        print("📋 Tables in database:")
        for table in tables:
            print(f"  - {table[0]}")

    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())