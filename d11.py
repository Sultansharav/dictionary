# хэн 2оос олон найзтай вэ
import data
humuus=data.persons
k=0
for hun in humuus:
    if len(hun['naizuud']) >2:
        k+=1
print(k)