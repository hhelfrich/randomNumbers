from randomNumbers import LinearCongruential
import matplotlib.pyplot as plt

ran1 = LinearCongruential()
ran2 = LinearCongruential(1.0,6.0)

print(ran1.random())
print(ran1.random(10))
print(ran2.random())
print(ran2.random(10))

x = ran1.random(1000)

plt.plot(x, ".")
plt.show()