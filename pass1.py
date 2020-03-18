""" The output of Pass 1 is:
1. Symbol Table SYBTAB: should be displayed on the screen.
2. LOCCTR, PRGLTH, PRGNAME, ...
3. Intermediate file (.mdt): Stored on the secondary storage. """

#open file to read it
sic_source_file = open("source.txt", "r")

#read  all input lines
sic_assembly = sic_source_file.readlines()

#initialize symbol table, program name, program length and locctr
symbol_table = [["label1", 1], ["label2",2]]
opt_table = []
prog_name = ""
prog_leng = 0
loc_ctr 

#initialize instruction comp
label
opcode
operand
comment

#create a .text files  
intermid_file = open("intermid.txt","w+")

#initialize a list of directives
directives = ["START", "END", "BYTE", "WORD", "RESB", "RESW", "BASE", "LTORG"]


for ind, line in enumerate(sic_assembly):
    #read first input line
    if ind == 0 and line[9:15].strip() == "START":
        prog_name = line[0:8].strip()
        loc_ctr = line[9:15].strip()
        intermid_file.write(loc_ctr+" "+line)
    else:
        loc_ctr = 0

    #if this is not a comment line
    if line[0] != '.':

        #read label field
        label = line[0:8]
        #if there is asymbol in label field
        if label != "":
            #serch SYMTAB for LABEL
            for j in len(symbol_table):
                #if found
                if symbol_table[j][0]==label:
                    #set error flag
                    print("ERROR, Duplicate symbol!")
                    break
            #insert [label, LOCCTR] into SYMTAB
            symbol_table.append([label,loc_ctr])

        #read opcode
        found = 0
        opcode = line[9:15].strip()
        #search OPTAB for OPCODE
        for j in len(opt_table):
            #if found
            if opt_table[j]==opcode:
                found = 1
                #add 3 {instruction length} to LOCCTR
                loc_ctr += 3
            if found = 0:
                if opcode == "WORD":
                    loc_ctr += 3
                elif opcode == "RESW":
                    operand = int(line[17:35].strip())
                    loc_ctr += 3*operand



    




        #list of operands
        #if len(line) >= 17:
    
        #list of comments
        #if len(line) >= 35:
            #comments.append(line[35:66].strip())

#close file
sic_source_file.close()

print("name of the program: ",name_prog)




