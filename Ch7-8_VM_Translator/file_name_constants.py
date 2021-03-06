# A file containing constants of the project file names so that it is easier to switch between them when testing

#########################################
# Template ##############################
#########################################

# Files Name ####################
# ..._IN = ".../.../....vm"	(Input File Directory)
# ..._OUT = ".../.../....vm"	(Output File Directory)
# ..._FILES = [".../.../...", "....vm", ...]	([Directory, Class1, Class2, ...])

#########################################
# Self Testing Files ####################
#########################################

# Self Testing Files ####################
SELF_TESTING_IN = "TestFiles/SelfTesting/SelfTesting.vm"
SELF_TESTING_OUT = "TestFiles/SelfTesting/SelfTesting.asm"

#########################################
# Chapter 7 Files #######################
#########################################

# Stack Arithmetic ######################

# SimpleAdd
SIMPLE_ADD_IN = "TestFiles/Chapter7/StackArithmetic/SimpleAdd/SimpleAdd.vm"
SIMPLE_ADD_OUT = "TestFiles/Chapter7/StackArithmetic/SimpleAdd/SimpleAdd.asm"

# StackTest
STACK_TEST_IN = "TestFiles/Chapter7/StackArithmetic/StackTest/StackTest.vm"
STACK_TEST_OUT = "TestFiles/Chapter7/StackArithmetic/StackTest/StackTest.asm"

# Memory Access #########################

# BasicTest
BASIC_TEST_IN = "TestFiles/Chapter7/MemoryAccess/BasicTest/BasicTest.vm"
BASIC_TEST_OUT = "TestFiles/Chapter7/MemoryAccess/BasicTest/BasicTest.asm"

# PointerTest
POINTER_TEST_IN = "TestFiles/Chapter7/MemoryAccess/PointerTest/PointerTest.vm"
POINTER_TEST_OUT = "TestFiles/Chapter7/MemoryAccess/PointerTest/PointerTest.asm"

# StaticTest
STATIC_TEST_IN = "TestFiles/Chapter7/MemoryAccess/StaticTest/StaticTest.vm"
STATIC_TEST_OUT = "TestFiles/Chapter7/MemoryAccess/StaticTest/StaticTest.asm"

#########################################
# Chapter 8 Files #######################
#########################################

# Function Calls ########################

# FibonacciElement
FIBONACCI_ELEMENT_IN = "TestFiles/Chapter8/FunctionCalls/FibonacciElement/FibonacciElementCompiled.vm"
FIBONACCI_ELEMENT_OUT = "TestFiles/Chapter8/FunctionCalls/FibonacciElement/FibonacciElement.asm"
FIBONACCI_ELEMENT_FILES = ["TestFiles/Chapter8/FunctionCalls/FibonacciElement/", "Sys.vm", "Main.vm"]

# NestedCall
NESTED_CALL_IN = "TestFiles/Chapter8/FunctionCalls/NestedCall/Sys.vm"
NESTED_CALL_OUT = "TestFiles/Chapter8/FunctionCalls/NestedCall/NestedCall.asm"

# SimpleFunction
SIMPLE_FUNCTION_IN = "TestFiles/Chapter8/FunctionCalls/SimpleFunction/SimpleFunction.vm"
SIMPLE_FUNCTION_OUT = "TestFiles/Chapter8/FunctionCalls/SimpleFunction/SimpleFunction.asm"

# StaticsTest
STATICS_TEST_IN = "TestFiles/Chapter8/FunctionCalls/StaticsTest/StaticsTestCompiled.vm"
STATICS_TEST_OUT = "TestFiles/Chapter8/FunctionCalls/StaticsTest/StaticsTest.asm"
STATICS_TEST_FILES = ["TestFiles/Chapter8/FunctionCalls/StaticsTest/", "Sys.vm", "Class1.vm", "Class2.vm"]

# Program Flow ##########################

# BasicLoop
BASIC_LOOP_IN = "TestFiles/Chapter8/ProgramFlow/BasicLoop/BasicLoop.vm"
BASIC_LOOP_OUT = "TestFiles/Chapter8/ProgramFlow/BasicLoop/BasicLoop.asm"

# FibonacciSeries
FIBONACCI_SERIES_IN = "TestFiles/Chapter8/ProgramFlow/FibonacciSeries/FibonacciSeries.vm"
FIBONACCI_SERIES_OUT = "TestFiles/Chapter8/ProgramFlow/FibonacciSeries/FibonacciSeries.asm"

