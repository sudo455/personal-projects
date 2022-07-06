'''
Αντικειμενοστρεφής προγραμματισμός (Object-oriented programming - OOP)
Πρόκειται για είδος προγραμματισμού που περιστρέφεται γύρω από την έννοια της Κλάσης (Class), 
η οποία περιγράφει Αντικείμενα (Objects), τα οποία περιέχουν δεδομένα στη μορφή 
Ιδιοτήτων/Χαρακτηριστικών (Properties/Attributes) και κώδικα στη μορφή Μεθόδων (Methods).

Κάθε αντικείμενο αποτελεί ένα στιγμιότυπο (instance) ενός τύπου δεδομένων που δημιουργείται 
από μία κλάση (class).
'''

'''
Για την αναπαράσταση σύνθετων αντικειμένων, χρησιμοποιείται η εντολή class.

'''

class Dog :     # Παράδειγμα Δημιουργίας κλάσης
    pass

lucy = Dog()  # Παράδειγματα δημιουργίας στιγμιοτύπου (instances)
azor = Dog() # me lene...

lucy.name = 'lucy'      # Καθορισμός χαρακτηριστικών (Attributes) των στιγμιοτύπων
lucy.breed = 'boxer'    
lucy.age = 3
azor.name = 'azor'
azor.breed = 'bulldog'
azor.age= 1

print(lucy.name)
print(lucy.age)
print(azor.breed)
print(azor.age)


'''
Χαρακτηριστικά τα οποία είναι κοινά για όλα τα αντικείμενα
μιας συγκεκριμένης κλάσης δίνονται κατά τον ορισμό της
κλάσης:

Για να δώσουμε τις προκαθορισμένες τιμές στα χαρακτηριστικά
(attributes) ενός αντικειμένου κάποιας κλάσης, π.χ., ενός
αντικειμένου τύπου Cat, χρησιμοποιούμε τη μέθοδο  __init__().
Η __init__() καλείται αυτόματα κατά την κατασκευή
αντικειμένων μιας συγκεκριμένης κλάσης. 

'''

class Cat :     # Παράδειγμα Δημιουργίας κλάσης
    """ Create a cat from name, age and breed """
    # Ορίζουμε τα χαρακτηριστικά (attributes) 
   
      
    def __init__ (self, name, breed, age) :
       self.name =  name
       self.br = breed
       self.age = age
       self.home = 'Y'
          
    def description(self) :   # Παράδειγματα δημιουργίας μεθόδου
       return '{} is a {} years old {} cat.'.format(self.name, self.age, self.br)

    '''Μπορούμε να χρησιμοποιήσουμε μια μέθοδο για να αλλάξουμε την τιμή ενός χαρακτηριστικού'''
    def at_home (self):
        self.home = 'Y'
    
    def not_at_home (self) :
        self.home = 'N'
        
    
   
cat1 = Cat('Spitha', 'Aegean', 4)  # Δίνουμε τιμές στα χαρακτηριστικά για τη δημιουρίγα αντικειμένων
cat2 = Cat('Boying', 'Psipsina', 3)       


print(cat1)
print(cat1.name)  # Εκτύπωση χαρακτηριστικών των αντικειμένων: όνομα_αντικειμένου.χαρακτηριστικό
print(cat2.br)


print('{} is a {} years old {} cat'.format(cat1.name, cat1.age, cat1.br))  
print(cat1.description())      # Εκτύπωση με τη χρήση μέθοδου: όνομα_αντικειμένου.μέθοδος()
print(Cat.description(cat1))  # Εκτύπωση με το όνομα της κλάσης



cat1.not_at_home()

cat1.at_home()

cat2.not_at_home()

cat2.at_home()

print(cat1.home)

