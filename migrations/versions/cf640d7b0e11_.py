"""empty message

Revision ID: cf640d7b0e11
Revises: 48e58db23dca
Create Date: 2023-01-13 10:35:39.538129

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf640d7b0e11'
down_revision = '48e58db23dca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('institution', sa.Column('secretary_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'institution', 'secretary', ['secretary_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'institution', type_='foreignkey')
    op.drop_column('institution', 'secretary_id')
    # ### end Alembic commands ###