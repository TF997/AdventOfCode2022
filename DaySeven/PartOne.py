Instructions = open("input.txt", "r").read().split("\n")

# Create a list of all the instructions
Instructions = [Instruction.split(" ") for Instruction in Instructions]
curr_dir = ["/"]
Files = {}
for Instruction in Instructions:
    print("Current Path: " + str(curr_dir))
    if Instruction[0] == "$":
        if Instruction[1] == "cd":
            if Instruction[2] == "..":
                print("Going up a directory")
                curr_dir.pop()
            else:
                print("Going into directory: " + Instruction[2])
                curr_dir.append(Instruction[2])
    else:
        if Instruction[0] == "dir":
            print("Directory: " + Instruction[1])
        else:
            for _dir_ in curr_dir:
                if _dir_ == "/":
                    current_path = _dir_
                else:
                    current_path += _dir_ + "/"
                if current_path in Files:
                    Files[current_path] += int(Instruction[0])
                else:
                    Files[current_path] = int(Instruction[0])
            #print("File: " + Instruction[1])
            #print("Size: " + Instruction[0])

total = 0
for file in Files:
    if Files[file] <= 100000:
        print(file + ": " + str(Files[file]))
        total += Files[file]

print(total)
