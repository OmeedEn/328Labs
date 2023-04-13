#Omeed Enshaie

d = {'dogfish': 4, 'dog': 3, 'catfish': 2, 'cat': 1, 'seahorse': 6, 'horse': 5}

with open("input.txt", 'r+') as file:
    file = file.readlines()[0]

for key, value in d.items():
    file = file.replace(f'{key}', f'{value}')

with open("output.txt", 'w+') as file_write:
    file_write.write(file)

