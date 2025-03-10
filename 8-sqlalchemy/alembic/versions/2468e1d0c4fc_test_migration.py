"""test migration

Revision ID: 2468e1d0c4fc
Revises: 0b15d4679776
Create Date: 2025-03-03 20:29:43.124760

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2468e1d0c4fc'
down_revision: Union[str, None] = '0b15d4679776'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('flowers', sa.Column('price', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('flowers', 'price')
    # ### end Alembic commands ###
