from distutils.core import setup

setup(name='pbf_project',
      version='.1',
      description="Programmer's Best Friend Utility Extension for pbf_project",
      author='', # Add your name here
      author_email='', # Add your e-mail here
      packages=['pbf_project', 'pbf_project.Commands', 'pbf_project.templates'],
      #package_data = {'pbf_project.templates':[]}, # Add template files
     )