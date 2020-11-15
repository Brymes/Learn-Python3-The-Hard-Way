try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description' : 'Gothon Web',
    'author' : 'Timothy Odebunmi',
    'url' :'URL to get it at.',
    'download_url' : 'Where to download it.',
    'author_email' : 'timboluinfinite@gmail.com, tbodebunmijnr@gmail.com',
    'version' : '0.1',
    'install_requires' : ['nose', 'Flask'],
    'packages' : ['gothonweb'],
    'scripts' : [],
    'name' : 'GothonWeb'
}

setup(**config)
