qipan = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
def com():
	s=[(0,1,2),(0,2,1),(1,2,0),(3,4,5),(3,5,4),(4,5,3),(6,7,8),(6,8,7),(7,8,6),(0,3,6),(0,6,3),
		(3,6,0),(1,4,7),(1,7,4),(4,7,1),(2,5,8),(2,8,5),
		(5,8,2),(0,4,8),(0,8,4),(4,8,0),(2,4,6),(2,6,4),(4,6,2)]
	for i in s:
		a,b,c=i
		if qipan[a]==qipan[b]=='#' and qipan[c]==' ':
			qipan[c]='#'
			print('{}\n{}\n{}'.format((qipan[0],qipan[1],qipan[2]),(qipan[3],\
					qipan[4],qipan[5]),(qipan[6],qipan[7],qipan[8])))
			return
	for i in s:
		a,b,c=i
		if qipan[a]==qipan[b]!=' ' and qipan[c]==' ':
			qipan[c]='#'
			print('{}\n{}\n{}'.format((qipan[0],qipan[1],qipan[2]),(qipan[3],\
					qipan[4],qipan[5]),(qipan[6],qipan[7],qipan[8])))
			return
	s2 = (4,0,2,6,8,1,3,5,7)
	for n in s2:
		if qipan[n]==' ':
			qipan[n]='#'
			print('{}\n{}\n{}'.format((qipan[0],qipan[1],qipan[2]),(qipan[3],\
					qipan[4],qipan[5]),(qipan[6],qipan[7],qipan[8])))
			return
def winner():
	win = [(1,2,0),(4,5,3),(7,8,6),(1,4,7),(2,5,8),(3,6,0),(0,4,8),(2,4,6)]
	for i in win:
		m,n,z=i
		if qipan[m]==qipan[n]==qipan[z]=='*':
			return('你赢了')
		elif qipan[m]==qipan[n]==qipan[z]=='#':
			return('你输了')
	if ' ' not in qipan:
		return('平局')
	return('0')

print('{}\n{}\n{}'.format((qipan[0],qipan[1],qipan[2]),(qipan[3],\
					qipan[4],qipan[5]),(qipan[6],qipan[7],qipan[8])))

while True:
	'''
	不会写异常啊啊啊！！！覆盖落子有bug
	try:
		a = int(input('123456789:'))
		if qipan[a] == ' '
			print()
	except BaseException :
		print('有子了')
	'''
	a = int(input('123456789:'))
	qipan[a-1]='*'
	com()
	j=winner()
	if not j=='0':
		print(j)
		break


