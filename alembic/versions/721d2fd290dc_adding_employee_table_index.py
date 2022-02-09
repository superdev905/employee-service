"""adding employee table index

Revision ID: 721d2fd290dc
Revises: 2b3da73b6d27
Create Date: 2022-02-09 13:28:06.995288

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '721d2fd290dc'
down_revision = '2b3da73b6d27'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_employee_id'), 'employee', ['id'], unique=True)
    op.create_index(op.f('ix_employee_maternal_surname'),
                    'employee', ['maternal_surname'], unique=False)
    op.create_index(op.f('ix_employee_names'),
                    'employee', ['names'], unique=False)
    op.create_index(op.f('ix_employee_paternal_surname'),
                    'employee', ['paternal_surname'], unique=False)
    op.create_index(op.f('ix_employee_run'), 'employee', ['run'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_employee_run'), table_name='employee')
    op.drop_index(op.f('ix_employee_paternal_surname'), table_name='employee')
    op.drop_index(op.f('ix_employee_names'), table_name='employee')
    op.drop_index(op.f('ix_employee_maternal_surname'), table_name='employee')
    op.drop_index(op.f('ix_employee_id'), table_name='employee')
    # ### end Alembic commands ###
