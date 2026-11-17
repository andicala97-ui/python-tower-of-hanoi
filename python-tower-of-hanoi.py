Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> ef hanoi_solver(n):
...     rods = [list(range(n, 0, -1)), [], []]
...     moves = []
... 
...     def record_state():
...         moves.append(f"{rods[0]} {rods[1]} {rods[2]}")
... 
...     def move_disks(n, source, auxiliary, target):
...         if n == 1:
...             disk = rods[source].pop()
...             rods[target].append(disk)
...             record_state()
...             return
... 
...         move_disks(n - 1, source, target, auxiliary)
... 
...         disk = rods[source].pop()
...         rods[target].append(disk)
...         record_state()
... 
...         move_disks(n - 1, auxiliary, source, target)
... 
...     record_state()
...     move_disks(n, 0, 1, 2)
... 
...     return "\n".join(moves)
