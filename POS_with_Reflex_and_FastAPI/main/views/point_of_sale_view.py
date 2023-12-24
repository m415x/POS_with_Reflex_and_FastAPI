import reflex as rx

# import panels
from ...tabs.point_of_sale.panels.tool_panel import tool_panel
from ...tabs.point_of_sale.panels.item_panel import item_panel
from ...tabs.point_of_sale.panels.cart_panel import cart_panel
from ...tabs.point_of_sale.panels.checkout_panel import checkout_panel

# import styles
from ...styles.colors import DarkThemeColor


def point_of_sale_view() -> rx.Component:
    return rx.grid(
        rx.grid_item(
            tool_panel(),
            col_span=19,
            row_span=1,
        ),
        rx.grid_item(
            cart_panel(),
            col_span=8,
            row_span=7,
            border_radius="15px",
            bg=DarkThemeColor.SECONDARY.value,
        ),
        rx.grid_item(
            item_panel(),
            col_span=19,
            row_span=10,
        ),
        rx.grid_item(
            checkout_panel(),
            col_span=8,
            row_span=4,
            border_radius="15px",
            bg=DarkThemeColor.CONTENT.value,
        ),
        template_columns="repeat(27, 1fr)",
        template_rows="repeat(11, 1fr)",
        gap=2,
    )
