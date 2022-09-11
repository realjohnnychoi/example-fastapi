"""add content column to posts table

Revision ID: 6ff7cc75ba44
Revises: 0e35a03af5b2
Create Date: 2022-09-08 10:36:34.286382

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ff7cc75ba44'
down_revision = '0e35a03af5b2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
