from fastapi_crudrouter import SQLAlchemyCRUDRouter
from app.database.main import get_database
from .model import AfpIsp
from .schema import AfpIsp as AfpIspSchema, AfpIspCreate


router = SQLAlchemyCRUDRouter(
    schema=AfpIspSchema,
    create_schema=AfpIspCreate,
    db_model=AfpIsp,
    db=get_database,
    prefix="afp-isp"
)
