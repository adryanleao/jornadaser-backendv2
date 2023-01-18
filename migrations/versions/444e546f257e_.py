"""empty message

Revision ID: 444e546f257e
Revises: 9ece1481ea95
Create Date: 2022-12-13 17:36:40.973512

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '444e546f257e'
down_revision = '9ece1481ea95'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('maas',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('position', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('slug', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('module',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('secretary_maas_rating',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('maas_id', sa.Integer(), nullable=True),
    sa.Column('secretary_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['maas_id'], ['maas.id'], ),
    sa.ForeignKeyConstraint(['secretary_id'], ['secretary.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('team',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.Column('module_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['module_id'], ['module.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('team')
    op.drop_table('secretary_maas_rating')
    op.drop_table('module')
    op.drop_table('maas')
    # ### end Alembic commands ###
