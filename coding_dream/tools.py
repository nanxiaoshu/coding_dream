#!/usr/bin/env python
# -*- coding:utf-8 -*-
from html import escape
from urllib.parse import parse_qs


def get_request_data(request):
    old_request_data = parse_qs(request.get('QUERY_STRING'))
    new_request_data = {}
    for k, v in old_request_data.items():
        new_request_data[k] = v[0]
    return new_request_data


def post_request_data(request):
    try:
        request_body_size = int(request.get('CONTENT_LENGTH', 0))
    except ValueError:
        request_body_size = 0
    request_body = request.get('wsgi.input').read(request_body_size)
    old_request_data = parse_qs(request_body)
    new_request_data = {}
    for k, v in old_request_data.items():
        k, v = escape(str(k, encoding='utf-8')), escape(str(v[0], encoding='utf-8'))
        new_request_data[k] = v
    return new_request_data


def get_request_method(request):
    return request.get('REQUEST_METHOD')


def get_cookie(request):
    cookie_str = request.get('HTTP_COOKIE')
    cookie_dict = {}
    if cookie_str:
        cookie_lst = cookie_str.split(';')
        for cookie_kv in cookie_lst:
            cookie_kv = cookie_kv.strip(' ')
            cookie_kv = cookie_kv.split('=')
            cookie_dict[cookie_kv[0]] = cookie_kv[1]
    return cookie_dict
