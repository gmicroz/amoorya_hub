
# import queue
from queue import Queue

taboor = Queue()

taboor.put("ahmed")
taboor.put("salem")
taboor.put("khalid")
taboor.put("faisal")
taboor.put("mohammed")

taboor_names = list(taboor.queue)
# print(taboor_names)  # لطباعة لستة بجميع اسماء عناصر الطابور

# لطباعة الأسماء منفصلة في حلفة تكراريةو FOR
for name in taboor_names:
    print(name)


taboor2 = Queue()

taboor2.put("Huda")
taboor2.put("Nada")
taboor2.put("Sara")
taboor2.put("Amal")

taboor_names_girls = list(taboor2.queue)

for name in taboor_names_girls:
    print(name)