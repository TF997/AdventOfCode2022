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

total = 0 # Create a variable to store the total size of the paths
for path in PathTotalSize: # For each path in the dictionary
    if PathTotalSize[path] <= 100000: # If the path is less than or equal to 100000
        print(path + ": " + str(PathTotalSize[path])) # Print the path and the size
        total += PathTotalSize[path] # Add the size to the total

print(total) # Print the total size of the paths
