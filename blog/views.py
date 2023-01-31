from django.shortcuts import render


def index_view(request):
    return render(request, 'index.html')


def error_view(request, code: int, msg: str, exception):
    response = render(request, 'error.html', {'code': code, 'msg': msg, 'exception': exception})
    response.status_code = code
    return response


def bad_request(request, exception):
    return error_view(request, code=400, msg="你的请求有误，可能是因为网站使用的协议已经更新", exception=exception)


def permission_denied(request, exception):
    return error_view(request, code=403, msg="你没有权限查看此页面，请检查是否已经登录了正确的账号", exception=exception)


def page_not_found(request, exception):
    return error_view(request, code=404, msg="此页面不存在，或已经被删除", exception=exception)


def error(request):
    return error_view(request, code=500, msg="服务器出现了没有预料到的错误，请稍后再试", exception=None)
