import flet as ft
from controles_estilizados import MyButton

def main(page: ft.Page):

    page.add(MyButton(text="OK"), MyButton(text="Cancel"))

ft.app(main)
