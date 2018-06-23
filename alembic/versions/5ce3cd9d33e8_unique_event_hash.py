"""unique event hash

Revision ID: 5ce3cd9d33e8
Revises: bee6bc0bfefc
Create Date: 2018-06-23 08:55:36.765679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ce3cd9d33e8'
down_revision = 'bee6bc0bfefc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('event_hash', sa.String(), nullable=False))
    op.create_unique_constraint(None, 'events', ['event_hash'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'events', type_='unique')
    op.drop_column('events', 'event_hash')
    # ### end Alembic commands ###