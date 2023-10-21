import flet as ft


    
def main(page: ft.Page):
    page.scroll = "auto"

    page.fonts = {
        "Roboto Mono": "RobotoMono-VariableFont_wght.ttf",
    }
    
    #Toggler for edit

    is_editing=False 
   
    def edit_toggler():
        global is_editing  # Use nonlocal to modify the outer scope variable

        # Hide or show MarkDownInput and MarkDownOutput based on is_editing
        MarkDownInput.visible = is_editing
        MarkDownOutput.visible = not is_editing
        page.update_layout()  # Update the layout to reflect the changes
    
    def update_markdown(e):
        MarkDownOutput.value = MarkDownInput.value
        MarkDownOutput.update()

    
    
    # To create a multiline input field
    MarkDownInput = ft.TextField(label="MarkDown", 
                                 multiline=True, 
                                 autofocus=True, 
                                 border=ft.InputBorder.NONE, 
                                 filled=True, 
                                 on_change=update_markdown,
                                 visible=True
                                )                   
   
   # Passing the MarkDownInput value to Markdown module 
    MarkDownOutput = ft.Markdown(MarkDownInput.value,
            selectable=True,
            code_theme="atom-one-dark",
            code_style=ft.TextStyle(font_family="Roboto Mono"),
            extension_set="gitHubWeb",
            on_tap_link=lambda e: page.launch_url(e.data),
            visible=False)
    
    toggle_button = ft.TextButton(text="Toggle Edit Mode", on_click=edit_toggler)
    page.add(toggle_button)


    page.add(MarkDownInput)
    page.add(MarkDownOutput)


ft.app(target=main, assets_dir="assets")