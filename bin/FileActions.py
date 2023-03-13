import os
import shutil
import json


def create_file(path, text=""):
    """Creates a file with the given name and text."""
    try:
        with open(f"{path}", "w+") as f:
            f.write(text)
            return 0
    except FileExistsError:
        return -1


def create_folder(path):
    """Creates a folder at path given."""
    try:
        os.mkdir(path)
        return 0
    except OSError as e:
        return e.errno.as_integer_ratio()


def delete_file(path):
    """Deletes the file given."""
    try:
        os.remove(path)
    except OSError as e:
        return e


def delete_folder(path):
    """Deletes the folder at the given path."""
    if not os.path.exists(path):
        return -1
    try:
        files = os.listdir(path)
    except OSError as e:
        return e
    for file in files:
        if "." not in file:
            delete_folder(f"{path}{file}/")
        else:
            delete_file(f"{path}{file}")
    os.rmdir(path)

def overwrite_file(path, text=""):
    """Overwrites file data with the text given."""
    if not os.path.exists(path):
        return -1
    with open(f"{path}", "w+") as f:
        f.write(text)
        return 0


def overwrite_file_lines(path, lines):
    """Overwrites file data with the given lines."""
    if not os.path.exists(path):
        return -1
    with open(f"{path}", "w+") as f:
        f.writelines(lines)
        return 0


def write_to_file(path, text=""):
    """Appends the text given to the path given."""
    try:
        with open(f"{path}", "a") as f:
            f.write(text)
            return 0
    except FileNotFoundError:
        return -1


def get_lines(path):
    """Returns a list of each line in the given file."""
    try:
        with open(f"{path}", "r") as f:
            data = []
            for line in f:
                data.append(line.strip())
            return data
    except FileNotFoundError:
        return -1


def get_first_line_of(path, search):
    """Gives you the first line that contains the given search string."""
    try:
        with open(f"{path}", "r") as f:
            for num, line in enumerate(f, 1):
                if search in line:
                    return num
    except FileNotFoundError:
        return -1


def get_lines_of(path, search):
    """Returns a list of line numbers that contain the search string given."""
    try:
        with open(f"{path}", "r") as f:
            lines = []
            for num, line in enumerate(f, 1):
                if search in line:
                    lines.append(num)
            return lines
    except FileNotFoundError:
        return -1


def get_text_at_line(path, line_number):
    """Returns the string of the line number given."""
    try:
        with open(f"{path}", "r") as f:
            for num, line in enumerate(f, 1):
                if num == line_number:
                    return line
    except FileNotFoundError:
        return -1


def get_num_lines(path):
    """Returns the number of lines a file has."""
    data = get_lines(path)
    if data == -1:
        return data
    return len(data)


def delete_line(path, line_number):
    """Removes the line number from the file given."""
    lines = []
    try:
        with open(f"{path}", "r") as f:
            for num, line in enumerate(f, 1):
                if num == line_number:
                    continue
                lines.append(line)
    except FileNotFoundError:
        return -1

    with open(f"{path}", "w+") as f:
        f.writelines(lines)
        return 0


def replace_line(path, line_number, text):
    """Replaces the line number given with the given text in the given file."""
    lines = []
    try:
        with open(f"{path}", "r") as f:
            for num, line in enumerate(f, 1):
                if num == line_number:
                    lines.append(f"{text}\n")
                    continue
                lines.append(f"{line}\n")
    except FileNotFoundError:
        return -1

    with open(f"{path}", "w+") as f:
        f.writelines(lines)
        return 0


def insert_line(path, position, text):
    """Inserts a line with the given text at the given position in the given file."""
    lines = []
    try:
        with open(f"{path}", "r") as f:
            for num, line in enumerate(f, 1):
                lines.append(line)
    except FileNotFoundError:
        return -1

    lines.insert(position, text)

    with open(f"{path}", "w+") as f:
        f.writelines(lines)
        return 0


def rename(path, new_name):
    """Renames a file or a folder to the given name. Both need to have path."""
    try:
        os.rename(path, new_name)
        return 0
    except OSError as e:
        return e.errno.as_integer_ratio()


def read_file_lines_in_folder(path):
    """Returns all the lines of the files in the given folder."""
    try:
        files = os.listdir(path)
    except OSError as e:
        raise e

    data = []
    for file in files:
        if "." in file:
            data.append({"name":file,"lines":get_lines(f"{path}/{file}")})

    return data


def read_folder_in_folder(path):
    """Basically returns the folders in this folder."""
    try:
        files = os.listdir(path)
    except OSError as e:
        return e.errno.as_integer_ratio()

    folders = []
    for file in files:
        if not "." in file:
            folders.append(file)

    return folders


def list_files(path):
    """Gives a list of files in the given path."""
    try:
        files = os.listdir(path)
    except OSError as e:
        return e.errno.as_integer_ratio()

    file_list = []
    for file in files:
        if "." in file:
            file_list.append(file)

    return file_list


def copy_json_file(file, new_loc):
    """Copies a json file to a new location"""
    try:
        with open(file, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return -1
    try:
        with open(new_loc, "w+") as c:
            json.dump(data, c)
    except FileExistsError:
        return -2
    return 0


def copy_file(file, new_loc):
    """Copies a file to a new location"""
    try:
        with open(file, "r") as f:
            data = f.readlines()
    except FileNotFoundError:
        return -1
    try:
        with open(new_loc, "w+") as c:
            c.writelines(data)
    except FileExistsError:
        return -2
    return 0


def move_file(file, new_file):
    """Moves the given file to the new location"""
    os.rename(file, new_file)
    shutil.move(file, new_file)
