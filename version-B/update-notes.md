# Kryoss version-B update notes
## Kryoss is not a space sensitive language anymore
*That means both commands are acceptable*
```
let a int = 1
let a int=1
```
## New Exceptions
**WrongModifierException**<br>
*For adding a wrong modifier in say command*<br><br>
Sample code:<br>
```
say hello $h
```
Error message:<br>
```
Exception occurced at line number 2
Command: say hello $h
Reason: only $n and $s modifiers are allowed
```
**WrongLimitException**<br>
*For configuring limit to a wrong value*<br><br>
Sample code:<br>
```
config infiniteRecursionLimit -1
```
Error message:<br>
```
Exception occurced at line number 2
Command: config infiniteRecursionLimit -1
Reason: adding a wrong limit value
```
