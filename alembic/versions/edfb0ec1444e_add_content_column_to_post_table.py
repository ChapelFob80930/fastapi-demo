"""add_content_column_to_post_table

Revision ID: edfb0ec1444e
Revises: ac5cad686b1f
Create Date: 2025-06-06 01:02:56.143472

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'edfb0ec1444e'
down_revision: Union[str, None] = 'ac5cad686b1f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('post', sa.Column('content', sa.String(), nullable = False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('post', 'content')
    pass
