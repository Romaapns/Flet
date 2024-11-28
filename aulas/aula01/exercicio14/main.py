import flet as ft

def main(page: ft.Page):
 
    first_name = ft.TextField(hint_text="First Name")
    last_name = ft.TextField(hint_text="Last Name")

  
    c = ft.Column(controls=[
        first_name,
        last_name
    ])

  
    c.disabled = True

    page.add(c)

ft.app(main)