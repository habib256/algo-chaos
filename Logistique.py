import matplotlib.pyplot as plt

nmax = 28
r = 2.5
u0 = 0.7

def u(n):
    u=u0
    for i in range(n):
        u=r*u*(1-u)
    return u

title ="Suite logistique "+"$X_{n+1} ="+str(r)+"X_n (1-X_n)$"+" avec "+"$U_0 ="+str(u0)+"$"
plt.title(title)
plt.xlabel("n")
plt.ylabel("$X_n$")

plt.plot([u(k) for k in range(nmax)],'b')

plt.show()