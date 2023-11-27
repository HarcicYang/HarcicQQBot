# HarcicQQBot
适配OneBot协议的QQ机器人


### 基本功能：
- AI 聊天：支持腾讯混元、讯飞星火等众多模型；
- 入群欢迎
- [插件系统](https://github.com/HarcicYang/HarcicQQBot/blob/main/plugin.md) （尚在完善）

## 使用
该项目需要配合支持OneBot协议的QQ机器人框架，例如[Lagrange](https://github.com/LagrangeDev/Lagrange.Core)、[go-cqhttp](https://github.com/Mrs4s/go-cqhttp)。

### 配置文件 (config.py)
~~~ python
class data:  # 不要动
    repliedList = []
    enabledModuleList = []


class General:
    BotQQ = int("")  # 机器人的QQ号
    SelfQQ = int("")  # 你自己QQ号（这个QQ号将拥有对于Bot的管理权）
    bot_chatting = str(1)  # 聊天消息发送模式 0:使用reply事件回复 1:使用@回复 2:使用指定的命令回复（需要配置bot_chatting_cmd） QQ号:回复时@指定用户的QQ
    bot_chatting_cmd = ""
    filterList = []  # 当前被架空（悲
    default = "spark" # 默认聊天使用模型 hunyuan spark palm2 claude poe_gpt_3_5 poe_palm poe_llama poe_claude
    save_log = True # 是否保存日志
    # log_path = "" # 
    class Connection:
        type = "HTTP"  # ForwardWS HTTP , 仅使用OneBot协议时有效
        host = "0.0.0.0" # 链接地址，HTTP协议建议0.0.0.0，其他建议127.0.0.1  目前强制向127.0.0.1上报消息发送、回复等内容 (记得按需编辑control.html，一般无需)
        port = 5004  # ForwardWS协议时OneBot通过这个端口建立连接
        port_http = 5003  # HTTP协议时HarcicQQBot通过这个端口向OneBot发送命令
        port_rev = 5002  # HTTP协议时OneBot向这个端口上报消息



class OpenAIOAPI:  # OpenAI官方API（因为付费制度被架空
    desc = "OpenAI_API"
    enabled = False
    key = ""


class OpenAIWeb:  # ChatGPT逆向工程API（因为Pyinstaller原因被架空 https://github.com/acheong08/ChatGPT
    desc = "ChatGPT_Web"
    enabled = False
    email = ""
    password = ""
    conversation_id = ""


class Palm:  # Google Makersuite API （官方）
    desc = "Palm2_API"
    enabled = False
    key = ""


class Claude:  # Claude逆向工程API 配置参考：https://github.com/wwwzhouhui/Claude2-PyAPI
    desc = "Claude_Web"
    enabled = False
    conversation_id = ""
    cookies = ""

class Spark:  # 讯飞星火逆向工程API 配置参考：https://github.com/HildaM/sparkdesk-api
    desc = "Spark_Web"
    enabled = True
    cookie = ""
    fd = ""
    gttoken = ""
    chat_id = ""


class StabilityDrawAPI:  # Stability API （官方）
    desc = "Drawing_API"
    enabled = True
    key = ""


class Poe:  # Poe逆向工程API 配置参考：https://github.com/snowby666/poe-api-wrapper
    class Bots:
        GPT_3_5_Turbo = "gpt3_5"
        PaLM = "acouchy"
        Llama = "llama_2_70b_chat"
        Claude = "a2"
        WebSearch = "websearch"
        Draw = "stablediffusionxl"

    desc = "poe_chats"
    enabled = False
    cookie = ""

class HunYuan:  # 腾讯混元逆向工程API 配置参考：https://github.com/HarcicYang/rev_HunYuan
    desc = "HunYuan"
    enabled = True
    cookie = ""

class Hypixel:  # 查询Hypixel玩家信息 https://api.hypixel.net/
    desc = "Hypixel_Info"
    enabled = True
    key = ""

~~~

### 群内操作（命令系统）
- 基本：
  - 与AI机器人聊天 .chat {message}
  - 设置AI机器人聊天使用的模型
    - .claude
    - .palm2
    - .spark
    - .hunyuan
    - .poe_gpt3.5
    - .poe_palm
    - .poe_llama
    - .poe_claude
  - 设置Bot回复模式 .bot_chatting {0/1/2} {cmd(第一个参数为2时需要指定)}
  - 获取当前信息 .info
  - 查询Hypixel玩家信息 .hypixel {PlayerName} （需要配置Hypixel API Key）
  - AI画图 .draw {prompt} (需要配置StabilityDrawAPI)
  - 发送群消息 .alert {group_id} {message}
  - 插件相关 .plugins
