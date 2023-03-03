import flet


run_loader = None

def main(page: flet.Page):
    page.title = "YouLoad"
    page.vertical_alignment = "center"
    page.window_height = 800
    page.window_width = 600


    def handle_submit(e):
        if not url_input.value:
            url_input.error_text = "Please enter URL"
            page.update()
        else:
            url_input.error_text = None
            run_loader(url_input.value, in_progress, on_complete, handle_error)
            page.update()

    def in_progress(*args):
        download_complete.value = "Download In Progress"
        page.update()

    def on_complete(*args):
        download_complete.value = "Download Complete"
        page.update()

    def handle_error(*args):
        download_complete.value = "Something went wrong, try again"
        page.update()

    url_input = flet.TextField(label="Video URL")
    download_button = flet.TextButton("Download", on_click=handle_submit)
    download_complete = flet.Text()

    page.add(flet.Column([flet.Row([url_input], alignment=flet.MainAxisAlignment.CENTER),
                          flet.Row([download_button], alignment=flet.MainAxisAlignment.CENTER),
                          flet.Row([download_complete], alignment=flet.MainAxisAlignment.CENTER)],
                         alignment=flet.MainAxisAlignment.CENTER, spacing=50))


def window():
    flet.app(target=main)


if __name__ == "__main__":
    window()
