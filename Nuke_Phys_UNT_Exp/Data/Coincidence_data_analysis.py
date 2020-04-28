import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.style as style
#####################       DATA_SET         ##########################
data = np.genfromtxt('coincidence_data.csv', delimiter=',', skip_header=1)
angles = data[0:19,0]
coin_15 = data[0:19,1]
coin_30 = data[0:19,2]
#####################         PLOT          #############################
#         15 cm distance
fig, ax = plt.subplots()
ax.scatter(angles,coin_15,s=30,c='darkblue',label="15 cm")
ax.set_title("Angular Correlation in Coincidence")
ax.set_ylabel("Counts per Second")
ax.set_xlabel("Angle")
#         30 cm distance
ax.scatter(angles,coin_30,s=30,label="30 cm",c='darkorange')
plt.grid()
plt.tight_layout()
ax.legend()
######################        FIT          ###############################
# Code written to plot a gaussian fit to the data above.
#         15 cm distance
mean1 = sum(angles * coin_15) / sum(coin_15)
sigma1 = np.sqrt(sum(coin_15 * (angles - mean1)**2) / sum(coin_15))
def Gauss1(angles, a, angles0, sigma1):
    return a * np.exp(-(angles - angles0)**2 / (2 * sigma1**2))
popt,pcov = curve_fit(Gauss1, angles, coin_15, p0=[max(coin_15), mean1, sigma1])
plt.plot(angles, Gauss1(angles, *popt), linewidth=1.2,c="blue")
#         30 cm distance
mean2 = sum(angles * coin_30) / sum(coin_30)
sigma2 = np.sqrt(sum(coin_30 * (angles - mean2)**2) / sum(coin_30))
def Gauss2(angles, a, angles0, sigma2):
    return a * np.exp(-(angles - angles0)**2 / (2 * sigma2**2))
popt,pcov = curve_fit(Gauss2, angles, coin_30, p0=[max(coin_30), mean2, sigma2])
plt.plot(angles, Gauss2(angles, *popt),c="orange", linewidth=1.2)
style.use('fivethirtyeight')
fig.savefig("coincidence_gauss_fit")
