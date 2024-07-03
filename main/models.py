import sqlalchemy

from main.database import metadata

films = sqlalchemy.Table(
    "films",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.BigInteger, primary_key=True),
    sqlalchemy.Column("film", sqlalchemy.String, nullable=False, unique=True),
    sqlalchemy.Column("name", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("language", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("quality", sqlalchemy.BigInteger, nullable=True),
    sqlalchemy.Column("state", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("date", sqlalchemy.BigInteger, nullable=True),
    sqlalchemy.Column("type", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("instagram", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("tiktok", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("you_tube", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("status", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("code", sqlalchemy.BigInteger, unique=True, nullable=False),
)