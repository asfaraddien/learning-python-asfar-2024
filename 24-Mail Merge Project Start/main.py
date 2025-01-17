#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt", "r") as f:
    name = f.readlines()

with open("./Input/Letters/starting_letter.txt") as format:
    temp = format.read()
    for i in name:
        new_name = i.strip()
        order = temp.replace(PLACEHOLDER, new_name)
        with open(f"./Output/ReadyToSend/for_{new_name}.txt", "w") as go:
            go.write(order)


