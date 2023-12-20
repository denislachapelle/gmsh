# ------------------------------------------------------------------------------
#
#  Gmsh Python genarating a plate 1x1 with two holes of 0.1 of diameter
#  one centered at 0.5, 0.5 and one at 0.25, 0.25.
#
# Using tansfinite command the generated mesh density is controlled to better define
# both circle circonference.
#
# Denis Lachapelle
# Dec 18, 2023
# ------------------------------------------------------------------------------


import gmsh
import sys

gmsh.initialize()

gmsh.model.add("gmsh-1")

lc = 0.1
#draw a rectangle.
gmsh.model.occ.addPoint(0, 0, 0, lc, 1)
gmsh.model.occ.addPoint(1, 0, 0, lc, 2)
gmsh.model.occ.addPoint(1, 1, 0, lc, 3)
gmsh.model.occ.addPoint(0, 1, 0, lc, 4)
gmsh.model.occ.addLine(1, 2, 1)
gmsh.model.occ.addLine(2, 3, 2)
gmsh.model.occ.addLine(3, 4, 3)
gmsh.model.occ.addLine(4, 1, 4)
gmsh.model.occ.addCurveLoop([1, 2, 3, 4], 1)
#draw a circle.
gmsh.model.occ.addCircle(0.5, 0.5, 0.0, 0.1, 5) 
gmsh.model.occ.addCurveLoop([5], 2)

#draw a circle.
gmsh.model.occ.addCircle(0.25, 0.25, 0.0, 0.1, 6) 
gmsh.model.occ.addCurveLoop([6], 3)
#add a surface
gmsh.model.occ.addPlaneSurface([1, 2, 3], 1)

gmsh.model.occ.synchronize()
#gmsh.model.occ.synchronize()

gmsh.model.mesh.setTransfiniteCurve(5, 72)
gmsh.model.mesh.setTransfiniteCurve(6, 72)

#add a physical group.
gmsh.model.addPhysicalGroup(2, [1], 1, name="copper")
gmsh.model.addPhysicalGroup(1, [1], 2, name="ground")
gmsh.model.addPhysicalGroup(1, [3], 3, name="onevolt")
gmsh.model.addPhysicalGroup(1, [2, 4], 4, name="zeroflux")

# glvis can read mesh version 2.2
gmsh.option.setNumber("Mesh.MshFileVersion", 2.2)


# We can then generate a 2D mesh...
gmsh.model.mesh.generate(2)

#gmsh.option.setNumber("Mesh.MshFileVersion", 1)

# ... and save it to disk
gmsh.write("gmsh-1a.msh")

# start gmsh
if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

#before leaving.
gmsh.finalize()
