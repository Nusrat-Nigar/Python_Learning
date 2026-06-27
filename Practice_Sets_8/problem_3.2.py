import shutil
import os

shutil.copy('note.txt', 'dir')

shutil.move('tasks.txt', 'new_folder')

os.remove('delete.txt')