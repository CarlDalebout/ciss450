#==========================================================
# Makefile for main.exe
# Carl Dalebout
#==========================================================

#==========================================================
# Macros
#==========================================================

#==========================================================
# Executable
#==========================================================

#==========================================================
# Object files
#==========================================================

#==========================================================
# Utilities
#==========================================================
push:
	git add .
	git commit
	git push origin main
p:
	git add .
	git commit
	git push origin main