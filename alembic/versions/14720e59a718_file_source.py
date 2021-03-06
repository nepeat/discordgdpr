"""file source

Revision ID: 14720e59a718
Revises: 5ce3cd9d33e8
Create Date: 2018-06-23 09:15:26.230964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14720e59a718'
down_revision = '5ce3cd9d33e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('event_source', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events', 'event_source')
    # ### end Alembic commands ###
