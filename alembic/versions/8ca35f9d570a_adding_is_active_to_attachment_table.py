"""adding is active to attachment table

Revision ID: 8ca35f9d570a
Revises: b3775395a084
Create Date: 2021-11-10 17:14:10.310747

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ca35f9d570a'
down_revision = 'b3775395a084'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('attachment', sa.Column('is_active', sa.Boolean(), server_default='1', nullable=False))
    op.create_unique_constraint(None, 'attachment', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'attachment', type_='unique')
    op.drop_column('attachment', 'is_active')
    # ### end Alembic commands ###
