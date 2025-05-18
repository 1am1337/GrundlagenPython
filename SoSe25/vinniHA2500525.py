import sys
import os

ARGV = sys.argv
if len(ARGV) < 1:
	print("insufficient commandline args")
	exit(1)

FILE_NAME = ARGV[1]

if not os.path.exists(FILE_NAME):
	os.system("touch " + FILE_NAME)

print(os.path.exists(FILE_NAME))


fileContents = ""

try:
	with open(FILE_NAME, "r") as file:
		fileContents = file.read()
except FileNotFoundError:
	print("FileNotFoundError")
	exit(1)
print(fileContents)