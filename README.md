# Medical-Office-ABM
Program for the load of patients and diagnoses of a medical office

A doctor has decided to computerize his office, and for this task he needs two text files in CSV format: One to store patient data and another
to keep a record for each visit or query made.

patient file
· Medical history number
· Name and surname of the patient
· Prepaid or Social Work

query file
· Medical history number
· Diagnosis
Date (with YYYYMMDD format)

Grades:
· Both the Name field of the patient file and the Diagnosis field of the query file must be stored in UPPERCASE to avoid differences during the search.
· The Date field of the query file is stored in the format YYYYMMDD.
· When uploading a new patient, it must be verified that the Clinical Record No. is unique.
Otherwise, the patient's discharge will be rejected.
· When entering a consultation or visit, it must be verified that the patient exists.
· Neither of the two files is ordered.

The Practical Work consists of developing three programs:

1. and 2. Write TWO programs to load data into the files, i.e. one program
for each of them.

3. Write another program to perform searches as follows: The user enters the name of a patient (all or part) and a screen is displayed
List of patients that match the search performed. Of that
list a patient will be selected to display a list of all consultations
or visits that patient made, ordered by date. The list must include
as title the medical history number, the name of the patient and the prepaid
involved, and detailing the date and diagnosis of each consultation or visit. Remember that the file is not ordered and that the list must be.
These three programs must be managed from a central program that offers
a menu of options to launch any of them, in any order.
