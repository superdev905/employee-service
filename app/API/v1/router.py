from fastapi import APIRouter
from ..v1.modules.activity.routes import router as activity_router
from ..v1.modules.bank.routes import router as bank_router
from ..v1.modules.marital_status.routes import router as marital_status_router
from ..v1.modules.nationality.routes import router as nationality_router
from ..v1.modules.relationship.routes import router as relationship_router
from ..v1.modules.rsh.routes import router as rsh_router
from ..v1.modules.scholarship.routes import router as scholarship_router
from ..v1.modules.type_home.routes import router as type_home_router
from ..v1.modules.type_subsidy.routes import router as type_subsidy_router
from ..v1.modules.employee.routes import router as employee_router


router = APIRouter()


router.include_router(employee_router)
router.include_router(activity_router)
router.include_router(bank_router)
router.include_router(marital_status_router)
router.include_router(nationality_router)
router.include_router(relationship_router)
router.include_router(rsh_router)
router.include_router(scholarship_router)
router.include_router(type_home_router)
router.include_router(type_subsidy_router)
