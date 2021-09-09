"""removing attributes from specialization table

Revision ID: 1c4f6f67814e
Revises: 995ce972cca8
Create Date: 2021-09-09 04:50:02.404391

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c4f6f67814e'
down_revision = '995ce972cca8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('specialization', 'specialty')
    op.drop_column('specialization', 'specialty_detail')
    op.drop_column('specialization', 'certifying_entity')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('specialization', sa.Column('certifying_entity', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.add_column('specialization', sa.Column('specialty_detail', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.add_column('specialization', sa.Column('specialty', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
