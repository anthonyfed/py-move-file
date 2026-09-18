import os


class CommandStringError(Exception):
    pass

def move_file(command: str) -> None:
    command_parts = command.split()
    command_name, source, destination = command_parts

    if len(command_parts) != 3 or command_parts[0] != "mv":
        raise CommandStringError

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    directory = os.path.dirname(destination)

    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(source, "r") as file_source, open(destination, "w") as file_directory:
        file_directory.write(file_source.read())

    os.remove(source)
