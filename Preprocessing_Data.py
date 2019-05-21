import numpy as np 
from random import shuffle

# Đọc data thô
data = []
with open("F:/UIT/ML/House_Boston/house.data", "r") as f:
	while True:
		line = f.readline()
		if not line:
			break
		data.append(line)

# Trả về data gồm các số thực
data1 = []
for i in data:
	new = i.split("\n")[0].split(" ")
	new_data = []
	for j in new:
		if j != '':
			new_data.append(float(j))
	data1.append(new_data)

# Trộn đều data
shuffle(data1)

# Tách data thành tâp X, y
X = []
y = []
for i in data1:
	new_X = i[:13]
	new_y = i[13]

	X.append(new_X)
	y.append(new_y)	

# Tách data thành train và test theo tỷ lệ 2 : 1
train_X = X[0:len(X)//3*2]
test_X = X[len(X)//3*2:]

train_y = y[0:len(y)//3*2]
test_y = y[len(y)//3*2:]

np.save("F:/UIT/ML/House_Boston/train_X.npy", train_X)
np.save("F:/UIT/ML/House_Boston/test_X.npy", test_X)
np.save("F:/UIT/ML/House_Boston/train_y.npy", train_y)
np.save("F:/UIT/ML/House_Boston/test_y.npy", test_y)