import sys
import kryoss_errors
import kryoss_classes
import kryoss_config

# things
config = kryoss_config.KryossConfig()
datatypes = ["string", "int", "float", "boolean", "char", "nothing"]
opcodes = ["add", "sub", "mul", "div"]
marks: list[kryoss_classes.Mark] = list()
flags = [-1, -1, -1, -1, 0, 0]
variables: list[kryoss_classes.Variable] = list()
stack: list[kryoss_classes.Variable] = list()
coverageList: list[kryoss_classes.Command] = list()

# helper methods


def makeException(desc: str, command: kryoss_classes.Command):
    print(f"Exception occurced at line number {command.lineNumber}")
    print(f"Command: {command.withoutLineBreakCommand}")
    print(f"Reason: {desc}")
    flags[3] = 7
    handleCoverage()
    quit(7)


def handleCoverage():
    if (flags[5]):
        writeCoverage()


def findVariableByName(name: str):
    for variable in variables:
        if variable.name == name:
            return variable
    return None


def findMarkByName(name: str):
    for mark in marks:
        if mark.name == name:
            return mark
    return None


def writeCoverage():
    try:
        file = open(fileName+".cvg", "w")
        for command in coverageList:
            file.write(command.__str__()+"\n")
        file.close()
    except IOError:
        kryoss_errors.CoverageCannotWriteException().handleException()


def resetFlags():
    flags[0] = -1
    flags[1] = -1
    flags[2] = -1
    flags[3] = -1


def showCaseVariable():
    print("Variables start")
    for variable in variables:
        print(variable)
    print("Variables end")


def showCaseFlag():
    print("Flags start")
    print(f"less: {flags[0]}")
    print(f"more: {flags[1]}")
    print(f"same: {flags[2]}")
    print(f"flags: {flags[3]}")
    print(f"command_number: {flags[4]}")
    print(f"coverage: {flags[5]}")
    print("Flags end")


def showCaseStack():
    print("Stack start")
    for variable in stack:
        print(variable)
    print("Stack End")


def initializeFileSystem() -> str:
    length = len(sys.argv)
    try:
        if (length == 1):
            raise kryoss_errors.InvalidTerminalCommandException
        if (length == 3):
            if (sys.argv[2] == "coverage"):
                flags[5] = True
            else:
                kryoss_errors.InvalidTerminalCommandException.handleException()
        return sys.argv[1]

    except kryoss_errors.InvalidTerminalCommandException:
        kryoss_errors.InvalidTerminalCommandException.handleException()


def readFile(filename: str) -> dict:
    try:
        file = open(filename, "r")
    except FileNotFoundError:
        handleCoverage()
        kryoss_errors.InvalidFileException.handleException()
    out: list[kryoss_classes.Command] = list()
    lineNumber = 1
    for line in file.readlines():
        out.append(kryoss_classes.Command(line, lineNumber))
        lineNumber += 1
    out = [i for i in out if i.commandList != []]
    file.close()
    return out


def initializeSimpleVariables():
    variables.append(kryoss_classes.Variable("zero", "int", 0))
    variables.append(kryoss_classes.Variable("one", "int", 1))

# command executing methods


def checkComment(command: kryoss_classes.Command):
    commandList: list = command.commandList
    return (commandList[0] == ";")


def checkLetStatement(command: kryoss_classes.Command) -> bool:
    commandList: list = command.commandList
    length: int = len(commandList)
    if (length != 5 and length != 3):
        return False
    if (commandList[0] != "let"):
        return False
    if (length == 5 and commandList[3] != "="):
        return False
    if (commandList[2] not in datatypes):
        return False
    return True


def processLetStatement(command: kryoss_classes.Command):
    commandList = command.commandList
    name = commandList[1]
    datatype = commandList[2]
    length = len(commandList)
    if (length == 3):
        variables.append(kryoss_classes.Variable(name, datatype))
        return
    value = commandList[4]
    try:
        if (datatype == "int"):
            value = int(value)
        if (datatype == "float"):
            value = float(value)
        if (datatype == "boolean"):
            value = bool(value)
        if (datatype == "char"):
            if (len(value) != 1):
                raise ValueError
        if (datatype == "null"):
            value = None
    except ValueError:
        makeException(kryoss_errors.InvalidValueException.desc, command)
    variable = findVariableByName(name)
    if (variable == None):
        variables.append(kryoss_classes.Variable(name, datatype, value))
    else:
        variable.datatype = datatype
        variable.value = value


def checkDelStatement(command: kryoss_classes.Command) -> bool:
    commandList = command.commandList
    if (len(commandList) != 2):
        return False
    if (commandList[0] != "del"):
        return False
    return True


def processDelStatement(command: kryoss_classes.Command):
    commandList = command.commandList
    name = commandList[1]
    variable = findVariableByName(name)
    if (variable == None):
        makeException(kryoss_errors.VariableNotFoundException.desc, command)
    else:
        variables.remove(variable)


def checkOppStatement(command: kryoss_classes.Command) -> bool:
    commandList = command.commandList
    if (len(commandList) != 4):
        return False
    if (commandList[0] not in opcodes):
        return False
    return True


def processOppStatement(command: kryoss_classes.Command):
    commandList = command.commandList
    opcode = commandList[0]
    var1 = findVariableByName(commandList[1])
    var2 = findVariableByName(commandList[2])
    var3 = findVariableByName(commandList[3])
    if (var1 == None or var2 == None or var3 == None):
        makeException(kryoss_errors.VariableNotFoundException.desc, command)
    datatype1 = var1.datatype
    datatype2 = var2.datatype
    datatype3 = var3.datatype
    if (datatype1 == "int" and datatype2 == "int" and datatype3 == "int"):
        if (opcode == "add"):
            var1.value = var2.value + var3.value
        elif (opcode == "sub"):
            var1.value = var2.value - var3.value
        elif (opcode == "mul"):
            var1.value = var2.value * var3.value
        elif (opcode == "div"):
            try:
                var1.value = var2.value // var3.value
            except ZeroDivisionError:
                makeException(
                    kryoss_errors.ZeroDivisionException.desc, command)
    elif (datatype1 == "float" and datatype2 == "float" and datatype3 == "float"):
        if (opcode == "add"):
            var1.value = var2.value + var3.value
        elif (opcode == "sub"):
            var1.value = var2.value - var3.value
        elif (opcode == "mul"):
            var1.value = var2.value * var3.value
        elif (opcode == "div"):
            try:
                var1.value = var2.value / var3.value
            except ZeroDivisionError:
                makeException(
                    kryoss_errors.ZeroDivisionException.desc, command)
    else:
        makeException(kryoss_errors.TypeMisMatchException.desc, command)


def checkCopyStatement(command: kryoss_classes.Command) -> bool:
    commandList = command.commandList
    if (len(commandList) != 3):
        return False
    if (commandList[0] != "cpy"):
        return False
    return True


def processCopyStatement(command: kryoss_classes.Command):
    commandList = command.commandList
    variable1 = findVariableByName(commandList[1])
    variable2 = findVariableByName(commandList[2])
    if (variable1 == None or variable2 == None):
        makeException(kryoss_errors.VariableNotFoundException.desc, command)
    if (variable1.datatype != variable2.datatype):
        makeException(kryoss_errors.TypeMisMatchException.desc, command)
    variable1.value = variable2.value


def checkSayStatement(command: kryoss_classes.Command) -> bool:
    commandList = command.commandList
    if (len(commandList) < 2):
        return False
    if (commandList[0] != "say"):
        return False
    return True


def processSayStatement(command: kryoss_classes.Command):
    commandList = command.commandList
    if (len(commandList) > 2):
        message = " ".join(commandList[1:])
        if message.endswith("$n"):
            print(" ".join(commandList[1:-1]), end="\n")
        elif message.endswith("$s"):
            print(" ".join(commandList[1:-1]), end=" ")
        else:
            makeException(kryoss_errors.WrongModifierException.desc, command)
    else:
        variable = findVariableByName(commandList[1])
        if (variable == None):
            print(" ".join(commandList[1:]), end="")
        else:
            variable.printValue()


def checkAskStatement(command: kryoss_classes.Command) -> bool:
    commandList = command.commandList
    if (len(commandList) != 2):
        return False
    if (commandList[0] != "ask"):
        return False
    return True


def processAskStatement(command: kryoss_classes.Command):
    commandList = command.commandList
    variable = findVariableByName(commandList[1])
    taking = input()
    try:
        if (variable.datatype == "string"):
            variable.value = taking
        if (variable.datatype == "int"):
            variable.value = int(taking)
        if (variable.datatype == "float"):
            variable.value = float(taking)
        if (variable.datatype == "boolean"):
            variable.value = bool(taking)
        if (variable.datatype == "char"):
            if (len(taking) != 1):
                raise ValueError
            else:
                variable.value = taking
        if (variable.datatype == "null"):
            variable.value = None
    except ValueError:
        makeException(kryoss_errors.InvalidValueException.desc, command)


def checkMarkStatement(command: kryoss_classes.Command) -> bool:
    commandList = command.commandList
    if (len(commandList) != 2):
        return False
    if (commandList[0] != "mark"):
        return False
    return True


def processMarkStatement(command: kryoss_classes.Command, itrNumber: int):
    commandList = command.commandList
    name = commandList[1]
    mark = findMarkByName(name)
    if (mark == None):
        marks.append(kryoss_classes.Mark(name, itrNumber))
    else:
        makeException(kryoss_errors.MarkRedefinedException.desc, command)


def checkGotoStatement(command: kryoss_classes.Command) -> bool:
    commandList = command.commandList
    if (len(commandList) != 2):
        return False
    if (commandList[0] != "goto"):
        return False
    return True


def processGotoStatement(command: kryoss_classes.Command) -> int:
    commandList = command.commandList
    mark = findMarkByName(commandList[1])
    if (mark == None):
        makeException(kryoss_errors.MarkNotFoundException.desc, command)
    mark.limit += 1
    if (mark.limit > config.infiniteRecursionLimit):
        flags[3] = config.infiniteRecursionErrorCode
        makeException(kryoss_errors.InfiniteRecursionException.desc, command)
    return mark.itrNumber


def checkCompareStatement(command: kryoss_classes.Command) -> bool:
    commandList = command.commandList
    if (len(commandList) != 3):
        return False
    if (commandList[0] != "com"):
        return False
    return True


def processCompareStatement(command: kryoss_classes.Command) -> bool:
    commandList = command.commandList
    variable1 = findVariableByName(commandList[1])
    variable2 = findVariableByName(commandList[2])
    if (variable1.datatype == "int" and variable2.datatype == "int" or
            variable1.datatype == "float" and variable2.datatype == "float"):
        if (variable1.value < variable2.value):
            flags[0] = 1
            flags[1] = 0
            flags[2] = 0
            flags[3] = 0
        elif (variable1.value > variable2.value):
            flags[0] = 0
            flags[1] = 1
            flags[2] = 0
            flags[3] = 0
        else:
            flags[0] = 0
            flags[1] = 0
            flags[2] = 1
            flags[3] = 0
    else:
        makeException(kryoss_errors.WrongTypeException.desc, command)


def checkSetStatement(command: kryoss_classes.Command) -> bool:
    commandList = command.commandList
    if (len(commandList) != 2):
        return False
    if (commandList[0] != "set"):
        return False
    return True


def processSetStatement(command: kryoss_classes.Command) -> int:
    commandList = command.commandList
    flag = commandList[1]
    if (flag == "true"):
        flags[0] = 0
        flags[1] = 0
        flags[2] = 0
        flags[3] = 1
    elif (flag == "false"):
        flags[0] = 0
        flags[1] = 0
        flags[2] = 0
        flags[3] = 0
    else:
        variable = findVariableByName(flag)
        if (variable == None):
            makeException(
                kryoss_errors.VariableNotFoundException.desc, command)
        else:
            if (variable.datatype != "boolean"):
                makeException(kryoss_errors.WrongTypeException.desc, command)
            else:
                flags[0] = 0
                flags[1] = 0
                flags[2] = 0
                if (variable.value):
                    flags[3] = 1
                else:
                    flags[3] = 0


def checkShowStatement(command: kryoss_classes.Command) -> bool:
    commandList = command.commandList
    if (len(commandList) != 2):
        return False
    if (commandList[0] != "show"):
        return False
    return True


def processShowStatement(command: kryoss_classes.Command) -> bool:
    commandList = command.commandList
    thing = commandList[1]
    if (thing == "vars"):
        showCaseVariable()
    elif (thing == "flags"):
        showCaseFlag()
    elif (thing == "stack"):
        showCaseStack()
    else:
        makeException(kryoss_errors.InvalidCommandException.desc, command)


def checkIfStatement(command: kryoss_classes.Command) -> bool:
    commandList = command.commandList
    if (len(commandList) < 4):
        return False
    if (commandList[0] != "if" and commandList[2] != "?"):
        return False
    return True


def processIfStatement(command: kryoss_classes.Command):
    commandList = command.commandList
    flag = commandList[1]
    for i in flags:
        if (i == -1):
            makeException(kryoss_errors.FlagsNotSetException.desc, command)
    check = False
    if (flag == "less"):
        check = flags[0] == 1
    elif (flag == "more"):
        check = flags[1] == 1
    elif (flag == "same"):
        check = flags[2] == 1
    elif (flag == "flag"):
        check = flags[3] == 1
    else:
        makeException(kryoss_errors.InvalidCommandException.desc, command)
    resetFlags()
    if (check):
        thenCommand = kryoss_classes.Command(
            " ".join(commandList[3:]), command.lineNumber)
        executeCommand(thenCommand)
    else:
        return


def checkPassStatement(command: kryoss_classes.Command) -> bool:
    commandList = command.commandList
    if (len(commandList) != 1):
        return False
    if (commandList[0] != "pass"):
        return False
    return True


def handleExit(command: kryoss_classes.Command) -> bool:
    commandList = command.commandList
    if (len(commandList) == 1):
        if commandList[0] == "exit":
            quit()


def checkPushStatement(command: kryoss_classes.Command) -> bool:
    commandList = command.commandList
    if (len(commandList) != 2):
        return False
    if (commandList[0] != "push"):
        return False
    return True


def processPushStatement(command: kryoss_classes.Command) -> int:
    commandList = command.commandList
    variable = findVariableByName(commandList[1])
    if (variable == None):
        makeException(kryoss_errors.VariableNotFoundException.desc, command)
    stack.append(variable)
    if (len(stack) > config.stackOverflowLimit):
        makeException(kryoss_errors.StackOverflowException.desc, command)


def checkPopStatement(command: kryoss_classes.Command) -> bool:
    commandList = command.commandList
    if (len(commandList) != 2):
        return False
    if (commandList[0] != "pop"):
        return False
    return True


def processPopStatement(command: kryoss_classes.Command) -> int:
    commandList = command.commandList
    variable = findVariableByName(commandList[1])
    if (variable == None):
        makeException(kryoss_errors.VariableNotFoundException.desc, command)
    try:
        temp = stack.pop(0)
        if (temp.datatype != variable.datatype):
            makeException(kryoss_errors.TypeMisMatchException.desc, command)
        variable.value = temp.value
    except IndexError:
        makeException(kryoss_errors.EmptyStackException.desc, command)


def executeCommand(command: kryoss_classes.Command):
    if (checkComment(command)):
        return
    elif (handleExit(command)):
        return
    elif (checkPassStatement(command)):
        return
    elif (checkMarkStatement(command)):
        return
    elif (checkGotoStatement(command)):
        flags[4] = processGotoStatement(command)
    elif (checkLetStatement(command)):
        processLetStatement(command)
    elif (checkDelStatement(command)):
        processDelStatement(command)
    elif (checkOppStatement(command)):
        processOppStatement(command)
    elif (checkCopyStatement(command)):
        processCopyStatement(command)
    elif (checkSayStatement(command)):
        processSayStatement(command)
    elif (checkAskStatement(command)):
        processAskStatement(command)
    elif (checkCompareStatement(command)):
        processCompareStatement(command)
    elif (checkSetStatement(command)):
        processSetStatement(command)
    elif (checkShowStatement(command)):
        processShowStatement(command)
    elif (checkIfStatement(command)):
        processIfStatement(command)
    elif (checkPushStatement(command)):
        processPushStatement(command)
    elif (checkPopStatement(command)):
        processPopStatement(command)
    else:
        makeException(kryoss_errors.InvalidCommandException.desc, command)


def processCommands(commands: list[kryoss_classes.Command]):
    commandCount: int = len(commands)
    for i in range(commandCount):
        command = commands[i]
        if (checkMarkStatement(command)):
            processMarkStatement(command, i)
    while (flags[4] < commandCount):
        command = commands[flags[4]]
        flags[4] += 1
        coverageList.append(command)
        executeCommand(command)


# lifecycle
fileName = initializeFileSystem()
commands: list[kryoss_classes.Command] = readFile(fileName)
initializeSimpleVariables()
processCommands(commands)
handleCoverage()
