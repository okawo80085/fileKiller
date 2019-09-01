# killer agent

import os
import hashlib as h

class KILLER():
	def __init__(self, rootPath, *agents):
		self.Files = []
		self.Folders = []
		self.rootPath = rootPath
		with open(__file__, 'rt') as f:
			self.agents = {__file__:(os.stat(__file__).st_size, h.md5(f.read().encode()).hexdigest())}

		for i in agents:
			if i not in self.agents:
				with open(i, 'rt') as f:
					self.agents[i] = (os.stat(i).st_size, h.md5(f.read().encode()).hexdigest())

	def __repr__(self):
		if len(self.Folders) > 0 and len(self.Files) > 0:
			return '<agent 47, location={},\ntargets:\n\tfiles=[{}],\n\n\tfolders=[{}]>'.format(self.rootPath, ',\n\t'.join(['"{}"'.format(i) for i in self.Files]), ',\n\t'.join(['"{}"'.format(i) for i in self.Folders]))

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

	def checkFromAgents(self, location):
		'''
		checks if an agent in location
		'''

		tempSize = os.stat(location).st_size

		if tempSize > 133504000:
			tempSize -1
			tempHash = 0
		else:
			with open(location, 'rt') as f:
				if f.read(14) == '# killer agent':
					try:
						tempHash = h.md5(f.read().encode()).hexdigest()

					except UnicodeDecodeError:
						tempHash = 0

				else:
					tempHash = 0

		for agentLoc, agentId in self.agents.items():
			if agentId[0] == tempSize:
				if agentId[1] == tempHash:
					return True

		return False

	def kill(self):
		'''
		deletes everything that was found by pfr()
		'''
		for i in self.Files:
			if not self.checkFromAgents(i):
				os.unlink(i)

		for i in self.Folders:
			try:
				os.rmdir(i)

			except Exception as e:
				print ('failed to remove \'{}\': {}, maybe an agent is inside'.format(i, e))
