import flet as ft


    
def main(page: ft.Page):
    page.scroll = "auto"

    page.fonts = {
        "Roboto Mono": "RobotoMono-VariableFont_wght.ttf",
    }
    
    #Toggler for edit

    is_editing=False 
   
    

    
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
    
    def edit_toggler(e):
        global is_editing  # Use nonlocal to modify the outer scope variable

        # Hide or show MarkDownInput and MarkDownOutput based on is_editing
        
        if(MarkDownOutput.visible):
            MarkDownOutput.visible=False
            MarkDownInput.visible=True
            toggle_button.text = "Preview"
            page.update()
        else:
            MarkDownOutput.visible=True 
            MarkDownInput.visible=False
            toggle_button.text = "Edit"
            page.update()
        # page.update_layout()  # Update the layout to reflect the changes


    toggle_button = ft.TextButton(text="Preview", on_click=edit_toggler)
    page.add(toggle_button)


    page.add(MarkDownInput)
    page.add(MarkDownOutput)


ft.app(target=main, assets_dir="assets", port=5000,view=ft.AppView.WEB_BROWSER )
