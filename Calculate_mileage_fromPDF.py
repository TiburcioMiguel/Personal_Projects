#!/usr/bin/env python3

## This is to test out the idea I have for 
## automating the mileage sheet process for FCUSD
import sys
from PyPDF2 import PdfReader
## Creating the lists that contain the distance between 2 sites
distance_one = ["FHE", "SJG", 4.1]
distance_two = ["SJG", "EOE", 5.2]
distance_three = ["EOE", "BSE", 4]
distance_four = ["FHE", "EOE", 2]
distance_five = ["FHE", "BSE", 2.7]
distance_six =["FHE", "ESC", 6.7]
distance_seven = ["FHE", "SMS", 3.4]
distance_eight = ["FHE", "CSE", 3.5]
distance_nine = ["FHE", "NSE", 4.9]
distance_ten = ["FHE", "FHS", 4.8]
distance_eleven = ["FHE", "RRE", 4.2]
distance_twelve = ["FHE", "VDLHS", 3.7]
distance_thirteen = ["FHE", "FMS", 2.1]
distance_fourteen = ["FHE", "TJE", 2.9]
distance_fifteen = ["FHE", "MRE", 6.2]
distance_sixteen = ["FHE", "OCE", 2.5]
distance_seventeen = ["FHE", "GRE", 3.8]
distance_eighteen = ["SJG", "BSE", 2.6]
distance_nineteen = ["SJG", "MRE", 5.3]
distance_twenty = ["SJG", "OCE", 3.1]
distance_twentyone = ["SJG", "GRE", 2.5]
distance_twentytwo = ["SJG", "SMS", 2.4]
distance_twentythree = ["SJG", "CSE", 5]
distnace_twentyfour = ["SJG", "FHS", 0.8]
distance_twentyfive = ["SJG", "NSE", 2]
distance_twentysix = ["SJG", "VDLHS", 3.8]
distance_twentyseven = ["SJG", "RRE", 4.6]
distance_twentyeight = ["SJG", "FMS", 2.2]
distance_twentynine = ["SJG", "TJE", 2.5]
distance_thirty = ["SJG", "ESC", 3.2]
distance_thirtyone = ["EOE", "ESC", 8.6]
distance_thirtytwo = ["EOE", "MRE", 5.1]
distance_thirtythree = ["EOE", "OCE", 1.7]
distance_thirtyfour = ["EOE", "GRE", 3.3]
distance_thirtyfive = ["EOE", "SMS", 4.8]
distance_thirtysix = ["EOE", "CSE", 5]
distance_thirtyseven = ["EOE", "FHS", 5.8]
distance_thirtyeight = ["EOE", "NSE", 6.3]
distance_thirtynine = ["EOE", "VDLHS", 1.9]
distance_fourty = ["EOE", "RRE", 2.4]
distance_fortyone = ["EOE", "FMS", 3.5]
distance_fortytwo = ["EOE", "TJE", 4.8]
distance_fortythree = ["BSE","ESC", 5]
distance_fortyfour = ["BSE", "MRE", 5.7]
distance_fortyfive = ["BSE", "OCE", 2.5]
distance_fortysix = ["BSE", "GRE", 3.2]
distance_fortyseven = ["BSE", "SMS", 1.7]
distance_fortyeight = ["BSE", "CSE", 3.8]
distance_fortynine = ["BSE", "FHS", 3.2]
distance_fifty = ["BSE", "NSE", 3.2]
distance_fiftyone = ["BSE", "VDLHS", 4.1]
distance_fiftytwo = ["BSE", "RRE", 6.1]
distance_fiftythree = ["BSE", "FMS", 1.2]
distance_fiftyfour = ["BSE", "TJE", 1.2]
distance_fiftyfive = ["BSE", "FLHS", 2.7]
distance_fiftysix = ["MRE", "ESC", 7.5]
distance_fiftyseven = ["MRE", "OCE", 5.1]
distance_fiftyeight = ["MRE", "GRE", 3.8]
distance_fiftynine = ["MRE", "SMS", 5.8]
distance_sixty = ["MRE", "CSE", 9.7]
distance_sixtyone = ["MRE", "FHS", 4.7]
distance_sixtytwo = ["MRE", "FLHS", 5.4]
distance_sixtythree = ["MRE", "NSE", 7.5]
distance_sixtyfour = ["MRE", "VDLHS", 3.7]
distance_sixtyfive = ["MRE", "RRE", 3.9]
distance_sixtysix = ["MRE", "FMS", 5.3]
distance_sixtyseven = ["MRE", "TJE", 6]
distance_sixtyeight = ["OCE", "GRE", 2.6]
distance_sixtynine = ["OCE", "SMS", 3]
distance_seventy = ["OCE", "CSE", 5.9]
distance_seventyone = ["OCE", "FHS", 4]
distance_seventytwo = ["OCE", "FLHS", 3.5]
distance_seventythree = ["OCE", "NSE", 4.1]
distance_seventyfour = ["OCE", "VDLHS", 2.9]
distance_seventyfive = ["OCE", "RRE", 3.5]
distance_seventysix = ["OCE", "FMS", 1.5]
distance_seventyseven = ["OCE", "TJE", 2.9]
distance_seventyeight = ["GRE", "SMS", 3]
distance_seventynine = ["GRE", "CSE", 5.9]
distance_eighty = ["GRE", "FHS", 4.2]
distance_eightyone = ["GRE", "FLHS", 3.5]
distance_eightytwo = ["GRE", "NSE", 4.3]
distance_eightythree = ["GRE", "VDLHS", 2.9]
distance_eightyfour = ["GRE", "RRE", 3.9]
distance_eightyfive = ["GRE", "FMS", 1.5]
distance_eightysix = ["GRE", "TJE", 2.9]
distance_eightyseven = ["SMS", "CSE", 5.9]
distance_eightyeight = ["SMS", "FHS", 4]
distance_eightynine = ["SMS", "FLHS", 3.5]
distance_ninety = ["SMS", "NSE", 4.3]
distance_ninetyone = ["SMS", "VDLHS", 2.9]
distance_ninetytwo = ["SMS", "RRE", 3.9]
distance_ninetythree = ["SMS", "FMS", 1.5]
distance_ninetyfour = ["SMS", "TJE", 2.9]
distance_ninetyfive = ["CSE", "FHS", 4.2]
distance_ninetysix = ["CSE", "FLHS", 3.5]
distance_ninetyseven = ["CSE", "NSE", 4.4]
distance_ninetyeight = ["CSE", "VDLHS", 2.9]
distance_ninetynine = ["CSE", "RRE", 3.9]
distance_hundred = ["CSE", "FMS", 1.5]
distance_hundredone = ["CSE", "TJE", 2.9]
distance_hundredtwo = ["OCE", "ESC", 6.1]
distance_hundredthree = ["GRE", "ESC", 5.9]
distance_hundredfour = ["SMS", "ESC", 5.1]
distance_hundredfive = ["CSE", "ESC", 5.6]
distance_hundredsix = ["FHS", "ESC", 3.1]
distance_hundredseven = ["FHS", "FLHS", 1]
distance_hundredeight = ["FHS", "NSE", 1.8]
distance_hundrednine = ["FHS", "VDLHS", 3.7]
distance_hundredten = ["FHS", "RRE", 4.7]
distance_hundredeleven = ["FHS", "FMS", 2.8]
distance_hundredtwelve = ["FHS", "TJE", 2.7]
distance_hundredthirteen = ["NSE", "ESC", 3.1]
distance_hundredfourteen = ["NSE", "VDLHS", 3.7]
distance_hundredfifteen = ["NSE", "RRE", 4.9]
distance_hundredsixteen = ["NSE", "FMS", 2.8]
distance_hundredseventeen = ["NSE", "TJE", 2.7]
distance_hundredeighteen = ["VDLHS", "ESC", 3.1]
distance_hundrednineteen = ["VDLHS", "RRE", 4.9]
distance_hundredtwenty = ["VDLHS", "FMS", 2.8]
distance_hundredtwentyone = ["VDLHS", "TJE", 2.7]
distance_hundredtwentytwo = ["RRE", "ESC", 7.4]
distance_hundredtwentythree = ["RRE", "FMS", 4.8]
distance_hundredtwentyfour = ["RRE", "TJE", 6.5]
distance_hundredtwentyfive = ["FMS", "ESC", 5.5]
distance_hundredtwentysix = ["FMS", "TJE", 1.6]
distance_hundredtwentyseven = ["TJE", "ESC", 4.3]

list_of_distances = [
    distance_one,
    distance_two,
    distance_three,
    distance_four,
    distance_five,
    distance_six,
    distance_seven,
    distance_eight,
    distance_nine,
    distance_ten,
    distance_eleven,
    distance_twelve,
    distance_thirteen,
    distance_fourteen,
    distance_fifteen,
    distance_sixteen,
    distance_seventeen,
    distance_eighteen,
    distance_nineteen,
    distance_twenty,
    distance_twentyone,
    distance_twentytwo,
    distance_twentythree,
    distnace_twentyfour,
    distance_twentyfive,
    distance_twentysix,
    distance_twentyseven,
    distance_twentyeight,
    distance_twentynine,
    distance_thirty,
    distance_thirtyone,
    distance_thirtytwo,
    distance_thirtythree,
    distance_thirtyfour,
    distance_thirtyfive,
    distance_thirtysix,
    distance_thirtyseven,
    distance_thirtyeight,
    distance_thirtynine,
    distance_fourty,
    distance_fortyone,
    distance_fortytwo,
    distance_fortythree,
    distance_fortyfour,
    distance_fortyfive,
    distance_fortysix,
    distance_fortyseven,
    distance_fortyeight,
    distance_fortynine,
    distance_fifty,
    distance_fiftyone,
    distance_fiftytwo,
    distance_fiftythree,
    distance_fiftyfour,
    distance_fiftyfive,
    distance_fiftysix,
    distance_fiftyseven,
    distance_fiftyeight,
    distance_fiftynine,
    distance_sixty,
    distance_sixtyone,
    distance_sixtytwo,
    distance_sixtythree,
    distance_sixtyfour,
    distance_sixtyfive,
    distance_sixtysix,
    distance_sixtyeight,
    distance_sixtynine,
    distance_seventy,
    distance_seventyone,
    distance_seventytwo,
    distance_seventythree,
    distance_seventyfour,
    distance_seventyfive,
    distance_seventysix,
    distance_seventyseven,
    distance_seventyeight,
    distance_seventynine,
    distance_eighty,
    distance_eightyone,
    distance_eightytwo,
    distance_seventythree,
    distance_seventyfour,
    distance_seventyfive,
    distance_seventysix,
    distance_seventyseven,
    distance_seventyeight,
    distance_seventynine,
    distance_eighty,
    distance_eightyone,
    distance_eightytwo,
    distance_eightythree,
    distance_eightyfour,
    distance_eightyfive,
    distance_eightysix,
    distance_eightyseven,
    distance_eightyeight,
    distance_eightynine,
    distance_ninety,
    distance_ninetyone,
    distance_ninetytwo,
    distance_ninetythree,
    distance_ninetyfour,
    distance_ninetyfive,
    distance_ninetysix,
    distance_ninetyseven,
    distance_ninetyeight,
    distance_ninetynine,
    distance_hundred,
    distance_hundredone,
    distance_hundredtwo,
    distance_hundredthree,
    distance_hundredfour,
    distance_hundredfive,
    distance_hundredsix,
    distance_hundredseven,
    distance_hundredeight,
    distance_hundrednine,
    distance_hundredten,
    distance_hundredeleven,
    distance_hundredtwelve,
    distance_hundredthirteen,
    distance_hundredfourteen,
    distance_hundredfifteen,
    distance_hundredsixteen,
    distance_hundredseventeen,
    distance_hundredeighteen,
    distance_hundrednineteen,
    distance_hundredtwenty,
    distance_hundredtwentyone,
    distance_hundredtwentytwo,
    distance_hundredtwentythree,
    distance_hundredtwentyfour,
    distance_hundredtwentyfive,
    distance_hundredtwentysix,
    distance_hundredtwentyseven
]



## Extract data from PDF
def pdf_extract():
    mileage_pdf = sys.argv[1]
    pdf_reader = PdfReader(open(mileage_pdf, "rb"))

    dict_of_all_fields = pdf_reader.get_form_text_fields() 

    ## Create a while loop that will create a  string name for all 26 rows of "STOPS MADE"
    ## after name is created, it will increment the counter c by 1, and return the value 
    ## for that field fuck yeah B)

    total_distance = []
    first_travel = []
    c = 1
    while c < 27:
        ## Get the keys for the value of the "first site" and for the first "travel"
        temp_name = str("STOPS MADERow"+str(c))
        temp_namee = str("FROM FIRST PLACE OF WORKRow"+str(c))
        my_field_value = (dict_of_all_fields[temp_name])
        field_value = (dict_of_all_fields[temp_namee])
        ## Now I want to take that str value and turn it into a list that 
        ## can be used with a different loop I have
        if field_value is None and my_field_value is None:
            print("Row "+str(c)+" total miles:    0")
        else:
            real_list = my_field_value.split(", ")
            first_travel.append(field_value)
            first_travel.append(real_list[0])
            ## Loop to check the distance from start site to first travel site
            for z in list_of_distances:

                if first_travel[0] in z:

                    if first_travel[1] in z:

                        total_distance.append(z[2])
            

            ## List comprehension to get the pair of sites
            list_of_pairs = [[real_list[i], real_list[i + 1]] for i in range(len(real_list) - 1)]
            
            ## Loop to check the distance to all the travel sites
            for x in list_of_pairs:
                
                for y in list_of_distances:

                    if x[0] in y:

                        if x[1] in y:

                            total_distance.append(y[2])
            ## if statement purely for cosmetic purposes, if the counter c <10, it
            ## will print with 5 'spaces' after "total miles:" and if it is >9, it
            ## will print with 4 'spaces' after "total miles:"
            if c < 10:

                print("Row "+str(c)+" total miles:     "+str(round(sum(total_distance), 2)))

            else: 

                print("Row "+str(c)+" total miles:    "+str(round(sum(total_distance), 2)))


        ## Have to clear the contents of the lists before
        ## the next iteration                    
        first_travel.clear()        
        total_distance.clear()
        c += 1
    if c >= 27:
        print("Congratulations!! You just saved 15 minutes!! Go take a break now ;)")
    return ""
    

print(pdf_extract())
