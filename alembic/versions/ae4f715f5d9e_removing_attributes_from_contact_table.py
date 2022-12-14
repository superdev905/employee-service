"""removing attributes from contact table

Revision ID: ae4f715f5d9e
Revises: 98e83c144838
Create Date: 2021-09-09 05:49:58.178902

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae4f715f5d9e'
down_revision = '98e83c144838'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employee_contact', sa.Column('commune_id', sa.Integer(), nullable=False))
    op.drop_column('employee_contact', 'region')
    op.drop_column('employee_contact', 'commune')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employee_contact', sa.Column('commune', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('employee_contact', sa.Column('region', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('employee_contact', 'commune_id')
    # ### end Alembic commands ###
