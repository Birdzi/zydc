"""
菜品展示蓝图
"""


from flask import Blueprint

items_display = Blueprint('items_display', __name__)


@items_display.route('/item')
def items_display():
    pass




