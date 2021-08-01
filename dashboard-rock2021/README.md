# Computing for bioinformatics Open Prescribing Dashboard

This repository contains the code for a dashboard displaying a data extract from the Open Prescribing dataset.

## Contributors
MSc module 'Computing for Bioinformatics' staff,
Jadene Lewis,
Helena Robinson,
Keith Graham,
Katherine Winfield,
Katie Williams.

## Dataset
More information is available about the dataset here:
https://digital.nhs.uk/data-and-information/areas-of-interest/prescribing/practice-level-prescribing-in-england-a-summary

A glossary of useful terms relating to the dataset is here:
https://digital.nhs.uk/data-and-information/areas-of-interest/prescribing/practice-level-prescribing-in-england-a-summary/practice-level-prescribing-glossary-of-terms

## Instructions to run the dashboard
In order to view the dashboard clone the repository to your machine and then run 'run.py'. Once running paste the following url into a browser http://127.0.0.1:5000/dashboard/home/

## About features
###### Menu
 Creatinine Clearance calculator:
  Input required - Patient sex, Patient age in years, Weight of patient (kg), Serum creatinine leavels in micromol/L
  Calculates CrCl according to the Cockcroft-Gault equation. The Cockcroft-Gault (CG) formula is provided on this website for research purposes only.
  Output - creatine clearance rate in 0 ml/minute


###### Tiles
  Total number of Items:
    Tile dispaly the total number of prescribed items across all primary care trust

  Average ACT cost:
    Tile dispalys the actual average cost per unit prescribed by dividing the total cost of all prescribed medication by the number of total prescription. 

  Top Prescribed Item:
    Tile displays the most routinely prescribed item across all primary care trusts as a percentage of the total items prescribed

  Number of Unique Item:
   Tile dispalys the total number of unquie items prescribed across all primary care trust
  
###### BarChart
  Prescribed items per Primary Care Trust (PCT) 
    Chart displays the total number f prescibed items per Primary care trust. Trust PCT code on the X axis, number of prescriptions on the Y
 
###### Progress bar graph 
  Infection treatment drug as % of all infection treatments
    Graph display the 4 types of infection treatment categories as a percentage of all infection treatment prescribed across all trusts

###### BNF data per PCT 
 Shows prescription data for each Primary Care Trust (PCT), for each drug (arranged by BNF code). This feature is still in development.


