"""
pure path objects提供路径处理操作，实际上并不访问文件系统。
有三种方法可以访问这些类，我们也称之为flavours:
class pathlib.PurePath(*pathsegments):
    一个代表system's path flavour的通用类（实例化它可以创建一个PurePosixPath或PureWindowsPath）:
"""
from pathlib import PurePath, Path
a = PurePath('basic use.py')
print(type(a))
print(a)

"""
pathsegments 的每个元素可以是一个代表path segment 的字符串，
也可以是一个实现os.PathLike interface 的对象，
它返回一个字符串，或者是另一个path object。
"""
b = PurePath("foo", "some/path", "bar")
print(type(b))
print(b)

c = PurePath(Path('foo'), Path('bar'))
print(type(c))
print(c)

"""
当pathsegments为空时，假定为当前目录。
"""
d = PurePath()
print(type(d))
print(d)



