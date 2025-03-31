# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1743441675.990893
_enable_loop = True
_template_filename = 'D:/Users/nvt23/AppData/Local/anaconda3/envs/nikola-env/lib/site-packages/nikola/data/themes/bootstrap4/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_headstart', 'late_load_js', 'html_stylesheets', 'html_navigation_links', 'html_navigation_links_entries', 'html_feedlinks', 'html_translations']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('feeds_translations', context._clean_inheritance_tokens(), templateuri='feeds_translations_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'feeds_translations')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        use_cdn = _import_ns.get('use_cdn', context.get('use_cdn', UNDEFINED))
        url_replacer = _import_ns.get('url_replacer', context.get('url_replacer', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        url_type = _import_ns.get('url_type', context.get('url_type', UNDEFINED))
        is_rtl = _import_ns.get('is_rtl', context.get('is_rtl', UNDEFINED))
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        mathjax_config = _import_ns.get('mathjax_config', context.get('mathjax_config', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        meta_generator_tag = _import_ns.get('meta_generator_tag', context.get('meta_generator_tag', UNDEFINED))
        comment_system_id = _import_ns.get('comment_system_id', context.get('comment_system_id', UNDEFINED))
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        comment_system = _import_ns.get('comment_system', context.get('comment_system', UNDEFINED))
        def html_feedlinks():
            return render_html_feedlinks(context)
        theme_color = _import_ns.get('theme_color', context.get('theme_color', UNDEFINED))
        extra_head_data = _import_ns.get('extra_head_data', context.get('extra_head_data', UNDEFINED))
        def html_stylesheets():
            return render_html_stylesheets(context)
        favicons = _import_ns.get('favicons', context.get('favicons', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html\n')
        __M_writer("prefix='")
        __M_writer('og: http://ogp.me/ns# article: http://ogp.me/ns/article#\n')
        if comment_system == 'facebook':
            __M_writer('fb: http://ogp.me/ns/fb# ')
        __M_writer("'")
        if is_rtl:
            __M_writer('dir="rtl" ')
        __M_writer('lang="')
        __M_writer(str(lang))
        __M_writer('">\n    <head>\n    <meta charset="utf-8">\n')
        if description:
            __M_writer('    <meta name="description" content="')
            __M_writer(filters.html_escape(str(description)))
            __M_writer('">\n')
        __M_writer('    <meta name="viewport" content="width=device-width, initial-scale=1">\n')
        if title == blog_title:
            __M_writer('        <title>')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</title>\n')
        else:
            __M_writer('        <title>')
            __M_writer(filters.html_escape(str(title)))
            __M_writer(' | ')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</title>\n')
        __M_writer('\n    ')
        __M_writer(str(html_stylesheets()))
        __M_writer('\n    <meta name="theme-color" content="')
        __M_writer(str(theme_color))
        __M_writer('">\n')
        if meta_generator_tag:
            __M_writer('    <meta name="generator" content="Nikola (getnikola.com)">\n')
        __M_writer('    ')
        __M_writer(str(html_feedlinks()))
        __M_writer('\n    <link rel="canonical" href="')
        __M_writer(str(abs_link(permalink)))
        __M_writer('">\n\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer('            <link rel="')
                __M_writer(str(name))
                __M_writer('" href="')
                __M_writer(str(file))
                __M_writer('" sizes="')
                __M_writer(str(size))
                __M_writer('"/>\n')
        __M_writer('\n')
        if comment_system == 'facebook':
            __M_writer('        <meta property="fb:app_id" content="')
            __M_writer(str(comment_system_id))
            __M_writer('">\n')
        __M_writer('\n')
        if prevlink:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(prevlink))
            __M_writer('" type="text/html">\n')
        if nextlink:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(nextlink))
            __M_writer('" type="text/html">\n')
        __M_writer('\n    ')
        __M_writer(str(mathjax_config))
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <!--[if lt IE 9]><script src="https://html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer('        <!--[if lt IE 9]><script src="')
            __M_writer(str(url_replacer(permalink, '/assets/js/html5.js', lang, url_type)))
            __M_writer('"></script><![endif]-->\n')
        __M_writer('\n    ')
        __M_writer(str(extra_head_data))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        luxon_locales = _import_ns.get('luxon_locales', context.get('luxon_locales', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        use_cdn = _import_ns.get('use_cdn', context.get('use_cdn', UNDEFINED))
        date_fanciness = _import_ns.get('date_fanciness', context.get('date_fanciness', UNDEFINED))
        use_bundles = _import_ns.get('use_bundles', context.get('use_bundles', UNDEFINED))
        social_buttons_code = _import_ns.get('social_buttons_code', context.get('social_buttons_code', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <script src="http://code.jquery.com/jquery-3.5.1.min.js" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>\n        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.1/umd/popper.min.js" integrity="sha256-/ijcOLwFf26xEYAjW75FizKVo5tnTYiQddPZoLUHHZ8=" crossorigin="anonymous"></script>\n        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>\n        <script src="https://cdnjs.cloudflare.com/ajax/libs/baguettebox.js/1.11.1/baguetteBox.min.js" integrity="sha256-ULQV01VS9LCI2ePpLsmka+W0mawFpEA0rtxnezUj4A4=" crossorigin="anonymous"></script>\n')
        if use_bundles and use_cdn:
            __M_writer('        <script src="/assets/js/all.js"></script>\n')
        elif use_bundles:
            __M_writer('        <script src="/assets/js/all-nocdn.js"></script>\n')
        else:
            if not use_cdn:
                __M_writer('            <script src="/assets/js/jquery.min.js"></script>\n            <script src="/assets/js/popper.min.js"></script>\n            <script src="/assets/js/bootstrap.min.js"></script>\n            <script src="/assets/js/baguetteBox.min.js"></script>\n')
        if date_fanciness != 0:
            if date_fanciness == 2:
                __M_writer('            <script src="https://polyfill.io/v3/polyfill.js?features=Intl.RelativeTimeFormat.%7Elocale.')
                __M_writer(str(luxon_locales[lang]))
                __M_writer('"></script>\n')
            if use_cdn:
                __M_writer('            <script src="https://cdn.jsdelivr.net/npm/luxon@1.24.1/build/global/luxon.min.js" integrity="sha256-5FiU7kNb/UJWqMesUFnKv4dJzLMiTWljH0ONkz+h704=" crossorigin="anonymous"></script>\n')
            else:
                __M_writer('            <script src="/assets/js/luxon.min.js"></script>\n')
            if not use_bundles:
                __M_writer('            <script src="/assets/js/fancydates.min.js"></script>\n')
        __M_writer('    ')
        __M_writer(str(social_buttons_code))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        use_bundles = _import_ns.get('use_bundles', context.get('use_bundles', UNDEFINED))
        has_custom_css = _import_ns.get('has_custom_css', context.get('has_custom_css', UNDEFINED))
        needs_ipython_css = _import_ns.get('needs_ipython_css', context.get('needs_ipython_css', UNDEFINED))
        use_cdn = _import_ns.get('use_cdn', context.get('use_cdn', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">\n        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/baguettebox.js/1.11.1/baguetteBox.min.css" integrity="sha256-cLMYWYYutHkt+KpNqjg7NVkYSQ+E2VbrXsEvOqU7mL0=" crossorigin="anonymous">\n')
        if use_bundles and use_cdn:
            __M_writer('        <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
        elif use_bundles:
            __M_writer('        <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
        else:
            if not use_cdn:
                __M_writer('            <link href="/assets/css/bootstrap.min.css" rel="stylesheet" type="text/css">\n            <link href="/assets/css/baguetteBox.min.css" rel="stylesheet" type="text/css">\n')
            __M_writer('        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/theme.css" rel="stylesheet" type="text/css">\n')
            if has_custom_css:
                __M_writer('            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        if needs_ipython_css:
            __M_writer('        <link href="/assets/css/ipython.min.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/nikola_ipython.css" rel="stylesheet" type="text/css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        def html_navigation_links_entries(navigation_links_source):
            return render_html_navigation_links_entries(context,navigation_links_source)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(html_navigation_links_entries(navigation_links)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links_entries(context,navigation_links_source):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        tuple = _import_ns.get('tuple', context.get('tuple', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        for url, text in navigation_links_source[lang]:
            if isinstance(url, tuple):
                __M_writer('            <li class="nav-item dropdown"><a href="#" class="nav-link dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">')
                __M_writer(str(text))
                __M_writer('</a>\n            <div class="dropdown-menu">\n')
                for suburl, text in url:
                    if rel_link(permalink, suburl) == "#":
                        __M_writer('                    <a href="')
                        __M_writer(str(permalink))
                        __M_writer('" class="dropdown-item active">')
                        __M_writer(str(text))
                        __M_writer(' <span class="sr-only">')
                        __M_writer(str(messages("(active)", lang)))
                        __M_writer('</span></a>\n')
                    else:
                        __M_writer('                    <a href="')
                        __M_writer(str(suburl))
                        __M_writer('" class="dropdown-item">')
                        __M_writer(str(text))
                        __M_writer('</a>\n')
                __M_writer('            </div>\n')
            else:
                if rel_link(permalink, url) == "#":
                    __M_writer('                <li class="nav-item active"><a href="')
                    __M_writer(str(permalink))
                    __M_writer('" class="nav-link">')
                    __M_writer(str(text))
                    __M_writer(' <span class="sr-only">')
                    __M_writer(str(messages("(active)", lang)))
                    __M_writer('</span></a>\n')
                else:
                    __M_writer('                <li class="nav-item"><a href="')
                    __M_writer(str(url))
                    __M_writer('" class="nav-link">')
                    __M_writer(str(text))
                    __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(feeds_translations.head(classification=None, kind='index', other=False)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        sorted = _import_ns.get('sorted', context.get('sorted', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        for langname in sorted(translations):
            if langname != lang:
                __M_writer('            <li class="nav-item"><a href="')
                __M_writer(str(_link("root", None, langname)))
                __M_writer('" rel="alternate" hreflang="')
                __M_writer(str(langname))
                __M_writer('" class="nav-link">')
                __M_writer(str(messages("LANGUAGE", langname)))
                __M_writer('</a></li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "D:/Users/nvt23/AppData/Local/anaconda3/envs/nikola-env/lib/site-packages/nikola/data/themes/bootstrap4/templates/base_helper.tmpl", "uri": "base_helper.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 0, "33": 2, "34": 64, "35": 99, "36": 127, "37": 131, "38": 154, "39": 158, "40": 166, "46": 4, "75": 4, "76": 8, "77": 9, "78": 10, "79": 11, "80": 13, "81": 14, "82": 15, "83": 18, "84": 18, "85": 18, "86": 21, "87": 22, "88": 22, "89": 22, "90": 24, "91": 25, "92": 26, "93": 26, "94": 26, "95": 27, "96": 28, "97": 28, "98": 28, "99": 28, "100": 28, "101": 30, "102": 31, "103": 31, "104": 32, "105": 32, "106": 33, "107": 34, "108": 36, "109": 36, "110": 36, "111": 37, "112": 37, "113": 39, "114": 40, "115": 41, "116": 41, "117": 41, "118": 41, "119": 41, "120": 41, "121": 41, "122": 44, "123": 45, "124": 46, "125": 46, "126": 46, "127": 48, "128": 49, "129": 50, "130": 50, "131": 50, "132": 52, "133": 53, "134": 53, "135": 53, "136": 55, "137": 56, "138": 56, "139": 57, "140": 58, "141": 59, "142": 60, "143": 60, "144": 60, "145": 62, "146": 63, "147": 63, "153": 66, "165": 66, "166": 67, "167": 68, "168": 73, "169": 74, "170": 75, "171": 76, "172": 77, "173": 78, "174": 79, "175": 85, "176": 86, "177": 87, "178": 87, "179": 87, "180": 89, "181": 90, "182": 91, "183": 92, "184": 94, "185": 95, "186": 98, "187": 98, "188": 98, "194": 102, "204": 102, "205": 103, "206": 104, "207": 107, "208": 108, "209": 109, "210": 110, "211": 111, "212": 112, "213": 113, "214": 116, "215": 119, "216": 120, "217": 123, "218": 124, "224": 129, "233": 129, "234": 130, "235": 130, "241": 133, "253": 133, "254": 134, "255": 135, "256": 136, "257": 136, "258": 136, "259": 138, "260": 139, "261": 140, "262": 140, "263": 140, "264": 140, "265": 140, "266": 140, "267": 140, "268": 141, "269": 142, "270": 142, "271": 142, "272": 142, "273": 142, "274": 145, "275": 146, "276": 147, "277": 148, "278": 148, "279": 148, "280": 148, "281": 148, "282": 148, "283": 148, "284": 149, "285": 150, "286": 150, "287": 150, "288": 150, "289": 150, "295": 156, "302": 156, "303": 157, "304": 157, "310": 160, "321": 160, "322": 161, "323": 162, "324": 163, "325": 163, "326": 163, "327": 163, "328": 163, "329": 163, "330": 163, "336": 330}}
__M_END_METADATA
"""
