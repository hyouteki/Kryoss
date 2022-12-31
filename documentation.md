
# Code examples

*defining and initializing variables at same time*<br>
*syntax ~ `let <variable> <datatype> = <value>`* <br>
let string1 string = abc<br>
let num1 int = 0<br>
let num2 int = 1<br>
let num3 int = 2<br>
let char1 char = a<br>
let float1 float = 1.1<br>
let float2 float = 0.54<br>
let float3 float = 7.8<br>
let boolean1 boolean = false<br>
let nothing1 nothing = null<br>

*defining variables*<br>
*syntax ~ `let <variable> <datatype>`*<br>
let string2 string<br>
let num4 int<br>
let char2 char<br>
let float4 float<br>
let boolean2 boolean<br>
let nothing2 nothing<br>

*deleting variables*<br>
*syntax ~ `del <variable>`*<br>
del string2<br>

*arithmatic operations on variables of int and float type*<br>
*syntax ~ `<opcode> <variable> <variable> <variable>`*<br>
add num1 num2 one<br>
sub num1 num1 num2<br>
mul float1 float2 float3<br>
div float2 float2 float3<br>

*displaying variable values*<br>
*syntax ~ `say <variable>`*<br>
say string1<br>

*displaying messages*<br>
*syntax ~ `say <message>`*<br>
say hello fellas<br>

*displaying messages with special characters*<br>
*syntax ~ `say <message> <special-character>`*<br>
[$n]: line-break-character<br>
[$s]: space-character<br>
say hello fellas $n<br>
say hello fellas $s<br>

*taking user input and storing in variables*<br>
*syntax ~ `ask <variable>`*<br>
ask string1<br>

*commenting*<br>
*syntax ~ `; type here anything`*<br>
; hello fellas<br>

*marking a stage in code*<br>
*syntax ~ `mark <mark>`*<br>
mark hello <br>

*for going to a certain mark*<br>
*syntax ~ `goto <mark>`*<br>
goto hello<br>

*for comparing the variables and setting off the flags*<br>
*syntax ~ `com <variable> <variable>`*<br>
com num1 num2<br>

*for settings flags*<br>
*syntax ~ `set <flag>`*<br>
set false<br>
set true<br>
set boolean1<br>

*for copying variable values*<br>
*syntax ~ `cpy <variable> <variable>`*<br>
cpy num1 num2<br>

*for displaying various things*<br>
*syntax ~ `show <thing>`*<br>
show vars<br>
show flags<br>
show stack<br>

*for doing nothing*<br>
*syntax ~ `pass`*<br>
pass<br>

*if statement*<br>
*syntax ~ `if <flag> ? <command>`*<br>
if less ? goto hello<br>
if greater ? say greater<br>
if equal ? ask string1<br>
if flag ? pass<br>

*for pushing into stack*<br>
*syntax ~ `push <variable>`*<br>
push num1<br>

*for poping from stack*<br>
*syntax ~ `pop <variable>`*<br>
pop num1<br>

*for exiting in between of execution*<br>
*syntax ~ `exit`*<br>
exit<br>

# Flags

*[less, more, same, error_code, command_number, coverage]*<br>

*for less, more & same*<br>
[-1]: no-value<br>
[ 0]: false<br>
[ 1]: true<br>

*for flags*<br>
[-1]: no-value<br>
[ 0]: false<br>
[ 1]: true<br>
[ 7]: OtherError<br>
[ 8]: StackOverflowException<br>
[ 9]: InfinteRecurrsionException<br>

*for flags*<br>
[ 0]: false<br>
[ 1]: true<br>

*command number*<br>
contains the number of currently executing command<br>

# Execution command

## Step1
*Downloads all the python files to your working directory*<br>

## Step2
*Write your Kryoss program with extension .kry*<br>

## Step3
*Run your code with either commands*<br>
*`python kryoss_compiler.py <file-name.kry>`*<br>

for executing with coverage<br>
*`python kryoss_compiler.py <file-name.kry> coverage`*<br>

# Must know

*some basic variables like zero, one, true, false no need to waste time on making them*<br>

*not understanding what's happening in your code, make sure to run it with coverage to visualize*<br>

*remember to maintain spaces as Kryoss is space sensitive*<br>
