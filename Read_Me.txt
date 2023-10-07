Objective :
To create an OOP basic structure used to analysis the data (which is in JSON format, i.e. the 10 files) of the report cards belong to the different grades (classes) in a school. 

The Data Flow :
The overall data flow among the files :
            report_card.py  -->  school.py  -->  main.py
report_card.py: 
This file defines the base ReportCard class, which is foundational and doesn't depend on anything else.
school.py: 
This file imports the ReportCard class from report_card.py, signifying a dependency. The School class uses the ReportCard class to aggregate and analyze report cards.
main.py: 
This file is the entry point and imports the School class from school.py, indicating another layer of dependency. It orchestrates the process of loading and displaying report card data.

How to Run the Program ? 
First, clone the repository [ Using : git clone https://github.com/Soft-Artisan/School_Result_Analysis.git ] on your local machine, then
You can execute the program using “main.py”

Output :
Average Student Grade: 53.88
Hardest Subject: history
Easiest Subject: geography
Best Performing Grade: 4
Worst Performing Grade: 1
Best Student ID: 6
Worst Student ID: 7