"""Creating employee contact and relative table

Revision ID: a391d94511d6
Revises: e303a51a0e39
Create Date: 2021-07-28 21:20:46.334566

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a391d94511d6'
down_revision = 'e303a51a0e39'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employee_contact',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('employee_run', sa.String(length=12), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=False),
    sa.Column('number', sa.String(length=100), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=False),
    sa.Column('longitude', sa.Float(), nullable=False),
    sa.Column('region_id', sa.Integer(), nullable=False),
    sa.Column('commune_id', sa.Integer(), nullable=False),
    sa.Column('housing_group', sa.String(length=255), nullable=True),
    sa.Column('block', sa.String(length=255), nullable=True),
    sa.Column('department', sa.String(length=255), nullable=True),
    sa.Column('mobile_phone', sa.String(length=9), nullable=True),
    sa.Column('landline_phone', sa.String(length=12), nullable=True),
    sa.Column('other_phone', sa.String(length=9), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('is_confirmed', sa.Boolean(), nullable=True),
    sa.Column('state', sa.String(length=7), nullable=False),
    sa.Column('is_main', sa.Boolean(), nullable=False),
    sa.Column('created_by', sa.String(length=20), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('update_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['employee_run'], ['employee.run'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('employee_run')
    )
    op.create_table('employee_relative',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('employee_run', sa.String(length=12), nullable=False),
    sa.Column('run', sa.String(length=12), nullable=True),
    sa.Column('names', sa.String(length=255), nullable=False),
    sa.Column('paternal_surname', sa.String(length=120), nullable=False),
    sa.Column('maternal_surname', sa.String(length=120), nullable=False),
    sa.Column('born_date', sa.DateTime(), nullable=False),
    sa.Column('gender', sa.String(length=50), nullable=False),
    sa.Column('marital_status_id', sa.Integer(), nullable=True),
    sa.Column('scholarship_id', sa.Integer(), nullable=True),
    sa.Column('nationality_id', sa.Integer(), nullable=True),
    sa.Column('job_id', sa.Integer(), nullable=True),
    sa.Column('relationship_id', sa.Integer(), nullable=True),
    sa.Column('legal_charge', sa.String(length=2), nullable=False),
    sa.Column('rsh', sa.String(length=2), nullable=True),
    sa.Column('rsh_percentage_id', sa.Integer(), nullable=True),
    sa.Column('state', sa.String(length=7), nullable=False),
    sa.Column('is_main', sa.Boolean(), nullable=False),
    sa.Column('created_by', sa.String(length=20), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('update_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['employee_run'], ['employee.run'], ),
    sa.ForeignKeyConstraint(['job_id'], ['activity.id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['marital_status_id'], ['marital_status.id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['nationality_id'], ['nationality.id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['relationship_id'], ['relationship.id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['rsh_percentage_id'], ['rsh.id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['scholarship_id'], ['scholarship.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('run')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employee_relative')
    op.drop_table('employee_contact')
    # ### end Alembic commands ###
