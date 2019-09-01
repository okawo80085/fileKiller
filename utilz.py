import os
import hashlib as h
import re

def pathsFromRoot(rootPath):
	'''
	returns only paths with real files
	'''

	pathList = [i[0] for i in os.walk(rootPath)]

	out = []

	for i in pathList:
		for j in os.listdir(i):
			if os.path.lexists(os.path.normpath(''.join([i, '/', j]))):
				out.append(os.path.normpath(''.join([i, '/', j])))

	return out