import flet as ft


def main(page: ft.Page):
    page.title = 'URI 1001'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    page.adaptive = True

    titulo =  ft.Text(
        "URI 1001", theme_style=ft.TextThemeStyle.DISPLAY_LARGE
        )

    num01 = ft.TextField(
        label="Digite apenas números",
        input_filter=  ft.NumbersOnlyInputFilter(), #Apenas numeros
        autofocus= True
    )

    num02 = ft.TextField(
        label="Digite apenas números",
        input_filter=  ft.NumbersOnlyInputFilter(), #Apenas numeros
    )

    resultado = ft.Text()

    def somar(e):
        n1 = int(num01.value)
        n2 = int(num02.value)
        print(f'Soma = {n1+n2}')
        resultado.value = f'Soma = {n1+n2}'
        page.update()

    botao_somar = ft.ElevatedButton("SOMAR", on_click=somar)

    page.add(ft.Column(controls = [titulo, num01,num02, botao_somar,resultado,]) )



ft.app(main)
