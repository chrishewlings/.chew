#/usr/bin/env python

# check and see if server is already installed

if os.path.exists((homedir + "Library/.server_installed")):
	print("Server is already installed on this user account.")
	sys.exit(1)