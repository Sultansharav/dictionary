# 20-оос доош насны хүмүүсийн нэрсийг гарга.
import data
humuus=data.persons
for hun in humuus:
    if hun['nas'] < 20:
        print(hun['ner'])