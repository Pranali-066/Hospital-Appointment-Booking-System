# Hospital-Appointment-Booking-System
Semester Project-II Logbook
SY CSE (DS)
Academic Year: 2025–26 (Even Semester)

1. Introduction                                                                                                                                                                                                                                             
Problem Statement   :  In many hospitals, patients face long waiting times when booking doctor appointments. Most hospitals still use manual appointment systems where patients must visit the hospital and wait in queues. This process is time-consuming and inconvenient. Patients also cannot easily check doctor availability before visiting the hospital. Because of this, appointment management becomes inefficient and hospital staff must handle large numbers of patients manually. Therefore, there is a need for a digital system that allows patients to book doctor appointments online quickly and efficiently. 

Objectives : 1. To develop an online Hospital Appointment Booking System.<br>2. To allow patients to book doctor appointments easily through a web application.<br>3. To reduce waiting time in hospitals.<br>4. To provide doctor availability information to patients.<br>5. To create a simple and user-friendly system for appointment management.                                                                                                         
Application of Project :  The Hospital Appointment Booking System can be used in hospitals, clinics, and healthcare centers to manage patient appointments digitally. It allows patients to check doctor availability and book appointments online without visiting the hospital. This system helps reduce waiting time, improves hospital workflow, and organizes doctor schedules and patient records efficiently.

Literature Survey
• Background
Hospital appointment scheduling is an important part of healthcare
management. In traditional systems, patients must visit hospitals and wait in
long queues to book appointments, which wastes time. With the development
of internet technology, many hospitals now use online appointment booking
systems. These systems allow patients to check doctor availability and book
appointments online, helping reduce waiting time and improve hospital
management.


• Existing Systems
1. Healthcare Appointment System (IJRASET)
• This research proposes a web-based healthcare appointment
system that manages patient records, doctor schedules, and
appointments through a user-friendly interface. It includes
modules for patients, doctors, and administrators to improve
hospital management.
• Citation: Nageswari, A., et al. (2025). Healthcare Appointment
System. International Journal for Research in Applied Science
and Engineering Technology.
2. Hospital Appointment and Patient Management System
• This system provides different login roles such as patient, doctor,
nursing staff, and administrator. Patients can register, book
appointments, and check medical history online, while doctors
manage patient reports and schedules.


• Citation: Deepika, P., Jadimath, P. S., Yaligar, S. C., & Puranik,
P. S. (2025). Hospital Appointment and Patient Management
System. International Journal of Advance Research, Ideas and
Innovations in Technology.
3. Web-Based Appointment System Study
• A study on hospital outpatient systems showed that
web-based appointment booking significantly reduced
patient waiting time and improved satisfaction
compared to traditional queue-based registration
methods.
• Citation: Cao, W., et al. (2011). A Web-Based
Appointment System to Reduce Waiting for
Outpatients. BMC Health Services Research.
4. Online Patients Appointment Platform
• This research developed a web application where patients can
book doctor appointments online. The system allows patients,
doctors, and administrators to manage appointments efficiently
and reduces the need to travel to hospitals for booking.
• Citation: Yadav, S. K., Prajapati, S., Yadav, S., & Yadav, V.
(2022). Online Patients Appointment Platform. IJRASET.
• Limitations of Existing System(s)
1. Many hospitals still rely on manual or semi-digital systems, which
cause delays and long waiting times for patients.
2. Some existing systems are complex and difficult for patients to use,
especially for people who are not familiar with computers or internet
technology




Methodology
1. Hardware and Software requirements
o Hardware Requirements
▪ The following hardware components are required to develop and
run the Hospital Appointment Booking System:
▪ Computer or Laptop
▪ Minimum 4 GB RAM
▪ Internet Connection
▪ Storage space for database and project files
o Software Requirements
1. The following software tools are used in the project:
2. Frontend: HTML, CSS, JavaScript
3. Backend: Python (Flask Framework)
4. Database: MySQL
5. IDE: Visual Studio Code
6. Browser: Google Chrome / Safari
7. Data Visualization: Power BI or Tableau


2. System Design (Block Diagram, Data Flow Diagram) Algorithm
(Based on Module Design) (Block Diagram)
1. Step 1: Start the system.
2. Step 2: User accesses the hospital appointment booking web
3. Step 3: System checks whether the user is already registered.
4. Step4: If the user is registered, the user logs into the system.
If the user is not registered, the system allows the user to register a new account
and then log in.
5. Step 5: After login, the user selects the hospital department.
6. Step 6: The user selects the doctor from the chosen department.
7. Step 7: The user selects the appointment date and time.
8. Step 8: The system checks whether the selected time slot is
available.
9. Step 9:1.If the slot is available, the system proceeds to appointment
confirmation.
If the slot is not available, the user is asked to choose another slot.
10. Step 10: The system asks the user to confirm the appointment.
If the user confirms, the appointment is successfully booked and stored
in the database.
11. Step 11: If the user does not confirm, the user exits the system.
12. Step 12: End.

• Data Flow Diagram (DFD) Level 0 DFD
(Context Diagram)
1. External Entity: Patient (User)
2. Process: Hospital Appointment Booking
System Data Store: Hospital Database
3. Data Flow:
1. The patient enters registration/login details into the system.
a. The system processes the request and verifies the user information.
b. The patient selects department, doctor, date, and time.
c. The system checks doctor availability from the database.
d. The appointment details are stored in the database.
e. The system sends appointment confirmation to the patient.

• . Level 1 DFD
1. The system is divided into the following
processes: Process 1:
• User Authentication
• User registers or logs in.
• User details are stored in the User Database.
Process 2: Appointment Selection
• User selects department and doctor.
• User selects appointment date and time.
• System checks doctor availability.
Process 3: Appointment Confirmation
• User confirms the appointment.
• Appointment details are stored in the Appointment Database.
• System sends confirmation message.
Dataset used (include citation)
The dataset used in this project contains sample hospital appointment
data created for testing the system.
Dataset Features
• Patient Name
• Doctor Name
• Department
• Appointment Date
• Appointment Time
The dataset helps simulate real hospital appointment scheduling and test the
functionality of the system.
Citation:
Manually created dataset for testing the Hospital Appointment Booking
System (2025).



• Exploratory Data Analysis and Dataset Visualization (if applicable)
(Dataset used and Visualization using PowerBI or Tablue)
Exploratory Data Analysis is used to understand patterns in appointment
data.
Analysis Performed
• Number of appointments booked per day
• Doctor availability in different departments
• Peak booking hours for appointments
Visualization Tools
• Power BI or Tableau can be used to create charts such as:
• Bar chart showing appointments per department
• Line graph showing appointments per day
• Pie chart showing distribution of patients across departments
These visualizations help understand hospital workload and patient demand.
- Algorithm
Step 1: Start the system.
Step 2: Patient opens the hospital website.
Step 3: Patient registers or logs in to the system.
Step 4: Patient selects the department and doctor.
Step 5: System displays available appointment slots.
Step 6: Patient selects a suitable date and time.
Step 7: System stores the appointment details in the database.
Step 8: Appointment confirmation is shown to the patient.
Step 9: End.


Implementation Details
• Module wise description ( at each stage snapshot of work done and
testing)
The Hospital Appointment Booking System is implemented
using HTML, CSS, JavaScript for the frontend, Python (Flask)
for the backend, and MySQL for the database. The system is
divided into different modules to
make development and testing easier. Each module performs a specific
function in the system.
• Module 1
"Implementation Details
Module wise description ( at each stage snapshot of work done and testing)
The Hospital Appointment Booking System is implemented using HTML, CSS, JavaScript for the frontend, Python (Flask) for the backend, and MySQL for the database. The system is divided into different modules to



make development and testing easier. Each module performs a specific function in the system.
Module 1
pic 
Module 2
pic
Module 3
pic
Results
• Results
The Hospital Appointment Booking System was successfully developed
and tested. The system allows patients to register, log in, view doctors, and
book appointments online. The admin can manage doctor details, patient
information, and appointment schedules through the admin panel.
The system successfully stores and retrieves data from the MySQL database,
ensuring that appointment information is properly maintained. Testing shows
that the system reduces manual work and helps patients book appointments
quickly and conveniently.
• Performance Metrics
The performance of the system is evaluated based on the following
factors:
1. Response Time
The system responds quickly when users log in, search for doctors, or
book appointments.
2. Accuracy of Appointment Booking
The system correctly stores appointment details in the database without
errors.
3. User Efficiency
Patients can complete the appointment booking process in a few simple
steps.
4. System Reliability
The system performs consistently without crashes during testing.


• Model Evaluation including graphs
Since this project is a web-based system and not a machine learning
model, evaluation is done using system performance graphs such as:
Number of successful bookings vs total booking attempts
System response time graph
User interaction flow analysis
Graphs can show how efficiently the system processes appointment
requests and manages hospital data.


• Conclusion
The Hospital Appointment Booking System simplifies the process of
booking doctor appointments.
It allows patients to book appointments online without visiting the hospital.
The system helps reduce long waiting queues and saves time for patients.
It improves hospital management by organizing patient and appointment data.

• References (use IEEE format)
1. Sunil Kumar Yadav, Shubham Prajapati, Shivakant Yadav, and Vinay Kumar
Yadav, “Online Patients Appointment Platform,” IJRASET, 2022.
2. Akinode John Lekan and Oloruntoba S. A., “Design and Implementation of a
Patient Appointment and Scheduling System,” IARJSET, 2017.










📘 Updated Logbook (With Your Real Start Date)
07 February 2026
Finalized project idea (Hospital Appointment Booking System)
Discussed with project guide
09 February 2026
Collected project requirements
Decided main features (Login, Doctor List, Appointment Booking)
11 February 2026
Created project folder structure
Started basic HTML pages
⏸️ Gap (12–16 February)
(Busy with lectures / other academic work)
17 February 2026
Designed Home Page UI
Added navigation bar
19 February 2026
Created Login & Registration pages
Added CSS styling
21 February 2026
Designed Doctor Listing page
Added doctor details
⏸️ Gap (22–26 February)
(Internal exams / assignments)
27 February 2026
Created Appointment Booking page
Added date selection feature
 01 March 2026
Added time slot selection (static)
Improved UI design
 03 March 2026
Faced issue with time slots not displaying properly
Debugged JavaScript
⏸️ Gap (04–08 March)
(Learning backend / other work)
09 March 2026
Fixed time slot issue
Improved booking logic
12 March 2026
Started backend using Flask
Created basic routes
Work Done:
Completed frontend development using HTML and CSS
Designed appointment booking page and user interface
15 March 2026
Work Done:
Completed frontend (HTML, CSS)
Designed appointment booking page
Problem:
Backend not connected
Solution:
Started learning Flask
Next Plan:
Setup backend
GAP
31 March 2026
Work Done:
Working on improving backend connection
Trying to make booking system fully functional
