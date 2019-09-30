# bymba хэдэн найзтай вэ
import data
humuus = data.persons
for hun in humuus:
    if hun['ner'] == 'bymba':
        print(len(hun['naizuud']))