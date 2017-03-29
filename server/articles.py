import util

import itertools
import os
import os.path
import subprocess

PANDOC_CMD = 'pandoc'

class Articles(object):
	def __init__(self):
		self.articles = {}

	def load_from_dir(self, directory):
		for filename in filter(lambda f: f.endswith('.pandoc'), os.listdir(directory)):
			a_id = filename[:-7]
			article = Article(a_id)
			article.load(os.path.join(directory, filename))
			self.articles[a_id] = article

	def list_by_date(self):
		lsorted = sorted(
			self.articles.values(),
			key=lambda a: '' if a.date is None else a.date,
			reverse=True
		)
		return lsorted

	def get(self, article_id):
		if not article_id in self.articles:
			return None

		return self.articles[article_id]

class Article(object):
	def __init__(self, id_):
		self.id = id_
		self.filename = None
		self.title = None
		self.authors = None
		self.date = None

	def __str__(self):
		return "<Article id=%r title=%r>" % (self.id, self.title)

	def load(self, filename):
		self.filename = filename
		self._load_title_block()
		self._load_content()

	def _load_title_block(self):
		title_block = itertools.takewhile(lambda l: l.startswith('%') or l.startswith('  '), util.flines(self.filename))
		parsed_title_block = util.pad(parse_title_block(title_block), 3, '')
		parsed_title_block = list(map(lambda e: None if len(e) == 0 else e, parsed_title_block))
		self.title = parsed_title_block[0]
		self.authors = parsed_title_block[1]
		self.date = parsed_title_block[2]

	def _load_content(self):
		pandoc = subprocess.run([PANDOC_CMD, '-t', 'html', self.filename], stdout=subprocess.PIPE)
		self.content = pandoc.stdout.decode('utf-8')

def parse_title_block(title_block):
	elements = []
	last_element = None

	for line in title_block:
		if line.startswith('%'):
			elements.append(last_element)
			last_element = line[2:].strip()

		elif line.startswith('  '):
			if last_element is None:
				continue
			last_element += " " + line[2:].strip()

	elements.append(last_element)

	return elements[1:] # remove initial None added by the first %
