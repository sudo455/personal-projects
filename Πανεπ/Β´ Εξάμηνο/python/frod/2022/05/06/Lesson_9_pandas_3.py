'''
ΔΙΑΧΕΙΡΙΣΗ ΑΡΧΕΙΩΝ ΣΤΗ ΒΙΒΛΙΟΘΗΚΗ pandas

'''



import pandas as pd

import os  # Μας επιτρέπει να μπορούμε να ορίσουμε τη διαδρομή του φακέλου που βρίσκεται το αρχειο μας


path ='C:/Users/despo_000/Desktop' # ορίζουμε τη διαδρομή

'''
ΠΡΟΣΟΧΗ: Οι φάκελοι πρέπει να διαχωρίζονται μεταξύ τους με / και ΟΧΙ \.

'''


filename= 'WHO_COVID_19_2021_01_10.csv' # Δίνουμε το όνομα του αρχείου που θέλουμε να ανοίξουμε
fullpath = os.path.join(path,filename)
data = pd.read_csv(fullpath)
print(data)


print(data.columns.values)
print(data.head(10))
print(data.shape)

print(data.loc[:,['Name', 'WHO Region','Transmission Classification']])