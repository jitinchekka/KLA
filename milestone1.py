# Read the file Format_Source.txt
data = ""


class coordinates:
	x = -1
	y = -1

	def __init__(self) -> None:
		pass


class poly:
	layer = 0
	number_of_vertices = 0
	# list of coordinates class objects
	vertices = [] #array of coordinates
	def __init__(self) -> None:
		pass

class Polygons:
	header = []
	polygons = [] #array of poly
	number_of_polygons = 0
	footer = []

	def __init__(self) -> None:
		pass


with open("Milestone_Input\Milestone 1\Format_Source.txt", "r") as f:
	header = []
	data = f.readlines()
	p = Polygons() #Whole file
	# Remove all empty lines in a string
	header_flag = 0
	# Remove all empty strings from the list of strings data
	data = [x for x in data if x != '\n']
	n = len(data)
	# print("n = ",n)
	# print(data)
	for i in range(n):
		# Header
		if header_flag == 0:
			if (data[i]=="strname top\n"):
				# print("End of header")
				header_flag=1
				print(i)
			p.header.append(data[i])
		else:
		# polygon
			if(data[i]=='boundary\n'):
				p1=poly() #object of class poly
				p1.vertices=[]
				p1.layer=-1
				p1.number_of_vertices=0
				p1.layer = data[i + 1].split()[1] #layer
				# data[i+3] has the coordinates
				arr = data[i + 3].split()
				# print("Arr = ",arr)
				p1.number_of_vertices = int(arr[1]) #number of vertices
				# print("Number of vertices = ",p1.number_of_vertices)
				j=2
				while j<len(arr):
					points=coordinates()
					points.x=arr[j]
					points.y=arr[j+1]
					# print(points.x,points.y)
					p1.vertices.append(points)
					j+=2
				# print(len(p1.vertices))
				# print("i=",i)
				p.number_of_polygons+=1
				p.polygons.append(p1)
				i=i+4
			elif data[i] == "endstr":
				while i!=n-1:
					p.footer.append(data[i])
				break		
		# Footer
		if data[i]=="endstr\n":
			p.footer.append(data[i])
			p.footer.append(data[i+1])
			break
	# Print all the polygons
	# print("The header is ",p.header)
	# print("The number of polygons are",p.number_of_polygons)

	# Write to ouptut file
	

with open('output.txt', 'w') as f:
    for x in p.header:
        f.write(x)
    n=p.number_of_polygons
    for i in range(2):
        f.write("boundary\n")
        f.write("layer ")
        f.write(p.polygons[i].layer)
        f.write("\n")
        f.write("datatype 0\n")
        f.write("xy ")
        # print(p.polygons[i].number_of_vertices,"Test")
        f.write(str(p.polygons[i].number_of_vertices))
        f.write(" ")
        for j in range(p.polygons[i].number_of_vertices):
            f.write(p.polygons[i].vertices[j].x)
            f.write(" ")
            f.write(p.polygons[i].vertices[j].y)
            f.write(" ")
        f.write("\n")
        f.write("endel\n")
    f.write(p.footer[0])
    f.write(p.footer[1])
    

# print("The footer is ")
# print(p.footer)
'''for i in range(p.number_of_polygons):
	print("Polygon ",i)
	print("It has ",p.polygons[i].number_of_vertices," vertices")
	print(len(p.polygons[i].vertices))
	print("They are:")
	for v in p.polygons[i].vertices:
		print(v.x,v.y)
	print()'''