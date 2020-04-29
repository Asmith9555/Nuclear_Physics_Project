This is the Project Folder for the Gamma-Gamma Coincidence Experiment done at
UNT under the University of Central Arkansas. The sub-folders and their contents
are as described below:

Directories:

-Data: This directory contians the raw data file (coincidence_data.csv) and all
       analysis files written in python. Running either file: "Overlapping_area_
       gauss_fit.py" or "coincidence_data_analysis.py" will save a png of the
       data (entailed in the file name) visualized in a plot.

-Dump: Contains a dump of spectrum data that was analysed to create the raw data
       file "coincidence_data.csv".

-Report: Contains the main tex file "final_report_main".tex", a directory filled
         with each subsection, and another directory titled "Figures" which hold
         pngs and jpgs of each figure included in the .tex file. There is also a
         .bib file which contains all of the citation information. In order to
         compile the .tex file run the following commands in the "Report"
         directory:

         $pdflatex final_report_main

         $biber final_report_main

         $pdflatex final_report_main

         $pdflatex final_report_main
