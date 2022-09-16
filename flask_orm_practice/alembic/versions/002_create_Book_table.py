"""002_create_Book_table

Revision ID: 002_create_Book_table
Revises: 001_create_Author_table
Create Date: 2022-09-13 20:29:11.368024

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '002_create_Book_table'
down_revision = '001_create_Author_table'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "book",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String, nullable=False, unique=True),
        sa.Column("description", sa.String, nullable=True)
    )


def downgrade() -> None:
    op.drop_table("book")
