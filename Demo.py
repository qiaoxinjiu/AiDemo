from mxnet import nd
x = nd.arange(12)
print(x.size)
print(x.reshape(3,4))
y = nd.array([[2,1,4,3],[1,2,3,4],[4,3,2,1]])
nd.concat(x, y, dim=0), nd.concat(x, y, dim=1)
print(y)
