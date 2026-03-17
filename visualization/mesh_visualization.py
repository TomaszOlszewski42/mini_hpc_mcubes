import pyvista as pv
import numpy as np

cube_triangles = [
    # PRZÓD
    [-1.0, -1.0,  1.0], [ 1.0, -1.0,  1.0], [ 1.0,  1.0,  1.0],
    [ 1.0,  1.0,  1.0], [-1.0,  1.0,  1.0], [-1.0, -1.0,  1.0],
    # TYŁ
    [-1.0, -1.0, -1.0], [-1.0,  1.0, -1.0], [ 1.0,  1.0, -1.0],
    [ 1.0,  1.0, -1.0], [ 1.0, -1.0, -1.0], [-1.0, -1.0, -1.0],
    # GÓRA
    [-1.0,  1.0,  1.0], [ 1.0,  1.0,  1.0], [ 1.0,  1.0, -1.0],
    [ 1.0,  1.0, -1.0], [-1.0,  1.0, -1.0], [-1.0,  1.0,  1.0],
    # DÓŁ
    [-1.0, -1.0,  1.0], [-1.0, -1.0, -1.0], [ 1.0, -1.0, -1.0],
    [ 1.0, -1.0, -1.0], [ 1.0, -1.0,  1.0], [-1.0, -1.0,  1.0],
    # PRAWA STRONA
    [ 1.0, -1.0,  1.0], [ 1.0, -1.0, -1.0], [ 1.0,  1.0, -1.0],
    [ 1.0,  1.0, -1.0], [ 1.0,  1.0,  1.0], [ 1.0, -1.0,  1.0],
    # LEWA STRONA
    [-1.0, -1.0,  1.0], [-1.0,  1.0,  1.0], [-1.0,  1.0, -1.0],
    [-1.0,  1.0, -1.0], [-1.0, -1.0, -1.0], [-1.0, -1.0,  1.0]
]

faces_help = np.arange(len(cube_triangles), dtype=int)
faces_help = faces_help.reshape(-1, 3)

faces = []

for face in faces_help:
    faces.append(np.concatenate(([3], face)))

mesh = pv.PolyData(cube_triangles, faces)

points = mesh.points
points_max = points.max(axis=0)
points_min = points.min(axis=0)
rgb_values = (points - points_min) / (points_max - points_min)

mesh.point_data['rgb'] = rgb_values
mesh.plot(scalars='rgb', rgb=True)