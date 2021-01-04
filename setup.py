# Created by Andy at 04-Jan-21

# Enter description here

# ___________________________________
from setuptools import setup, find_packages

setup(name="tabu_search",
      version = "0.0.1",
      author="Andy Cai",
      author_email="andycai517@gmail.com",
      packages = find_packages("src"),
      package_dir= {"":"src"})