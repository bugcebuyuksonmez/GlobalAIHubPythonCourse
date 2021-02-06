

class Employees():
    def __init__(self, name, age, lang):
        self.name = name
        self.age = age
        self.lang= lang
        
    def print_lang(self):
        print(self.lang)
        
Serhat = Employees("Serhat",21,"Turkish")
Zeynep=Employees("Zeynep", 25, ("Turkish","English"))
Fatma= Employees("Fatma", 33, ("German","Turkish"))
Serdar=Employees("Serdar", 35, "English")

Serhat.print_lang()
Zeynep.print_lang()
Fatma.print_lang()
Serdar.print_lang()


class Managers():
    def __init__(self, name, age, lang):
        self.name = name
        self.age = age
        self.lang= lang
        
Ali=Managers("Ali", 45, ("Turkish","English"))
Melis=Managers("Melis", 43, ("Turkish"",""English"))
Jane= Managers("Jane", 52, ("English", "Italian"))
David=Managers("David", 53, ("English", "Spanish"))