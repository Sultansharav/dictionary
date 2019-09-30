# Нэр нь bymba байх хүний мэдээллийг хэвлэж харуул
import data
humuus = data.persons
for hun in humuus:
    if hun['ner'] == 'bymba':
        print(hun)