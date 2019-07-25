# 首页名称
    index.html
# 帖子模板文件名称
    post_tem.html(作为母板)
# 帖子文件名
    post.html(继承post_tem.html)
# 注册登录
    login.html
    registration.html
# 注销
    转到/account/logout
# js/css/imag路径
    ../js/xxx.js || ../css/xxx.css || ../imag/xxx.jpg
# 板块列表变量
    CATEGORY_LIST
## 板块变量成员
    -id(返回给后端)
    -name
# 存放帖子的列表变量名
    POST_LIST
## 成员变量
    -title
    -summary
    -category
    -content
    -view_count
    -comment_count
    -author
    -ranking
    -publish_date
    -modify_date
## 可用于
    -index.html
# 后端返回给post.html的符合id要求帖子变量名
    POST
# 帖子显示路径
    /post/{{变量名.id}}/
# 快速显示评论
    首先{% load comments %}
    在需要的地方显示{% render_comment_list for POST%}
## 获取评论到变量（自定义形式显示）
    {% get_comment_list for POST as reversed as 新变量%}
    eg：
        {% get_comment_list for POST as reversed as comment_list %}
            {% for comment in comment_list reversed %}
                {{ comment.submit_date}} <br />
                {{ comment.comment}} <hr />
## 获取评论数量
    {% get_comment_count for [object] as [varname] %}
### 例如：
    {% get_comment_count for POST as comment_count %}
    This entry has {{ comment_count }} comments.
# 添加评论
    {% get_comment_form for POST as form %}
        <table>
          <form action="{% comment_form_target %}" method="post"> 
                {% csrf_token %}
                {{ form.comment }}
                {{ form.honeypot }} 
                {{ form.content_type }}
                {{ form.object_pk }}
                {{ form.timestamp }}
                {{ form.security_hash }}
                <input type="hidden" name="next" value="{% url 'curr_post' POST.id %}" /> （这句话不可改变，请直接使用）
                <input type="submit" value="提交评论" id="id_submit" />
        </table>
# 当前帖子地址变量：
    {% url 'curr_post' POST.id %}
# 表示当前用户的变量
    user
# 判断登录
    {% if user.is_authenticated %}
        {% else %}
    <p>请先<a href="{% url 'login' %}">登录</a>后方可评论.</p>
    {% endif %}
    {% render_comment_list for POST %}