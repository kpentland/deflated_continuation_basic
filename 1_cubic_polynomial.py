# CONTINUED DEFLATION TEST

"""
Here we solve the polynomial:
    
    (u^3)/3 + qu + 0.1 = 0
    
This equation has one, two, or three roots, depending on the value of q. 
"""

%clear -f 
%reset -f 


# import necessary packages
# -----------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton


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

    return M*((u**3)/3 + q*u + (1/10))
    

    
# define lambda range
# -----------------------
lmbda = np.linspace(0.5, -1.5, 501)

# initial solutions list
# -----------------------
S = [None] * len(lmbda)
S[0] = [-0.195]




# deflated continuation
# -----------------------
for i in range(len(lmbda) - 1):
    
    S[i+1] = []
    q = lmbda[i+1]

    # continue the existing branches for lambda_{i+1}
    for u in S[i]:
        try:
            root1 = newton(func=F, x0=u, args=(S[i+1], q), maxiter=30, full_output=True, tol=1e-12)
            if root1[1].converged:
                u_star = root1[0]
                S[i+1].append(u_star)
        except:
            continue

    # look for new branches for lambda_{i+1}
    for u in S[i]:
        success = True
        while success:
            try:
                root1 = newton(func=F, x0=u, args=(S[i+1], q), maxiter=30, full_output=True, tol=1e-12)
                if root1[1].converged:
                    u_star = root1[0]
                    S[i+1].append(u_star)
                else:
                    success = False
            except:
                success = False


# print the results
# -----------------------
for i in range(len(S)):
    print(f"Lambda = {round(lmbda[i],2)} --> # of solutions = {len(S[i])} ---> Solutions = {S[i]}")



# collect and plot
# -----------------------
u_values = []
lmbda_values = []

for i in range(len(S)):
    for u in S[i]:
        u_values.append(u)
        lmbda_values.append(lmbda[i])

plt.figure(figsize=(6, 6))
plt.grid(True, alpha=0.5)
plt.scatter(lmbda_values, u_values, color='k', s=1)
plt.xlabel(r'$\lambda$')
plt.ylabel('u')
plt.title('Bifurcation Diagram')
plt.show()

