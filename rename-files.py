# TODO
# 1. cycle through each file
# 2. find the file file file name
# 3. check if the file name contains "st", or "th", or "nd". We will use this to rename the file. If nothing, leave the file alone.
# 4. generate new file name based on #3
# 5. rename the file using the file name generated in #4


from datetime import datetime
import glob, os
import re

folder_path = "" #insert file path to your Obsidian vault here

def main():  
  os.chdir(folder_path)

  for file_name in glob.glob("*.md"):
    #cycle through the list of files in the current directory
    
    current_file_name = file_name.split(".")[0]
    print("Current Filename is -> " + current_file_name)

    #Generate new file name
    d = datetime.strptime(solve(current_file_name), '%B %d, %Y')
    new_file_name = d.strftime('%Y-%m-%d')
    print("New File name is -> " + new_file_name)

    rename_file(file_name,new_file_name + ".md")

def solve(s):                                             
    # Source: https://stackoverflow.com/questions/21496246/how-to-parse-date-days-that-contain-st-nd-rd-or-th
    return re.sub(r'(\d)(st|nd|rd|th)', r'\1', s)


def rename_file(src, dest):
  # Source: https://www.geeksforgeeks.org/rename-multiple-files-using-python/
  os.chdir(folder_path)
  os.rename(src, dest)

main()
