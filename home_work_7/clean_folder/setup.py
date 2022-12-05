from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='2.0',
      description='Very useful code',
      url='link to github',
      author='Pivtorak Serhii',
      author_email='pivtorak.s90@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:start']}
)
