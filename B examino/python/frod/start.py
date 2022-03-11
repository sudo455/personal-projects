'''
                             ΣΥΝΑΡΤΗΣΕΙΣ
Η έννοια των συναρτήσεων αποτελεί ένα από τα πιο σημαντικά δομικά στοιχεία
ενός προγράμματος σε όλες τις γλώσσες προγραμματισμού. Οι συναρτήσεις μπορεί να
είναι είτε έτοιμες από τη γλώσσα προγραμματισμού είτε να δημιουργούνται από εμάς.

Οι συναρτήσεις είναι επαναχρησιμοποιήσιμα μέρη προγραμμάτων. Μας επιτρέπουν να 
δίνουμε ένα όνομα σε ένα σύνολο εντολών και να το εκτελούμε καλώντας το όνομά τους, 
οπουδήποτε στο πρόγραμμα και όσες φορές θέλουμε. 
                        
Οι συναρτήσεις ορίζονται χρησιμοποιώντας τη χαρακτηριστική λέξη def, στη συνέχεια 
ακολουθεί ένα όνομα που ταυτοποιεί την εκάστοτε συνάρτηση και μετά προσθέτουμε ένα 
ζευγάρι παρενθέσεων που μπορούν να περικλείουν μερικά ονόματα παραμέτρων και η γραμμή 
τελειώνει με διπλή τελεία :

def myfunction():  # Ορισμός συνάρτησης (δεν είναι απαραίτητο να επιστρέφει τιμή)
    1η γραμμή εντολής
    2η γραμμή εντολής
    κλπ

Μια συνάρτηση μπορεί να δεχθεί παραμέτρους, οι οποίες χρησιμοποιούνται για
να δίνουμε διάφορες τιμές στη συνάρτηση, έτσι ώστε αυτή να παράγει κάποιο αποτέλεσμα
 ή να εκτελεί κάποιες ενέργειες χρησιμοποιώντας τις τιμές αυτές. 

Οι παράμετροι καθορίζονται μέσα στο ζευγάρι των παρενθέσεων στον ορισμό της
συνάρτησης και διαχωρίζονται με κόμμα. Όταν καλούμε τη συνάρτηση δίνουμε και τις 
τιμές με τον ίδιο τρόπο. Οι τιμές που δίνουμε όταν καλούμε τη συνάρτηση ονομάζονται
ορίσματα.
   
Για να επιστρέφει η συνάρτηση την τιμή κάποιας παραμέτρου χρειάζεται να το
 δηλώσουμε με τη εντολή return.
    
Η ακόλουθη συνάρτηση επιστρέφει την τιμή του μέγιστου τριών αριθμών :
'''
def maximum(num1, num2, num3) :
    if num1>=num2 and num1>=num3 :
        return num1
    elif num2>=num1 and num2>=num3 :
        return num2
    else :
        return num3

print(maximum(66,45,153))

'''
Η ακόλουθη συνάρτηση επιστρέφει την τιμή της απόστασης σε ευθύγραμμη επιταχυνόμενη
κίνηση σε χρόνο t, με αρχική ταχύτητα v0 και επιτάχυνηση γ.
'''
def y(v0, gamma, t):
    return v0*t + 0.5*gamma*t**2 


v0 = 10
gamma=10
time = 10
print(y(v0, gamma, time))

'''
Η ακόλουθη συνάρτηση επιστρέφει την οριζόντια και την κάθετη θέση σε χρόνο t κατά τη 
βολή ενός σώματος
'''

def xy(v0x, v0y, t):
    g = 9.81 # acceleration of gravity
    return v0x*t, v0y*t - 0.5*g*t**2

v_init_x = 5.0 # initial velocity in x
v_init_y = 10.0 # initial velocity in y
time = 1. # chosen point in time

x, y = xy(v_init_x, v_init_y, time)
print(xy(v_init_x, v_init_y, time))
print(x,y)

'''
Εφόσον ο χρόνος που ενδιαφερόμαστε είναι σταθερός π.χ. 2, η συνάρτηση μπορεί να
γραφτεί:
'''

def xy(v0x, v0y, t=2):
    g = 9.81 # acceleration of gravity
    return v0x*t, v0y*t - 0.5*g*t**2

v_init_x = 2.0 # initial velocity in x
v_init_y = 5.0 # initial velocity in y

x1, y1 = xy(v_init_x, v_init_y)
print(x1,y1)

'''
Με προκαθορισμένες τιμές για όλες τις παραμέτρους, η συνάρτηση π.χ. μπορεί να
γραφτεί:
'''

def xy(v0x=2.0, v0y=5.0, t=1):
    g = 9.81 # acceleration of gravity
    return v0x*t, v0y*t - 0.5*g*t**2

(x2, y2) = xy()

print(x2, y2)

'''
Οι παράμετροι των συναρτήσεων μπορούν να οριστούν και όπως τα παραδείγματα:
'''

def mynames(name1, name2, name3):
    print(name3)

mynames(name1 = "John", name2 = "Jim", name3 = "Jordan") 

mynames(name3 = "John", name2 = "Jim", name1 = "Jordan") 

mynames(name1 = "John", name3 = "Jim", name2 = "Jordan") 


'''
H παράμετρος μίας συνάρτησης μπορεί να είναι μία ακολουθία (λίστα/συμβολοσειρά κλπ):
'''
def my_function(names):
  for x in names:
    print(x)

x1 = ["John", "Jim", "Jordan"]
my_function(x1)

x2 = 'university'
my_function(x2)


'''
Όταν δεν γνωρίζουμε τον αριθμό των παραμέτρων χρησιμοποιούμε το *:
'''

def mynames(*names):
    print(names[2])

mynames('John', 'Jim', 'Jordan', 'George') 

mynames('John', 'Jordan', 'George') 



'''

Η συνάρτηση που μπορεί να γραφτεί σε μία γραμμή, μπορεί να γραφτεί ως συνάρτηση lambda   
Η συνάρτηση αυτή είναι μια ανώνυμη συνάρτηση  (Αγγλικά: anonymous function ή function literal ή lambda abstraction) είναι ένας ορισμός μιας συνάρτησης ή οποία περιέχει το σώματα της συνάρτησης αλλά δεν περιέχει όνομα (δηλαδή αναγνωριστικό). 
Οι ανώνυμες συναρτήσεις συνήθως:
περνιούνται ως παράμετροι σε συναρτήσεις ανώτερου βαθμού,
ή δημιουργούν ως αποτέλεσμα συναρτήσεις ανώτερου βαθμού που χρειάζεται να επιστρέψει μια συνάρτηση.              
'''
g = lambda x: x**2

print(g(3))

'''
που είναι ισοδύναμη με τη συνάρτηση:                  
'''

def g(x):
    return x**2

print(g(4))
'''
Παραδείγματα 
'''
def absolutevalue(x):  #επιστρέφει την απόλυτη τιμή ενός αριθμού
    if x<0 :
        return -x
    else:
        return x
print (absolutevalue(-5))

def add(x, y):
    return x+y
print(add(2, 3))
print('Hello','word')


def add2(x, y):
    print(x + y)

add2(3,7)
sum = add2(3,7)
print(sum)  #none σημαίνει ότι δεν θα επιστρέψει καμία τιμή

def add3(x,y):
    s = x + y
    return s

print(add3(3,7))
#print(s)     #προσοχή


'''
                    ΜΑΘΗΜΑΤΙΚΕΣ ΣΥΝΑΡΤΗΣΕΙΣ

Python παρέχει υλοποιήσεις πολλών μαθηματικών συναρτήσεων στη βιβλιοθήκη math. 
Για να χρησιμοποιήσουμε τις συναρτήσεις από τη βιβλιοθήκη αυτή πρέπει πρώτα να
ενημερώσουμε την Python με την εντολή import math. 
'''
import math
'''

Μπορούμε επίσης να συντομεύσουμε κάπως την κλήση των μαθηματικών συναρτήσεων 
γράφοντας:
'''
import math as m
'''

και καλώντας, για παράδειγμα, τη συνάρτηση τετραγωνική ρίζα ως
'''
z = m.sqrt(3.0)
print(z)

'''
H Python ορίζει τις μαθηματικές σταθερές math.pi, math.e

Παραδείγματα των γνωστότερων μαθηματικών συναρτήσεων :

math.floor(x). Ο μεγαλύτερος ακέραιος μικρότερος ή ίσος του x.

'''
#Παράδειγμα εφαρμογής των συναρτήσεων
import math
print(math.floor(1.4))
'''
math.ceil(x). Ο μικρότερος ακέραιος μεγαλύτερος ή ίσος του x.
math.trunc(x). Το ακέραιο μέρος του x.
math.sqrt(x). Η τετραγωνική ρίζα του x.
math.pow(x, y). Ο αριθμός x^y εναλλακτικά του τελεστή δύναμης **
math.exp(x). Ο αριθμός e^x.
math.log(x). Ο φυσικός λογάριθμός του x.
math.log10(x). Ο δεκαδικός λογάριθμος του x.
math.log2(x). Ο λογάριθμος του x με βάση το 2.
math.log(x, base). Ο λογάριθμος του x με βάση τον αριθμό base.

Οι τριγωνομέτρικές συναρτήσεις της Python είναι οι math.sin,  math.cos
και  math.tan, το όρισμα των οποίων είναι σε ακτίνια.

H Python παρέχει τις συναρτήσεις math.degrees(x) για
μετατροπή από ακτίνια σε μοίρες και math.radians(x) για
την αντίστροφη μετατροπή.

Οι αντίστροφες τριγωνομετρικές συναρτήσεις που ορίζονται
στη μαθηματική βιβλιοθήκη είναι οι  math.asin(x),  math.acos(x) και
 math.atan(x), οι οποίες επιστρέφουν γωνίες σε ακτίνια.
'''

'''
       ΕΝΣΩΜΑΤΩΜΕΝΕΣ ΣΥΝΑΡΤΗΣΕΙΣ (Built-in Functions) ΤΗΣ PYTHON
    
Η Python έχει ένα μεγάλο αριθμό ενσωματωμένων (εσωτερικών) συναρτήσεων και τύπων, 
οι οποίες είναι πάντοτε διαθέσιμες. Παρακάτω παρουσιάζονται με αλφαβητική σειρά: 

Ο τρόπος εφαρμογής τους με παραδείγματα περιγράφεται στην ιστοσελίδα:

https://docs.python.org/3/library/functions.html

abs()
all()
any()
ascii()
bin()
bool()
breakpoint()
bytearray()
bytes()
callable()
chr()
classmethod()
compile()
complex()
delattr()
dict()
dir()
divmod()
enumerate()
eval()
exec()
filter()
float()
format()
frozenset()
getattr()
globals()
hasattr()
hash()
help()
hex()
id()
input()
int()
isinstance()
issubclass()
iter()
len()
list()
locals()
map()
max()
memoryview()
min()
next()
object()
oct()
open()
ord()
pow()
print()
property()
range()
repr()
reversed()
round()
set()
setattr()
slice()
sorted()
staticmethod()
str()
sum()
super()
tuple()
type()
vars()
zip()
__import__()

'''

