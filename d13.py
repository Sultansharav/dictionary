# хэдэн хүн prius машинтай вэ
import data
humuus=data.persons
k=0
for hun in humuus:
    priustei_yu = False # neg hun 2 buiu tuunees deesh priustei baij boloh yum bol
    for mashin in hun['mashinuud']:
        if mashin['zagwar'] == 'prius':
            priustei_yu = True
            break
    if priustei_yu == True: k+=1
print(k)