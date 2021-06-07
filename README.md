# Assessor

One common task in academia is bring together a group of people to assess some output.

This output might be submitted course work or conference paper submissions. 

Very often, this work requires meetings where marks are shared and calibrated. This package aims to facilitate this process.

It was first used in selecting the NeurIPS 2014 Program. Every day each area chair was given a list of papers via a google spreadsheet with the current status of the paper and information about where it was in the ranking of papers likely to be accepted. This helped area chairs ensure that papers in the 'grey area' were having enough discussion.

It was also used in marking and collatign the marks of the Machine Learning and Adaptive Intelligence course at the University of Sheffield in 2014, 2015 and 2016. 

It was originally contained in the `pods` package, but regular changes to Google APIs meant that it required more regular maintenance, so it's been separated out. The Google sheet access funcitonality has also been separated out into a python library called [`googoal`](https://github.com/lawrennd/googoal/) which acts as a wrapper to the authentication libraries and the `gdata` and `gspread` libraries.

The library needs authentication to access google spreadsheets and uses the Google Oauth capability to do this. 
