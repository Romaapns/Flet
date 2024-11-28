import flet as ft


def main(page: ft.Page):
    page.title = "Exemplo de Botão"

    def button_clicked(e):
      page.add(ft.Text("Clicado"))

    page.add(ft.ElevatedButton(text='Clique aqui', on_click=button_clicked))

ft.app(main)
