#!/usr/bin/env python
AUTHORS = (
    'Rémy Hubscher',
)

SITENAME = u'REST @ SEA — Mini 433'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

# Social widget
SOCIAL = (('Github', 'https://github.com/Natim/rest-sea'),)

DEFAULT_PAGINATION = False

THEME = "pure"

COVER_IMG_URL = '/theme/sidebar.jpg'

SOCIAL = (
    ('envelope', 'mailto:rest-at-sea@trunat.fr'),
    ('rss', SITEURL + '/feeds/all.atom.xml'),
    ('facebook', 'https://www.facebook.com/pg/remymini433/'),
    ('github', 'https://github.com/Natim/rest-sea'),
)

MENUITEMS = (
    ('Nouvelles', 'archives.html'),
    (u'Bateau', 'pages/le-bateau-rest-at-sea-mini-433.html'),
    (u'Équipage', 'pages/equipage.html'),
    (u'Contactez-nous', 'pages/a-propos.html'),
)
STATIC_PATHS = ['images']
EXTRA_PATH_METADATA = {
#    'extra/robots.txt': {'path': 'robots.txt'},
}
PLUGIN_PATHS = ['plugins']
PLUGINS = ['post_stats']
RESPONSIVE_IMAGES = True
