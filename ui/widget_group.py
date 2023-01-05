class WidgetGroup:

    def __init__(self):
        self.widgets = {}

    def add_widget(self, key, widget):
        self.widgets[key] = widget

    def remove_widget(self, key):
        del self.widgets[key]

    def render(self):
        for widget_name, widget in self.widgets.items():
            widget.draw()