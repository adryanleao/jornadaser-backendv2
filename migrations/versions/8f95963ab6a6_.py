"""empty message

Revision ID: 8f95963ab6a6
Revises: b8f94deaa786
Create Date: 2022-12-08 16:36:58.125292

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f95963ab6a6'
down_revision = 'b8f94deaa786'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('institution',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('hash_id', sa.String(length=36), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('site', sa.String(length=255), nullable=True),
    sa.Column('cell_phone', sa.String(length=255), nullable=True),
    sa.Column('responsible', sa.String(length=255), nullable=True),
    sa.Column('responsible_phone', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('function', sa.String(length=255), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('hash_id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('secretary',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('hash_id', sa.String(length=36), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('organ', sa.String(length=255), nullable=True),
    sa.Column('site', sa.String(length=255), nullable=True),
    sa.Column('cell_phone', sa.String(length=255), nullable=True),
    sa.Column('responsible', sa.String(length=255), nullable=True),
    sa.Column('responsible_phone', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('function', sa.String(length=255), nullable=True),
    sa.Column('image_key', sa.String(length=255), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('hash_id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('institution_address',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('code_post', sa.String(length=256), nullable=True),
    sa.Column('street', sa.String(length=256), nullable=True),
    sa.Column('number', sa.String(length=256), nullable=True),
    sa.Column('district', sa.String(length=256), nullable=True),
    sa.Column('complement', sa.String(length=256), nullable=True),
    sa.Column('lat', sa.String(length=256), nullable=True),
    sa.Column('long', sa.String(length=256), nullable=True),
    sa.Column('city_id', sa.Integer(), nullable=True),
    sa.Column('institution_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['city_id'], ['city.id'], ),
    sa.ForeignKeyConstraint(['institution_id'], ['institution.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('secretary_address',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('code_post', sa.String(length=256), nullable=True),
    sa.Column('street', sa.String(length=256), nullable=True),
    sa.Column('number', sa.String(length=256), nullable=True),
    sa.Column('district', sa.String(length=256), nullable=True),
    sa.Column('complement', sa.String(length=256), nullable=True),
    sa.Column('lat', sa.String(length=256), nullable=True),
    sa.Column('long', sa.String(length=256), nullable=True),
    sa.Column('city_id', sa.Integer(), nullable=True),
    sa.Column('secretary_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['city_id'], ['city.id'], ),
    sa.ForeignKeyConstraint(['secretary_id'], ['secretary.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('secretary_address')
    op.drop_table('institution_address')
    op.drop_table('secretary')
    op.drop_table('institution')
    # ### end Alembic commands ###
