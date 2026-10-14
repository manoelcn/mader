from dataclasses import asdict

from sqlalchemy import select

from mader.models import Book, User, Writer


def test_create_user(session, mock_db_time):
	with mock_db_time(model=User) as time:
		new_user = User(
			username='manoel', password='secret', email='teste@test'
		)
		session.add(new_user)
		session.commit()

	user = session.scalar(select(User).where(User.username == 'manoel'))

	assert asdict(user) == {
		'id': 1,
		'username': 'manoel',
		'password': 'secret',
		'email': 'teste@test',
		'created_at': time,
	}


def test_create_writer(session):
	new_writer = Writer(name='manoel')
	session.add(new_writer)
	session.commit()

	writer = session.scalar(select(Writer).where(Writer.name == 'manoel'))

	assert asdict(writer) == {
		'id': 1,
		'name': 'manoel',
		'books': [],
	}


def test_create_book(session):
	writer = Writer(name='manoel')
	session.add(writer)
	session.flush()

	new_book = Book(title='Mader', year=2026, writer_id=writer.id)
	session.add(new_book)
	session.commit()

	book = session.scalar(select(Book).where(Book.title == 'Mader'))

	assert book is not None
	assert (book.id, book.title, book.year, book.writer_id) == (
		1,
		'Mader',
		2026,
		writer.id,
	)
	assert book.authorship == writer
	assert writer.books == [book]
