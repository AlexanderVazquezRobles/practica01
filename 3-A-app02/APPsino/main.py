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


page.add(
    ft.column(
        [
            lbl1,
            img1,
            ft.Row([btnSI,btnNO])
        ]
    )
    
)

ft.app(main)