x = 4 #creates int object with value 4, then variable x is assigned value of 4(points on that value in INT object)
print(f"x: value {x} at address {id(x)}")#4
y = 4#since value 4 is already exists in int object, y simply being assigned 4 and points on the same value that x
print(f"y: value {y} at address {id(y)}")#4
z = x#before assigning to z, right side computes(gets value of variable x), variable z points on the value that x points too
print(f"z: value {z} at address {id(z)}")#4
x = x + 10#right side computes 4 + 10, creates new INT object with value 14, which is assigning to x
print("after x = x + 10...")
print(f"x: value {x} at address {id(x)}")#14, address changed
print(f"y: value {y} at address {id(y)}")#no changes
print(f"z: value {z} at address {id(z)}")#no changes to z since values with type int are immutable
z = 42#new int object creates with value 42 and z points on that value, since value 4 is still existing. because y is pointing on it, it won't move to 'garbage collector' unless y-value changes
print("after z = 42...")
print(f"x: value {x} at address {id(x)}")#no changes
print(f"y: value {y} at address {id(y)}")#no changes
print(f"z: value {z} at address {id(z)}")#42, address changed
