from fastapi import APIRouter

from api.dependencies import UOWDep
from schemas.users import UserSchemaAdd
from services.users import UsersService
from utils.hash_password import hash_password

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("")
async def add_user(
    user: UserSchemaAdd,
    uow: UOWDep,
):
    user_id = await UsersService().add_user(uow, user)
    return {"user_id": user_id}


@router.get("")
async def get_users(
    uow: UOWDep,
):
    users = await UsersService().get_users(uow)
    return users

@router.post("/register")
async def register_user(
    user: UserSchemaAdd,
    uow: UOWDep,
):
    user_id = await UsersService().register_user(uow, user)
    return {"user_id": user_id}


@router.post("/test-password")
async def test_password(password: str):
    """Тестируем хеширование пароля"""
    print(f"🧪 ТЕСТОВЫЙ ЗАПРОС:")
    print(f"   Получен пароль: '{password}'")
    print(f"   Длина: {len(password)}")
    print(f"   Байты: {len(password.encode('utf-8'))}")

    try:
        hashed = hash_password(password)
        return {
            "success": True,
            "original_length": len(password),
            "byte_length": len(password.encode('utf-8')),
            "hashed": hashed
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "original_length": len(password),
            "byte_length": len(password.encode('utf-8'))
        }