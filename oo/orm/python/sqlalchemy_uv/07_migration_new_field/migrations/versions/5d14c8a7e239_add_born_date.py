"""add born_date to pessoa

Revision ID: 5d14c8a7e239
Revises: b92a9493ba88
Create Date: 2026-10-03

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5d14c8a7e239"
down_revision: Union[str, Sequence[str], None] = "b92a9493ba88"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("tabela_pessoa", sa.Column("born_date", sa.Date(), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("tabela_pessoa", "born_date")
