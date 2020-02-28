
import sqlalchemy
import sqlalchemy.orm

import core.db

import models.user
import models.message

core.db.Base.metadata.create_all(
    core.db.engine
)

user = models.user.User(
    name='Lucas Ricciardi', 
    email='lucas@email.com', 
    password='admin'
)

message = models.message.Message(
    content='Minha mensagem'
)

session = core.db.Session()

session.add(user)
session.add(message)

session.commit()

