from distutils.core import setup

setup(name='pbf_project',
      version='0.1.0',
      description="Programmer's Best Friend Utility Extension for pbf_project",
      author='Chris Loew',
      author_email='cloew123@gmail.com',
      packages=['pbf_project', 'pbf_project.Commands', 'pbf_project.helpers'],
      #package_data = {'pbf_project.templates':[]}, # Add template files
     )