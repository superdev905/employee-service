from fastapi import APIRouter, Depends
from .middlewares.auth import JWTBearer
from ..v1.modules.employee.routes import router as employee_router, public_router as employee_public_router
from ..v1.modules.employee_contact.routes import router as employee_contact_router
from ..v1.modules.employee_relative.routes import router as employee_relative_router
from ..v1.modules.pension_situation.routes import router as pension_situation_router
from ..v1.modules.housing_situation.routes import router as housing_situation_router
from ..v1.modules.specialization.routes import router as specialization_router
from ..v1.modules.employee_job.routes import router as employee_job_router
from ..v1.modules.attachment.routes import router as attachment_router


router = APIRouter(dependencies=[Depends(JWTBearer())])


router.include_router(employee_router)

router.include_router(employee_contact_router)
router.include_router(employee_relative_router)
router.include_router(pension_situation_router)
router.include_router(housing_situation_router)
router.include_router(specialization_router)
router.include_router(employee_job_router)
router.include_router(attachment_router)

public_router = APIRouter()
public_router.include_router(employee_public_router)
