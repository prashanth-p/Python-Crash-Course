from restaurant import Restaurant

myResta = Restaurant("Honey on the beach", "Tandoor")

# myResta.cuisine_type
myResta.set_number_served(25)
myResta.inc_number_served(25)
print(myResta.number_served)
myResta.open_restaurant()
print()
myResta.descirbe_restaurant()
