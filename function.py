import math

def quadratic(a, b, c):
	#定义三个变量 用来做返回值 
	x1 = None
	x2 = None
	xx = None
	#判断是否有解
	if (b * b - 4*a*c) >= 0:
		x1 = (-b + math.sqrt(b * b - 4*a*c)) / 2 * a
		x2 = (-b - math.sqrt(b * b - 4*a*c)) / 2 * a
		if(x1 == x2):
			xx = '此方程有两个相同解！'
		else:
			xx = '此方程有两个不同解！'
	else:
		xx = '此方程无解！'
	return x1,x2,xx
# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
if quadratic(2, 3, 1) != (-2.0, -4.0, '此方程有两个不同解！'):
	print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0, '此方程有两个不同解！'):
    print('测试失败')
else:
    print('测试成功')