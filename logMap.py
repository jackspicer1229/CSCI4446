import matplotlib.pyplot as plt

m = input('Enter a value for m: ')
R = 3
x0 = 0.2
nArray = []
xNarray = []
xNPlusOneArray = []

for i in range (0,m):
	x_n1 = R*x0*(1-x0)
	xNarray.append(x0)
	xNPlusOneArray.append(x_n1)
	x0 = x_n1
	nArray.append(i)

xNPlusTwoArray = xNPlusOneArray[1:m]

plt.figure(figsize=(12,4))
plt.suptitle("Logistic Maps using m = " + str(m) + " and R = " + str(R))
plt.subplot(131)
plt.plot(nArray, xNarray, 'ko', markersize=1)
plt.title("$X_n$ versus $n$")
plt.xlabel("n")
plt.ylabel("$X_n$")

plt.subplot(132)
plt.plot(xNarray, xNPlusOneArray, 'ko', markersize=1)
plt.title("$X_{n+1}$ versus $X_n$")
plt.xlabel("$X_n$")
plt.ylabel("$X_{n+1}$")

plt.subplot(133)
plt.plot(xNarray[0:m-1], xNPlusTwoArray, 'ko', markersize=1)
plt.title("$X_{n+2}$ versus $X_n$")
plt.xlabel("$X_n$")
plt.ylabel("$X_{n+2}$")

plt.tight_layout()
plt.subplots_adjust(top=0.85)
plt.show()
