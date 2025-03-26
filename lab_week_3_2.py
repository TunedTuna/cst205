import pickle
word_list =[]
with open('poem.txt','r') as my_file:
    line_list = my_file.readlines()
    word_list = my_file.read()

liner=0
for counter, line in enumerate(line_list):
    liner+=1
liner-1
print(f'Lines: {liner}\n')

# task 2-- no work :(
words = 0
for counter, wordword in enumerate(line_list):
    word_list.split()
print(f'Words: {words}\n')

# task 3

inputU = ""
reminder=[]
while inputU != 'n':
    inputU = input("Enter a reminder. (Enter 'n' if done.)\n")
    if inputU != 'n':
            reminder.append(inputU)


print("\nHere are your reminders:")
print(reminder)

# task 4----
with open('remindy.txt','wb') as da_file:
    pickle.dump(reminder,da_file)
# taks 4----