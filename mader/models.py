from datetime import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import (
	Mapped,
	mapped_as_dataclass,
	mapped_column,
	registry,
	relationship,
)

table_registry = registry()


@mapped_as_dataclass(registry=table_registry)
class Account:
	__tablename__ = 'accounts'

	id: Mapped[int] = mapped_column(init=False, primary_key=True)
	username: Mapped[str] = mapped_column(unique=True)
	password: Mapped[str]
	email: Mapped[str] = mapped_column(unique=True)
	created_at: Mapped[datetime] = mapped_column(
		init=False, server_default=func.now()
	)


@mapped_as_dataclass(registry=table_registry)
class Writer:
	__tablename__ = 'writers'

	id: Mapped[int] = mapped_column(init=False, primary_key=True)
	name: Mapped[str] = mapped_column(unique=True)
	books: Mapped[list['Book']] = relationship(
		init=False, back_populates='authorship', cascade='all, delete-orphan'
	)


@mapped_as_dataclass(registry=table_registry)
class Book:
	__tablename__ = 'books'

	id: Mapped[int] = mapped_column(init=False, primary_key=True)
	title: Mapped[str] = mapped_column(unique=True)
	year: Mapped[int] = mapped_column()
	writer_id: Mapped[int] = mapped_column(ForeignKey('writers.id'))
	authorship: Mapped[Writer] = relationship(
		init=False, back_populates='books'
	)
