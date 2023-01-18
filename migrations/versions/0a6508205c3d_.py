"""empty message

Revision ID: 0a6508205c3d
Revises: 5630000b53f8
Create Date: 2022-12-23 16:13:23.184373

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a6508205c3d'
down_revision = '5630000b53f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('team_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'user', 'team', ['team_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column('user', 'team_id')
    # ### end Alembic commands ###