# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1744178337.047585
_enable_loop = True
_template_filename = 'themes/bktheme2/templates/base.tmpl'
_template_uri = 'base.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'belowtitle', 'sourcelink', 'extra_header', 'content', 'extra_footer', 'extra_js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

    ns = runtime.TemplateNamespace('notes', context._clean_inheritance_tokens(), templateuri='annotation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'notes')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        def extra_footer():
            return render_extra_footer(context._locals(__M_locals))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        def extra_header():
            return render_extra_header(context._locals(__M_locals))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        content_footer = _import_ns.get('content_footer', context.get('content_footer', UNDEFINED))
        theme_config = _import_ns.get('theme_config', context.get('theme_config', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        show_sourcelink = _import_ns.get('show_sourcelink', context.get('show_sourcelink', UNDEFINED))
        navigation_alt_links = _import_ns.get('navigation_alt_links', context.get('navigation_alt_links', UNDEFINED))
        show_blog_title = _import_ns.get('show_blog_title', context.get('show_blog_title', UNDEFINED))
        momentjs_locales = _import_ns.get('momentjs_locales', context.get('momentjs_locales', UNDEFINED))
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        js_date_format = _import_ns.get('js_date_format', context.get('js_date_format', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        date_fanciness = _import_ns.get('date_fanciness', context.get('date_fanciness', UNDEFINED))
        def belowtitle():
            return render_belowtitle(context._locals(__M_locals))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer(str(set_locale(lang)))
        __M_writer('\n')
        __M_writer(str(base.html_headstart()))
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n<meta name="google-site-verification" content="qNXALWQ-4rcCIoX7DiJ0sr09q7-PUK5bHt8htUBKnmk" />\n')
        __M_writer(str(template_hooks['extra_head']()))
        __M_writer('\n</head>\n<body>\n<a href="#content" class="sr-only sr-only-focusable">')
        __M_writer(str(messages("Skip to main content")))
        __M_writer('</a>\n\n<!-- Menubar -->\n\n<nav class="navbar navbar-expand-md static-top mb-4\n')
        if theme_config.get('navbar_light'):
            __M_writer('navbar-light bg-light\n')
        else:
            __M_writer('navbar-dark bg-dark\n')
        __M_writer('">\n    <div class="container"><!-- This keeps the margins nice -->\n        <a class="navbar-brand" href="')
        __M_writer(str(abs_link(_link("root", None, lang))))
        __M_writer('">\n')
        if logo_url:
            __M_writer('            <img src="')
            __M_writer(str(logo_url))
            __M_writer('" alt="')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('" id="logo" class="d-inline-block align-top">\n')
        __M_writer('\n')
        if show_blog_title:
            __M_writer('            <span id="blog-title">')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</span>\n')
        __M_writer('        </a>\n        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#bs-navbar" aria-controls="bs-navbar" aria-expanded="false" aria-label="Toggle navigation">\n            <span class="navbar-toggler-icon"></span>\n        </button>\n\n        <div class="collapse navbar-collapse" id="bs-navbar">\n            <ul class="navbar-nav mr-auto">\n                ')
        __M_writer(str(base.html_navigation_links_entries(navigation_links)))
        __M_writer('\n                ')
        __M_writer(str(template_hooks['menu']()))
        __M_writer('\n            </ul>\n')
        if search_form:
            __M_writer('                ')
            __M_writer(str(search_form))
            __M_writer('\n')
        __M_writer('\n            <ul class="navbar-nav navbar-right">\n                ')
        __M_writer(str(base.html_navigation_links_entries(navigation_alt_links)))
        __M_writer('\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'belowtitle'):
            context['self'].belowtitle(**pageargs)
        

        __M_writer('\n')
        if show_sourcelink:
            __M_writer('                    ')
            if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
                context['self'].sourcelink(**pageargs)
            

            __M_writer('\n')
        __M_writer('                ')
        __M_writer(str(template_hooks['menu_alt']()))
        __M_writer('\n            </ul>\n        </div><!-- /.navbar-collapse -->\n    </div><!-- /.container -->\n</nav>\n\n<!-- End of Menubar -->\n\n<div class="container" id="content" role="main">\n    <div class="body-content">\n        <div class="row">\n        <!--Body content-->\n            <div class="col-lg-9">\n                ')
        __M_writer(str(template_hooks['page_header']()))
        __M_writer('\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_header'):
            context['self'].extra_header(**pageargs)
        

        __M_writer('\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n            </div>\n            <div class="col-md-3 ">\n            <div class="card card-body bg-light">\n            <p>\n            Hi, I\'m <a>Ngo Truong</a>.  This is\n            <a href="/">the place</a> where I documenting my learning note.\n            </p>\n            <p>\n            Twitter: <a href="">no</a>\n            </p>\n\t\t\t<p>\n\t\t\tUsing <a href="https://github.com/bjlkeng/bjlkeng.github.io/tree/source/source/themes">theme</a> by <a href="https://bjlkeng.io/">Brian Keng</a>\n\t\t\t</p>\n            <br/>\n            </p>\n            </div>\n            </div>\n            </div>\n        </div>\n        <!--End of body content-->\n\n        <footer id="footer">\n            ')
        __M_writer(str(content_footer))
        __M_writer('\n            ')
        __M_writer(str(template_hooks['page_footer']()))
        __M_writer('\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_footer'):
            context['self'].extra_footer(**pageargs)
        

        __M_writer('\n        </footer>\n    </div>\n</div>\n\n')
        __M_writer(str(base.late_load_js()))
        __M_writer('\n')
        if date_fanciness != 0:
            __M_writer('        <!-- fancy dates -->\n        <script>\n        moment.locale("')
            __M_writer(str(momentjs_locales[lang]))
            __M_writer('");\n        fancydates(')
            __M_writer(str(date_fanciness))
            __M_writer(', ')
            __M_writer(str(js_date_format))
            __M_writer(');\n        </script>\n        <!-- end fancy dates -->\n')
        __M_writer('    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer("\n    <script>\n    baguetteBox.run('div#content', {\n        ignoreClass: 'islink',\n        captions: function(element) {\n            return element.getElementsByTagName('img')[0].alt;\n    }});\n    </script>\n")
        __M_writer(str(body_end))
        __M_writer('\n')
        __M_writer(str(template_hooks['body_end']()))
        __M_writer('\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_belowtitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        base = _mako_get_namespace(context, 'base')
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        def belowtitle():
            return render_belowtitle(context)
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            __M_writer('                    <li>')
            __M_writer(str(base.html_translations()))
            __M_writer('</li>\n')
        __M_writer('                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        def extra_header():
            return render_extra_header(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        def extra_footer():
            return render_extra_footer(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/bktheme2/templates/base.tmpl", "uri": "base.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 0, "73": 2, "74": 3, "75": 4, "76": 4, "77": 5, "78": 5, "83": 8, "84": 10, "85": 10, "86": 13, "87": 13, "88": 18, "89": 19, "90": 20, "91": 21, "92": 23, "93": 25, "94": 25, "95": 26, "96": 27, "97": 27, "98": 27, "99": 27, "100": 27, "101": 29, "102": 30, "103": 31, "104": 31, "105": 31, "106": 33, "107": 40, "108": 40, "109": 41, "110": 41, "111": 43, "112": 44, "113": 44, "114": 44, "115": 46, "116": 48, "117": 48, "122": 53, "123": 54, "124": 55, "129": 55, "130": 57, "131": 57, "132": 57, "133": 70, "134": 70, "139": 71, "144": 72, "145": 95, "146": 95, "147": 96, "148": 96, "153": 97, "154": 102, "155": 102, "156": 103, "157": 104, "158": 106, "159": 106, "160": 107, "161": 107, "162": 107, "163": 107, "164": 111, "169": 111, "170": 119, "171": 119, "172": 120, "173": 120, "179": 6, "188": 6, "194": 49, "206": 49, "207": 50, "208": 51, "209": 51, "210": 51, "211": 53, "217": 55, "231": 71, "245": 72, "259": 97, "273": 111, "287": 273}}
__M_END_METADATA
"""
