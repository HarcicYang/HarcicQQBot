class Info:
    name = "Test Plugin"
    version = "0.1"
    author = "Harcic"
    desc = "A test plugin"
    # active = "command"
    cmd = ".test"
    helps = "没什么可写的帮助信息"

times = 0

class Main:
    def process(self, message: str, isOwner: bool = False):
        global times
        if Info().cmd in message:
            message = message.split(" ")
            args = [message[2], message[3]]
            times += 1
            if isOwner:
                result = str(args) + "IN: " + Info.name + "  你拥有管理权" + str(times)
            else:
                result = str(args) + "IN: " + Info.name + "  你不拥有管理权"
            class return_:
                action = "reply"
                msg = result
        else:
            class return_:
                action = None
                msg = None
        return return_()
