# HarcicQQBot插件开发指南


## 目录
- [API v1(通用)](#apiv1)
- [API v2(v4.0及更高版本)](#apiv2)
- [配置插件到HarcicQQBot](#配置插件到harcicqqbot)
- [常见问题](#一部分常见问题)

## APIv1
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
（在v3.9的插件API中，process应如下定义：）
`def process(self, message: str, sender: str, is_owner: bool = False):`
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
（注：在v3.9的插件API中，`action`应写作`actions`(list类型)）
如果您的插件无意处理该消息（该消息不在您插件的处理范围内），您可以像这样返回：
~~~python
class return_:
  action = None
  msg = None
return return_()
~~~
但是，切记**Class类型的返回值是必须的**


## APIv2
以下是一个示例插件([`example_plugin2.py`](https://github.com/HarcicYang/HarcicQQBot/blob/main/example_plugin2.py))：
~~~python
from bot_lib import PluginFramework


class Plugin(PluginFramework.Base):
    def __init__(self):
        super().__init__()
        self.name = "API v2测试"
        self.cmd = None

    def handle(self, message: str, user: int, is_owner: bool = False):
        self.set.reply("Hello from API v2")
        return 0
~~~

如你所见，API v2提供了统一的API Framework，handle方法需要传入三个参数：`message`, `user`和`is_owner`。
其中：
  - `message` 为str类型，储存用户在QQ中发出的原始信息；
  - `user`为发送者QQ号；
  - `is_owner` 为bool类型，区分操作者是否拥有对机器人的管理权（是否为机器人主人）;
  - `handle`应定义在Plugin类下，`Plugin`类应继承自`PluginFramework`下的`Base`类。

`__init__()`下有如下变量可定义：
 - `self.name = "Test v2"` 插件名；
 - `self.api_version = "v2"` 插件API版本；
 - `self.cmd = ".tester"` 插件激活命令（可以为`None`）；
 - `self.helps = "Nothing is needed to be helped."` 插件帮助信息。

在操作Bot时，您可以使用`self.set.<action>()`方法：
 - `self.set.reply(message)` 回复消息；
 - `self.set.delete()` 撤回消息；
 - `self.set.mute(duration)` 禁言消息发送者；
 - `self.set.mute()` 解除消息发送者禁言；
 - `self.set.kick` 踢出消息发送者；

完成操作设置后，您应当`return 0`以通知HarcicQQBot“插件正常完成了处理”。如果操作中出现了意外错误，您可以使用`self.set.exception(message)`然后`return 1`，HarcicQQBot将进入错误处理进程。

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

## 一部分常见问题
 `ModuleNotFoundError: No module named 'xxxx'`或`ImportError: cannot import name 'xxx' from 'xxxx.xx' (DX:\xx\xx\xx\xx\xx\x\xxx\__init__.pyc)`
 解决方法：
  1. 进入自己python的安装目录，进入`\Lib\site-packages\`；
  2. 找到缺失的库文件夹并复制；
  3. 把这个库文件夹复制到HarcicQQBot存在的目录下的`.\_internal\bot_plugins\`中；
