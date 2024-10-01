from sys import getsizeof
from datetime import datetime
d = datetime.now()
# datetime.datetime(2024, 10, 1, 10, 8, 38, 230054)
>>> getsizeof(d)
48
>>> d.timestamp()
1727770118.230054
>>> d.isoformat()
'2024-10-01T10:08:38.230054'
>>> getsizeof(d.isoformat())
67
>>> getsizeof(d.timestamp())
24