from setuptools import setup

setup(name='firex-bundle-foobar',
      version='0.1.',
      description='Example library with fake Firexapp tasks',
      url='https://github.com/FireXStuff/firex-bundle-foobar.git',
      author='Core FireX Team',
      author_email='firex-dev@gmail.com',
      license='BSD-3-Clause',
      packages=['firex_bundle_foobar'],
      zip_safe=True,
      install_requires=[
          "firexapp",
      ],
      entry_points={'firex.bundles': 'firex-bundle-foobar = firex_bundle_foobar'},
      )
