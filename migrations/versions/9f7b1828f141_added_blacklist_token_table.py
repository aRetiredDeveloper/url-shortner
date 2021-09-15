"""added blacklist token table

Revision ID: 9f7b1828f141
Revises: c723efeea219
Create Date: 2021-09-01 00:38:54.418719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f7b1828f141'
down_revision = 'c723efeea219'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklist_tokens',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('token', sa.String(length=500), nullable=False),
    sa.Column('blacklisted_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blacklist_tokens')
    # ### end Alembic commands ###
