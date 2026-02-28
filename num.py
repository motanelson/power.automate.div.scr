import matplotlib.pyplot as plt
from scipy import stats

plt.style.use('dark_background')

# Dados
x = list(range(20))
y = [int(float(v) * 2.25) for v in x]

# Regressão linear
slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept
print(slope)
print(intercept)
print(r)
print(p)
mymodel = list(map(myfunc, x))
print(x)
print(y)
print(mymodel)
# Gráfico
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()