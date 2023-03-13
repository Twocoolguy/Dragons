from FileActions import read_folder_in_folder, delete_folder, rename, copy_json_file, delete_file
from User import User


def get_users(path):
    """Prints out all of the users."""
    folders = read_folder_in_folder(f"{path}/Dragons/")
    for folder in folders:
        print(folder)
    if len(folders) == 0:
        print("None")


def get_user_list(path):
    """Gets each name of a user and puts it in a list."""
    users = read_folder_in_folder(f"{path}/Dragons/")
    users.append("default")
    return users


def delete_user(name, path):
    """Deletes the given user."""
    delete_folder(f"{path}/Dragons/{name}/")


def user_rename(name, new_user, config_reader):
    """Basically renames the dragon to the given name"""
    usr = User(name, config_reader)
    rename(usr.path, f"{usr.config_reader.normal_path}/Dragons/{new_user}/")


def dragon_rename(name, new_name, usr):
    """Renames the dragon with the given name to the new name"""
    rename(f"{usr.path}{name}.json", f"{usr.path}{new_name}.json")


def get_achievement(number, config_reader):
    """Basically gets the achievement with the given number."""
    for ach in config_reader.achievements:
        if ach.number == number:
            return ach
    return None


def dragon_move(cur_user, dragon, new_user):
    """Moves the given dragon to another user."""
    err = copy_json_file(f"{cur_user.path}{dragon.name}.json", f"{new_user.path}{dragon.name}.json")
    if err == 0:
        delete_file(f"{cur_user.path}{dragon.name}.json")
