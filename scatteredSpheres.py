from maya import cmds
import random

# generates the coordinates of the first Sphere
firstSphereX = random.uniform(-12,12)
firstSphereZ = random.uniform(-12,12)

# creates and moves the sphere in position
cmds.polySphere(r=0.5, name='pSphere0')
cmds.move(firstSphereX, 0, firstSphereZ)

# creates a list and adds the first sphere
existingSpheres = ['pSphere0']

# creates a distanceBetween node
cmds.shadingNode('distanceBetween', asUtility=True)

# creates number of spheres
for i in range(500):
	#  generates new coordinates for new sphere
	testSphereX = random.uniform(-12,12)
	testSphereZ = random.uniform(-12,12)
	
	# creates and moves the new sphere in position
	cmds.polySphere(r=0.5, name='testSphere')
	cmds.move(testSphereX, 0, testSphereZ)
	
	# number of spheres added to the list
	numSpheres = len(existingSpheres)
	# print(f'numSpheres:{numSpheres})')
	
	counter = 0
	
	# loop through the list of existing spheres
	for j in range(numSpheres):
		# print(f'j: {j}')
		# connects the distanceBetween node to the test sphere
		cmds.connectAttr('testSphere.translate', 'distanceBetween1.point1')
		# connects the other end of the distanceBetweenNode to the current existing sphere
		cmds.connectAttr(f'{existingSpheres[j]}.translate', 'distanceBetween1.point2')
		
		# get the distance between the two
		dist = cmds.getAttr('distanceBetween1.distance')
		
		# disconnect distance betweenNode
		cmds.disconnectAttr('testSphere.translate','distanceBetween1.point1')
		cmds.disconnectAttr(f'{existingSpheres[j]}.translate', 'distanceBetween1.point2')
		
		# if the distance is more than 1 then increment the counter
		if dist > 1:
			counter = counter + 1

	# if the counter is equal to the length of the list
	if counter == len(existingSpheres):
		# rename the testSphere and append it to the list
		cmds.rename('testSphere', f'pSphere{str(len(existingSpheres))}')
		existingSpheres.append(f'pSphere{str(len(existingSpheres))}')
	else:
		# otherwise delete the testSphere
		cmds.select('testSphere', replace=True)
		cmds.delete()