import flet as ft
from Database1 import init_db
from Dev1 import inventory_ui


def main(page: ft.Page):
    return inventory_ui(page)


if __name__ == "__main__":
    init_db()
    ft.app(target=main)
