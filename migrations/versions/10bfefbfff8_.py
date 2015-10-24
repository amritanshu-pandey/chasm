"""empty message

Revision ID: 10bfefbfff8
Revises: 1b66d5ac7a1
Create Date: 2015-10-24 23:45:21.546680

"""

# revision identifiers, used by Alembic.
revision = '10bfefbfff8'
down_revision = '1b66d5ac7a1'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('config',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('parameter', sa.String(), nullable=False),
    sa.Column('value', sa.String(), nullable=True),
    sa.Column('description', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('config')
    ### end Alembic commands ###