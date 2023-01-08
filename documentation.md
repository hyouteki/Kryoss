
# Code examples

*defining and initializing variables at same time*<br>
*syntax ~ `let <variable> <datatype> = <value>`* <br>
```
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
```

*defining variables*<br>
*syntax ~ `let <variable> <datatype>`*<br>
```
let string2 string
let num4 int
let char2 char
let float4 float
let boolean2 boolean
let nothing2 nothing
```

*deleting variables*<br>
*syntax ~ `del <variable>`*<br>
```
del string2
```

*arithmatic operations on variables of int and float type*<br>
*syntax ~ `<opcode> <variable> <variable> <variable>`*<br>
```
add num1 num2 one
sub num1 num1 num2
mul float1 float2 float3
div float2 float2 float3
```

*displaying variable values*<br>
*syntax ~ `say <variable>`*<br>
```
say string1
```

*displaying messages*<br>
*syntax ~ `say <message>`*<br>
```
say hello fellas
```

*displaying messages with modifiers*<br>
*syntax ~ `say <message> <modifier>`*<br>
[$n]: line-break-character<br>
[$s]: space-character<br>
```
say hello fellas $n
say hello fellas $s
```

*taking user input and storing in variables*<br>
*syntax ~ `ask <variable>`*<br>
```
ask string1
```

*commenting*<br>
*syntax ~ `; type here anything`*<br>
```
; hello fellas
```

*marking a point in code*<br>
*syntax ~ `mark <mark>`*<br>
```
mark hello
```

*for going to a certain mark*<br>
*syntax ~ `goto <mark>`*<br>
```
goto hello
```

*for comparing the variables and setting off the flags*<br>
*syntax ~ `com <variable> <variable>`*<br>
```
com num1 num2
```

*for settings flags*<br>
*syntax ~ `set <flag>`*<br>
```
set false
set true
set boolean1
```

*for copying variable values*<br>
*syntax ~ `cpy <variable> <variable>`*<br>
```
cpy num1 num2
```

*for displaying various things*<br>
*syntax ~ `show <thing>`*<br>
```
show vars
show flags
show stack
```

*for doing nothing*<br>
*syntax ~ `pass`*<br>
```
pass
```

*if statement*<br>
*syntax ~ `if <flag> ? <command>`*<br>
```
if less ? goto hello
if more ? say greater
if same ? ask string1
if flag ? pass
```

*for pushing into stack*<br>
*syntax ~ `push <variable>`*<br>
```
push num1
```
*for poping from stack*<br>
*syntax ~ `pop <variable>`*<br>
```
pop num1
```
*for exiting in between of execution*<br>
*syntax ~ `exit`*<br>
```
exit
```
# Config commands
*for configuring limits*<br>
*syntax ~ `config <limit> <value>`*<br>
```
config stackOverflowLimit 100
config infiniteRecursionLimit 1000
```

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

*coverage*<br>
contains flag indicating whether to generate a coverage file or not<br>
[ 0]: false<br>
[ 1]: true<br>

# Execution command

## Step1
*Downloads all the python files from latest version to your working directory*<br>

## Step2
*Write your Kryoss program with extension .kry*<br>

## Step3
*Run your code with either commands*<br>
```
python3 kryoss_compiler.py <file-name.kry>
```

*for executing with coverage*<br>
```
python3 kryoss_compiler.py <file-name.kry> coverage
```

# Must know

*Some basic variables like zero, one, true, false are already there. So, no need to waste time on making one yourself*<br>

*Not understanding what's happening in your code, make sure to run it with coverage to visualize*<br>

*You can change infiniteRecursionLimit, stackOverflowLimit & other limits permanently from kryoss_config.KryossConfig class*<br>
