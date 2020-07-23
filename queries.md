# Create a model called User following the ERD above

class Users(models.Model):
first_name = models.CharField(max_length=255)
last_name = models.CharField(max_length=255)
email_address = models.CharField(max_length=255)
age = models.IntegerField()

# Run the shell and import your User model

from users_app.models import Users

# Query: Create 3 new users

Users.objects.create(first_name="Carito", last_name="Da Silva", email_address="caritodasilva@gmail.com", age=37)
Users.objects.create(first_name="Linda", last_name="Hernandez", email_address="luciernaga201@hotmail.com", age=5)  
Users.objects.create(first_name="Mitzuro", last_name="Calzadilla", email_address="mitzuroelvenezolano@gmail.com", age=13)

# Query: Retrieve all the users

Users.objects.all().values()

# Query: Retrieve the last user

Users.objects.last()

# Query: Retrieve the first user

Users.objects.first()

# Query: Change the user with id=3 so their last name is Pancakes.

user_three = Users.objects.get(id=3)
user_three.last_name = "Pancakes"
user_three.save()

# Query: Delete the user with id=2 from the database

user_two = Users.objects.get(id=2)
user_two.delete()
Users.objects.all().order_by('-first_name').values()
