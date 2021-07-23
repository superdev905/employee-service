"""Creating collection tables

Revision ID: a1bd87b0f3f7
Revises: 
Create Date: 2021-07-23 07:07:02.838926

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1bd87b0f3f7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('activity',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('description', sa.String(
                        length=255), nullable=False),
                    sa.Column('created_by', sa.String(
                        length=20), nullable=True),
                    sa.Column('created_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.Column('update_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('description')
                    )
    op.create_table('bank',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('description', sa.String(
                        length=255), nullable=False),
                    sa.Column('created_by', sa.String(
                        length=20), nullable=True),
                    sa.Column('created_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.Column('update_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('description')
                    )
    op.create_table('marital_status',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('description', sa.String(
                        length=255), nullable=False),
                    sa.Column('created_by', sa.String(
                        length=20), nullable=True),
                    sa.Column('created_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.Column('update_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('description')
                    )
    op.create_table('nationality',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('description', sa.String(
                        length=255), nullable=False),
                    sa.Column('created_by', sa.String(
                        length=20), nullable=True),
                    sa.Column('created_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.Column('update_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('description')
                    )
    op.create_table('relationship',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('description', sa.String(
                        length=255), nullable=False),
                    sa.Column('created_by', sa.String(
                        length=20), nullable=True),
                    sa.Column('created_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.Column('update_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('description')
                    )
    op.create_table('rsh',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('description', sa.String(
                        length=255), nullable=False),
                    sa.Column('created_by', sa.String(
                        length=20), nullable=True),
                    sa.Column('created_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.Column('update_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('description')
                    )
    op.create_table('scholarship',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('description', sa.String(
                        length=255), nullable=False),
                    sa.Column('created_by', sa.String(
                        length=20), nullable=True),
                    sa.Column('created_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.Column('update_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('description')
                    )
    op.create_table('types_home',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('description', sa.String(
                        length=255), nullable=False),
                    sa.Column('created_by', sa.String(
                        length=20), nullable=True),
                    sa.Column('created_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.Column('update_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('description')
                    )
    op.create_table('types_subsidy',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('description', sa.String(
                        length=255), nullable=False),
                    sa.Column('created_by', sa.String(
                        length=20), nullable=True),
                    sa.Column('created_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.Column('update_at', sa.DateTime(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('description')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('types_subsidy')
    op.drop_table('types_home')
    op.drop_table('scholarship')
    op.drop_table('rsh')
    op.drop_table('relationship')
    op.drop_table('nationality')
    op.drop_table('marital_status')
    op.drop_table('bank')
    op.drop_table('activity')
    # ### end Alembic commands ###
