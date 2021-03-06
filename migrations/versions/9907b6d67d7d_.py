"""empty message

Revision ID: 9907b6d67d7d
Revises: ee6a81b83e0d
Create Date: 2020-05-01 11:01:09.507329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9907b6d67d7d'
down_revision = 'ee6a81b83e0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_log', sa.Column('if_sure', sa.BOOLEAN(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_log', 'if_sure')
    # ### end Alembic commands ###
