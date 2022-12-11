str = 'Hello people!' #γράφει το μήνημα αυτό στο τερματικό


list = [ 'abcdefg', 428 , 3.226, 'giannis', 0.365 ] 
tinylist = [359, 'spyros']
""" απλός πίνακας που μπορεί να έχει όλου του τύπου τών μεταβλητών που έχει η python"""
tinydict  =  {'name':  'omkar','code':5526, 
'oportunities': 'sales'}
""" python dictionary οπου το πρώτο στοιχείο του είναι το κλειδι και με την χρήση
της : διαχορίζεται στο δεύτερο στοιχείο που είναι η τιμή αυτού του κλειδιου"""

print (8+6) 
print ((33-12)*5) 
print  (7/2,  7/2.0,  7.0/2,  7.0/2.0,  7./2, 7/2., 7./2.)
print (9**2, 9**0.5)
""" εμφανίζει το αρθροισμα από τις παραπάνω πράξεις"""

a=4
b=-10 
c=50
diak=(b*b-4*a*c) 
print (diak)
"""βρίσκει την διακρίνουσα"""

def ifpy():
    # Filename: if.py 
 
    number = 55
    guess = int(input('Εισάγετε έναν ακέραιο αριθμό: ')) 
    
    if guess == number: 
        print('Συγχαρητήρια, τον μαντέψατε.') 
        print('(Αλλά δεν κερδίζετε και κανένα βραβείο!)') 
    
    elif guess < number: 
        print('Όχι, είναι λίγο μεγαλύτερος.') 
    
    else: 
        print('Όχι, είναι λίγο μικρότερος.') 
    
    print('Τέλος')
    """εδώ εαν βρεί ή δεν βρει με την βοηθεια της if
    το νούμερο θα εμφανίσει το κατάλιλο μήνημα"""
    
def whilepy():
    # Filename: while.py 
    number = 62
    running = True 
    while running: 
        guess = int(input('Εισάγετε έναν ακέραιο αριθμό: ')) 
    
        if guess == number: 
            print('Συγχαρητήρια, τον μαντέψατε.') 
            running = False # αυτό κάνει τον βρόχο while να σταματήσει εδώ 
        
        elif guess < number: 
            print('Όχι, είναι λίγο μεγαλύτερος.') 
        
        else: 
            print('Όχι, είναι λίγο μικρότερος.') 
        
        print('Ο βρόχος while τερματίστηκε.') 
        
    # Μπορείτε να προσθέσετε ότι άλλο θέλετε εδώ 
    print('Τέλος')
    """εδώ εαν βρεί το νούμερο θα τερματίσει ο βρόχος
    αλλιώς εαν δεν βρει το νούμερο θα συνεχήσει μέχρι ο χρήστης
    να βρεί το νούμερο και θα εμφανίσει το κατάλιλο μήνημα σε κάθε περίπτωση"""


def forpy():
    # Filename: for.py 
 
    for i in range(0, 100): 
        print(i) 
    
    else: 
        print('Ο βρόχος loop τερματίστηκε')
"""εδώ απλώς θα εμφανίσει τα νούμερα [0,99]"""

# Filename: function1.py 
def function1():
    def sayHello(): 
        print('Hello World!') # σύνολο εντολών που ανήκουν στη συνάρτηση 
    
        # Τέλος της συνάρτησης 
    sayHello() # κλήση της συνάρτησης 
    sayHello() # κλήση της συνάρτησης ξανά

# Filename: mymodule_demo.py 
def mymodule_demo():
    import mymodule # Προαιρετικά import * 
    mymodule.sayhi()
    print ('Version', mymodule.__version__)


ifpy()
whilepy()
forpy()
function1()
mymodule_demo()