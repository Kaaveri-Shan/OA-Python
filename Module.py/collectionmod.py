from collections import ChainMap,Counter,defaultdict,OrderedDict,namedtuple,deque

# Counter
data = [1, 2, 2, 3, 3, 3]
count = Counter(data)
print(count)
print(data[3])

# Default Dict
d = defaultdict(int)
d["a"] += 1
print(d)

# Ordered Dict
od = OrderedDict()
od["one"] = 1
od["two"] = 2
print(od)

# NamedTuple
Student = namedtuple("Student", ["name", "age", "marks"])
s1 = Student("Kaaveri", 20, 90)
print(s1.name, s1.marks)

# Deque
dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)
dq.pop()
dq.popleft()
print(dq)

# ChainMap
d1 = {"a": 1, "b": 2}
d2 = {"b": 20, "c": 3}

cm = ChainMap(d1, d2)
print(cm)
print(cm["a"])
print(cm["b"])
print(cm["c"])
