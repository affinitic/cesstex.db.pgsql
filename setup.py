from setuptools import setup, find_packages

version = '0.2dev'

setup(name='cesstex.db.pgsql',
      version=version,
      description="DB postgresql connexion",
      classifiers=[], # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      keywords='postgresql cesstex',
      author='Affinitic',
      author_email='info@affinitic.be',
      url='http://svn.affinitic.be/plone/cesstex/cesstex.db.pgsql',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['cesstex', 'cesstex.db'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'sqlalchemy',
        'affinitic.pwmanager'],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
