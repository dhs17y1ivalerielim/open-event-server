"""empty message

Revision ID: 0ac3fd02c230
Revises: aa204a8b5743
Create Date: 2016-08-19 11:04:17.563277

"""

# revision identifiers, used by Alembic.
revision = '0ac3fd02c230'
down_revision = 'aa204a8b5743'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('custom_placeholder', sa.Column('copyright', sa.String(), nullable=True))
    op.add_column('custom_placeholder', sa.Column('origin', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('custom_placeholder', 'origin')
    op.drop_column('custom_placeholder', 'copyright')
    ### end Alembic commands ###
