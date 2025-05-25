"""create freebies table

Revision ID: 93dec0bd24d6
Revises: 5f72c58bf48c
Create Date: 2025-05-25 13:46:10.580597

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93dec0bd24d6'
down_revision = '5f72c58bf48c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('freebies',
    sa.Column('id', sa.Integer(), primary_key=True),
    sa.Column('item_name', sa.String(), nullable=False),
    sa.Column('value', sa.Integer(), nullable=False),
    sa.Column('dev_id', sa.Integer(), sa.ForeignKey('devs.id')),
    sa.Column('company_id', sa.Integer(), sa.ForeignKey('companies.id'))
    )
    
    pass


def downgrade() -> None:
    op.drop_table('freebies')
    pass
