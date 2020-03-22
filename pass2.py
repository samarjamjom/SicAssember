#pass2 outputs
#object code: 
#listingFile and object code

#open intermediate file to read it
intermid_file = open("intermid.txt","r")

#read  all input lines
intermediate_assembly = intermid_file.readlines()

#open listing file 
listing_file = open("listing.txt","+w")

#open object program file
object_prog_file = open("obj.txt","+w")

#read first input line {from intermediate file}
first_line = intermediate_assembly[0]
if first_line[18:24].strip() == "START":
    listing_file.write(first_line+"")
    prog_name = first_line[9:17]
    starting_add = first_line[0:5]
    prog_len = 12

header = []
header[0:1] = "H"
header[1:7] = prog_name
header [7:13] = starting_add

#write Header record to object program
object_prog_file.write(str(header))

#initialize first Text record 
for ind,line in enumerate(intermediate_assembly):
    if ind>0:
        #search OPTAB for opocode
        #if found
            #store value
            #if there is asymbol in operand field
                #if found
                    #store value
                #else
                    #error

                #else 


        #if not found
    
