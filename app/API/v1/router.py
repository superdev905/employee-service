from fastapi import APIRouter
from ..v1.modules.activity.routes import router as activity_router
from ..v1.modules.bank.routes import router as bank_router
from ..v1.modules.marital_status.routes import router as marital_status_router
from ..v1.modules.nationality.routes import router as nationality_router
from ..v1.modules.relationship.routes import router as relationship_router
from ..v1.modules.rsh.routes import router as rsh_router
from ..v1.modules.scholarship.routes import router as scholarship_router
from ..v1.modules.type_home.routes import router as type_home_router
from ..v1.modules.property_home.routes import router as property_home_router
from ..v1.modules.type_subsidy.routes import router as type_subsidy_router
from ..v1.modules.employee.routes import router as employee_router
from ..v1.modules.employee_contact.routes import router as employee_contact_router
from ..v1.modules.employee_relative.routes import router as employee_relative_router
from ..v1.modules.isapre_fonasa.routes import router as isapre_fonasa_router
from ..v1.modules.afp_isp.routes import router as afp_isp_router
from ..v1.modules.pension_situation.routes import router as pension_situation_router
from ..v1.modules.housing_situation.routes import router as housing_situation_router
from ..v1.modules.specialty.routes import router as specialty_router
from ..v1.modules.sub_specialty.routes import router as sub_specialty_router
from ..v1.modules.entity.routes import router as entity_router
from ..v1.modules.specialization.routes import router as specialization_router
from ..v1.modules.employee_job.routes import router as employee_job_router


router = APIRouter()


router.include_router(employee_router)
router.include_router(employee_contact_router)
router.include_router(employee_relative_router)
router.include_router(pension_situation_router)
router.include_router(housing_situation_router)
router.include_router(specialization_router)
router.include_router(employee_job_router)
router.include_router(activity_router)
router.include_router(specialty_router)
router.include_router(sub_specialty_router)
router.include_router(entity_router)
router.include_router(isapre_fonasa_router)
router.include_router(afp_isp_router)
router.include_router(bank_router)
router.include_router(marital_status_router)
router.include_router(nationality_router)
router.include_router(relationship_router)
router.include_router(rsh_router)
router.include_router(scholarship_router)
router.include_router(type_home_router)
router.include_router(property_home_router)
router.include_router(type_subsidy_router)
