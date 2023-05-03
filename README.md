# Kryoss

## Contents
- [Overview](#overview)
- [Code examples](#code-examples)
- [Config commands](#config-commands)
- [Flags](#flags)
- [Execution command](#execution-command)
- [Must know](#must-know)

# Overview
- __Kryoss__ is a case sensitive language.
- Made using __Python__ and inspired by __Assembly language__.
- Some sample programs are already there.

# Code examples

defining and initializing variables at same time<br> 
syntax ~ `let <variable> <datatype> = <value>`
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
> Caution: Using variables to intialize different variables is prohibited and may lead to `TypeMisMatchException`<br>
> Example: `let num1 int = one`

defining variables<br>
syntax ~ `let <variable> <datatype>`
```
let string2 string
let num4 int
let char2 char
let float4 float
let boolean2 boolean
let nothing2 nothing
```

deleting variables<br>
syntax ~ `del <variable>`
```
del string2
```

arithmatic operations on variables of int and float type<br>
syntax ~ `<opcode> <variable> <variable> <variable>`
```
add num1 num2 one
sub num1 num1 num2
mul float1 float2 float3
div float2 float2 float3
```

displaying variable values<br>
syntax ~ `say <variable>`
```
say string1
```

displaying messages<br>
syntax ~ `say <message>`
```
say hello fellas
```

displaying messages with modifiers<br>
syntax ~ `say <message> <modifier>`<br>
$n: line-break-character<br>
$s: space-character
```
say hello fellas $n
say hello fellas $s
```

taking user input and storing in variables<br>
syntax ~ `ask <variable>`
```
ask string1
```

commenting<br>
syntax ~ `; type here anything`
```
; hello fellas
```

marking a point in code<br>
syntax ~ `mark <mark>`
```
mark hello
```

for going to a certain mark<br>
syntax ~ `goto <mark>`
```
goto hello
```

for comparing the variables and setting off the flags<br>
syntax ~ `com <variable> <variable>`
```
com num1 num2
```

for setting flags<br>
syntax ~ `set <flag>`
```
set false
set true
set boolean1
```

for copying variable values<br>
syntax ~ `cpy <variable> <variable>`
```
cpy num1 num2
```

for displaying various things<br>
syntax ~ `show <thing>`
```
show vars
show flags
show stack
```

for doing nothing<br>
syntax ~ `pass`
```
pass
```

if statement<br>
syntax ~ `if <flag> ? <command>`
```
if less ? goto hello
if more ? say greater
if same ? ask string1
if flag ? pass
```

for pushing into stack<br>
syntax ~ `push <variable>`
```
push num1
```
for poping from stack<br>
syntax ~ `pop <variable>`
```
pop num1
```
for exiting in between of execution<br>
syntax ~ `exit`
```
exit
```
# Config commands
for configuring limits<br>
syntax ~ `config <limit> <value>`
```
config stackOverflowLimit 100
config infiniteRecursionLimit 1000
```

# Flags

__Internally flags are stored in an array in this order__<br>
`[less, more, same, error_code, command_number, coverage]`

- __For less, more & same__
  - -1: no-value
  - 0: false
  - 1: true

- __For Flags and error-codes__
  - -1: no-value
  - 0: false
  - 1: true
  - 7: OtherError
  - 8: StackOverflowException
  - 9: InfinteRecurrsionException

- __Command number__<br>
  contains the number of currently executing command<br>

- __Coverage__<br>
  contains flag indicating whether to generate a coverage file or not<br>
  - 0: false
  - 1: true

# Execution command

## Step1
Downloads all the python files from latest version to your working directory

## Step2
Write your Kryoss program with extension .kry

## Step3
Run your code with either commands
```
python3 kryoss_compiler.py <file-name.kry>
```
for executing with coverage
```
python3 kryoss_compiler.py <file-name.kry> coverage
```

# Must know

- Some basic variables like `zero`, `one`, `true`, and `false` are already there. So, no need to waste time on making one yourself.
- Not understanding what's happening in your code, make sure to run it with coverage to visualize.
- You can change `infiniteRecursionLimit`, `stackOverflowLimit` & other limits permanently from __kryoss_config.KryossConfig__ class
