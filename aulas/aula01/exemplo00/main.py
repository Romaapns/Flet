import flet as ft

from controles_estilizados import Mybutton


def main (page: ft.page):
    page.add(
       Mybutton("Ok"),
       MyButton("Cancel")
    )
    
ft.app(main)
