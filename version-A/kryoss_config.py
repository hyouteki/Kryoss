class KryossConfig():
    def __init__(this):
        this.infiniteRecursionLimit = 1000
        this.infiniteRecursionErrorCode = 9
        this.stackOverflowLimit = 100
        this.stackOverflowErrorCode = 8

    def setInfiniteRecursionLimit(this, value):
        this.infiniteRecursionLimit = value

    def setStackOverflowLimit(this, value):
        this.infiniteRecursionLimit = value
