import flet


def main(page: flet.Page):
    page.title = "YouLoad"
    page.vertical_alignment = "center"
    page.window_height = 800
    page.window_width = 600


def window():
    flet.app(target=main)


if __name__ == "__main__":
    window()
