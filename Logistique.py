import matplotlib.pyplot as plt

nmax = 40
r = 3.4
u0 = 0.7

def u(n):
    u=u0
    for i in range(n):
        u=r*u*(1-u)
    return u

title ="Suite logistique "+"$u_{n+1} ="+str(r)+"u_n (1-u_n)$"+" avec "+"$u_0 ="+str(u0)+"$"
plt.title(title)
plt.xlabel("n")
plt.ylabel("$u_n$")

plt.plot([u(k) for k in range(nmax)],'bo')

plt.show()