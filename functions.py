FILEPATH = "tasks.txt"

def get_tasks(filepath=FILEPATH):
	""" Read a text file and return
	the list of tasks items.
	"""
	with open(filepath, "r") as file:
		tasks_local = file.readlines()
	return tasks_local


def write_tasks(tasks_local, filepath=FILEPATH):
	""" Write the tasks items in the text file."""
	with open(filepath, "w") as file:
		file.writelines(tasks_local)


if __name__ == "__main__":  # __name__ muda de nome se chamado por outro arquivo.
	print("This is being run directly from the file.")