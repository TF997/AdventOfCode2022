Instructions = open("input.txt", "r").read().split("\n")

# Create a list of all the instructions
Instructions = [Instruction.split(" ") for Instruction in Instructions]
curr_dir = ["/"]
Files = {}
for Instruction in Instructions:
    if Instruction[0] == "$":
        if Instruction[1] == "cd":
            if Instruction[2] == "..":
                curr_dir.pop()
            else:
                curr_dir.append(Instruction[2])
    else:
        if Instruction[0] != "dir":
            for _dir_ in curr_dir:
                if _dir_ == "/":
                    current_path = _dir_
                else:
                    current_path += _dir_ + "/"
                if current_path in Files:
                    Files[current_path] += int(Instruction[0])
                else:
                    Files[current_path] = int(Instruction[0])
valid_dir = []
for file in Files:
    sorted(Files.values())
    if Files[file] > 1035571:
        valid_dir.append(Files[file])
valid_dir.sort()

print(valid_dir[0])

print("\n")
print("Total Space Used: " + str(Files["/"]) + " Out of 70000000")
print("Remaining Space: " + str(70000000 - Files["/"]) + " Out of 70000000")
print("Needed for Update: 30000000")
print("Remaining Space After Update: " + str(70000000 - Files["/"] - 30000000) + " Out of 70000000")
