# ZY 点餐系统


解决方案：Flask + Mysql + Nginx + FastCGI

## 需求

一、用户界面和用户后台

蓝图：index.py

1. 浏览菜单

2. 相似推荐

3. 取餐提醒

4. 登录——历史记录、收藏，积分

二、服务前台

蓝图： order.py

1. 接单并改变订单状态
2. 当订单状态改为：等待取货 时，自动叫号

三、管理界面

蓝图：admin.py
1. 管理菜品 名称、图片、描述、利润
2. 查看用户信息
3. 订单比例饼形图 利润饼形图
4. 流水导出（xlsx）


## 实现

- 前后端不分离
- WebSocket
- 模板使用 Jinja 2, ORM 使用 Flask 的 SQLAlchemy 扩展
