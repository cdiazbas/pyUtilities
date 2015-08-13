# Author: cdiazbas@iac.es
# Code: Script translated from IDL version
#       @vivivum: https://github.com/vivivum/MilosIDL/
#		Author: D. Orozco Suarez & J.C. del Toro Iniesta

# ; INPUTS:
# ;           DAMP: A scalar with the damping parameter
# ;           VV: Wavelength axis usually in Doppler units.
# ; OUTPUTS:
# ;           H: Voigt function
# ;           F: Faraday-Voigt function
# ; NOTES:
# ;           A rational approximation to the complex error function is used
# ;           after Hui, Armstrong, and Wray(1978, JQSRT 19, 509-516). H and F are 
# ;           the real and imaginary parts of such function, respectively.

def fvoigt(damp,vv):

	from numpy import array, ones, real, sign, imag

	A=[122.607931777104326, 214.382388694706425, 181.928533092181549,\
		93.155580458138441, 30.180142196210589, 5.912626209773153,\
		0.564189583562615]

	B=[122.60793177387535, 352.730625110963558, 457.334478783897737,\
		348.703917719495792, 170.354001821091472, 53.992906912940207,\
		10.479857114260399,1.]

	z = array(damp*ones(len(vv)) + -abs(vv)*1j)

	Z=((((((A[6]*z+A[5])*z+A[4])*z+A[3])*z+A[2])*z+A[1])*z+A[0])/\
	(((((((z+B[6])*z+B[5])*z+B[4])*z+B[3])*z+B[2])*z+B[1])*z+B[0])

	h=real(Z)
	f=sign(vv)*imag(Z)*0.5

	return [h,f]



if __name__ == "__main__":
	import numpy as np
	import matplotlib.pyplot as plt

	uvals = np.linspace(-100., 100., 200)
	a = 1e-1

	[h,f] = fvoigt(a,uvals)

	# plt.plot(uvals,f,'k-')
	# plt.plot(uvals,h,'r-')

	# from voigt import voigt,voigtslow

	# v2 = voigt(a, uvals)
	# plt.plot(uvals,v2,'g-')
	# print('error relativo:',max((h-v2)/h))

	# plt.show()

	#  Normalization
	from scipy import integrate

	ddop = 10.
	uvals = uvals/ddop
	[h,f] = fvoigt(a,uvals)
	sqrtpi = 1./np.sqrt(np.pi)
	print(integrate.simps(sqrtpi*h/ddop))
	print(integrate.simps(sqrtpi*f/ddop))

