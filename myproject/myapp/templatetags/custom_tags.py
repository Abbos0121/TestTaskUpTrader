from django import template
from ..models import MenuItem

register = template.Library()


def render_menu(menu_items):
    menu_html = ""
    for item in menu_items:
        menu_html += f"<li><a href='{item.url}'>{item.name}</a>"
        if item.child_items.exists():
            menu_html += "<ul>"
            menu_html += render_menu(item.child_items.all())
            menu_html += "</ul>"
        menu_html += "</li>"
    return menu_html


@register.simple_tag
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(name=menu_name)

    if not menu_items.exists():
        return ""

    menu_html = render_menu(menu_items)
    return menu_html
