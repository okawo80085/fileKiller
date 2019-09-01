import os
import hashlib as h
import re

class KILLER():
	def __init__(self, rootPath):
		self.Files = []
		self.Folders = []
		self.rootPath = rootPath

	def __repr__(self):
		return '<killer (agent 47), location={}, targets: files={}, folders={}>'.format(self.rootPath, self.Files, self.Folders)

	def __call__(self):
		if os.path.exists(self.rootPath) and os.path.isdir(self.rootPath):
			self.pfr()
			self.kill()

		else:
			print ('root path bad')

	def pfr(self):
		'''
		returns paths from root
		'''
		def lel(path):
			return sum([1 for i in path.split(os.sep)])

		pathList = [i[0] for i in os.walk(self.rootPath)]

		for i in pathList:
			for j in os.listdir(i):
				pp = os.path.normpath(''.join([i, '/', j]))
				if os.path.lexists(pp):
					if os.path.isfile(pp):
						self.Files.append(pp)

					elif os.path.isdir(pp):
						self.Folders.append(pp)

		self.Files, self.Folders = sorted(self.Files, key=lel)[::-1], sorted(self.Folders, key=lel)[::-1]

	def kill(self):
		for i in self.Fiels:
			os.unlink(i)

		for i in self.Folders:
			os.rmdir(i)
