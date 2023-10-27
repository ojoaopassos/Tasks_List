import functions
import PySimpleGUI

label = PySimpleGUI.Text("Type in a task:")
input_box = PySimpleGUI.InputText(tooltip="Enter Task", key="task")
add_button = PySimpleGUI.Button("Add")

exit_button = PySimpleGUI.Button("Exit")

window = PySimpleGUI.Window("My Tasks App",
							layout=[[label], [input_box, add_button], [exit_button]],
							font=("Helvetica", 20))

while True:
	event, value = window.read()
	print(event)
	print(value)
	match event:
		case "Add":
			tasks = functions.get_tasks()

			task_to_append = value["task"] + "\n"
			task_to_append = task_to_append.capitalize()

			tasks.append(task_to_append)

			functions.write_tasks(tasks)

		case "Exit":
			break
		case PySimpleGUI.WIN_CLOSED:
			break

window.close()