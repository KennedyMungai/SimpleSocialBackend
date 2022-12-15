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
    op.add_column('post', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users', local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete='CASCADE')


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
