""" The output of Pass 1 is:
1. Symbol Table SYBTAB: should be displayed on the screen.
2. LOCCTR, PRGLTH, PRGNAME, ...
3. Intermediate file (.mdt): Stored on the secondary storage. """

#open file to read it
sic_source_file = open("source.txt", "r")

#read  all input lines
sic_assembly = sic_source_file.readlines()

#initialize symbol table, program name, program length and locctr
symbol_table = []
prog_name = ""
prog_leng = 0
loc_ctr = 0

#create a .text files  
intermid_file = open("intermid.txt","w+")

#initialize a list of directives
directives = ["START", "END", "BYTE", "WORD", "RESB", "RESW", "BASE", "LTORG"]

for ind, line in enumerate(sic_assembly):
    #read first input line
    if ind == 0 and line[9:15].strip() == "START":
        name_prog = line[0:8].strip()
        
    if line[0] == '.':
        comm_cnt += 1

    #if this is not a comment line
    else:
        
        #list of opcodes
        opcod = line[9:15].strip()
        

        #list of operands
        #if len(line) >= 17:
    
        #list of comments
        #if len(line) >= 35:
            #comments.append(line[35:66].strip())

#close file
sic_source_file.close()

print("name of the program: ",name_prog)




