#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Mail Merge Project Start/Input/Letters/starting_letter.txt", "r") as file:
    starting_letter = file.readlines()

with open("./Mail Merge Project Start/Input/Names/invited_names.txt", "r") as names:
    names_list = names.readlines()

dear_name = starting_letter[0]
for i in names_list:
    j = i.strip("\n")
    new_name = dear_name.replace("[name]", j)
    starting_letter[0] = new_name
    new_letter = ''.join(starting_letter)
    with open(f"./Mail Merge Project Start/Output/ReadyToSend/{j}", "w") as send_letter:
        send_letter.write(f"{new_letter}")
