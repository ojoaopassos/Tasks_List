import functions
import PySimpleGUI

label = PySimpleGUI.Text("Type in a task:")
input_box = PySimpleGUI.InputText(tooltip="Enter Task")
add_button = PySimpleGUI.Button("Add")

window = PySimpleGUI.Window("My Tasks App", layout=[[label], [input_box, add_button]])
window.read()
window.close()