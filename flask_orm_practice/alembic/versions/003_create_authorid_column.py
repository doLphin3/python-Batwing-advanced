"""003_create_authorid_column

Revision ID: 003_create_authorid_column
Revises: 002_create_Book_table
Create Date: 2022-09-16 20:22:00.798800

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '003_create_authorid_column'
down_revision = '002_create_Book_table'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("book", sa.Column("author_id", sa.Integer, sa.ForeignKey("author.id")))


def downgrade() -> None:
    op.drop_column("book", "author_id")
