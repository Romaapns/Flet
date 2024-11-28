import flet as ft

def main(page: ft.Page):
    page.title = "Exemplo de Botão"


    def button_clicked(e):
        page.add(ft.Text("Clique aqui!"))

  
    btn = ft.ElevatedButton("Click me!", on_click=button_clicked)

    page.add(btn)

ft.app(target=main)