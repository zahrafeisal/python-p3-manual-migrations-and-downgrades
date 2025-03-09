"""Renaming email column to school_email

Revision ID: 47e024998e68
Revises: 7faee1913b02
Create Date: 2025-03-09 18:02:10.601044

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47e024998e68'
down_revision = '7faee1913b02'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column(
        table_name='scholars',
        column_name='email',
        new_column_name='school_email'
    )

def downgrade() -> None:
    op.alter_column(
        table_name='scholars',
        column_name='school_email',
        new_column_name='email'
    )
