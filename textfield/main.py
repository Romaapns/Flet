import flet as ft

def main(page: ft.Page):
    
    def atualizar_estilos(e):
        # Atualizar  TextField com base nas escolhas
        text_field.border_color = dropdown_border_color.value
        text_field.fill_color = dropdown_fill_color.value
        text_field.border_radius = int(dropdown_border_radius.value)
        text_field.text_style = ft.TextStyle(
            size=int(dropdown_text_size.value),
            font_family=dropdown_font_family.value,
            color=dropdown_text_color.value,
        )
        text_field.cursor_color = dropdown_cursor_color.value
        page.update()

    # textfield que sera mostrado aqui
    text_field = ft.TextField(
        label="TextField",
        hint_text="Personalize-me!",
        width=400,
        border_radius=5,
        fill_color="lightgray",
        border_color="blue",
        text_style=ft.TextStyle(size=16, color="black", font_family="Arial"),
    )

    #  estilizar o TextField
    dropdown_border_color = ft.Dropdown(
        label="Cor Borda",
        options=[
            ft.dropdown.Option("blue", "Azul"),
            ft.dropdown.Option("purple", "Roxo"),
            ft.dropdown.Option("green", "Verde"),
            ft.dropdown.Option("black", "Preto"),
        ],
        value="blue",
        on_change=atualizar_estilos,
    )

    dropdown_fill_color = ft.Dropdown(
        label="Cor Preenchimento",
        options=[
            ft.dropdown.Option("lightgray", "Cinza Claro"),
            ft.dropdown.Option("white", "Branco"),
            ft.dropdown.Option("yellow", "Amarelo"),
            ft.dropdown.Option("pink", "Rosa"),
        ],
        value="lightgray",
        on_change=atualizar_estilos,
    )

    dropdown_border_radius = ft.Dropdown(
        label="Arredondamento Borda (px)",
        options=[
            ft.dropdown.Option("0", "Sem borda arredondada"),
            ft.dropdown.Option("5", "5px"),
            ft.dropdown.Option("10", "10px"),
            ft.dropdown.Option("20", "20px"),
        ],
        value="5",
        on_change=atualizar_estilos,
    )

    dropdown_text_size = ft.Dropdown(
        label="Tamanho Texto (px)",
        options=[
            ft.dropdown.Option("12", "12px"),
            ft.dropdown.Option("16", "16px"),
            ft.dropdown.Option("20", "20px"),
            ft.dropdown.Option("24", "24px"),
             ft.dropdown.Option("32", "32px"),
        ],
        value="16",
        on_change=atualizar_estilos,
    )

    dropdown_cursor_color = ft.Dropdown(
        label="Cor Cursor",
        options=[
            ft.dropdown.Option("black", "Preto"),
            ft.dropdown.Option("blue", "Azul"),
            ft.dropdown.Option("red", "Vermelho"),
            ft.dropdown.Option("green", "Verde"),
        ],
        value="black",
        on_change=atualizar_estilos,
    )

    dropdown_font_family = ft.Dropdown(
        label="Fonte Texto",
        options=[
            ft.dropdown.Option("Arial", "Arial"),
            ft.dropdown.Option("Courier New", "Courier New"),
            ft.dropdown.Option("Times New Roman", "Times New Roman"),
            
        ],
        value="Arial",
        on_change=atualizar_estilos,
    )

    dropdown_text_color = ft.Dropdown(
        label="Cor Texto",
        options=[
            ft.dropdown.Option("black", "Preto"),
            ft.dropdown.Option("blue", "Azul"),
            ft.dropdown.Option("red", "Vermelho"),
            ft.dropdown.Option("green", "Verde"),
            ft.dropdown.Option("purple", "Roxo"),
        ],
        value="black",
        on_change=atualizar_estilos,
    )

    page.title = "Editor de TextField com Fontes, Cores e Tamanhos"
    page.add(
        text_field,
        ft.Divider(),
        ft.Text("Estilize o TextField usando as opções abaixo:", size=18),
        dropdown_border_color,
        dropdown_fill_color,
        dropdown_border_radius,
        dropdown_text_size,
        dropdown_cursor_color,
        dropdown_font_family,
        dropdown_text_color,
    )

ft.app(target=main)
