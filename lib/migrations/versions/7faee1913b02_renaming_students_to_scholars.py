"""Renaming students to scholars

Revision ID: 7faee1913b02
Revises: 791279dd0760
Create Date: 2025-03-09 17:51:16.171673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7faee1913b02'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')