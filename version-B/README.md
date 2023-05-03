# Kryoss version-B update notes
## Kryoss is not a space sensitive language anymore
That means both commands are acceptable
```
let a int = 1
let a int=1
```
## New Exceptions
### WrongModifierException
For adding a wrong modifier in say command<br><br>
Sample code:
```
say hello $h
```
Error message:<br>
```
Exception occurced at line number 2
Command: say hello $h
Reason: only $n and $s modifiers are allowed
```
### WrongLimitException
For passing a wrong value in limit<br><br>
Sample code:
```
config infiniteRecursionLimit -1
```
Error message:
```
Exception occurced at line number 2
Command: config infiniteRecursionLimit -1
Reason: adding a wrong limit value
```
### WrongConfigException
For passing a wrong config name<br><br>
Sample code:
```
config stackOverflowLimitt 100
```
Error message:
```
Exception occurced at line number 2
Command: config stackOverflowLimitt 100
Reason: adding a wrong config name
```
