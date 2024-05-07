'''
Design a logger system that receives a stream of messages along with their timestamps. Each unique message should only be printed at most every 10 seconds (i.e. a message printed at timestamp t will prevent other identical messages from being printed until timestamp t + 10).

All messages will come in chronological order. Several messages may arrive at the same timestamp.

Implement the Logger class:

Logger() Initializes the logger object.
bool shouldPrintMessage(int timestamp, string message) Returns true if the message should be printed in the given timestamp, otherwise returns false.


Example 1:

Input
["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage"]
[[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
Output
[null, true, true, false, false, false, true]

'''

class Logger:

    def __init__(self):
        self.msgDict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:

        if self.msgDict.__contains__(message):
            timee = self.msgDict.get(message)
            if timee > timestamp:
                return False
            else:
                self.msgDict[message] = timestamp + 10
                return True
        else:
            self.msgDict[message] =  timestamp + 10
            return True

        # Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)