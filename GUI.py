import flet as ft

def main(page: ft.Page):
    def button_clicked(e):
        t.value = f"Ban la: {tb1.value} {tb2.value} hoc lop {tb3.value} khoa {tb4.value}"
        page.update()

    page.window_width = 300
    page.window_height = 600
    # page.window_resizable = True
    t = ft.Text()
    tb1 = ft.TextField(label="Nhap ho cua ban")
    tb2 = ft.TextField(label="Nhap ten cua ban")
    tb3 = ft.TextField(label="Nhap lop cua ban")
    tb4 = ft.TextField(label="Nhap khoa cua ban")
    btn = ft.ElevatedButton(text = "OK",on_click=button_clicked)
    page.add(tb1,tb2,tb3,tb4,btn,t)

ft.app(main)