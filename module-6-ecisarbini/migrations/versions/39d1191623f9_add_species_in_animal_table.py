"""add species in animal table

Revision ID: 39d1191623f9
Revises: d5b717a1bf72
Create Date: 2024-02-19 15:33:55.454811

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39d1191623f9'
down_revision = 'd5b717a1bf72'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('animal', schema=None) as batch_op:
        batch_op.add_column(sa.Column('species', sa.String(length=100), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('animal', schema=None) as batch_op:
        batch_op.drop_column('species')

    # ### end Alembic commands ###
