"""empty message

Revision ID: 93a9f4a60f1d
Revises: 17fe463631bc
Create Date: 2020-04-23 20:27:42.300097

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '93a9f4a60f1d'
down_revision = '17fe463631bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('role', 'if_add_student')
    op.drop_column('role', 'if_look_other')
    op.drop_column('role', 'if_drop_user')
    op.drop_column('role', 'if_sure')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('role', sa.Column('if_sure', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('role', sa.Column('if_drop_user', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('role', sa.Column('if_look_other', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('role', sa.Column('if_add_student', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
