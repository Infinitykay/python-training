import sys

if sys.platform == "mac":
  print("Welcome to macbook Installation")
else:
  raise Exception(f"{sys.platform} is not a mac operating system. Try to install on macOS only")
