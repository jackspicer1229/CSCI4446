import matplotlib.pyplot as plt

l = input('Enter a value for l: ')
m = 300
R = 2.8
x0 = 0.2
nArrayArray = []
rArray = []

while(int(R)!=4):	
	x_nArray = []
	for i in range (0,m):
		x_n1 = R*x0*(1-x0)
		x_nArray.append(x0)
		x0 = x_n1
	x_nArray = x_nArray[l:m]
	rArray.append(R)
	nArrayArray.append(x_nArray)
	R += 0.0005

print("We out here")


plt.figure(figsize=(12,8))
plt.suptitle("Bifurcation Diagram using m = " + str(m) + " and l = " + str(l))
for xe, ye in zip(rArray, nArrayArray):
    plt.scatter([xe] * len(ye), ye, s=0.005, c="black")
plt.xlabel("R")
plt.ylabel("$X_n$")


plt.tight_layout()
plt.subplots_adjust(top=0.85)
plt.show()

# plt.savefig("fig2.png")