from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import IsapreFonasa
from .schema import IsapreFonasa as IsapreFonasaSchema, IsapreFonasaCreate


router = SQLAlchemyCRUDRouter(
    schema=IsapreFonasaSchema,
    create_schema=IsapreFonasaCreate,
    db_model=IsapreFonasa,
    db=get_database,
    prefix="isapre-fonasa"
)
