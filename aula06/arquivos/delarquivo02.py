import os
if os.path.exists("C:\\tools\demofile.txt"):
  os.remove("C:\\tools\demofile.txt")
else:
  print("The file does not exist")