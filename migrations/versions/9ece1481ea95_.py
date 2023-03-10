"""empty message

Revision ID: 9ece1481ea95
Revises: 8f95963ab6a6
Create Date: 2022-12-09 10:09:48.589488

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ece1481ea95'
down_revision = '8f95963ab6a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('extra_material',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('hash_id', sa.String(length=36), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('type', sa.String(length=255), nullable=True),
    sa.Column('user_type', sa.String(length=255), nullable=True),
    sa.Column('module', sa.String(length=255), nullable=True),
    sa.Column('link', sa.String(length=255), nullable=True),
    sa.Column('file_key', sa.String(length=255), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('institution_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['institution_id'], ['institution.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('hash_id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('notification',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('hash_id', sa.String(length=36), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('user_type', sa.String(length=255), nullable=True),
    sa.Column('team', sa.String(length=255), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('institution_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['institution_id'], ['institution.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('hash_id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('notification')
    op.drop_table('extra_material')
    # ### end Alembic commands ###
