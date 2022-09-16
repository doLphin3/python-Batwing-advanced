"""001_create_Author_table

Revision ID: 001_create_Author_table
Revises: 
Create Date: 2022-09-12 23:57:57.386802

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '001_create_Author_table'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "author",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String, nullable=False, unique=True),
        sa.Column("age", sa.Integer, nullable=False)
    )


def downgrade() -> None:
    op.drop_table("author")
