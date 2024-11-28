import flet as ft


def main(page: ft.Page):
    first_name = ft.TextField(hint_text= "Romário")
    last_name = ft.TextField(hint_text = "Araújo")

    c = ft.Column(controls=[
        first_name,
        last_name
    ])
    
    c.disabled = True 
    page.add(c)

ft.app(main)
