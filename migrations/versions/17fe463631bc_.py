"""empty message

Revision ID: 17fe463631bc
Revises: 590081006b40
Create Date: 2020-04-19 20:43:57.404397

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '17fe463631bc'
down_revision = '590081006b40'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('equipment_alarm',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('alarm_time', sa.DateTime(), nullable=False),
    sa.Column('reason', sa.TEXT(), nullable=True),
    sa.Column('equipment_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['equipment_id'], ['equipment.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('equipment_record')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('equipment_record',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('alarm_time', mysql.DATETIME(), nullable=False),
    sa.Column('reason', mysql.TEXT(), nullable=True),
    sa.Column('equipment_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['equipment_id'], ['equipment.id'], name='equipment_record_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('equipment_alarm')
    # ### end Alembic commands ###
