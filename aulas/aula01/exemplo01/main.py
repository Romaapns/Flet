import flet as ft


def main(page: ft.Page):
  t = ft.Text(value='Ola Mundo!', color = 'green')
  page.controls.append(t)
  page.update()


ft.app(main)
