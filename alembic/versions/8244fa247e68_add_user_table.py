"""add user table

Revision ID: 8244fa247e68
Revises: 6ff7cc75ba44
Create Date: 2022-09-08 10:41:36.270505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8244fa247e68'
down_revision = '6ff7cc75ba44'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
