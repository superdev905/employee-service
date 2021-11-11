"""adding comments and phone_owner to employee and employee contact

Revision ID: 31b4c673deee
Revises: 8ca35f9d570a
Create Date: 2021-11-11 14:43:39.910018

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31b4c673deee'
down_revision = '8ca35f9d570a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employee', sa.Column('comments', sa.String(length=800), nullable=True))
    op.add_column('employee_contact', sa.Column('phone_owner', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('employee_contact', 'phone_owner')
    op.drop_column('employee', 'comments')
    # ### end Alembic commands ###
