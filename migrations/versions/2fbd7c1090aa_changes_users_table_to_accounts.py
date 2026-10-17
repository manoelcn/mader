"""changes users table to accounts

Revision ID: 2fbd7c1090aa
Revises: eef0432baf32
Create Date: 2026-10-16 18:30:03.751567

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = '2fbd7c1090aa'
down_revision: Union[str, Sequence[str], None] = 'eef0432baf32'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.rename_table('users', 'accounts')


def downgrade() -> None:
    """Downgrade schema."""
    op.rename_table('accounts', 'users')
