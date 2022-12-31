
# Code examples

*defining and initializing variables at same time*
*syntax ~ let <variable> <datatype> = <value>* 
let string1 string = abc
let num1 int = 0
let num2 int = 1
let num3 int = 2
let char1 char = a
let float1 float = 1.1
let float2 float = 0.54
let float3 float = 7.8
let boolean1 boolean = false
let nothing1 nothing = null

*defining variables*
*syntax ~ let <variable> <datatype>*
let string2 string
let num4 int
let char2 char
let float4 float
let boolean2 boolean
let nothing2 nothing

*deleting variables*
*syntax ~ del <variable-name>*
del string2

*arithmatic operations on variables of int and float type*
*syntax ~ <opcode> <variable1> <variable2> <variable3>*
add num1 num2 one
sub num1 num1 num2
mul float1 float2 float3
div float2 float2 float3

*displaying variable values*
*syntax ~ say <variable>*
say string1

*displaying messages*
*syntax ~ say <message>*
say hello fellas

*displaying messages with special characters*
*syntax ~ say <message> <special-character>*
[$n]: line-break-character
[$s]: space-character
say hello fellas $n
say hello fellas $s

*taking user input and storing in variables*
*syntax ~ ask <variable>*
ask string1

*commenting*
*syntax ~ ; type here anything*
; hello fellas

*marking a stage in code*
*syntax ~ mark <mark-name>*
mark hello 

*for going to a certain mark*
*syntax ~ goto <mark-name>*
goto hello

*for comparing the variables and setting off the flags*
*syntax ~ com <variable1> <variable2>*
com num1 num2

*for settings flags*
*syntax ~ set <flag>*
set false
set true
set boolean1

*for copying variable values*
*syntax ~ cpy <variable> <variable>*
cpy num1 num2

*for displaying various things*
*syntax ~ show <thing>*
show vars
show flags
show stack

*for doing nothing*
*syntax ~ pass*
pass

*if statement*
*syntax ~ if <flag> ? <command>*
if less ? goto hello
if greater ? say greater
if equal ? ask string1
if flag ? pass

*for pushing into stack*
*syntax ~ push <variable>*
push num1

*for poping from stack*
*syntax ~ pop <variable>*
pop num1

*for exiting in between of execution*
*syntax ~ exit*
exit

======================================================

# Flags

*[less, more, same, error_code, command_number, coverage]*

*for less, more & same*
[-1]: no-value
[ 0]: false
[ 1]: true

*for flags*
[-1]: no-value
[ 0]: false
[ 1]: true
[ 7]: OtherError
[ 8]: StackOverflowException
[ 9]: InfinteRecurrsionException

*for flags*
[ 0]: false
[ 1]: true

*command number*
contains the number of currently executing command

======================================================

# Execution command

*python kryoss_compiler.py <file-name.kry>*

for executing with coverage
*python kryoss_compiler.py <file-name.kry> coverage*

======================================================

# Must know

*some basic variables like zero, one, true, false no need to waste time on making them*

*not understanding what's happening in your code, make sure to run it with coverage to visualize*

*remember to maintain spaces as Kryoss is space sensitive*

======================================================