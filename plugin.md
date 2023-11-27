# HarcicQQBot插件开发指南


以下是一个示例插件（[`example_plugin1.py`](https://github.com/HarcicYang/HarcicQQBot/blob/main/example_plugin1.py)）
~~~python
class Info:
    name = "Test Plugin"
    version = "0.1"
    author = "Harcic"
    desc = "A test plugin"
    cmd = ".test"
    helps = "没什么可写的帮助信息"


class Main:
    def process(self, message: str, isOwner: bool = False):
        if Info().cmd in message:
            message = message.split(" ")
            args = [message[2], message[3]]
            if isOwner:
                result = str(args) + "IN: " + Info.name + "  你拥有管理权"
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

~~~

其中：
### 定义插件
您需要在插件文件中定义一个名为`Info`的类，用于储存插件基本信息。
~~~python
class Info:
    name = "" # 插件名称
    version = "" # 插件版本
    author = "" # 插件开发者
    desc = "" # 对插件的描述
    cmd = "" # 激活插件功能需要的命令（或关键词，建议包含"."）
    helps = "" # 插件的使用帮助信息
~~~
### 处理消息

接下来，在同一文件中定义`Main`类，并在该类下定义`process`方法：
~~~python
class Main:
    def process(self, message: str, isOwner: bool = False):
      # your codes here......
    def func(self, arg1, arg2 ......):
      # your own functions
~~~
如你所见，process方法需要传入两个参数：`message`和`isOwner`。
其中：
  - `message` 为str类型，储存用户在QQ中发出的原始信息；
  - `isOwner` 为bool类型，区分操作者是否拥有对机器人的管理权（是否为机器人主人）;
### 返回结果
您需要让`process`方法返回一个类。
~~~python
class return_:
  action = "reply"
  msg = result
return return_()
~~~
其中：
  - `action`为需要进行的操作，目前有如下可用的类型：
    - `reply`：正常回复；
    - `kick`：踢出发送该消息的QQ用户并回复；
    - `mute`：禁言发送该消息的QQ用户并回复；
  - `msg`为要回复的内容
如果您的插件无意处理该消息（该消息不在您插件的处理范围内），您可以像这样返回：
~~~python
class return_:
  action = None
  msg = None
return return_()
~~~
但是，切记**Class类型的返回值是必须的**

### 配置插件到HarcicQQBot
1. 找到HarcicQQBot的存在目录；
2. 进入`.\_internal\bot_plugins\`，把插件放进去（`.py`或`.pyc`文件）；
3. 编辑`bot_plugins`下的`__init__.py`:
  ~~~python
  from bot_plugins import plugin1
  from bot_plugins import plugin2
  ......

  plugins = [plugin1, plugin2, ......]
  ~~~

### 一部分常见问题
 `ModuleNotFoundError: No module named 'xxxx'`或`ImportError: cannot import name 'xxx' from 'xxxx.xx' (DX:\xx\xx\xx\xx\xx\x\xxx\__init__.pyc)`
 解决方法：
  1. 进入自己python的安装目录，进入`\Lib\site-packages\`；
  2. 找到缺失的库文件夹并复制；
  3. 把这个库文件夹复制到HarcicQQBot存在的目录下的`.\_internal\bot_plugins\`中；
