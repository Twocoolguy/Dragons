import FileActions

exit(0)
# line_one_remove = ""["".index(":") + 2:"".index("#")]
# line_two_remove = ""["".index(":") + 2:"".index("!")]
# line_three_remove = ""["".index(":") + 2:"".index("$")]
# line_four_remove = ""["".index(":") + 2:"".index("%")]
# line_five_remove = ""["".index(":") + 2:"".index("&")]
# line_six_remove = ""["".index(":") + 2:"".index(")")]

move_files = FileActions.read_file_lines_in_folder(f"C:/Users/TurtlesAreHot/Desktop/Dragons e/Config/Moves/")

for move_file in move_files:
    name = move_file["name"]
    lines = move_file["lines"]
    new_lines = [lines[0][lines[0].index(":") + 2:lines[0].index("#")] + "\n",
                 lines[1][lines[1].index(":") + 2:lines[1].index("!")] + "\n",
                 lines[2][lines[2].index(":") + 2:lines[2].index("$")] + "\n",
                 lines[3][lines[3].index(":") + 2:lines[3].index("%")] + "\n",
                 lines[4][lines[4].index(":") + 2:lines[4].index("&")] + "\n",
                 lines[5][lines[5].index(":") + 2:lines[5].index(")")]]
    FileActions.overwrite_file_lines(f"C:/Users/TurtlesAreHot/Desktop/Dragons e/Config/Moves/{move_file['name']}", new_lines)
import FileActions

exit(0)
# line_one_remove = ""["".index(":") + 2:"".index("#")]
# line_two_remove = ""["".index(":") + 2:"".index("!")]
# line_three_remove = ""["".index(":") + 2:"".index("$")]
# line_four_remove = ""["".index(":") + 2:"".index("%")]
# line_five_remove = ""["".index(":") + 2:"".index("&")]
# line_six_remove = ""["".index(":") + 2:"".index(")")]

move_files = FileActions.read_file_lines_in_folder(f"C:/Users/TurtlesAreHot/Desktop/Dragons e/Config/DragonBosses/")
print(move_files)

for move_file in move_files:
    name = move_file["name"]
    lines = move_file["lines"]
    print(lines)
    new_lines = [lines[0][lines[0].index(":") + 2:lines[0].index("#")] + "\n",
                 lines[1][lines[1].index(":") + 2:lines[1].index("$")] + "\n",
                 lines[2][lines[2].index(":") + 2:lines[2].index("*")] + "\n",
                 lines[3][lines[3].index(":") + 2:lines[3].index("^")]]
    FileActions.overwrite_file_lines(f"C:/Users/TurtlesAreHot/Desktop/Dragons e/Config/DragonBosses/{move_file['name']}", new_lines)
