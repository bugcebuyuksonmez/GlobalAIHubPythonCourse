

class Animals:

  def __init__(self, name, color, age):
    self.animal_name=name
    self.animal_color=color
    self.animal_age= age

  def print_name(self):
    print("Animal's name is: ", self.animal_name)

  def print_color(self):
    print("It's skin color is: ", self.animal_color)
 
  def print_age(self):
    print(self.animal_name,"is ", self.animal_age, "years old. ")
    
class Dogs(Animals):
  def __init__(self, dog_breeds):
    self.dog_breeds = dog_breeds
  
  def print_dog_breeds(self):
    print("The breed of the dog is:", self.dog_breeds)

dog = Dogs("Bulldog")
dog.animal_name = "Ghost"
dog.animal_color = "White"
dog.animal_age ="2"

dog.print_name()
dog.print_color()
dog.print_age()
dog.print_dog_breeds()

class Cats(Animals):
  def __init__(self, cat_breeds):
    self.cat_breeds = cat_breeds
  
  def print_cat_breeds(self):
    print("The breeds of the cat is:", self.cat_breeds)

cat = Cats("Scottish Fold")
cat.animal_name = "Luna"
cat.animal_color = "Black"
cat.animal_age ="4"

cat.print_name()
cat.print_color()
cat.print_age()
cat.print_cat_breeds()