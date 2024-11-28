import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora de Conta"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    itens = {
        1: {"descricao": "Cachorro Quente", "preco": 4.00},
        2: {"descricao": "X-Salada", "preco": 4.50},
        3: {"descricao": "X-Bacon", "preco": 5.00},
        4: {"descricao": "Torrada Simples", "preco": 2.00},
        5: {"descricao": "Refrigerante", "preco": 1.50},
    }

    lanche_selecao = ft.RadioGroup(
        content=ft.Column(
            [
                ft.Radio(value=1, label="Cachorro Quente - R$ 4.00"),
                ft.Radio(value=2, label="X-Salada - R$ 4.50"),
                ft.Radio(value=3, label="X-Bacon - R$ 5.00"),
                ft.Radio(value=4, label="Torrada Simples - R$ 2.00"),
                ft.Radio(value=5, label="Refrigerante - R$ 1.50"),
            ]
        )
    )

    quantidade_slider = ft.Slider(
        min=1, max=20, divisions=20, label="{value}", width=300
    )

    resultado_texto = ft.Text(value="", size=18)

    def calcular_total(e):
        try:
            codigo = int(lanche_selecao.value)
            quantidade = int(quantidade_slider.value)

            if codigo in itens:
                preco = itens[codigo]["preco"]
                total = preco * quantidade
                resultado_texto.value = (
                    f"Item: {itens[codigo]['descricao']}\n"
                    f"Quantidade: {quantidade}\n"
                    f"Total  R$ {total:.2f}"
                )
            else:
                resultado_texto.value = "Selecione um lanche válido!"
        except TypeError:
            resultado_texto.value = "Escolha um lanche!"

        page.update()

    calcular_btn = ft.ElevatedButton(
        text="Calcular preço total",
        on_click=calcular_total
    )

    page.add(
        ft.Column(
            [
                ft.Text("Selecione o lanche:", size=16),
                lanche_selecao,
                ft.Text("Quantidade De Lanches:", size=16),
                quantidade_slider,
                calcular_btn,
                resultado_texto,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
