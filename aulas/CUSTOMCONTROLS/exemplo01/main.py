import flet as ft

class MyButton(ft.ElevatedButton):
    def __init__(self, text, clicar):
        super().__init__()
        self.bgcolor = ft.colors.YELLOW_300
        self.color = ft.colors.RED_800
        self.text = text
        self.clicar = clicar

def main(page: ft.Page):

    def clicou(e):
        print("Clicou")
    
    def não_clicou(e):
        print("Não clicou")

    page.add(
        MyButton(text="Sim", clicar=clicou),
        MyButton(text="Não", clicar=não_clicou),
    )

ft.app(main)
