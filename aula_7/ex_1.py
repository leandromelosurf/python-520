
import datetime

import sqlalchemy

nome_do_banco = input('Digite o nome do banco: ')

engine = sqlalchemy.create_engine(
    'sqlite:///{}.db'.format(nome_do_banco),
    echo=True
)

metadata = sqlalchemy.MetaData(bind=engine)

users_table = sqlalchemy.Table(
    'tb_users',
    metadata,
    sqlalchemy.Column(
        'id',
        sqlalchemy.Integer,
        primary_key=True
    ),
    sqlalchemy.Column(
        'name',
        sqlalchemy.String(50),
        index=True
    ),
    sqlalchemy.Column(
        'age',
        sqlalchemy.Integer,
        nullable=False
    ),
    sqlalchemy.Column(
        'password',
        sqlalchemy.String        
    ),
    sqlalchemy.Column(
        'created_at',
        sqlalchemy.DateTime,
        default=datetime.datetime.now
    ),
    sqlalchemy.Column(
        'updated_at',
        sqlalchemy.DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now
    )
)

addrs_table = sqlalchemy.Table(
    'tb_addresses',
    metadata,
    sqlalchemy.Column(
        'id',
        sqlalchemy.Integer,
        primary_key=True
    ),
    sqlalchemy.Column(
        'name',
        sqlalchemy.String,
        nullable=False
    )
)

metadata.create_all(engine)