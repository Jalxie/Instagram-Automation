'''
Source:
https://www.geeksforgeeks.org/rename-multiple-files-using-python/#targetText=In%20Python3%2C%20rename()%20method,destination%20with%20the%20new%20name.
'''
import os


def ModifyFilename():
    index = 1
    path = '/Users/jalxiey/Documents/Coding/Github/Instagram-Automation/posts/'
    for filename in os.listdir(path):
        dst = "post" + str(index) + ".pdf"
        # if(~os.path.isfile(path + dst)):
        src = path + filename
        dst = path + dst
        # rename() function will
        # rename all the files
        os.rename(src, dst)
        # else:
        #     index += 1
        #     dst = "post" + str(index) + ".png"
        #     src = path + filename
        #     dst = path + dst
        #     # rename() function will
        #     # rename all the files
        #     os.rename(src, dst)

        index += 1
