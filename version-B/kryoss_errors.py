class InvalidTerminalCommandException(Exception):
    def handleException():
        print(f"Exception occurced at terminal command")
        print(f"Already messed up with the compile command sigh...")
        print(f"Reason: wrong number of arguments passed")
        quit()


class InvalidFileException(Exception):
    def handleException():
        print(f"Exception occurced at terminal command")
        print(f"Already messed up with the file name sigh...")
        print(f"Reason: file name is invalid")
        quit()


class CoverageCannotWriteException(Exception):
    def handleException():
        print(f"Exception occurced while opening coverage file")
        print(f"Don't know the issue")
        print(f"Reason: No clue")
        quit()


class InvalidValueException(Exception):
    name = "InvalidValueException"
    desc = "variable value does not match with the type specified"
    pass


class VariableNotFoundException(Exception):
    name = "VariableNotFoundException"
    desc = "variable not initialized or already deleted"
    pass


class MarkNotFoundException(Exception):
    name = "MarkNotFoundException"
    desc = "mark not initialized or already deleted"
    pass


class TypeMisMatchException(Exception):
    name = "TypeMisMatchException"
    desc = "variable datatype is mismatch"
    pass


class InvalidCommandException(Exception):
    name = "InvalidCommandException"
    desc = "wrong command"
    pass


class MarkRedefinedException(Exception):
    name = "MarkRedefinedException"
    desc = "redefining the mark variable"
    pass


class InfiniteRecursionException(Exception):
    name = "InfiniteRecursionException"
    desc = f"calling the same mark more than specified[default = 1000] times"
    pass


class WrongTypeException(Exception):
    name = "WrongTypeExceptions"
    desc = "wrong datatype found"
    pass


class FlagsNotSetException(Exception):
    name = "FlagsNotSetException"
    desc = "flags not set or resetted at some point"
    pass


class EmptyStackException(Exception):
    name = "EmptyStackException"
    desc = "cannot pop from an empty stack"
    pass


class StackOverflowException(Exception):
    name = "StackOverflowException"
    desc = "stack overflowed"
    pass


class ZeroDivisionException(Exception):
    name = "ZeroDivisionException"
    desc = "dividing by zero"
    pass


class WrongModifierException(Exception):
    name = "WrongModifierException"
    desc = "only $n and $s modifiers are allowed"
    pass


class WrongLimitException(Exception):
    name = "WrongLimitException"
    desc = "adding a wrong limit value"
    pass


class WrongConfigException(Exception):
    name = "WrongConfigException"
    desc = "found a wrong config name"
    pass
