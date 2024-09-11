import flet as ft


def main(page: ft.Page):
page.title="¿Me perdonas?"
page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
page.vertical_alignment=ft.MainAxisAlignment.CENTER
page.bgcolor="blue"

lbl1=ft.text("¿Me perdonas?",
            style=ft.TextStyle (size=40,weight="bold"))

img1=ft(src="triste.png",width=200,heiht=200)


btnSI=ft.ElevatedButton("SI"
                        color="green",
                        widht=100,
                        height=50)


btnNO=ft.ElevatedButton("NO"
                        color="orange",
                        widht=100,
                        height=50)

def no(e):
    btnSI.width+=30
    btnNO.height+10
    page.update()


def SI(e):
    img1.src="feliz.png"
    page.update()

btnSI.on_click=SI
btnNO.on_click=no 

page.add(
    ft.column(
        [
            lbl1,
            img1,
            ft.Row([btnSI,btnNO],
                alignment=ft.MainAxisAlignment.CENTER,
                ),
            
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20
        
        
    )
    
)

ft.app(main)