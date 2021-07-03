# delete file
import os
if os.path.exists("Output.txt"):
  os.remove("Output.txt")
else:
  print("The file does not exist") 
