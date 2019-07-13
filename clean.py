import os
import subprocess
import sys
from subprocess import Popen, PIPE

dir_files = str(Popen(['ls'], stdout=PIPE).communicate()[0])[2:-1]
dir_files = dir_files.split('\\n')[:-1]

def make_dirs(dir_files):
	for f in dir_files:
		if (not os.path.isdir(f) and
		   not os.path.isdir(f.split('.')[-1])):
			subprocess.call(['mkdir', f.split('.')[-1]])


def move_files(dir_files):
	for f in dir_files:
		if not os.path.isdir(f):
			# mv into previously created dirs
			subprocess.call(['mv', f, f.split('.')[-1]])


def main():
	make_dirs(dir_files)
	move_files(dir_files)


if __name__ == '__main__':
	try:
		print('The following files will be cleaned: ')
		for i in dir_files:
			print(f'\t{i}')
		input('Press ENTER To Continue, CNTL-C To Exit >>>')
		main()
		print('Done!')
	except KeyboardInterrupt:
		print('Aborted.')
		sys.exit()
