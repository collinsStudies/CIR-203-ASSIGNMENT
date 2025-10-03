# 1. Create a list of 10 delivery routes, each represented as a string.
deliveryRoutes = ["Kisumu road", "Siriba road", "Luanda road", "Nyerere road",
                 "Ahero road", "Nyando road", "Yala road", 
                 "Busia road", "Nairobi road", "Mbagathi road"]
# 2. Append a new route and remove a discontinued one.
deliveryRoutes.append("Jomo Kenyatta Highway")
deliveryRoutes.remove("Mbagathi road")
print(deliveryRoutes)
# 3.Sort the list alphabetically and reverse it
deliveryRoutes.sort()
deliveryRoutes.reverse()
print(deliveryRoutes)
# 4. Count how many routes start with the letter “N”
count = sum([1 for n in deliveryRoutes if n.startswith("N")])
print("Routes starting with letter N: ",count)
# 5. Use list comprehension to create a new list of routes longer than 10 characters
longRoutes = [r for r in deliveryRoutes if len(r) > 10]
print("Long routes: ",longRoutes)