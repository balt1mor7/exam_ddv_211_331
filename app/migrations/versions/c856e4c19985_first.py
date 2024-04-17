"""first

Revision ID: c856e4c19985
Revises: 
Create Date: 2024-04-17 15:41:43.625062

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c856e4c19985'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('performances',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_performances')),
    sa.UniqueConstraint('name', name=op.f('uq_performances_name'))
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(length=20), nullable=False),
    sa.Column('tel_number', sa.String(length=20), nullable=False),
    sa.Column('sms_code', sa.String(length=4), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users'))
    )
    op.create_table('tickets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('performance_id', sa.Integer(), nullable=False),
    sa.Column('sector', sa.String(length=1), nullable=False),
    sa.Column('place', sa.String(length=25), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('time', sa.Time(), nullable=False),
    sa.ForeignKeyConstraint(['performance_id'], ['performances.id'], name=op.f('fk_tickets_performance_id_performances')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_tickets_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_tickets'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tickets')
    op.drop_table('users')
    op.drop_table('performances')
    # ### end Alembic commands ###
