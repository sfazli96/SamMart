"""created products table

Revision ID: 326bfd4c3eea
Revises: 84579b8a50e1
Create Date: 2023-03-21 13:58:27.374781

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '326bfd4c3eea'
down_revision = '84579b8a50e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=1000), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('image_url', sa.String(length=1000), nullable=False),
    sa.Column('size', sa.String(length=25), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###