from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.button import MDFlatButton
from kivymd.uix.list import MDList
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.segmentedcontrol import MDSegmentedControl, MDSegmentedControlItem
from db_init import loadrecord
from kivy.uix.screenmanager import Screen, ScreenManager

# load customers
customer_record = loadrecord("customer")


class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)


class MainMenu(Screen):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.current_filter = MDSegmentedControlItem(
            text="Current",
        )
        self.paid_filter = MDSegmentedControlItem(
            text="Paid",
        )
        self.all_filter = MDSegmentedControlItem(
            text="All",
        )
        self.segmented_control = MDSegmentedControl(
            self.current_filter,
            self.paid_filter,
            self.all_filter,
            pos_hint={"center_x": 0.5, "center_y": 0.9}
        )

        self.add_widget(self.segmented_control)
        self.segmented_control.bind(
            on_active=lambda x, y: self.print_selected(self.segmented_control.current_active_segment))

        list_scroll_view = MDScrollView(
            pos_hint={"center_x": 0.5, "center_y": 0.35}
        )
        listing = MDList()
        for customer in customer_record:
            record_list = TwoLineListItem(
                text=customer[1],
                secondary_text='{:.2f}'.format(customer[2])
            )
            listing.add_widget(record_list)
            # record_list.bind(
            #     on_release=lambda record_list: self.print_selected(
            #         record_list)
            # )
            record_list.bind(
                on_release=lambda x: self.updateform()
            )

        list_scroll_view.add_widget(listing)
        self.add_widget(list_scroll_view)

    def print_selected(self, widget):
        print(widget.text)

    def updateform(self):
        self.manager.transition.direction = "left"
        self.manager.current = "update_form"


class UpdateForm(Screen):
    def __init__(self, **kwargs):
        super(UpdateForm, self).__init__(**kwargs)
    # back_button = MDFlatButton(
    #     text="Back",
    #     on_release=lambda x: self.mainmenu()
    # )
        self.add_widget(MDFlatButton(
            text="Back",
            on_release=lambda x: self.mainmenu()
        ))

    def mainmenu(self):
        self.manager.transition.direction = "right"
        self.manager.current = "main_menu"


class MainApp(MDApp):

    def build(self):
        self.title = "Listahan ng Utang App"
        # Add other widgets to the app here
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file("main.kv")


if __name__ == "__main__":
    MainApp().run()
