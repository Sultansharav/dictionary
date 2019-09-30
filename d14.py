# мэдээллийг насаар нь эрэмбэлээд нэр болон насыг харуул (visualgo.net)
import data
humuus=data.persons
urt = len(humuus)
for i in range(urt):
    for j in range(urt - i - 1):
        if humuus[j]['nas'] > humuus[j+1]['nas']:
            humuus[j], humuus[j+1]=humuus[j+1], humuus[j]
for i in humuus:
    print(i['ner'],i['nas'])