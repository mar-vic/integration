AUTHOR = 'Marek Vician'

SITENAME = 'Integration'
SITEURL = ''
SITEDESCRIPTION = "Site's description."
PATH = 'content'

TIMEZONE = 'Europe/Bratislava'
DEFAULT_LANG = 'sk'

THEME = './themes/integration'
THEME_STATIC_DIR = 'static'

PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [
    ('Domov', SITEURL + "/", "index.html", ""),
    ('O utečencoch', SITEURL + '/' + "o-utecencoch", "Short description of the contents of this subpage"),
    ('Integrácia', SITEURL + '/' + "integracia", "Short description of the contents of this subpage"),
    ('Komunikácia', SITEURL + '/' + "komunikacia", "Short description of the contents of this subpage"),
    ('Poznanie situácie', SITEURL + '/' + "poznanie-situacie", "Short description of the contents of this subpage"),
    ('Odborné vzdelávnie', SITEURL + '/' + "odborne-vzdelavanie", "Short description of the contents of this subpage"),
    ("O nás", SITEURL + "/o-nas", "")
]

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# PLUGINS SET-UP
PLUGIN_PATHS = ['plugins']
PLUGINS = ['page_hierarchy', 'jinja2content', 'search']

# Setting for page_hierarchy plugin
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
SLUGIFY_SOURCE = 'basename'

# Settings for jinja2content plugin
JINJA2CONTENT_TEMPLATES = ['templates']

# Settings for search plugin
STORK_INPUT_OPTIONS = {
    "base_directory": PATH,
}
