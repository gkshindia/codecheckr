"""empty message

Revision ID: 10524ee73214
Revises: e5a7318a9b83
Create Date: 2019-08-12 08:03:43.150758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10524ee73214'
down_revision = 'e5a7318a9b83'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('admin', sa.Boolean(), nullable=False))
    op.execute('UPDATE users SET admin=False')
    op.alter_column('users', 'admin', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'admin')
    # ### end Alembic commands ###
