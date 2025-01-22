from textual.app import App
from textual.widgets import Label, SelectionList


class BorderTitleAlignApp(App):
    CSS_PATH = "styles.tcss"

    def on_mount(self) -> None:
        self.theme = "gruvbox"

    def compose(self):
        lbl = Label("My title is on the left.")
        lbl.border_title = "Focus"
        yield lbl

        sel = SelectionList()
        lbl.border_title = "Tasks"
        yield lbl


if __name__ == "__main__":
    app = BorderTitleAlignApp()
    app.run()
