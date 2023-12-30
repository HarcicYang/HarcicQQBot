from bot_lib import PluginFramework


class Plugin(PluginFramework.Base):
    def __init__(self):
        super().__init__()
        self.name = "API v2测试"
        self.cmd = None

    def handle(self, message: str, user: int, is_owner: bool = False):
        self.set.reply("Hello from API v2")
        return 0
