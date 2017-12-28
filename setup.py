from setuptools import find_packages, setup

setup(name="flask-app",
      version = "0.1",
      description = "flask-app",
      author = "Alejandro Medina",
      platforms = ["any"],
      license = "GPLv3",
      include_package_data=True,
      packages = find_packages(),
      install_requires = ["Flask==0.12.2",
                          "gunicorn",
                          "SQLAlchemy",
                          "Flask-SQLAlchemy",
                          "PyMySQL==0.8.0",
                          "simplejson"],
      )
