#COMMON MODULES IN PYTHON
#Q.1- Print the current day using Datetime module.
import datetime as dt
day= dt.date.today()
print(day.strftime("%A"))


#Q.2- Open your browser and play a video using webbrowser module in python.
import webbrowser
search = "Difference"
webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % search)


#Q.3- Write a program to rename all the files in a directory and convert them into .jpg file format.
import os
path=r'''C:/Users/Asus/Desktop/Python/New_Directory'''
file=os.listdir(path)
i=1
for f in file:
    os.rename(os.path.join(path, f), os.path.join(path, str(i)+'.jpg'))
    i+=1
