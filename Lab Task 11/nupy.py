import numpy as np
ary=np.array([1,2,3,5])
print(ary)
type(ary)
bry=np.array([x for x in range(2,21,3)])
print(bry)
aary=np.array([[1,2,3],[4,5,6]])
print(aary)
aaary=np.array([[[1,2,3],[2,3,4]],[[5,6,7],[8,9,1]]])
print(aaary)
print(ary.dtype)
print(aary.dtype)
print(aary.shape)
print(ary.size)
print(aary.itemsize)
print()
print()
score=np.array([85,90,78,92,88])
print(score)
print(score.dtype)
score=np.array(score, dtype='f')
print(score)
print(score.dtype)
score1=score.copy()
print(score1)
score1+=5
print(score1)
x=np.where(score>85)
print(x)
print(score.shape)
print(score.ndim)
print(score.size)
print(score.itemsize)
print(score.dtype)
score.sort()
print(score)
print(score.max())
print(score.min())
print(score.sum())
print(score.mean())
print(score[::2])
print(score[-3:-1])
print(score[1:4])