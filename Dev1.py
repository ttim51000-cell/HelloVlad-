import flet as ft
import Logic1 as ctl


def inventory_ui(page: ft.Page):

    page.title = "Складской учёт"
    page.window_width = 900
    page.window_height = 700

    # ------------------- UI элементы --------------------

    product_name = ft.TextField(label="Название")
    product_desc = ft.TextField(label="Описание")
    product_price = ft.TextField(label="Цена", value="0")

    product_list = ft.Dropdown(label="Товар")

    supply_qty = ft.TextField(label="Количество поставки")
    sale_qty = ft.TextField(label="Количество продажи")

    output = ft.Text("", color="green")

    # ------------ загрузка списка товаров -------------

    def refresh_products():
        product_list.options = [
            ft.dropdown.Option(str(p.id), p.name) for p in ctl.get_all_products()
        ]
        page.update()

    refresh_products()

    # ---------------- обработчики ---------------------

    def add_product_click(e):
        ctl.add_product(
            product_name.value,
            product_desc.value,
            product_price.value
        )
        output.value = "Товар добавлен!"
        refresh_products()
        page.update()

    def edit_product_click(e):
        if not product_list.value:
            output.value = "Выберите товар"
        else:
            ctl.edit_product(
                product_list.value,
                product_name.value,
                product_desc.value,
                product_price.value
            )
            output.value = "Товар изменён!"
        refresh_products()
        page.update()

    def delete_product_click(e):
        if not product_list.value:
            output.value = "Выберите товар"
        else:
            ctl.delete_product(product_list.value)
            output.value = "Товар удалён!"
        refresh_products()
        page.update()

    def supply_click(e):
        if not product_list.value:
            output.value = "Выберите товар"
        else:
            ctl.supply_product(product_list.value, supply_qty.value)
            output.value = "Поставка добавлена!"
        refresh_products()
        page.update()

    def sell_click(e):
        try:
            ctl.sell_product(product_list.value, sale_qty.value)
            output.value = "Продажа проведена!"
        except ValueError as ex:
            output.value = str(ex)
        refresh_products()
        page.update()

    # ------------------- История -----------------------

    history_text = ft.Text("")

    def show_history(e):
        supplies = ctl.get_supply_history()
        sales = ctl.get_sales_history()

        s = "\n=== Поставки ===\n"
        for sup in supplies:
            s += f"{sup.date:%Y-%m-%d %H:%M}  {sup.product.name} +{sup.quantity}\n"

        s += "\n=== Продажи ===\n"
        for sal in sales:
            s += f"{sal.date:%Y-%m-%d %H:%M}  {sal.product.name} -{sal.quantity}\n"

        history_text.value = s
        page.update()

    # ------------------- Layout ------------------------

    page.add(
        ft.Row([
            ft.Column([
                ft.Text("Работа с товарами", size=20, weight="bold"),

                product_name,
                product_desc,
                product_price,

                ft.Row([
                    ft.ElevatedButton("Добавить", on_click=add_product_click),
                    ft.ElevatedButton("Изменить", on_click=edit_product_click),
                    ft.ElevatedButton("Удалить", on_click=delete_product_click),
                ]),

                ft.Divider(),

                product_list,
                supply_qty,
                ft.ElevatedButton("Добавить поставку", on_click=supply_click),

                sale_qty,
                ft.ElevatedButton("Продать", on_click=sell_click),

                output
            ], expand=1),

            ft.VerticalDivider(),

            ft.Column([
                ft.Text("История", size=20, weight="bold"),
                ft.ElevatedButton("Показать историю", on_click=show_history),
                ft.Container(history_text, padding=10, border=ft.border.all(1)),
            ], expand=1)
        ])
    )
