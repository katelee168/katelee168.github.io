import os
import subprocess

PARENT_DIR = os.getcwd()
BUILD_ALL = True
SKIP_FILES = ["README.md"]

def build_in_dir(dir, relative_dir):

	if BUILD_ALL:
		files = os.listdir(dir)

	# Recurse through directories
	subdirs = [filename for filename in files if os.path.isdir(filename)]
	for subdir in subdirs:
		build_in_dir(os.path.join(dir, subdir), '{}/..'.format(relative_dir))

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
		CSS_FILENAME = os.path.join(relative_dir, "pandoc.css")
		print(CSS_FILENAME)

		# Determine CSS path and base URL based on directory
		css_path = "css/newspaper.css" if relative_dir == '.' else "../css/newspaper.css"
		base_url = "" if relative_dir == '.' else "../"
		
		command = ["pandoc", "-s", 
					"--template={}/template.html".format(PARENT_DIR),
					"--variable=css-path:{}".format(css_path),
					"--variable=base-url:{}".format(base_url),
					"--include-in-header={}/google-analytics.html".format(relative_dir), 
					"-o", os.path.join(dir, "{}.html".format(filebase)), 
					os.path.join(dir, filename)]
		return command

	for filename in files:
		print("converting: {}".format(filename))
		subprocess.call(get_command(filename, dir))


build_in_dir(PARENT_DIR, '.')