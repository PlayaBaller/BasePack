import os

path = input('Enter the folder path to clarify it\'s size ')
totalSize = 0

for filename in os.listdir(path):
    if not os.path.isfile(os.path.join(path, filename)):
        continue
    totalSize = totalSize + os.path.isfile(os.path.join(path, filename))

print(totalSize)
