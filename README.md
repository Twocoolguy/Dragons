# Dragons v1.1.1
This is the open source code for Dragons v1.1.1.

Python 3.7+ Required
Install it here: https://www.python.org/downloads/release/python-379/

ONLY WORKS ON WINDOWS. IF YOU WANT MORE SUPPORT FOR OTHERS OPERATING SYSTEMS, YOU CAN JUST RUN THEM LIKE NORMAL PYTHON FILES.



Run "Run.bat" to play the game. - executes "python main.py"
Run "Fix Old Config"  to fix your old config. Before running this make sure you put the configs location in the config_loc.txt file. Putting "inthisfolder" will not work. That is just for if you do not have a config already and it uses the config in the folder. - executes "python oldfix.py"
Run "Check Config Syntax" to check the config folder for correct syntax. - executes "python syntax.py"
Run "Config Editor" to add new stuff to the config and change some settings. You can still do it the old fasion way, though wehave to admit this is a lot easier to use for most things (sadly it does not support story mode yet). - executes "python create.py"

1.1.1 Patch Notes:
- Fixed a bug when you were max level you could not get to the next boss/boss3 even if you won.
- Fixed a bug where sometimes you would get exp when you lost to a boss/boss3 when you shouldn't.
- Fixed a bug when you leveled up more than 2 tiems in a single fight it would not tell you how many levels you gained.
- Fixed a grammar issue saying that was "Your dragon leveled up {times} times and is now level {level}!" to "Your dragon leveled up {times} times and is now level {level}!".
- Added some functions for future updates.
- Removed some unused functions/comments from the GUI class.
- Removed unused comment in fight.py

This was a very small patch just mainly to fix some of the bigger issues that have been happening with the 1.1.0/1.0.0 release. There will be more patches like this in the future to fix bugs that need to be patched. Minor ones will be implemented into bigger releases (1.2.0, 1.3.0, etc.) while bigger issues will be patched in small releases (1.1.1, 1.1.2, etc). Thank you!
