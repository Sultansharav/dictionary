# найзуудын тоогоор эрэмбэлээд нэр болон найзын тоог харуул
import data
humuus=data.persons
urt = len(humuus)
for i in range(urt):
    for j in range(urt - i - 1):
        if len(humuus[j]['naizuud']) > len(humuus[j+1]['naizuud']):
            humuus[j], humuus[j+1]=humuus[j+1], humuus[j]
for i in humuus:
    print(i['ner'],len(i['naizuud']))