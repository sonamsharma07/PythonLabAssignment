distance_km = float(input("Enter the distance between two cities (in kilometers): "))

distance_centimeters = distance_km * 100000  
distance_inches = distance_km * 39370.1  
distance_feet = distance_km * 3280.84  
distance_meters = distance_km * 1000  

print(f"The distance in centimeters is: {distance_centimeters:.2f} cm")
print(f"The distance in inches is: {distance_inches:.2f} in")
print(f"The distance in feet is: {distance_feet:.2f} ft")
print(f"The distance in meters is: {distance_meters:.2f} m")
