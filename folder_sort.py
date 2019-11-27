import re, os, shutil, path, datetime
os.chdir('\\Users\\anthony.ime\\Desktop\\test_file')
from datetime import datetime
from os import scandir


def convert_time(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date
def match_finder(entry):
    pattern = re.compile(r'(\d{2})(\s)(.*)')
    match = pattern.match(entry)
    #return match.group(0) #this returns the all the matches
    return match.group(3) #this returns the month and the year w/o white spaces
def directory_files_ctime(file): #this function return the time the file was created
    #if os.path.isfile(file) == True:
        info = os.stat(file)
        info.st_ctime
        #print(f'{file}, created on {convert_time(info.st_ctime)}')
        #print(convert_time(info.st_ctime))
        #print(match_finder(convert_time(info.st_ctime)))
        return match_finder(convert_time(info.st_ctime))
def directory_files_mtime(file): #this function return the time the file was modified
    #if os.path.isfile(file) == True:
        info = os.stat(file)
        info.st_mtime
        #print(f'{file}, created on {convert_time(info.st_mtime)}')
        #print(convert_time(info.st_mtime))
        #print(match_finder(convert_time(info.st_mtime)))
        return match_finder(convert_time(info.st_mtime))


# months = []
# count = 0
# while count < 12:
#     user_input = input('months please: ')
#     months.append(user_input)
#     count+=1
    
# for month in months:
#     os.mkdir(os.getcwd()+'\\'+month)    
    
# yeah i know i can be that lazy    
    

            
months = ['Jan 2019',
 'Feb 2019',
 'Mar 2019',
 'Apr 2019',
 'May 2019',
 'Jun 2019',
 'Jul 2019',
 'Aug 2019',
 'Sep 2019',
 'Oct 2019',
 'Nov 2019',
 'Dec 2019']

entries = scandir(os.getcwd())
for entry in entries:
    if entry.is_file():
        print(directory_files_ctime(entry))
        shutil.move(os.getcwd()+'\\'+entry.name, os.getcwd()+'\\'+directory_files_ctime(entry))
        #print(os.getcwd()+'\\'+entry.name)