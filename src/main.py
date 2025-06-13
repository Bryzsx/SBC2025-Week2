import flet as ft
from flet import Icons  # <--- Correct for your version!

def main(page: ft.Page):
    page.title = "Bryce A. Corvera"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#121212"
    selected_tab = {"name": "home"}
    bottom_nav_container = ft.Container()

    def nav_button(tab_name, label, icon_):
        sel = selected_tab["name"] == tab_name
        return ft.GestureDetector(
            on_tap=lambda e: change_tab(tab_name),
            content=ft.Container(
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=4,
                    controls=[
                        ft.Icon(icon_, size=26, color="white" if sel else "#9e9e9e"),
                        ft.Text(label, color="white" if sel else "#9e9e9e", size=12)
                    ]
                ),
                padding=ft.padding.symmetric(horizontal=16, vertical=8),
                bgcolor="#1e88e5" if sel else None,
                border_radius=20
            ),
            expand=True
        )

    def render_bottom_nav():
        bottom_nav_container.content = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                nav_button("home", "Home", Icons.HOME),
                nav_button("chat", "Chat", Icons.CHAT),
                nav_button("settings", "Settings", Icons.SETTINGS)
            ])
        bottom_nav_container.update()

    def change_tab(tab_name): selected_tab["name"] = tab_name; render_bottom_nav()

    bottom_nav_container.bgcolor = "#1e1e1e"; bottom_nav_container.height = 70
    bottom_nav_container.border_radius = ft.border_radius.only(top_left=12, top_right=12)
    bottom_nav_container.border = ft.Border(top=ft.BorderSide(1, "#333"))
    bottom_nav_container.padding = ft.padding.symmetric(horizontal=10)

    header = ft.Container(
        content=ft.Row(
            vertical_alignment=ft.CrossAxisAlignment.CENTER, spacing=12,
            controls=[
                ft.Image(src="icon.png", width=40, height=40, border_radius=20),
                ft.Text("Bryce A. Corvera", size=20, weight="bold", color="white")
            ]
        ),
        padding=ft.padding.symmetric(horizontal=16, vertical=12)
    )

    page.add(ft.Column(controls=[header, ft.Container(expand=True), bottom_nav_container], expand=True))
    render_bottom_nav()

ft.app(target=main, assets_dir="assets")
