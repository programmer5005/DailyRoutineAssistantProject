from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class DailyRoutineAssistantApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, Assistant", halign="center")


DailyRoutineAssistantApp().run()
