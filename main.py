import file_name_constants

#########################################
# Global Variables ######################
#########################################

# These variables need to be changed to run different test. Refer to the constants file for the names
input_file_name = file_name_constants.STATIC_TEST_IN
output_file_name = file_name_constants.STATIC_TEST_OUT

# Used later for writing jumps in our asm code so that they don't repeat
asm_jump_counter = 0

# A list of all the arithmetic functions to make them easy to reference
arithmetic_function_list = ["add", "sub", "neg", "eq", "lt", "gt", "and", "or", "not"]

#########################################
# Main Running Area #####################
#########################################

# TODO: get StaticTest.vm to work. The big thing for it is getting the "static" pointer to work
def vm_to_asm():
	global input_file_name
	input_file = open(input_file_name, "r")
	raw_file_line_list = get_file_lines_as_list(input_file)
	cleaned_vm_line_list = clean_line_list(raw_file_line_list)
	hack_line_list = convert_vm_to_hack(cleaned_vm_line_list)
	write_hack_to_file(hack_line_list)


#########################################
# Cleanup and Convert Functions #########
#########################################


def get_file_lines_as_list(input_file):
	return input_file.readlines()


def clean_line_list(input_line_list):
	result_line_list = []
	for line in input_line_list:
		# removes any spaces and instances of spaces, \n, \r, and \t
		temp_line = line
		temp_line = temp_line.replace("\n", "")
		temp_line = temp_line.replace("\r", "")
		temp_line = temp_line.replace("\t", "")

		# removes any comments from a line if they exist
		if "//" in temp_line:
			temp_line = temp_line[:temp_line.index("//")]

		# clears any starting and ending spaces
		temp_line.strip()

		# turns any spaces longer than 1 space into 1 space
		while "  " in temp_line:
			temp_line.replace("  ", " ")

		# ignores the line if there is no actual code on it
		if temp_line != "":
			result_line_list.append(temp_line)
	return result_line_list


def convert_vm_to_hack(input_line_list):
	result_line_list = []

	for line in input_line_list:
		line_command_type = get_command_type(line)
		result_line = convert_line_to_hack(line, line_command_type)
		result_line_list.append(result_line)

	return result_line_list


def get_command_type(input_line):
	if input_line in arithmetic_function_list:
		return "C_ARITHMETIC"
	elif "push" in input_line:
		return "C_PUSH"
	elif "pop" in input_line:
		return "C_POP"
	elif "label" in input_line:
		return "C_GOTO"
	elif "if" in input_line:
		return "C_IF"
	elif "function" in input_line:
		return "C_FUNCTION"
	elif "return" in input_line:
		return "C_RETURN"
	elif "call" in input_line:
		return "C_CALL"
	else:
		print("ERROR: Command type not specified")
		return "C_ERROR"


def convert_line_to_hack(input_line, command_type):
	if command_type == "C_ARITHMETIC":
		return write_arithmetic(input_line)
	elif command_type == "C_PUSH" or command_type == "C_POP":
		return write_push_pop(input_line, command_type)
	elif command_type == "C_LABEL":
		return
	elif command_type == "C_GOTO":
		return
	elif command_type == "C_IF":
		return
	elif command_type == "C_FUNCTION":
		return
	elif command_type == "C_RETURN":
		return
	elif command_type == "C_CALL":
		return
	else:
		return "ERROR: Command not specified?"


# Arithmetic Code #######################


def write_arithmetic(input_line):
	result_string = ""
	# The first line of each if statement describes what the result of the operation should look like
	# y = M(@SP) - 1, and x = M(@SP) - 2
	if "add" in input_line:
		# x + y

		# Get the location the stack pointer is pointing
		result_string += "@" + pointer_type_to_ram_address("SP") + "\n"

		# Change the value of the stack pointer down one to where it should be after the computation
		result_string += "M=M-1" + "\n"

		# Move to where the stack pointer points to and store the value of the register at that point
		result_string += "A=M" + "\n"
		result_string += "D=M" + "\n"

		# Move to the point before the previous value, add the two together, and store the result there
		result_string += "A=A-1" + "\n"
		result_string += "M=D+M" + "\t//" + input_line
	elif "sub" in input_line:
		# x - y

		# Get the location the stack pointer is pointing
		result_string += "@" + pointer_type_to_ram_address("SP") + "\n"

		# Change the value of the stack pointer down one to where it should be after the computation
		result_string += "M=M-1" + "\n"

		# Move to the value before where the stack pointer points to and store the value of the register at that point
		result_string += "A=M-1" + "\n"
		result_string += "D=M" + "\n"

		# Move back up to the value we want to be subtracting, subtract the two in D and M, and store it to D
		result_string += "A=A+1" + "\n"
		result_string += "D=D-M" + "\n"

		# Store the value of the subtraction from D to where it should be in the stack
		result_string += "A=A-1" + "\n"
		result_string += "M=D" + "\t\t//" + input_line
	elif "neg" in input_line:
		# - y

		# Get the location in the stack where y is stored
		result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
		result_string += "A=M-1" + "\n"

		# Negate y and save it to where it should be
		result_string += "M=-M" + "\t\t//" + input_line
	elif "eq" in input_line or "gt" in input_line or "lt" in input_line:
		global asm_jump_counter
		# this first section gives us x - y, which is useful later

		# Access the stack pointer and bump it to where it should be after the operation
		result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
		result_string += "M=M-1" + "\n"
		result_string += "A=M" + "\n"

		# Store y and move to x
		result_string += "D=M" + "\n"
		result_string += "A=A-1" + "\n"

		# Continue with whatever function we want to do:
		if "eq" in input_line:
			# true (-1) if x = y, false (0) otherwise

			# Subtract the two values and check if the result is equal to 0
			result_string += "D=D-M" + "\n"
			result_string += "@EQJUMP" + str(asm_jump_counter) + "\n"

			# Jump ahead if the values are not equal
			result_string += "D;JNE" + "\n"

			# This only runs if the values are equal
			result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
			result_string += "A=M-1" + "\n"
			result_string += "M=-1" + "\n"

			# After this section executes, jump passed the code below
			result_string += "@EQFINISH" + str(asm_jump_counter) + "\n"
			result_string += "0;JMP" + "\n"

			# Jump to this line if the the values are not equal
			result_string += "(EQJUMP" + str(asm_jump_counter) + ")" + "\n"

			# This only runs if the values are not equal
			result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
			result_string += "A=M-1" + "\n"
			result_string += "M=0" + "\n"

			# Jump to this line when we are done with the comparison
			result_string += "(EQFINISH" + str(asm_jump_counter) + ")" + "\t//eq"
		elif "gt" in input_line:
			# true (-1) if x > y, false (0) otherwise

			# Subtract the two values and check if the result is greater than 0
			result_string += "D=D-M" + "\n"
			result_string += "@GTJUMP" + str(asm_jump_counter) + "\n"

			# Jump ahead if the result is not greater than 0
			# For some reason the gt function breaks when we write JGT rather than JGE, so we are using JGE
			result_string += "D;JGE" + "\n"

			# This only runs the result is greater than 0
			result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
			result_string += "A=M-1" + "\n"
			result_string += "M=-1" + "\n"

			# After this section executes, jump passed the code below
			result_string += "@GTFINISH" + str(asm_jump_counter) + "\n"
			result_string += "0;JMP" + "\n"

			# Jump to this line if the the resulting value is not greater than 0
			result_string += "(GTJUMP" + str(asm_jump_counter) + ")" + "\n"

			# This only runs if the result is not greater than 0
			result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
			result_string += "A=M-1" + "\n"
			result_string += "M=0" + "\n"

			# Jump to this line when we are done with the comparison
			result_string += "(GTFINISH" + str(asm_jump_counter) + ")" + "\t//gt"
		elif "lt" in input_line:
			# true (-1) if x < y, false (0) otherwise

			# Subtract the two values and check if the result is less than 0
			result_string += "D=D-M" + "\n"
			result_string += "@LTJUMP" + str(asm_jump_counter) + "\n"

			# Jump ahead if the result is not less than 0
			result_string += "D;JLE" + "\n"

			# This only runs if the result is less than 0
			result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
			result_string += "A=M-1" + "\n"
			result_string += "M=-1" + "\n"

			# After this section executes, jump passed the code below
			result_string += "@LTFINISH" + str(asm_jump_counter) + "\n"
			result_string += "0;JMP" + "\n"

			# Jump to this line if the the result is not less than 0
			result_string += "(LTJUMP" + str(asm_jump_counter) + ")" + "\n"

			# This only runs if the result is not less than 0
			result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
			result_string += "A=M-1" + "\n"
			result_string += "M=0" + "\n"

			# Jump to this line when we are done with the comparison
			result_string += "(LTFINISH" + str(asm_jump_counter) + ")" + "\t//lt"
		# Bump up the counter so that are jumps are not repeated
		asm_jump_counter += 1
	elif "and" in input_line:
		# x And y (bit-wise)

		# Access the stack pointer and bump it to where it should be after the operation
		result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
		result_string += "M=M-1" + "\n"
		result_string += "A=M" + "\n"

		# Store y and move to x
		result_string += "D=M" + "\n"
		result_string += "A=A-1" + "\n"

		# And the two together and store it to x
		result_string += "M=D&M" + "\t//and"
	elif "or" in input_line:
		# x Or y (bit-wise)

		# Access the stack pointer and bump it to where it should be after the operation
		result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
		result_string += "M=M-1" + "\n"
		result_string += "A=M" + "\n"

		# Store y and move to x
		result_string += "D=M" + "\n"
		result_string += "A=A-1" + "\n"

		# Or the two together and store it to x
		result_string += "M=D|M" + "\t//or"
	elif "not" in input_line:
		# Not y (bit-wise)

		# Access the stack pointer and go to the point before it
		result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
		result_string += "A=M-1" + "\n"

		# Not the value at that point and store it back to where we got it
		result_string += "D=M" + "\n"
		result_string += "M=!D" + "\t//not"
	else:
		result_string += "ERROR: tried to write arithmetic but command was not found"
		result_string += "" # This line is here so that I can close this else statement in the IDE
	return result_string


# Push/Pop Code #########################


def write_push_pop(input_line, command_type):
	segment_pointer_type = get_segment_pointer_type(input_line)
	push_pop_value = remove_segment_pointer_and_earlier(input_line, segment_pointer_type).strip()
	result_string = ""

	if command_type == "C_PUSH":
		# Access the value we want to push, and store that value for later
		result_string += "@" + push_pop_value + "\n"
		result_string += "D=A" + "\n"

		# Access the the pointer location and bump up for the next time the stack is called
		result_string += "@" + pointer_type_to_ram_address(segment_pointer_type) + "\n"
		result_string += "M=M+1" + "\n"

		# Move to the location that the stack pointer referred to before getting bumped up
		result_string += "A=M-1" + "\n"

		# Store the push value at the top of the stack
		result_string += "M=D" + "\t\t//" + input_line

		return result_string
	elif command_type == "C_POP":
		# the static pointer is a bit funky so we have to make this section different for it
		if "static" in input_line:
			# TODO: This needs to be finished
		else:
			# Access the pointer location and bump down for the next time the stack is called
			result_string += "@" + pointer_type_to_ram_address(
				segment_pointer_type) + "\t//" + segment_pointer_type + "\n"
			result_string += "M=M-1" + "\n"

		# Store the value that was at the top of the stack before we moved the pointer
		result_string += "A=A+1" + "\n"
		result_string += "D=M" + "\n"

		# Access the register where we want to store the value and store it there
		result_string += "@R" + push_pop_value + "\n"
		result_string += "M=D" + "\t\t//" + input_line

		return result_string
	return "ERROR: failure when writing push/pop"


# Segment Pointer Code


def get_segment_pointer_type(input_line):
	if "constant" in input_line:
		return "SP"
	elif "local" in input_line:
		return "LCL"
	elif "argument" in input_line:
		return "ARG"
	elif "this" in input_line:
		return "THIS"
	elif "that" in input_line:
		return "THAT"
	elif "pointer" in input_line:
		return "POINTER"
	elif "static" in input_line:
		return "STATIC"
	return "ERROR: could not find pointer type"

def remove_segment_pointer_and_earlier(input_line, segment_pointer_type):
	if segment_pointer_type == "SP":
		return input_line[input_line.find("constant") + len("constant"):]
	elif segment_pointer_type == "LCL":
		return input_line[input_line.find("local"):]
	elif segment_pointer_type == "ARG":
		return input_line[input_line.find("argument"):]
	elif segment_pointer_type == "THIS":
		return input_line[input_line.find("this"):]
	elif segment_pointer_type == "THAT":
		return input_line[input_line.find("that"):]
	return "ERROR: could not find pointer type"


def pointer_type_to_ram_address(segment_pointer_type):
	if segment_pointer_type == "SP":
		return "R0"
	elif segment_pointer_type == "LCL":
		return "R1"
	elif segment_pointer_type == "ARG":
		return "R2"
	elif segment_pointer_type == "THIS" or segment_pointer_type == "POINTER":
		return "R3"
	elif segment_pointer_type == "THAT":
		return "R4"
	elif segment_pointer_type == "STATIC":
		return "R" + str(16 + )
	# temp takes registers 5 to 12
	# 13 to 15 are used for general purpose functions by the VM implementation
	# static refers to the ram addresses starting at R16
	else:
		return "ERROR: register for pointer type not found"


#########################################
# Testing Area ##########################
#########################################


def write_hack_to_file(input_line_list):
	global output_file_name
	output_file = open(output_file_name, "w")
	write_string = ""
	for line in input_line_list:
		write_string += line + "\n"
	output_file.write(write_string)
	output_file.close()


vm_to_asm()

