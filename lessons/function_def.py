"""An example function definition."""


i: int = 1
d: int = 4

a0: int = i % d

i = i + 1
a1: int = i % d

i = i + 1
a2: int = i % d

i = i + 1
a3: int = i % d

i = i + 1
a4: int = i % d

print(a0 + a1 + a2 + a3 + a4)
