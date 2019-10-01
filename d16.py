# хэдэн найзын холбоо байна вэ?
import data
humuus = data.persons
urt = len(humuus)
holboo = 0
for i in range(urt):
    for j in range(urt-i-1):
        if humuus[j]['naizuud'] == humuus[j+1]['naizuud']:
            holboo+=1

print(holboo)