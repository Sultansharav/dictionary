# хүмүүсийн нэр найзын тоог гарга
import data
humuus=data.persons
for hun in humuus:
    print(hun['ner'], len(hun['naizuud']))