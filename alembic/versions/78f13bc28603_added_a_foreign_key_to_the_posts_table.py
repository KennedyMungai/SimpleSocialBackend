"""Added a foreign key to the posts table

Revision ID: 78f13bc28603
Revises: fa67f70a6946
Create Date: 2022-12-15 15:39:20.721948

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78f13bc28603'
down_revision = 'fa67f70a6946'
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
