import os.path
path = "/Users/temursayfutdinov/Documents/CompSci/Python/Nebula_Acdemy/Python_Course/2-12-24"
files = os.listdir(path)
txt_files = [f for f in files if f.endswith(".txt")]
print(txt_files)
totalWords = 0
for i in range(len(txt_files)):
    file = open(path + "/" + txt_files[i], "r")
    words = file.read().split()
    print(words)
    for word in words:
        totalWords += 1
    file.close()

print(totalWords)
