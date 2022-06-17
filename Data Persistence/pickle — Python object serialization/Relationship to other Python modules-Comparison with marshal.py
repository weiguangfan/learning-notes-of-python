"""
pickle module 实现了对 Python object structure进行serializing和de-serializing的二进制协议。
"pickling "是一个 Python object hierarchy 转换成 a byte stream的过程，
"unpickling "是一个逆向操作，即a byte stream (来自二进制文件或类似字节的对象) 被转换回a object hierarchy。
Pickling（和unpickling）也被称为 "serialization"、"marshalling "或 "flattening"；
然而，为了避免混淆，这里使用的术语是 "pickling "和 "unpickling"。

Python 有一个更原始的serialization module，叫做 marshal。
但一般来说 pickle 应该永远是serialize Python objects的首选方式。
marshal 的存在主要是为了支持 Python 的 .pyc 文件。

pickle module 在几个重要的方面与marshal不同。

pickle module 跟踪它已经serialized的对象，这样以后对the same object 的引用就不会再被serialized了。 marshal不这样做。

这对recursive object 递归对象和object sharing 对象共享都有影响。
Recursive objects 递归对象是包含对自身引用的对象。
marshal 不处理这些对象，事实上，尝试对recursive objects递归对象进行 marshal 会使你的 Python 解释器崩溃。
当在serialized 的object hierarchy中的不同地方有对同一个对象的多个引用时，就会发生object sharing 对象共享的情况。shared objects 共享的对象仍然是共享的，这对易变的对象非常重要。

marshal不能用来serialize用户定义的类和它们的实例。
pickle可以透明地保存和恢复类的实例，但是类的定义必须是可导入的，并且与对象被存储时生活在同一个模块中。

marshal serialization format 不能保证在不同的Python版本中都能移植。
因为它在生活中的主要工作是支持 .pyc 文件，Python 实现者保留在需要时以非向后兼容的方式改变序列化格式的权利。
如果选择了兼容的pickle协议，pickle序列化格式保证在Python版本之间向后兼容，并且如果你的数据跨越了独特的突破性语言边界，pickling和unpickling代码会处理Python 2到Python 3的类型差异。


"""