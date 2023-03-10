"""main company id

Revision ID: 2b9a7af5abf9
Revises: 91d972c5f83e
Create Date: 2022-07-30 21:19:08.795504

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2b9a7af5abf9'
down_revision = '91d972c5f83e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('main_company_address', sa.Column('main_company_id', sa.Integer(), nullable=True))
    op.drop_constraint('main_company_address_ibfk_2', 'main_company_address', type_='foreignkey')
    op.create_foreign_key(None, 'main_company_address', 'main_company', ['main_company_id'], ['id'])
    op.drop_column('main_company_address', 'company_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('main_company_address', sa.Column('company_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'main_company_address', type_='foreignkey')
    op.create_foreign_key('main_company_address_ibfk_2', 'main_company_address', 'main_company', ['company_id'], ['id'])
    op.drop_column('main_company_address', 'main_company_id')
    # ### end Alembic commands ###
