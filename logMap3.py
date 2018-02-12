import matplotlib.pyplot as plt

l = input('Enter a value for l: ')
m = 300
a = 0
b = 0.3
x0 = 0.19
x1 = 0.2
nArrayArray = []
rArray = []

while(a<=1.4):	
	x_nArray = []
	for i in range (0,m):
		x_n1 = 1 - a*x1*x1 + b*x0
		x_nArray.append(x1)
		x0 = x1
		x1 = x_n1
	x_nArray = x_nArray[l:m]
	rArray.append(a)
	nArrayArray.append(x_nArray)
	a += 0.0005

print("We out here")


plt.figure(figsize=(12,8))
plt.suptitle("Henon Map Bifurcation Diagram using m = " + str(m) + " and l = " + str(l))
for xe, ye in zip(rArray, nArrayArray):
    plt.scatter([xe] * len(ye), ye, s=0.005, c="black")
plt.xlabel("a")
plt.ylabel("$X_n$")


plt.tight_layout()
plt.subplots_adjust(top=0.85)
plt.show()

# plt.savefig("fig2.png")