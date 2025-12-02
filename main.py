import flet as ft
from flet import TextField
from flet_core.control_event import ControlEvent


def main(page: ft.Page):
    page.title = 'Increment Counter'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = 'dark'

    text_number: TextField = TextField(value='0', text_align=ft.TextAlign.RIGHT, width=70)
    
    def decrement(e: ControlEvent):
        text_number.value = str(int(text_number.value) - 1)
        page.update()

    def increment(e: ControlEvent):
        text_number.value = str(int(text_number.value) + 1)
        page.update()

    
    page.add(
        ft.Row(
            [ft.IconButton(ft.Icons.REMOVE, on_click=decrement),
             text_number,
             ft.IconButton(ft.Icons.ADD, on_click=increment)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)