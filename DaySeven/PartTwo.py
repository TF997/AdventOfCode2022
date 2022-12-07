Instructions = open("input.txt", "r").read().split("\n") # Read the input file
Instructions = [Instruction.split(" ") for Instruction in Instructions] # Create a list of all the instructions
curr_dir = ["/"] # Set the current directory to the root directory
PathTotalSize = {} # Create a dictionary to store the total size of each path
for Instruction in Instructions:
    if Instruction[0] == "$": # If the instruction is a command
        if Instruction[1] == "cd": # If the command is cd
            if Instruction[2] == "..": # If the command is cd ..
                curr_dir.pop() # Go up a directory
            else: # If the command is cd <directory>
                curr_dir.append(Instruction[2]) # Go into the directory
    else: # If ls
        if Instruction[0] != "dir": # If the file is not a directory
            for _dir_ in curr_dir: # For each directory in the current path
                if _dir_ == "/": # If the directory is the root directory
                    current_path = _dir_ # Set the current path to the root directory
                else: # If the directory is not the root directory
                    current_path += _dir_ + "/" # Add the directory to the current path
                if current_path in PathTotalSize: # If the current path is in the dictionary
                    PathTotalSize[current_path] += int(Instruction[0]) # Add the file size to the current path
                else: # If the current path is not in the dictionary
                    PathTotalSize[current_path] = int(Instruction[0]) # Add the current path to the dictionary with the file size



valid_dir = [] # Create a list of valid directories
for path in PathTotalSize: # For each path in the dictionary
    sorted(PathTotalSize.values()) # Sort the values in the dictionary
    if PathTotalSize[path] > (70000000 - PathTotalSize["/"] - 30000000) * -1: # If the file size is greater than the extra space needed for the update
        valid_dir.append(PathTotalSize[path]) # Add the file size to the list of valid directories
valid_dir.sort() # Sort the list of valid directories

print(valid_dir[0]) # Print the first element in the list of valid directories

print("\n")
print("Total Space Used: " + str(PathTotalSize["/"]) + " Out of 70000000")
print("Remaining Space: " + str(70000000 - PathTotalSize["/"]) + " Out of 70000000")
print("Needed for Update: 30000000")
print("Remaining Space After Update: " + str(70000000 - PathTotalSize["/"] - 30000000) + " Out of 70000000")
