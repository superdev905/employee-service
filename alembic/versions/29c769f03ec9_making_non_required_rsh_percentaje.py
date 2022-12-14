"""making non required rsh percentaje

Revision ID: 29c769f03ec9
Revises: ae4f715f5d9e
Create Date: 2021-09-15 15:22:37.292267

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29c769f03ec9'
down_revision = 'ae4f715f5d9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('employee_relative', 'rsh_percentage_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('employee_relative', 'rsh_percentage_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
