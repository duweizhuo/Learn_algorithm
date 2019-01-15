
import io, vtk, re

class node:
    count = 0
    
    def __init__(self, number, X, Y, Z):
        self.number = int(number.strip())
        self.X = float(X)
        self.Y = float(Y)
        self.Z = float(Z)
        node.count += 1
        
class tet4:
    count =0
    
    def __init__(self, number, node1, node2, node3, node4):
        self.number = int(number.strip())
        self.node1 = int(node1.strip())
        self.node2 = int(node2.strip())
        self.node3 = int(node3.strip())
        self.node4 = int(node4.strip())
        tet4.count += 1

f = open('demo.inp','r')   
data = f.readlines()

           
node_pattern = re.compile('\s*\d+\,\s*\-*\d+\.\d*E*\-*\d*\,\s*\-*\d+\.\d*E*\-*\d*\,\s*\-*\d+\.\d*E*\-*\d*\n')
tet4_pattern = re.compile('\s*\d+\,\s*\d+\,\s*\d+\,\s*\d+,\s*\d+\n')

node_list = []
tet4_list = []
#shell3_list = []

for line in data:
    if node_pattern.match(line):
        groups = line.split(',')
        node1 = node(groups[0],groups[1],groups[2],groups[3])
        node_list.append(node1)
    if tet4_pattern.match(line):
        groups = line.split(',')
        tet1 = tet4(groups[0],groups[1],groups[2],groups[3],groups[4])
        tet4_list.append(tet1)

        
print(node.count)
print(tet4.count)

      
def nodeReorder(node_list):
    i = 0
    node_num_order = {}
    for node in node_list:
        node_num_order[node.number] = i
        i += 1
    
    return node_num_order
        
node_ordered = nodeReorder(node_list)

#VTK insert points
points = vtk.vtkPoints()
print("adding nodes now.")
for node in node_list:
    points.InsertNextPoint(node.X, node.Y, node.Z)
    
#vtk generate mesh
mesh = vtk.vtkUnstructuredGrid()
tetra = vtk.vtkTetra()
cellarray = vtk.vtkCellArray()
for tet in tet4_list:
    tetra.GetPointIds().SetId(0, node_ordered[tet.node1])
    tetra.GetPointIds().SetId(1, node_ordered[tet.node2])
    tetra.GetPointIds().SetId(2, node_ordered[tet.node3])
    tetra.GetPointIds().SetId(3, node_ordered[tet.node4])
    cellarray.InsertNextCell(tetra)

mesh.SetPoints(points)
mesh.SetCells(vtk.VTK_TETRA, cellarray)

#extract surface
surface_filter = vtk.vtkDataSetSurfaceFilter()
surface_filter.SetInputData(mesh)
surface_filter.Update()
polydata = vtk.vtkPolyData()
polydata = surface_filter.GetOutput()

#output surface

i = 0
output = []
node_count = polydata.GetNumberOfPoints()
f = open('output.txt','w')
for i in range(node_count):
    point_tmp = polydata.GetPoint(i)
    f.writelines(str(point_tmp) + '\n')
f.close
