import re

def slugify(s: str):
	s = s.lower().strip()
	s = re.sub(r'[^\w\s-]', '', s)
	s = re.sub(r'[\s_-]+', '-', s)
	s = re.sub(r'^-+|-+$', '', s)
	return s