from Graphics import circle,rectangle
from Graphics.ThreeD_graphics import sphere,cuboid
c_radius=int(input("Enter radius of circle:"))
circle.area(c_radius)
circle.perimeter(c_radius)
print()
rect_l=int(input("Enter length of rectangle:"))
rect_b=int(input("Enter breadth of rectangle:"))
rectangle.area(rect_l,rect_b)
rectangle.perimeter(rect_l,rect_b)
print()
s_radius=int(input("Enter radius of Sphere:"))
sphere.area(s_radius)
sphere.perimeter(s_radius)
print()
c_l=int(input("Enter length of cube:"))
c_b=int(input("Enter breadth of cube:"))
c_h=int(input("Enter height of cube:"))
cuboid.area(c_l,c_b,c_h)
cuboid.perimeter(c_l,c_b,c_h)
