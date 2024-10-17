# CONTINUED DEFLATION TEST

"""
Here we solve Euler's elastic equation:
    
    u''(x) + lambda^2 sin(u) - mu  = 0 with u(0) = u(1) = 0.
    
This equation has a number of different solutions depending on the value of 
lambda (try switch the value of mu from 0 to 0.5 and the bifurcation diagram 
will change). 

May take a minute or so to run. 

"""


%clear -f 
%reset -f 

# import necessary packages
# -----------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, root
from scipy.sparse import diags


# set up spatial discretisation (finite difference stencil)
# -----------------------
n = 20                            # number of intervals
h = 1/n                            # mesh size
diag_main = np.full(n, -2/h**2)
diag_sub = np.full(n-1, 1/h**2)
Lap = diags([diag_sub, diag_main, diag_sub], [-1, 0, 1]).toarray() # finite difference stencil (Laplacian)
x = np.linspace(0, 1, num=n)

# define the function to be solved (and the delation operator)
# -----------------------
def F(u,        # solution to try
      u_stars,  # list of known solutions
      q         # lambda value (bifurcating paramter)
      ):
    
    # deflator
    p = 2.0
    sigma = 0.5
    M = 1.0
    for u_star in u_stars:
        M *= np.linalg.norm(u - u_star)**(-p) + sigma

    mu = 0  # try 0.5
    r = Lap.dot(u) + (q**2)*np.sin(u) - mu
    r[0] = 0
    r[-1] = 0
    
    return M*r
    

# define lambda range
# -----------------------
lmbda = np.linspace(0.0, 4*np.pi, 51)


# initial solutions list
# -----------------------
S = [None] * len(lmbda)
S[0] = [np.zeros(n,)+0.01]



# deflated continuation
# -----------------------
for i in range(len(lmbda) - 1):
    
    S[i+1] = list()
    q = lmbda[i + 1]

    # continue the existing branches for lambda_{i+1}
    for u in S[i]:
        try:
            root1 = root(F, u, args=(S[i+1], q), method="krylov", tol=1e-8, options={"maxiter": 200})
            if root1.success:
                u_star = root1.x
                S[i + 1].append(u_star)
        except:
            continue

    # look for new branches for lambda_{i+1}
    for u in S[i]:
        success = True
        while success:
            try:
                root1 = root(F, u, args=(S[i+1], q), method="krylov", tol=1e-8, options={"maxiter": 200})
                if root1.success:
                    u_star = root1.x
                    S[i + 1].append(u_star)
                else:
                    success = False
            except:
                success = False


# print the results
# -----------------------
for i in range(len(S)):
    print(f"Lambda = {round(lmbda[i],2)} --> # of solutions = {len(S[i])} ")




# collect and plot
# -----------------------
u_values = []
lmbda_values = []

for i in range(len(S)):
    for u in S[i]:
        u_values.append(np.sign((u[1]-u[0])/(x[1]-x[0]))*np.linalg.norm(u))
        lmbda_values.append(lmbda[i])

plt.figure(figsize=(6, 6))
plt.grid(True, alpha=0.5)
plt.scatter(lmbda_values, u_values, color='k', s=1)
plt.xlabel(r'$\lambda$')
plt.ylabel(r'$sign(u_x(0)) \| u \|_{2}$')
plt.title('Bifurcation Diagram')
plt.show()



