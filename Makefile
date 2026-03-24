check:
	ruff format oob_training tests
	ruff check oob_training tests --fix
	mypy oob_training tests