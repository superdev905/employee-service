"""adding disability % and type to employee table

Revision ID: 82fe4d85d07f
Revises: 174c3571fa0e
Create Date: 2021-11-05 14:06:35.887124

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82fe4d85d07f'
down_revision = '174c3571fa0e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employee', sa.Column('disability_type', sa.String(length=28), nullable=True))
    op.add_column('employee', sa.Column('disability_percentage', sa.String(length=40), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('employee', 'disability_percentage')
    op.drop_column('employee', 'disability_type')
    # ### end Alembic commands ###
