# killer agent

import os
import hashlib as h

class KILLER():
	def __init__(self, rootPath, *agents):
		self.Files = []
		self.Folders = []
		self.rootPath = rootPath
		self.kills = 0
		with open(__file__, 'rt') as f:
			self.agents = {__file__:(os.stat(__file__).st_size, h.md5(f.read().encode()).hexdigest())}

		for i in agents:
			if i not in self.agents:
				with open(i, 'rt') as f:
					self.agents[i] = (os.stat(i).st_size, h.md5(f.read().encode()).hexdigest())

	def __repr__(self):
		return '<class killer(agent 69 if you will), kills={}, location={}, targets: nfiles={}, nfolders={}>'.format(self.kills, self.rootPath, len(self.Files), len(self.Folders))

	def __call__(self):
		if os.path.exists(self.rootPath) and os.path.isdir(self.rootPath):
			if len(self.Files) > 0 or len(self.Folders) > 0:
				self.pfr()
				self.kill()
				return 'target killed'

			else:
				return 'no target to kill'

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
						if pp not in self.Files:
							self.Files.append(pp)

					elif os.path.isdir(pp):
						if pp not in self.Folders:
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
				try:
					ff = f.read()
					if ff[:14] == '# killer agent':
						tempHash = h.md5(ff.encode()).hexdigest()
					else:
						tempHash = 0

				except UnicodeDecodeError:
					tempHash = 0

		#print (tempHash)

		for agentLoc, agentId in self.agents.items():
			if agentLoc == location:
				return True

			if agentId[0] == tempSize:
				if agentId[1] == tempHash:
					return True

		return False

	def kill(self):
		'''
		deletes everything that was found by pfr(), except agents
		'''
		temp = []
		for i in self.Files:
			if not self.checkFromAgents(i):
				self.kills += 1
				os.unlink(i)

			else:
				temp.append(i)

		self.Files = temp
		temp = []

		for i in self.Folders:
			try:
				self.kills += 1
				os.rmdir(i)

			except Exception as e:
				temp.append(i)
				print ('failed to remove \'{}\': {}, agent inside or lacking permissions'.format(i, e))

		self.Folders = temp