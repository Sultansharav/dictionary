# машингүй хүн хэд байна вэ
import data
humuus=data.persons
k = 0
for hun in humuus:
    if len(hun['mashinuud']) == 0:
        k+=1
print(k)