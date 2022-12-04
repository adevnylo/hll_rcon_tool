"""Add constraint on player at datapoint

Revision ID: 11a37fe6d49c
Revises: 85c3ad32a4ad
Create Date: 2022-01-06 17:42:53.286519

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11a37fe6d49c'
down_revision = '85c3ad32a4ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('unique_player_at_count', 'player_at_count', ['playersteamid_id', 'servercount_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('unique_player_at_count', 'player_at_count', type_='unique')
    # ### end Alembic commands ###
