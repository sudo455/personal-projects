
'''
Εφαρμογή για την κατανόηση των instance variables (μοναδικές για κάθε στιγμιότυπο)
και class variables (ίδιες για όλα τα στιγμιότυπα της κλάσης)
'''


class Car :    
    
    annual_production_raise =1.1  # Παράδειγμα class variable που είναι σταθερή για όλη την κλάση
    
    def __init__ (self, model, color, annual_production) :
       self.model =  model
       self.color = color
       self.annual_production = annual_production
      
    def apply_raise(self) : 
        self.annual_production = int(self.annual_production * self.annual_production_raise)


model_1 = Car('Polo', 'Black', 50000)  
model_2 = Car('Golf', 'Red', 3000)       

model_1.annual_production_raise =1.20  # Αλλάζει μόνο την τιμή του production_raise για το model_1

print(Car.annual_production_raise)
print(model_1.annual_production_raise)  
print(model_2.annual_production_raise)

print(model_1.annual_production)
model_1.apply_raise()
print(model_1.annual_production)

model_2.apply_raise()
print(model_2.annual_production)
