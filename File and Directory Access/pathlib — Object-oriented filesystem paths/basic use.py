"""
本模块提供了代表文件系统路径的类，其语义适合于不同的操作系统。
path classes分为pure paths和concrete paths，
前者提供纯粹的计算操作，没有I/O，
后者继承了pure paths，但也提供I/O操作。

如果你以前从未使用过这个模块，或者只是不确定哪个类适合你的任务，Path很可能是你需要的。
它为代码所运行的平台实例化了一个具体的路径。

pure paths 在某些特殊情况下是有用的；
例如:
1:如果你想在Unix机器上操作Windows路径（或者反过来）。
在Unix上运行时，你不能实例化WindowsPath，但你可以实例化PureWindowsPath。

2:你要确保你的代码只操作路径而不实际访问操作系统。
在这种情况下，实例化一个纯类可能是有用的，因为那些纯类根本没有任何访问操作系统的操作。
"""
# Importing the main class:
from pathlib import Path

# Listing subdirectories:
p = Path('../../.')
print(type(p))
print(p)
print([x for x in p.iterdir() if x.is_dir()])

# Listing Python source files in this directory tree:
print(p.glob('**/*.py'))

# Navigating inside a directory tree:
p = Path('pure paths-general propreties.py')
q = p
# 返回相对路径
print(q)
# 返回绝对路径
print(q.resolve())

# Querying path properties:
print(q.exists())
print(q.is_dir())

# Opening a file:
with q.open() as f:
    f.readline()


