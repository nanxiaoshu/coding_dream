#!/usr/bin/env python
# -*- coding:utf-8 -*-
from jinja2 import Template


def redirect(request, html_path, **kwargs):
    request['coding_dream_location'] = html_path
    request['coding_dream_status'] = '307 Temporary Redirect'
    return b''


def render_html(html_path, **kwargs):
    with open(html_path, 'r', encoding='utf-8') as f:
        data_html = f.read()
        template = Template(data_html)
        return template.render(kwargs).encode('utf-8')
