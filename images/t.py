from os import listdir
from json import load
from shutil import copyfile

dirlist = listdir(r"G:\Workshop\Fields\Python\Projects\Jactithm New\code\trucks")

for i in dirlist:
    copyfile(fr"G:\Workshop\Fields\Python\Projects\Jactithm New\code\trucks\{i}\image.jpg")