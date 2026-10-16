def sanitization(text: str) -> str:
	text = ''.join(
		character
		for character in text.lower()
		if character.isalnum() or character.isspace()
	)
	return ' '.join(text.split())
