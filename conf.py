project = 'Secure_Anytime'
copyright = '2026'
author = 'Admin'

extensions = [] 

extensions = [ 'sphinx.ext.autodoc',
               'sphinx.ext.napoleon',
              ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'alabaster' # Screenshot wala classic white theme

# conf.py

html_title = "Download Kaspersky Total Security in your Windows PC"
html_short_title = "Download Kaspersky Total Security"
html_static_path = ['_static']
html_extra_path = ['_static/google5ffeff63dcb91d99.html'] 


# Meta Tags Configuration
html_context = {
    'metatags': '''
        <meta name="description" content="Download Malwarebytes gratis safely from the official site. All the easy steps shared here, the free version scans, detects, and removes malware fast.">
        <meta name="Download Malwarebytes Gratis" content="docs, guide, setup, tutorial">
     
    '''
}

