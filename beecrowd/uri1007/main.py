import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora de Diferença"

    #Entrada para dos valores 
    input_a = ft.TextField(label="Valor A", width=200)
    input_b = ft.TextField(label="Valor B", width=200)
    input_c = ft.TextField(label="Valor C", width=200)
    input_d = ft.TextField(label="Valor D", width=200)

    
    def calcular_diferenca(e):
        try:
            a = int(input_a.value)
            b = int(input_b.value)
            c = int(input_c.value)
            d = int(input_d.value)
            
            diferenca = (a * b) - (c * d)
            resultado.value = f"DIFERENCA = {diferenca}"
            page.update()
        except ValueError:
            resultado.value = "Por favor, insira apenas números inteiros."
            page.update()

   #botao de calcular
    botao_calcular = ft.ElevatedButton("Calcular", on_click=calcular_diferenca)

    #mostrar o resultado
    resultado = ft.Text(value="", size=20)

   
    page.add(
        ft.Column(
            [
                input_a,
                input_b,
                input_c,
                input_d,
                botao_calcular,
                resultado,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
