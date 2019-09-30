# насанд хүрээгүй хүн хэд байна вэ
import data
humuus=data.persons
k=0
for hun in humuus:
    if hun['nas'] < 18:
        k+=1
print(k)