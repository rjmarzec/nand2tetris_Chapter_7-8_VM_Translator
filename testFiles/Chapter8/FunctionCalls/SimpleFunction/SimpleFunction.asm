
(SimpleFunction.test)
@0
D=A
@R0
M=D
@0
D=A
@R0
M=D	//function SimpleFunction.test 2
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
@R0
M=M-1
A=M
D=M
A=A-1
M=D+M	//add
@R0
A=M-1
D=M
M=!D	//not
@0
D=A
@R2
M=D+M
A=M
D=M
@R0
M=M+1
A=M-1
M=D
@0
D=-A
@R2
M=D+M		//push argument 0
@R0
M=M-1
A=M
D=M
A=A-1
M=D+M	//add
@1
D=A
@R2
M=D+M
A=M
D=M
@R0
M=M+1
A=M-1
M=D
@1
D=-A
@R2
M=D+M		//push argument 1
@R0
M=M-1
A=M-1
D=M
A=A+1
D=D-M
A=A-1
M=D		//sub
@R1
D=M
@R0
M=M+1
A=M-1
M=D
@R0
M=M-1
A=M
D=M
@13
M=D
@14
D=M
D=D-1
D=D-1
D=D-1
D=D-1
D=D-1
@R0
M=M+1
A=M-1
M=D
@R0
M=M-1
A=M
D=M
@R2
M=D
@R0
D=M
@R0
M=M+1
A=M-1
M=D
@R0
M=M-1
A=M
D=M
@R2
M=D
@R2
D=M
@R0
M=M+1
A=M-1
M=D
@R0
A=M
M=M+1
@13
D=M
D=D-1
@R0
M=M+1
A=M-1
M=D
@R0
M=M-1
A=M
D=M
@R4
M=D
@13
D=M
D=D-1
D=D-1
@R0
M=M+1
A=M-1
M=D
@R0
M=M-1
A=M
D=M
@R3
M=D
@13
D=M
D=D-1
D=D-1
D=D-1
@R0
M=M+1
A=M-1
M=D
@R0
M=M-1
A=M
D=M
@R2
M=D
@13
D=M
D=D-1
D=D-1
D=D-1
D=D-1
@R0
M=M+1
A=M-1
M=D
@R0
M=M-1
A=M
D=M
@R1
M=D
@14
A=M
0;JMP
	//return
