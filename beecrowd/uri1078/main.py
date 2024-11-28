import flet as ft

def main(page: ft.Page):
    
    def gerar_tabuada(n):
        return [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(f"{i} x {n}")),
                    ft.DataCell(ft.Text(f"= {i * n}")),
                ]
            )
            for i in range(1, 11)
        ]

    
    entrada = ft.TextField(label="Digite um número (Sendo ele maior que dois e menor que 1000)", width=350)

    
    tabela_tabuada = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Operação")),
            ft.DataColumn(ft.Text("Resultado")),
        ],
        rows=[],
    )

    
    def on_click(e):
        try:
            n = int(entrada.value)
            if 2 < n < 1000:
                tabela_tabuada.rows = gerar_tabuada(n)
                page.update()
            else:
                page.snack_bar = ft.SnackBar(ft.Text("Número fora do intervalo!"))
                page.snack_bar.open = True
                page.update()
        except ValueError:
            page.snack_bar = ft.SnackBar(ft.Text("Digite um número válido!"))
            page.snack_bar.open = True
            page.update()

    # Botão tabuada
    botao = ft.ElevatedButton("Gerar Tabuada", on_click=on_click)

    
    page.add(entrada,
 botao, 
tabela_tabuada)


ft.app(target=main)


