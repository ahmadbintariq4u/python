file_loc="projects/color_text.txt"
f = open(file_loc, "a")
f.write(' -------------------------------\n')
for i in range(32,37):
    if(i==32):
        f.write('| ')
    f.write(f'\033[1;{i}mColor ')
    if(i==36):
        f.write('\033[1;37m|\n')

f.write(' -------------------------------\n') 
f.close()

#open and read the file after the appending:
f = open(file_loc, "r")
print(f.read())