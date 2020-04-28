import numpy as np
#Individual functions written to calculate for multiple angles at once.
def R_list(L,thetas):
    r_list = [L*np.tan(theta) for theta in thetas]
    return r_list
def Phi_list_1(r_1,r_2,r_list):
    phi_1_list = [np.arccos((R**2 + r_1**2 - r_2**2)/(2*r_1*R))
    for R in r_list]
    return phi_1_list
def Phi_list_2(r_1,r_2,r_list):
    phi_2_list = [np.arccos((R**2 + r_2**2 - r_1**2)/(2*r_2*R))
    for R in r_list]
    return phi_2_list
def Area_list(r_1,r_2,phi_1_list,phi_2_list):
    area_list_1 = [((r_1**2)*(phi_1 -(0.5*np.sin(2*phi_1))))
    for phi_1 in phi_1_list]
    area_list_2 = [((r_2**2)*(phi_2-(0.5*np.sin(2*phi_2))))
    for phi_2 in phi_2_list]
    area_list_total = [x + y for x, y in zip(area_list_1, area_list_2)]
    return area_list_total
############# Actual Calculation of the Over-Lapping Areas ###############
thetas = [0,np.pi/180,np.pi/90,np.pi/60,np.pi/45,np.pi/36,
          np.pi/30,np.pi/27.5,np.pi/18,np.pi/15]
r_1 = 4
r_2 = 4.25
r_list_15 = R_list(15,thetas)
r_list_30 = R_list(30,thetas)
phi_1_list_15 = Phi_list_1(r_1,r_2,r_list_15)
phi_1_list_30 = Phi_list_1(r_1,r_2,r_list_30)
phi_2_list_15 = Phi_list_2(r_1,r_2,r_list_15)
phi_2_list_30 = Phi_list_2(r_1,r_2,r_list_30)
area_list_15 = Area_list(r_1,r_2,phi_1_list_15,phi_2_list_15)
area_list_30 = Area_list(r_1,r_2,phi_1_list_30,phi_2_list_30)
print(area_list_15)
print(area_list_30)
