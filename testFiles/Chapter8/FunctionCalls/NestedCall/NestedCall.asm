(Sys.init)		//function Sys.init 0
@4000
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 4000
@R0
M=M-1
A=M
D=M
@3
M=D		//pop pointer 0
@5000
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 5000
@R0
M=M-1
A=M
D=M
@4
M=D		//pop pointer 1
@RETURNADDRESS0
D=M
@R0
M=M+1
A=M-1
M=D
@R1
D=M
@R0
M=M+1
A=M-1
M=D
@R2
D=M
@R0
M=M+1
A=M-1
M=D
@R3
D=M
@R0
M=M+1
A=M-1
M=D
@R4
D=M
@R0
M=M+1
A=M-1
M=D
@R0
D=M
@0
D=D-A
@5
D=D-A
@R2
M=D
@R0
D=M
@R1
M=D
@Sys.main
0;JMP
(RETURNADDRESS0)	//call Sys.main 0
@R0
M=M-1
A=M
D=M
@6
M=D		//pop temp 1
(LOOP)	//label LOOP
@LOOP
0;JMP	//goto LOOP
(Sys.main)
@R0
M=M+1
A=M-1
M=0
@R0
M=M+1
A=M-1
M=0
@R0
M=M+1
A=M-1
M=0
@R0
M=M+1
A=M-1
M=0
@R0
M=M+1
A=M-1
M=0		//function Sys.main 5
@4001
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 4001
@R0
M=M-1
A=M
D=M
@3
M=D		//pop pointer 0
@5001
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 5001
@R0
M=M-1
A=M
D=M
@4
M=D		//pop pointer 1
@200
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 200
@1
D=A
@R1
M=D+M
@R0
M=M-1
A=M
D=M
@R1
A=M
M=D
@1
D=-A
@R1
M=D+M		//pop local 1
@40
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 40
@2
D=A
@R1
M=D+M
@R0
M=M-1
A=M
D=M
@R1
A=M
M=D
@2
D=-A
@R1
M=D+M		//pop local 2
@6
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 6
@3
D=A
@R1
M=D+M
@R0
M=M-1
A=M
D=M
@R1
A=M
M=D
@3
D=-A
@R1
M=D+M		//pop local 3
@123
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 123
@RETURNADDRESS1
D=M
@R0
M=M+1
A=M-1
M=D
@R1
D=M
@R0
M=M+1
A=M-1
M=D
@R2
D=M
@R0
M=M+1
A=M-1
M=D
@R3
D=M
@R0
M=M+1
A=M-1
M=D
@R4
D=M
@R0
M=M+1
A=M-1
M=D
@R0
D=M
@1
D=D-A
@5
D=D-A
@R2
M=D
@R0
D=M
@R1
M=D
@Sys.add12
0;JMP
(RETURNADDRESS1)	//call Sys.add12 1
@R0
M=M-1
A=M
D=M
@5
M=D		//pop temp 0
@0
D=A
@R1
M=D+M
A=M
D=M
@R0
M=M+1
A=M-1
M=D
@0
D=-A
@R1
M=D+M		//push local 0
@1
D=A
@R1
M=D+M
A=M
D=M
@R0
M=M+1
A=M-1
M=D
@1
D=-A
@R1
M=D+M		//push local 1
@2
D=A
@R1
M=D+M
A=M
D=M
@R0
M=M+1
A=M-1
M=D
@2
D=-A
@R1
M=D+M		//push local 2
@3
D=A
@R1
M=D+M
A=M
D=M
@R0
M=M+1
A=M-1
M=D
@3
D=-A
@R1
M=D+M		//push local 3
@4
D=A
@R1
M=D+M
A=M
D=M
@R0
M=M+1
A=M-1
M=D
@4
D=-A
@R1
M=D+M		//push local 4
@R0
M=M-1
A=M
D=M
A=A-1
M=D+M	//add
@R0
M=M-1
A=M
D=M
A=A-1
M=D+M	//add
@R0
M=M-1
A=M
D=M
A=A-1
M=D+M	//add
@R0
M=M-1
A=M
D=M
A=A-1
M=D+M	//add
@R1
D=M
@13
M=D
@13
D=M
@5
D=D-A
A=D
D=M
@14
M=D
@R0
M=M-1
A=M
D=M
@R2
A=M
M=D
@R2
D=M+1
@R0
M=D
@13
D=M
@1
D=D-A
A=D
D=M
@R4
M=D
@13
D=M
@2
D=D-A
A=D
D=M
@R3
M=D
@13
D=M
@3
D=D-A
A=D
D=M
@R2
M=D
@13
D=M
@4
D=D-A
A=D
D=M
@R1
M=D
@14
A=M
0;JMP		//return
(Sys.add12)		//function Sys.add12 0
@4002
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 4002
@R0
M=M-1
A=M
D=M
@3
M=D		//pop pointer 0
@5002
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 5002
@R0
M=M-1
A=M
D=M
@4
M=D		//pop pointer 1
@0
D=A
@R2
A=D+M
D=M
@R0
M=M+1
A=M-1
M=D		//push argument 0
@12
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 12
@R0
M=M-1
A=M
D=M
A=A-1
M=D+M	//add
@R1
D=M
@13
M=D
@13
D=M
@5
D=D-A
A=D
D=M
@14
M=D
@R0
M=M-1
A=M
D=M
@R2
A=M
M=D
@R2
D=M+1
@R0
M=D
@13
D=M
@1
D=D-A
A=D
D=M
@R4
M=D
@13
D=M
@2
D=D-A
A=D
D=M
@R3
M=D
@13
D=M
@3
D=D-A
A=D
D=M
@R2
M=D
@13
D=M
@4
D=D-A
A=D
D=M
@R1
M=D
@14
A=M
0;JMP		//return
