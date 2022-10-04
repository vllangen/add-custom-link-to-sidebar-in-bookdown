
import os, fileinput, glob, sys

#file_location = os.path.join('.','*.html')
#file_type = ('*.html')

filenames = glob.glob('*.html')

print("\nThis is a python app that adds a language link to the sidebar of all HTML files in your working folder.")
print("Your working folder is:")
print(os.getcwd())
print("\nThe following HTML files will be processed:", filenames)
confirming = input('\nDo you want to continue? Press "y" or "Y" to continue or press any other key to cancel\n')

if confirming == "y" or confirming == "Y":
    print("Processing.")
    pass
else:
    print("Process canceled.")
    sys.exit()

#
# old = '<ul class="summary">'
# new = '<li> <a href="https://vldesign.kapsi.fi/r/"><i class="fa fa-language fa-fw"></i> Go to Finnish version<span></span></a></li>'
#
# for f in filenames:
#     for line in fileinput.FileInput(files=f, inplace=True):
#         if old in line:
#             line += new + os.linesep
#         print(line, end="")

