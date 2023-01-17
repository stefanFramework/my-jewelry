"""
create_sells_table

Revision ID: 4eb157d177d3
Revises: 18393773d848
"""

from alembic import op
import sqlalchemy as sa


revision = '4eb157d177d3'
down_revision = '18393773d848'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('sells',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('client_name', sa.String(length=255), nullable=False),
        sa.Column('client_email', sa.String(length=255), nullable=False),
        sa.Column('client_address', sa.Text(), nullable=False),
        sa.Column('product_id', sa.Integer(), nullable=False),
        sa.Column('price', sa.Float(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),

        sa.ForeignKeyConstraint(['product_id'], ['products.id']),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('sells')