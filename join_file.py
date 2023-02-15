"""
讲分割的文件拼接起来
"""
import sys
import os
dir = "./mp4"
f = open("./mp4/mp4.zip","wb+")
fnum_list = os.listdir(dir)
fnum_list.sort()
print(fnum_list)
for fnum in fnum_list:
    with open("./mp4/"+fnum,"rb") as ff:
        data = ff.read()
        f.write(data)
        ff.close()
f.close()
