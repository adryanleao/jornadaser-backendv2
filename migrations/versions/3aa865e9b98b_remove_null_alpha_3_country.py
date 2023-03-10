"""remove null alpha 3 country

Revision ID: 3aa865e9b98b
Revises: 2b9a7af5abf9
Create Date: 2022-07-31 01:42:13.863724

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3aa865e9b98b'
down_revision = '2b9a7af5abf9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('country', 'code_alpha3',
               existing_type=mysql.VARCHAR(length=3),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('country', 'code_alpha3',
               existing_type=mysql.VARCHAR(length=3),
               nullable=False)
    # ### end Alembic commands ###
