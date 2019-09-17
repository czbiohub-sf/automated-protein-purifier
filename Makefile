TOP_DIRECTORY = '.'
TEST_DIRECTORY = 'tests'

default:
	python3 -B -m unittest discover -v -t $(TOP_DIRECTORY) -s ./$(TEST_DIRECTORY)
