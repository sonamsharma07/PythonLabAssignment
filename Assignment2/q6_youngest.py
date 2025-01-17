ram_age = int(input("Enter the age of Ram: "))
shyam_age = int(input("Enter the age of Shyam: "))
ajay_age = int(input("Enter the age of Ajay: "))

if ram_age < shyam_age and ram_age < ajay_age:
    print("Ram is the youngest!")

elif shyam_age < ram_age and shyam_age < ajay_age:
    print("Shyam is the youngest!")

elif ajay_age < ram_age and ajay_age < shyam_age:
    print("Ajay is the youngest!")

elif ram_age == shyam_age and ram_age < ajay_age:
    print("Ram and Shyam are the youngest!")

elif ram_age == ajay_age and ram_age < shyam_age:
    print("Ram and Ajay are the youngest!")

elif shyam_age == ajay_age and shyam_age < ram_age:
    print("Shyam and Ajay are the youngest!")

else:
    print("All are of same age!")
