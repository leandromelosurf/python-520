
import sqlalchemy

import core.db


class User(core.db.Base):

    __tablename__ = 'tb_users'

    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True
    )

    name = sqlalchemy.Column(
        sqlalchemy.String
    )

    email = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=False,
        unique=True
    )

    password = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=False
    )
