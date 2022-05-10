
'''
                         Σύνολα (Sets)

Ta set είναι αταξινόμητες δομές δεδομένων που μπορούν περιέχουν στοιχεία από διάφορους τύπους δεδομένων.
Δεν επιτρέπεται να υπάρχουν δύο ίδια στοιχεία μέσα στο set.
Δεν μπόρούμε να τεμαχίσουμε ή να πρσπελάσουμε ένα set με χρήση δεικτών όπως π.χ. στις λίστες.
'''

myset = {'John', 'Jim', 'George', 'Jack', 15, True}
print(myset) 


myset = {'John', 'John', 'Jim', 'George', 'Jack', 'John'}
print(myset) #Τα στοιχεία που υπάρχουν πάνω από μία φορά εμφανίζονται στη εκτύπωση μία φορά

print(len(myset)) # Δίνει τον αριθμό των στοιχείων του συνόλου. Εφόσον υπάρχουν ίδια στοιχεία προσμετρώνται μία φορά.

myset= set(('a', 'b', 'c')) # Παράδειγμα δημιουργίας συνόλου με την εντολή set
print(myset) 
myset= set(['a', 'b', 'c']) # Παράδειγμα δημιουργίας συνόλου με την εντολή set
print(myset) 


#Μπορούμε να προσπελάσουμε τα στοιχεία ενός set με χρήση του for loop, 
myset = {'John', 'Jim', 'George', 'Jack'}

for x in myset:
    print(x) 

# Έλεγχος αν ένα στοιχείο βρίσκεται στο set
print('Jim' in myset) 


#Μπορούμε να προσθέσουμε ένα στοιχείο με την εντολή add
myset = {'John', 'Jim', 'George', 'Jack'}
myset.add('Jordan')
print(myset) 

# Παράδειγμα εισαγωγής ενός set σε ένα άλλο με την εντολή update
s1 = {'John', 'Jim', 'George', 'Jack'}
s2 = {'Mary', 'Helena'}

s1.update(s2)
print(s1) 

# Παράδειγμα δημιουργίας ενός νέου set με στοιχεία από δύο αρχικά set με την εντολή union
s1 = {'John', 'Jim', 'George', 'Jack'}
s2 = {'Mary', 'Helena'}

s3 = s1.union(s2)
print(s3) 

# Οι εντολές update & union έχουν πρακτικά την ίδια χρήση. Προσοχή όμως στην σύνταξη κάθε περίπτωσης!!!


# Mπορούμε να συνεννώσουμε τα στοιχεία μίας ακολουθίας (λίστας, πλειάδας, συμβολοσειράς) σε ένα set
s1 =  {'a', 'b', 'c'}
mylist = [1,2,3]

s1.update(mylist)
print(s1) 

snew = s1.union(mylist)
print(snew) 


s1 =  {'a', 'b', 'c'}
mystring = 'red'

s1.update(mystring)
print(s1) 

snew = s1.union(mystring)
print(snew) 



# Μπορούμε να αφαιρέσουμε ένα στοιχείο του set με την εντολή discard()
s = {'John', 'Jim', 'George', 'Jack'}
s.discard('Jim')
print(s) 

# Μπορούμε εναλλακτικά να χρησιμοποιήσουμε την εντολή remove, όμως προκύπτει σφάλμα αν δεν υπάρχει το στοιχείο που θέλουμε

# Η εντολή pop απομακρύνει ένα από τα στοιχεία του set.

s = {'John', 'Jim', 'George', 'Jack'}
s.pop()
print(s) 

# H εντολή clear() αδειάζει τα στοιχεία του set:

s = {'John', 'Jim', 'George', 'Jack'}
s.clear()#clear aka skoupa...
print(s) 

# H εντολή intersection() δίνει ένα νέο set που περιέχει μόνο τα κοινά στοιχεία από δύο set

s1 = {'John', 'Jim', 'George', 'Jack'}
s2 = {'Mary', 'Helena', 'Jim'}

s3 = s1.intersection(s2) #ta koina

print(s3) 


# Η εντολή intersection_update() κρατάει σε ένα set μόνο τα στοιχεία που είναι κοινά με ένα άλλο set.

s1 = {'John', 'Jim', 'George', 'Jack'}
s2 = {'Mary', 'Helena', 'Jim'}

s1.intersection_update(s2)

print(s1) #same HOWEVER....


# H εντολή isymmetric_difference() δίνει ένα νέο set που περιέχει μόνο τα όχι κοινά στοιχεία από δύο set

s1 = {'John', 'Jim', 'George', 'Jack'}
s2 = {'Mary', 'Helena', 'Jim'}

s3 = s1.symmetric_difference(s2)
print(s3) 


# Η εντολή symmetric_difference_update() κρατάει σε ένα set μόνο τα στοιχεία που δεν είναι κοινά με ένα άλλο set.

s1 = {'John', 'Jim', 'George', 'Jack'}
s2 = {'Mary', 'Helena', 'Jim'}

s1.symmetric_difference_update(s2)

print(s1)