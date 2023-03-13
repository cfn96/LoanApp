from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.list import MDList
from db_init import loadrecord
from kivy.uix.screenmanager import Screen, ScreenManager


# load customers
customer_record = loadrecord("customer")


class MainMenu(Screen):
    pass


class SettingsMenu(Screen):
    pass


class MainApp(MDApp):

    def build(self):
        self.title = "Listahan ng Utang App"
        # Add other widgets to the app here
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file("main.kv")

    def on_start(self):
        for customer in customer_record:
            record_list = TwoLineListItem(text=customer[1],
                                          secondary_text='{:.2f}'.format(customer[2]))
            record_list.bind(
                on_release=lambda record_list=record_list: self.print_id(record_list))

            record_list_widget = self.root.ids.container.add_widget(
                record_list)

        # return super().on_start()

    def print_id(self, widget):
        print(widget.text)


if __name__ == "__main__":
    MainApp().run()
