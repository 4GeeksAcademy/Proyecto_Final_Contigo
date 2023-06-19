"""empty message

Revision ID: 51342b3b0644
Revises: 
Create Date: 2023-06-19 17:06:27.608999

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51342b3b0644'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categorias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descripcion', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('descripcion')
    )
    op.create_table('modalidad',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descripcion', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('descripcion')
    )
    op.create_table('ong',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('cif', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('url', sa.String(length=80), nullable=False),
    sa.Column('dirección', sa.String(length=80), nullable=False),
    sa.Column('codigo_postal', sa.Integer(), nullable=False),
    sa.Column('telefono', sa.Integer(), nullable=False),
    sa.Column('logo', sa.String(length=300), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cif'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('logo'),
    sa.UniqueConstraint('nombre'),
    sa.UniqueConstraint('telefono'),
    sa.UniqueConstraint('url')
    )
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('apellido', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=False),
    sa.Column('password', sa.String(length=30), nullable=False),
    sa.Column('ong_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ong_id'], ['ong.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('recurso',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('categoria', sa.String(length=50), nullable=True),
    sa.Column('nombre', sa.String(length=80), nullable=False),
    sa.Column('modalidad', sa.String(length=20), nullable=True),
    sa.Column('dirección', sa.String(length=80), nullable=True),
    sa.Column('codigo_postal', sa.Integer(), nullable=True),
    sa.Column('telefono', sa.Integer(), nullable=False),
    sa.Column('descripcion', sa.String(length=400), nullable=False),
    sa.Column('img', sa.String(length=300), nullable=True),
    sa.Column('fichero', sa.String(length=300), nullable=True),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.Column('ong_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['categoria'], ['categorias.id'], ),
    sa.ForeignKeyConstraint(['modalidad'], ['modalidad.id'], ),
    sa.ForeignKeyConstraint(['ong_id'], ['ong.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('descripcion'),
    sa.UniqueConstraint('nombre')
    )
    op.create_table('peticion',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=80), nullable=False),
    sa.Column('apellido', sa.String(length=80), nullable=False),
    sa.Column('texto', sa.String(length=400), nullable=False),
    sa.Column('preferencia', sa.String(length=20), nullable=False),
    sa.Column('telefono', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(length=60), nullable=True),
    sa.Column('recurso_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['recurso_id'], ['recurso.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('peticion')
    op.drop_table('recurso')
    op.drop_table('usuario')
    op.drop_table('ong')
    op.drop_table('modalidad')
    op.drop_table('categorias')
    # ### end Alembic commands ###
