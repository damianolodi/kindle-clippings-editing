###########################################################
# REWRITE CLIPPINGS FILE MADE WITH KINDLE
#
#
#
###########################################################
import os

# change the current working directory
# os.getcwd()
os.chdir("/Users/DamianoLodi/Desktop")

new_file = open("reamke-clippings.txt", 'w+')
old_file = open("book-clippings.txt", 'r')

# write all the lines of old_file in a list and fin the length
all_lines = list(old_file)
list_length = len(all_lines)
# close the file
old_file.close()

for index, line in enumerate(all_lines):
    if line[0] == "-":
        pagina = line.split()[6]
        pos = line.split()[9]
        string = all_lines[index+2][:-1] + " - p%s, pos%s\n\n" % (pagina, pos)
        new_file.write(string)


new_file.close()
