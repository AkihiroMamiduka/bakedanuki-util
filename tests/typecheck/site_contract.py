"""サイト基点・URL生成・ブラウザー起動の公開型を固定する。"""

from typing import assert_type

from bd_util import site
from bd_util.py import web
from bd_util.py.web import open_url
from bd_util.site import SITE_BASE_URL, build_url

assert_type(site.SITE_BASE_URL, str)
assert_type(SITE_BASE_URL, str)
assert_type(site.build_url(""), str)
assert_type(build_url(page_path="tools/tool/bd-channel-box/"), str)
assert_type(web.open_url(SITE_BASE_URL), bool)
assert_type(open_url(url=build_url("tools/")), bool)
