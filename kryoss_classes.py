class Command:
    def __init__(this, commandString: str, lineNumber: int):
        this.commandString = commandString
        this.withoutLineBreakCommand = ""
        this.isNullCommand = False
        this.commandList = []
        if commandString.endswith("\n"):
            this.commandList = commandString[:-1].split()
            this.withoutLineBreakCommand = commandString[:-1]
        else:
            this.commandList = commandString.split()
            this.withoutLineBreakCommand = commandString
        this.lineNumber = lineNumber
        if len(this.commandList) == 0:
            this.isNullCommand == True

    def __str__(this):
        return f"{this.lineNumber}: {this.withoutLineBreakCommand}"


class Variable:
    def __init__(this, name: str, datatype: str, value=None):
        this.name = name
        this.datatype = datatype
        this.value = value

    def __str__(this):
        if (this.value == None):
            return f"{this.name}: {this.datatype} = null"
        else:
            return f"{this.name}: {this.datatype} = {this.value}"

    def printValue(this):
        if (this.value == None):
            print("null")
        else:
            print(this.value)

class Mark:
    def __init__(this, name: str, itrNumber: int):
        this.name = name
        this.itrNumber = itrNumber
        this.limit = 0
