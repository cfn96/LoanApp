from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import TwoLineListItem
from db_init import loadrecord

# load customers
customer_record = loadrecord("customer")


class MainApp(MDApp):
    def build(self):
        self.title = "Listahan ng Utang App"
        # Add other widgets to the app here
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file("main.kv")

    def on_start(self):
        for customer in customer_record:
            self.root.ids.container.add_widget(
                TwoLineListItem(text=customer[1],
                                secondary_text='{:.2f}'.format(customer[2]))
            )
        return super().on_start()


if __name__ == "__main__":
    MainApp().run()