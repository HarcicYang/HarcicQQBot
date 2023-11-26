import numpy

class Info:
    name = "三角函数"
    version = "0.1"
    author = "Harcic"
    desc = "一个用于计算三角函数的插件"
    active = "command"
    cmd = ".triangle"
    helps = ("计算三角函数\n.triangle <sin/cos/tan/csc/sec/cot> <degree>")


class Main:
    def process(self, message: str, isOwner: bool = False):
        if Info().cmd in message:
            message = message.split(" ")
            mode, degree = message[2], message[3]
            if mode == "sin":
                result = numpy.sin(numpy.radians(float(degree)))
            elif mode == "cos":
                result = numpy.cos(numpy.radians(float(degree)))
            elif mode == "tan":
                result = numpy.tan(numpy.radians(float(degree)))
            elif mode == "csc":
                result = 1 / numpy.sin(numpy.radians(float(degree)))
            elif mode == "sec":
                result = 1 / numpy.cos(numpy.radians(float(degree)))
            elif mode == "cot":
                result = 1 / numpy.tan(numpy.radians(float(degree)))
            else:
                result = "未知的模式"
            class return_:
                action = "reply"
                msg = result
        else:
            class return_:
                action = None
                msg = None
        return return_()

