#Exercise 1
import os
print("Exercise 1")
os.system("ls")

#Exercise 2 
import subprocess
print("\n\nExercise 2")
subprocess.run(["ls"])
 
#Exercise 3
 
subprocess.run(["ls","-l"])

#Exercise 4 
print("\n\nExercise 4")
subprocess.run(["ls","-l","README.md"])


#Exercise 5 
print("\n\nExercise 5")
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])


#Exercise 6
print("\n\nExercise 6")
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])