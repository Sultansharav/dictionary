# 20-оос дээш насны хэдэн хүн байгааг тоол.
import data
humuus=data.persons
too = 0
for hun in humuus:
    if hun['nas'] > 20:
        too+=1
print(too)
