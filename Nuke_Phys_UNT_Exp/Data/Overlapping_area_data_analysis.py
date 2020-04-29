import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.style as style
#####################       DATA_SET         ##########################
#         15 cm distance
angles_15 = np.array([12,10,8,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-8,-10,-12])
overlapping_area_15 = np.array([27.79,31.96,39.26,40.41,42.53,44.63,46.70,
                           48.68,50.25,50.27,50.25,48.68,46.70,44.63,42.53,40.41,
                           39.26,31.96,27.79])
#         30 cm distance
angles_30 = np.array([12,10,8,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-8,-10,-12])
overlapping_area_30 = np.array([6.70,13.01,25.87,28.05,32.12,36.26,40.45,44.64,
                           48.68,50.27,48.68,44.64,40.45,36.26,32.12,28.05,
                           25.87 ,13.01,6.70])
#####################         PLOT          #############################
#         15 cm distance
fig, ax = plt.subplots()
ax.scatter(angles_15,overlapping_area_15,s=30,c='darkblue',label="15 cm")
ax.set_title("Overlapping Area per Angle")
ax.set_ylabel("Area")
ax.set_xlabel("Angle")
#         30 cm distance
ax.scatter(angles_30,overlapping_area_30,s=30,label="30 cm",c='darkorange')
plt.tight_layout()
plt.grid()
ax.legend()
######################        FIT          ###############################
# Code written to plot a gaussian fit to the data above.
#         15 cm distance
mean1 = sum(angles_15 * overlapping_area_15) / sum(overlapping_area_15)
sigma1 = np.sqrt(sum(overlapping_area_15 * (angles_15 - mean1)**2) / sum(overlapping_area_15))
def Gauss1(angles_15, a, angles_150, sigma1):
    return a * np.exp(-(angles_15 - angles_150)**2 / (2 * sigma1**2))
popt,pcov = curve_fit(Gauss1, angles_15, overlapping_area_15, p0=[max(overlapping_area_15), mean1, sigma1])
plt.plot(angles_15, Gauss1(angles_15, *popt), linewidth=1.2,c="blue")
#         30 cm distance
mean2 = sum(angles_30 * overlapping_area_30) / sum(overlapping_area_30)
sigma2 = np.sqrt(sum(overlapping_area_30 * (angles_15 - mean2)**2) / sum(overlapping_area_30))
def Gauss2(angles_30, a, angles_300, sigma2):
    return a * np.exp(-(angles_30 - angles_300)**2 / (2 * sigma2**2))
popt,pcov = curve_fit(Gauss2, angles_30, overlapping_area_30, p0=[max(overlapping_area_30), mean2, sigma2])
plt.plot(angles_30, Gauss2(angles_30, *popt),c="orange", linewidth=1.2)
style.use('fivethirtyeight')
fig.savefig("overlapping_area_gauss_fit")
