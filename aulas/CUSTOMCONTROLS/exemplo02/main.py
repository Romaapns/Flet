import flet as ft
class Task(ft.Row):
    def __init__(self, text):
        super().__init__() 
        self.text_view = ft.Text(text)#Um componente de texto que exibe a descrição da tarefa.
        self.text_edit = ft.TextField(text, visible=False) #Um campo de texto que permite editar a tarefa. Ele é inicialmente invisível (visible=False).
        self.edit_button = ft.IconButton(icon=ft.icons.EDIT, on_click=self.edit)#botão com ícone de edição 
        self.save_button = ft.IconButton(visible=False, icon=ft.icons.SAVE, on_click=self.save)#botão de salvar
        self.controls = [
            ft.Checkbox(),
            self.text_view,
            self.text_edit,
            self.edit_button,
            self.save_button,
        ]#Uma lista de controles que inclui uma caixa de seleção para marcar a tarefa como concluída, 
        #a visualização de texto, o campo de edição, e os botões de editar e salvar.

    def edit(self, e): #E
        self.edit_button.visible = False
        self.save_button.visible = True
        self.text_view.visible = False
        self.text_edit.visible = True
        self.update()

    def save(self, e):
        self.edit_button.visible = True
        self.save_button.visible = False
        self.text_view.visible = True
        self.text_edit.visible = False
        self.text_view.value = self.text_edit.value
        self.update()

def main(page: ft.Page):

    page.add(
        Task(text="Fazer site"),
        Task(text="Comprar presente pro namorado"),
    )


ft.app(main)