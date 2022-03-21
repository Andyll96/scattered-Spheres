from maya import cmds
import random

firstSphereX = random.uniform(-12,12)
firstSphereZ = random.uniform(-12,12)

cmds.polySphere(r=0.5, name='pSphere0')
cmds.move(firstSphereX, 0, firstSphereZ)

existingSpheres = ['pSphere0']

cmds.shadingNode('distanceBetween', asUtility=True)

for i in range(500):
	testSphereX = random.uniform(-12,12)
	testSphereZ = random.uniform(-12,12)
	
	cmds.polySphere(r=0.5, name='testSphere')
	cmds.move(testSphereX, 0, testSphereZ)
	
	numSpheres = len(existingSpheres)
	# print(f'numSpheres:{numSpheres})')
	
	counter = 0
	
	for j in range(numSpheres):
		# print(f'j: {j}')
		cmds.connectAttr('testSphere.translate', 'distanceBetween1.point1')
		cmds.connectAttr(f'{existingSpheres[j]}.translate', 'distanceBetween1.point2')
		
		dist = cmds.getAttr('distanceBetween1.distance')
		
		cmds.disconnectAttr('testSphere.translate','distanceBetween1.point1')
		cmds.disconnectAttr(f'{existingSpheres[j]}.translate', 'distanceBetween1.point2')
		
		if dist > 1:
			counter = counter + 1
	if counter == len(existingSpheres):
		# rename the testSphere
		cmds.rename('testSphere', f'pSphere{str(len(existingSpheres))}')
		existingSpheres.append(f'pSphere{str(len(existingSpheres))}')
		# add it to the list of existing spheres
	else:
		cmds.select('testSphere', replace=True)
		cmds.delete()