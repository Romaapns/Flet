import flet as ft
import time

def main(page: ft.Page):
  t = ft.Text()
  page.add(t)


  for i in range(10):
    t.value = f"Passo: {i}"
    page.update()
    time.sleep(1)


ft.app(main)
