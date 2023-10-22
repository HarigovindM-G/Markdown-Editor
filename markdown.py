import flet as ft


    
def main(page: ft.Page):
    
    help='''
1. Editing Mode: Start typing your Markdown content in this area.

2. Toggle Mode: Click "Edit" to switch between editing and preview modes.

3. Markdown Syntax: Use Markdown formatting like **bold**, *italic*, [links](http://example.com).

4. Code Blocks: Create code blocks with triple backticks (```).

5. Lists: Make ordered (1., 2., 3.) and unordered (*, -) lists.

Enjoy writing and formatting your content!

'''


    page.scroll = "auto"

    page.fonts = {
        "Roboto Mono": "RobotoMono-VariableFont_wght.ttf",
    }
    
    #Toggler for edit

    is_editing=False 
   
    

    
    def update_markdown(e):
        MarkDownOutput.value = MarkDownInput.value
        MarkDownOutput.update()

    
    
    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()

    dlg = ft.AlertDialog(
        title=ft.Text('Markdown Editor Help'), content=ft.Text(help)
        
    )
    
    help_button = ft.TextButton(text="Help", on_click=open_dlg)

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
    

    page.add(

        ft.Row(
            [
                ft.Container(content=toggle_button),
                ft.Container(content=help_button)
            ],
            alignment=ft.MainAxisAlignment.END,
        ),
        
    )
  
    page.add(MarkDownInput)
    page.add(MarkDownOutput)


ft.app(target=main, assets_dir="assets")





