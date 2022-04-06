# print(dir(list))#'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# print(len(['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'])) #11

# a=[]
# print(a,type(a)) #[] list
# p=["Ameerpet",55]
# print(p,type(p))#['Ameerpet',55] list
# print(p[0],type(p[0])) #Ameerpet str
# print(p[1],type(p[1])) #55 int
# a=None
# print(a,type(a)) #None NoneType

# b=[2,7.9,"hi",None,True]
# print(b[0],type(b[0]))#2 int
# print(b[1],type(b[1]))#7.9 float
# print(b[2],type(b[2]))#hi str
# print(b[3],type(b[3]))#None NoneType
# print(b[4],type(b[4]))#True bool
# print(b[5],type(b[5]))#IndexError:list index out of range

# s="hello"
# s[0]="H" #TypeError:str object does not support item assignment

# b=[4,3.1,"python"]
# b[0]=89.23
# b[-1]='Gt'
# print(b) #[89.23,3.1,'Gt']
# n=[1,3.7,"hello",[10,11]]
# print(n,type(n))#[1,3.7,"hello",[10,11]] list
# print(n[0],type(n[0]))#1 int
# print(n[1],type(n[1]))#3.7 float
# print(n[2],type(n[2]))#hello str
# print(n[3],type(n[3]))#[10,11] list
# print(n[3][0],type(n[3][0]))#10 int
# print(n[3][1],type(n[3][1]))#11 int

# n=[1,3.7,"hello",[10,11]]
# n[0]=24
# n[3][0]=50
# print(n,type(n))#[24,3.7,"hello",[50,11]]
# print(n[0],type(n[0]))#24 int
# print(n[1],type(n[1]))#3.7 float
# print(n[2],type(n[2]))#hello str
# print(n[3],type(n[3]))#[50,11] list

# k=[1,3.7,"hello",[10,11]]
# k.append('josh')
# print(k)#[1,3.7,"hello",[10,11],'josh']
# k=[1,3.7,"hello",[10,11]]
# k.clear()
# print(k) #[]

# n=[5,10,15,20]
# print(n)#[5,10,15,20]
# b=n.copy()
# print(b)#[5,10,15,20]

# h=[5,10,'priya',10,'']
# print(h.count(' '))#0
# print(h.count(6))#0
# print(h.count(10))#2
# print(h.count('priya'))#1

# a=[5,10,15]
# b=[1,3,5,7]
# a.extend(b)
# print(a) #[5, 10, 15, 1, 3, 5, 7]
# b.extend(a)
# print(b)#[1, 3, 5, 7, 5, 10, 15]

# v=[2,4,6,8,'hello',4.5,[56]]
# print(v.index(14.5))#ValueErroe:14.5 is not on list
# print(v.index(8))#3
# print(v.index([56]))#6
# print(v.index([2]))#[2] is not in list

# u=[1,3,5,7,11,13,15]
# u.insert(6,9)
# u.insert(2,4)
# u.insert(-1,8)
# u.insert(-2,10)
# print(u)#[1,3,4,5,7,11,13,9,10,8,15]

# j=[10,20,30,40]
# j.pop()
# print(j) #[10,20,30]
# j.pop(0)
# print(j)#[20,30,40]
# j.pop(4)
# print(j)#IndexError: pop index oyt of range

# n=[10,20,'hello',30,40]
# n.remove('hello')
# n.index(100)#ValueError:100 is not in list
# print(n) #[10,20,30,40]

# c=[1,2,3,4,5]
# print(c[::-1])#[5,4,3,2,1]
# c.reverse()
# print(c)#[5,4,3,2,1]

# t=[1,5,4,3,2]
# t.sort()
# print(t) #[1,2,3,4,5]
# t.sort(reverse=False)
# print(t)#[1,2,3,4,5]
# t.sort(reverse=True)
# print(t)#[5, 4, 3, 2, 1]

# j=[2.8,3.5,6.8,1.4,2.6]
# j.sort()
# print(j)#[1.4,2.6,2.8,3.5,6.8]

# l=['HD','LK','SL','HH','HA','s','BA','PA','DA','WM','LH','PZ']
# l.sort()
# print(l)#['BA', 'DA', 'HA', 'HD', 'HH', 'LH', 'LK', 'PA', 'PZ', 'SL', 'WM', 's']
# l.sort(reverse=True)
# print(l)#['s', 'WM', 'SL', 'PZ', 'PA', 'LK', 'LH', 'HH', 'HD', 'HA', 'DA', 'BA']




