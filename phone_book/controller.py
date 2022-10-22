import ui
import operations_shell as opshell

def start_app():
    ui.show_instructions()
    input_command = ui.user_command()

    if input_command == 1:
        opshell.show()
    elif input_command == 2:
        opshell.add()
    elif input_command == 3:
        opshell.search()
    elif input_command == 4:
        opshell.delete()