import functions
import PySimpleGUI
import time

PySimpleGUI.theme("Black")

label_clock = PySimpleGUI.Text("", key="clock")
label = PySimpleGUI.Text("Type in a task:")
input_box = PySimpleGUI.InputText(tooltip="Enter Task", key="task")
add_button = PySimpleGUI.Button("Add")

tasks_box = PySimpleGUI.Listbox(values=functions.get_tasks(), key="selected_task",
								enable_events=True, size=[45, 10])

edit_button = PySimpleGUI.Button("Edit")

complete_button = PySimpleGUI.Button("Complete")

exit_button = PySimpleGUI.Button("Exit")

window = PySimpleGUI.Window("My Tasks App",
							layout=[[label_clock],
									[label],
									[input_box, add_button],
									[tasks_box, edit_button, complete_button],
									[exit_button]],
							font=("Helvetica", 20))

while True:
	event, value = window.read(timeout=200)
	window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

	match event:
		case "Add":
			tasks = functions.get_tasks()

			task_to_append = value["task"] + "\n"
			task_to_append = task_to_append.capitalize()

			tasks.append(task_to_append)

			functions.write_tasks(tasks)

			window["selected_task"].update(values=tasks)

		case "Edit":
			try:
				tasks = functions.get_tasks()
				task_to_edit = value["selected_task"][0]
				new_task = value["task"] + "\n"
				new_task = new_task.capitalize()
				index = tasks.index(task_to_edit)
				tasks[index] = new_task
				functions.write_tasks(tasks)
				window["selected_task"].update(tasks)
			except IndexError:
				PySimpleGUI.popup("You must select a task first.", font=("Helvetica", 20))

		case "Complete":
			try:
				tasks = functions.get_tasks()
				task_to_complete = value["selected_task"][0]
				tasks.remove(task_to_complete)
				functions.write_tasks(tasks)
				window["selected_task"].update(tasks)
				window["task"].update(value="")
			except IndexError:
				PySimpleGUI.popup("You must select a task first.", font=("Helvetica", 20))

		case "selected_task":
			window["task"].update(value=value["selected_task"][0])

		case "Exit":
			break
		case PySimpleGUI.WIN_CLOSED:
			break

window.close()
