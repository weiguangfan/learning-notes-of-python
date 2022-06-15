import math

# math.pi:数学常数π=3.141592...，达到可用精度。
print(math.pi)
# math.e:数学常数e=2.718281...，达到可用精度。
print(math.e)
"""
math.tau:数学常数τ=6.283185...，达到可用精度。
Tau是一个圆常数，等于2π，即一个圆的周长与半径的比值。
"""
print(math.tau)

"""
math.inf:浮点正无穷大。
（对于负无穷大，使用-math.inf.）
等效于float的输出（“inf”）。
"""
print(math.inf)

"""
math.nan:一个浮点的 "非数字"（NaN）值。
相当于float('nan')的输出。
由于IEEE-754标准的要求，math.nan和float('nan')不被认为等于任何其他数字值，包括它们自己。
要检查一个数字是否是NaN，请使用isnan()函数来测试NaN，而不是is或==。
"""
print(math.isnan(math.nan))