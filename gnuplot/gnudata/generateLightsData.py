import math
import io

output = io.open("LightsData.txt",'w');

thetaStart = -2*math.pi
thetaEnd   =  2*math.pi
thetaCount =  10000
deltaTheta =  (thetaEnd-thetaStart)/thetaCount
iRange = range(1,thetaCount,1)

theta  = thetaStart

for i in range(1,thetaCount,1):
	result  = math.sin(theta)
	if (result < 0):
		result = 0
		
	result8 = result**8
	if (result8 <0 ):
		result8 = 0
		
	result128 = result**128
	if (result128 < 0):
		result128 = 0
		
	output.write(u'%f  %f  %f  %f\n' %(theta, result, result8, result128))
	theta = theta + deltaTheta

	
output.close()


