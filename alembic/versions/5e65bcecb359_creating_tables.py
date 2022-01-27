"""creating tables

Revision ID: 5e65bcecb359
Revises: 
Create Date: 2021-09-07 16:00:29.451054

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e65bcecb359'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employee',
                    sa.Column('id', sa.Integer(),
                              autoincrement=True, nullable=False),
                    sa.Column('run', sa.String(length=12), nullable=False),
                    sa.Column('names', sa.String(length=120), nullable=False),
                    sa.Column('paternal_surname', sa.String(
                        length=120), nullable=False),
                    sa.Column('maternal_surname', sa.String(
                        length=120), nullable=False),
                    sa.Column('born_date', sa.DateTime(), nullable=False),
                    sa.Column('gender', sa.String(length=50), nullable=False),
                    sa.Column('marital_status_id',
                              sa.Integer(), nullable=False),
                    sa.Column('scholarship_id', sa.Integer(), nullable=False),
                    sa.Column('disability', sa.String(
                        length=2), nullable=False),
                    sa.Column('credential_disability',
                              sa.String(length=2), nullable=False),
                    sa.Column('recognize', sa.String(
                        length=2), nullable=False),
                    sa.Column('nationality_id', sa.Integer(), nullable=False),
                    sa.Column('alive', sa.String(length=2), nullable=False),
                    sa.Column('bank_id', sa.Integer(), nullable=False),
                    sa.Column('account_type', sa.String(
                        length=100), nullable=True),
                    sa.Column('account_number', sa.String(
                        length=100), nullable=True),
                    sa.Column('rsh', sa.String(length=100), nullable=True),
                    sa.Column('rsh_percentage', sa.String(
                        length=100), nullable=True),
                    sa.Column('state', sa.String(length=7),
                              server_default='CREATED', nullable=False),
                    sa.Column('created_by', sa.Integer(), nullable=False),
                    sa.Column('created_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.Column('update_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id', 'run'),
                    sa.UniqueConstraint('id'),
                    sa.UniqueConstraint('run')
                    )
    op.create_table('employee_contact',
                    sa.Column('id', sa.Integer(),
                              autoincrement=True, nullable=False),
                    sa.Column('employee_run', sa.String(
                        length=12), nullable=True),
                    sa.Column('address', sa.String(
                        length=255), nullable=False),
                    sa.Column('number', sa.String(length=100), nullable=False),
                    sa.Column('latitude', sa.Float(), nullable=False),
                    sa.Column('longitude', sa.Float(), nullable=False),
                    sa.Column('region_id', sa.Integer(), nullable=False),
                    sa.Column('region', sa.Integer(), nullable=False),
                    sa.Column('commune', sa.Integer(), nullable=False),
                    sa.Column('housing_group', sa.String(
                        length=255), nullable=True),
                    sa.Column('block', sa.String(length=255), nullable=True),
                    sa.Column('department', sa.String(
                        length=255), nullable=True),
                    sa.Column('mobile_phone', sa.String(
                        length=9), nullable=True),
                    sa.Column('landline_phone', sa.String(
                        length=12), nullable=True),
                    sa.Column('other_phone', sa.String(
                        length=9), nullable=True),
                    sa.Column('email', sa.String(length=255), nullable=False),
                    sa.Column('is_confirmed', sa.Boolean(), nullable=True),
                    sa.Column('state', sa.String(length=7), nullable=False),
                    sa.Column('is_main', sa.Boolean(), nullable=False),
                    sa.Column('confirmation_date',
                              sa.DateTime(), nullable=False),
                    sa.Column('created_by', sa.Integer(), nullable=False),
                    sa.Column('created_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.Column('update_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.ForeignKeyConstraint(
                        ['employee_run'], ['employee.run'], ondelete='CASCADE', onupdate="CASCADE"),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    op.create_table('employee_job',
                    sa.Column('id', sa.Integer(),
                              autoincrement=True, nullable=False),
                    sa.Column('employee_id', sa.Integer(), nullable=False),
                    sa.Column('admission_date', sa.DateTime(), nullable=False),
                    sa.Column('business_id', sa.Integer(), nullable=False),
                    sa.Column('business_name', sa.String(
                        length=255), nullable=True),
                    sa.Column('construction_id', sa.Integer(), nullable=False),
                    sa.Column('construction_name', sa.String(
                        length=255), nullable=True),
                    sa.Column('contract_term', sa.String(
                        length=50), nullable=False),
                    sa.Column('contract_type', sa.String(
                        length=50), nullable=False),
                    sa.Column('leave_date', sa.DateTime(), nullable=True),
                    sa.Column('leave_motive', sa.String(
                        length=120), nullable=True),
                    sa.Column('salary', sa.Float(), nullable=False),
                    sa.Column('state', sa.String(length=7), nullable=False),
                    sa.Column('created_by', sa.Integer(), nullable=False),
                    sa.Column('created_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.Column('update_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.ForeignKeyConstraint(
                        ['employee_id'], ['employee.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('employee_relative',
                    sa.Column('id', sa.Integer(),
                              autoincrement=True, nullable=False),
                    sa.Column('employee_run', sa.String(
                        length=12), nullable=False),
                    sa.Column('run', sa.String(length=12), nullable=True),
                    sa.Column('names', sa.String(length=255), nullable=False),
                    sa.Column('paternal_surname', sa.String(
                        length=120), nullable=False),
                    sa.Column('maternal_surname', sa.String(
                        length=120), nullable=False),
                    sa.Column('born_date', sa.DateTime(), nullable=False),
                    sa.Column('gender', sa.String(length=50), nullable=False),
                    sa.Column('marital_status_id',
                              sa.Integer(), nullable=False),
                    sa.Column('marital_status', sa.String(
                        length=100), nullable=False),
                    sa.Column('scholarship_id', sa.Integer(), nullable=False),
                    sa.Column('scholarship', sa.String(
                        length=100), nullable=False),
                    sa.Column('nationality_id', sa.Integer(), nullable=False),
                    sa.Column('nationality', sa.String(
                        length=100), nullable=False),
                    sa.Column('job_id', sa.Integer(), nullable=False),
                    sa.Column('relationship_id', sa.Integer(), nullable=False),
                    sa.Column('relationship_name', sa.String(
                        length=100), nullable=False),
                    sa.Column('legal_charge', sa.String(
                        length=2), nullable=False),
                    sa.Column('rsh', sa.String(length=2), nullable=True),
                    sa.Column('rsh_percentage_id',
                              sa.Integer(), nullable=False),
                    sa.Column('state', sa.String(length=7), nullable=False),
                    sa.Column('is_main', sa.Boolean(), nullable=False),
                    sa.Column('created_by', sa.Integer(), nullable=False),
                    sa.Column('created_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.Column('update_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.ForeignKeyConstraint(
                        ['employee_run'], ['employee.run'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('housing_situation',
                    sa.Column('id', sa.Integer(),
                              autoincrement=True, nullable=False),
                    sa.Column('employee_id', sa.Integer(), nullable=False),
                    sa.Column('type_home_id', sa.Integer(), nullable=False),
                    sa.Column('property_home_id',
                              sa.Integer(), nullable=False),
                    sa.Column('type_subsidy_id', sa.Integer(), nullable=False),
                    sa.Column('description', sa.String(
                        length=255), nullable=False),
                    sa.Column('state', sa.String(length=7), nullable=False),
                    sa.Column('is_main', sa.Boolean(), nullable=False),
                    sa.Column('created_by', sa.Integer(), nullable=False),
                    sa.Column('created_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.Column('update_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.ForeignKeyConstraint(
                        ['employee_id'], ['employee.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('pension_situation',
                    sa.Column('id', sa.Integer(),
                              autoincrement=True, nullable=False),
                    sa.Column('employee_id', sa.Integer(), nullable=False),
                    sa.Column('isapre_fonasa_id',
                              sa.Integer(), nullable=False),
                    sa.Column('afp_isp_id', sa.Integer(), nullable=False),
                    sa.Column('is_pensioner', sa.String(
                        length=2), nullable=False),
                    sa.Column('pension_amount', sa.Float(), nullable=True),
                    sa.Column('belongs_to_recognize', sa.String(
                        length=2), nullable=False),
                    sa.Column('state', sa.String(length=7), nullable=False),
                    sa.Column('is_main', sa.Boolean(), nullable=False),
                    sa.Column('created_by', sa.Integer(), nullable=False),
                    sa.Column('created_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.Column('update_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.ForeignKeyConstraint(
                        ['employee_id'], ['employee.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('specialization',
                    sa.Column('id', sa.Integer(),
                              autoincrement=True, nullable=False),
                    sa.Column('employee_id', sa.Integer(), nullable=False),
                    sa.Column('specialty_id', sa.Integer(), nullable=False),
                    sa.Column('specialty', sa.String(
                        length=255), nullable=False),
                    sa.Column('specialty_detail_id',
                              sa.Integer(), nullable=False),
                    sa.Column('specialty_detail', sa.String(
                        length=255), nullable=False),
                    sa.Column('is_self_taught', sa.String(
                        length=2), nullable=False),
                    sa.Column('certifying_entity_id',
                              sa.Integer(), nullable=True),
                    sa.Column('certifying_entity', sa.String(
                        length=255), nullable=False),
                    sa.Column('is_certificated', sa.String(
                        length=2), nullable=True),
                    sa.Column('certification_url', sa.String(
                        length=255), nullable=True),
                    sa.Column('certificated_date',
                              sa.DateTime(), nullable=True),
                    sa.Column('state', sa.String(length=7), nullable=False),
                    sa.Column('created_by', sa.Integer(), nullable=False),
                    sa.Column('created_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.Column('update_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.ForeignKeyConstraint(
                        ['employee_id'], ['employee.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('specialization')
    op.drop_table('pension_situation')
    op.drop_table('housing_situation')
    op.drop_table('employee_relative')
    op.drop_table('employee_job')
    op.drop_table('employee_contact')
    op.drop_table('employee')
    # ### end Alembic commands ###
