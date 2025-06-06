"""rename post table to posts

Revision ID: a9728be23e84
Revises: a6257d4e1021
Create Date: 2025-06-06 01:18:06.198520

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a9728be23e84'
down_revision: Union[str, None] = 'a6257d4e1021'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.rename_table('post', 'posts')
    # This renames the 'post' table to 'posts'.
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.rename_table('posts', 'post')
    # This renames the 'posts' table back to 'post'.
    pass
