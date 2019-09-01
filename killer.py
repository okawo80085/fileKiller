import os
import hashlib as h
import re

class KILLER():
	def __init__(self, rootPath, *agents):
		self.Files = []
		self.Folders = []
		self.rootPath = rootPath
		self.agents = [__file__]

		for i in agents:
			if i not in self.agents:
				self.agents.append(i)

	def __repr__(self):
		if len(self.Folders) > 0 and len(self.Files) > 0:
			return '<agent 47, location={},\ntargets:\n\tfiles=[{}],\n\n\tfolders=[{}]>'.format(self.rootPath, ',\n\t'.join(['\'{}\''.format(i) for i in self.Files]), ',\n\t'.join(['\'{}\''.format(i) for i in self.Folders]))

		else:
			return '<agent 47, location={}, targets: files={}, folders={}>'.format(self.rootPath, self.Files, self.Folders)

	def __call__(self):
		if os.path.exists(self.rootPath) and os.path.isdir(self.rootPath):
			self.pfr()
			self.kill()
			return 'target killed'

		else:
			return 'target escaped (bad root path)'

	def pfr(self):
		'''
		returns paths from root
		'''
		def lel(path):
			return sum([1 for i in path.split(os.sep)])

		pathList = [i[0] for i in os.walk(self.rootPath)]

		self.Files = []
		self.Folders = []

		for i in pathList:
			for j in os.listdir(i):
				pp = os.path.abspath(os.path.normpath(''.join([i, '/', j])))
				if os.path.lexists(pp):
					if os.path.isfile(pp):
						self.Files.append(pp)

					elif os.path.isdir(pp):
						self.Folders.append(pp)

		self.Files, self.Folders = sorted(self.Files, key=lel)[::-1], sorted(self.Folders, key=lel)[::-1]

	def kill(self):
		'''
		deletes everything that was found by pfr()
		'''
		for i in self.Files:
			os.unlink(i)

		for i in self.Folders:
			os.rmdir(i)
