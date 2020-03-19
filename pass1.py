""" The output of Pass 1 is:
1. Symbol Table SYBTAB: should be displayed on the screen.
2. LOCCTR, PRGLTH, PRGNAME, ...
3. Intermediate file (.mdt): Stored on the secondary storage. 
4.Your assembler can stop execution if there are errors in Pass 1"""

#open file to read it
sic_source_file = open("source.txt", "r")

#open file to read it
opcode_table_file = open("OPTAB.txt", "r")

#read  all input lines
sic_assembly = sic_source_file.readlines()

#read opcode table 
opcode_table = opcode_table_file.readlines()


#initialize symbol table, program name, program length and locctr
symbol_table = {}
opt_table = {}
prog_name = ""
prog_leng = 0
loc_ctr = 0
start_add = 0

#initialize instruction comp
label = ""
opcode = ""
operand = 0
comment = ""

#create a .text files  
intermid_file = open("intermid.txt","w+")

#initialize a list of directives
directives = ["START", "END", "BYTE", "WORD", "RESB", "RESW", "BASE", "LTORG"]

#store opcode table in 2D list
for ind, line in enumerate(opcode_table):
    #read file from third line 
    if ind>1:
        opt_table[line[0:11].strip()] = line[11:13].strip()

#read first input line
first_line = sic_assembly[0]
if first_line[9:15].strip() == "START":
    prog_name = first_line[0:8].strip()
    start_add =int(first_line[16:35].strip(), 16)
    loc_ctr = start_add
    intermid_file.write(str(hex(int(loc_ctr))) +" " +first_line)
else:
    loc_ctr = 0

for ind, line in enumerate(sic_assembly):
    #read opcode
    opcode = line[9:15].strip()
    if opcode != "END" and opcode != "START" and opcode != "BASE":
        #if this is not a comment line
        if line[0] != '.':
            #read label field
            label = line[0:8].strip()

            #if there is asymbol in label field
            if label != "":
                #serch SYMTAB for LABEL
                #if found
                if label in symbol_table:
                    #set error flag
                    print("ERROR, Duplicate symbol!")
                    break
                #else insert [label, LOCCTR] into SYMTAB
                else:
                    symbol_table[label] = hex(int(loc_ctr)).format(int(loc_ctr))

            #found is a boolean to  determine if opcode exist in opcode table
            found = 0

            loc_ctr = int(loc_ctr)
        
            #search OPTAB for OPCODE
            if opcode in opt_table:
                #if found
                found = 1

                #add 3 {instruction length} to LOCCTR
                loc_ctr += 3


            if found == 0 and opcode in directives:
                if opcode == "WORD":
                    #add 3 {instruction length}
                    loc_ctr += 3
                elif opcode == "RESW":
                    operand = line[16:35].strip()
                    loc_ctr += 3 * int(operand)
                elif opcode == "RESB":
                    operand = line[16:35].strip()
                    loc_ctr += int(operand)
                elif opcode == "BYTE":
                    operand = line[16:35].strip()
                    #find the length of constant in bytes and add it to loc_ctr
                    if operand[0] == 'X':
                        loc_ctr += (len(operand) - 3)/2;
                    elif operand[0] == 'C':
                        loc_ctr += (len(operand) - 3);
                elif opcode == "LTORG":
                    continue
                elif opcode[0:2] == '=X':
                    operand = line[16:35].strip()
                    loc_ctr += (len(operand) - 4)/2;
                elif opcode[0:2] == '=C':
                    operand = line[16:35].strip()
                    loc_ctr += (len(operand) - 4);
                else:
                    #set error flag
                    print("Invalid operation code")
                    break

    #write line to intermediate file 
    intermid_file.write(str(hex(int(loc_ctr)).format(int(loc_ctr)))+" "+line)


#save (loc_ctr - starting add ) as program length
prog_leng = int(loc_ctr) - int(start_add)


#close file
sic_source_file.close()
opcode_table_file.close()

print("name of the program: ",prog_name)
print("length of the program: ",hex(int(prog_leng)).format(int(prog_leng)))
print("LOCCTR: ",hex(int(loc_ctr)).format(int(loc_ctr)))
print("symbol table : ",symbol_table)