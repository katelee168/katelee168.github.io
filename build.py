import os
import subprocess

PARENT_DIR = os.path.abspath(os.getcwd())
BUILD_ALL = True
SKIP_FILES = ["README.md"]

def build_in_dir(dir):

	if BUILD_ALL:
		files = os.listdir(dir)

	# Recurse through directories
	subdirs = [filename for filename in files if os.path.isdir(filename)]
	for subdir in subdirs:
		build_in_dir(os.path.join(dir, subdir))

	# Filter for markdown or multi-markdown
	files = [filename for filename in files if os.path.splitext(filename)[1] in ['.mmd', '.md']]
	# Filter for not skiped files
	files = [filename for filename in files if filename not in SKIP_FILES]
	if not files:
		return 
	print("Entering: %s" % dir)
	os.chdir(dir)

	def get_command(filename, dir):
		filename = os.path.basename(filename)
		filebase = '.'.join(filename.split('.')[:-1])
		CSS_FILENAME = os.path.abspath(os.path.join(dir, "pandoc.css"))
		print(CSS_FILENAME)

		command = ["pandoc", "-s", 
					"-c", CSS_FILENAME, 
					"--filter", "/usr/local/bin/pandoc-crossref", 
					"--filter", "/usr/local/bin/pandoc-citeproc", 
					"--include-in-header={}/google-analytics.html".format(PARENT_DIR), 
					"-o", os.path.join(dir, "{}.html".format(filebase)), 
					os.path.join(dir, filename)]
		return command

	for filename in files:
		print("converting: {}".format(filename))
		subprocess.call(get_command(filename, dir))


build_in_dir(PARENT_DIR)