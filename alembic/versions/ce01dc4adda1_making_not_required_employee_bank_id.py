"""making not required employee bank id

Revision ID: ce01dc4adda1
Revises: 9637a26fd0e7
Create Date: 2021-11-08 14:33:28.830548

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce01dc4adda1'
down_revision = '9637a26fd0e7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('employee', 'bank_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('employee', 'bank_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
