--Create 3 new Dojos

Dojo.objects.create(name="Dojo 1", city= "City A", state= "State B")
Dojo.objects.create(name="Dojo 2", city= "City B", state= "State c")
Dojo.objects.create(name="Dojo 3", city= "City C", state= "State D")

--Delete the 3 Dojos

Dojo.object.all.delete()

--Create 3 more dojos
Dojo.objects.create(name="Dojo Alpha", city= "City X", state= "State X")
Dojo.objects.create(name="Dojo Beta", city= "City Y", state= "State Y")
Dojo.objects.create(name="Dojo Gamma", city= "City Z", state= "State Z")

--Create 3 ninjas that belong to the first dojo

Ninja.objects.create(first_name="Ninja1", last_name="One", dojo=dojo1)
Ninja.objects.create(first_name="Ninja2", last_name="Two", dojo=dojo1)
Ninja.objects.create(first_name="Ninja3", last_name="Three", dojo=dojo1)

--Create 3 ninjas that belong to the second dojo

Ninja.objects.create(first_name="Ninja4", last_name="Four", dojo=dojo2)
Ninja.object.create(first_name="Ninja5", last_name="Five", dojo=dojo2)
Ninja.object.create(first_name="Ninja6", last_name="Six", dojo=dojo2)

--Create 3 ninjas that belong to the third dojo
Ninja.objects.create(first_name="Ninja7", last_name="Seven", dojo=dojo3)
Ninja.objects.create(first_name="Ninja8", last_name="Eight", dojo=dojo3)
Ninja.objects.create(first_name="Ninja9", last_name="Nine", dojo=dojo3)

--Retrieve all the ninjas from the first dojo
dojo1.ninja.set_all()

--Retrieve all the ninjas from the last dojo
dojo3.ninja_set.all

--Retrieve the last ninja's dojo
Ninja.objects.last().dojo