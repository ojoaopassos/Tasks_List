import functions
import time

print("Welcome to your TASKS LIST!\n")

now = time.strftime("%b %d, %Y - %H:%M")
print("Today is ", now, "\n")

while True:
	user_prompt = input("Enter add, show, edit, complete, or exit: ")
	user_prompt = user_prompt.lower()
	user_prompt = user_prompt.strip()

	if user_prompt.startswith("add"):
		new_item = user_prompt[4:]
		new_item = new_item.title()

		tasks = functions.get_tasks()

		tasks.append(new_item + "\n")

		functions.write_tasks(tasks)

	elif user_prompt.startswith("show"):
		tasks = functions.get_tasks()

		for index, item in enumerate(tasks):
			item = item.strip("\n")
			print(f"{index + 1}. {item}")

	elif user_prompt.startswith("edit"):
		try:
			edit_index = int(user_prompt[5:]) - 1
			new_edit = input("Enter the new task: ") + "\n"

			tasks = functions.get_tasks()

			tasks[edit_index] = new_edit

			functions.write_tasks(tasks)

			print("Task edited!")

		except ValueError:
			print("Your command is not valid.")
			continue

	elif user_prompt.startswith("complete"):
		try:
			tasks = functions.get_tasks()

			completed_task = int(user_prompt[9:]) - 1
			print(f'The task {tasks[completed_task]} has been completed!')
			tasks.pop(completed_task)

			functions.write_tasks(tasks)

		except IndexError:
			print("There is no item with this value.")
			continue
		except ValueError:
			print("Your command is not valid. You should enter the number of the task.")
			continue

	elif user_prompt.startswith("exit"):
		break

	else:
		print("Invalid command, please try again!")

print("Until next time!")