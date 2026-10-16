import pytest

from mader.sanitization import sanitization


@pytest.mark.parametrize(
	('name', 'expected'),
	[
		('Machado de Assis', 'machado de assis'),
		('Manuel        Bandeira', 'manuel bandeira'),
		('Edgar Alan Poe         ', 'edgar alan poe'),
		(
			'Androides Sonham Com Ovelhas Elétricas?',
			'androides sonham com ovelhas elétricas',
		),
		(
			'  breve   história   do tempo  ',
			'breve história do tempo',
		),
		(
			'O mundo assombrado pelos demônios',
			'o mundo assombrado pelos demônios',
		),
	],
)
def test_sanitization(name, expected):
	assert sanitization(name) == expected
