import os
import pathlib
#import subprocess
#import sys
import setuptools


#def install(package):
#    subprocess.check_call([sys.excutable,"-m","pip","install",package])

# GH_TOKEN = os.getenv("GH_TOKEN")
# if GH_TOKEN is None:
#     required = 'python-dotenv==1.0.0'
#     install(required)
#     from dotenv import load_dotenv
#
#     load_dotenv()
#     GH_TOKEN = os.getenv("GH_USERNAME")+ ":" +os.getenv("GH_TOKEN")
#     print(f"##### GH_TOKEN is :::: {GH_TOKEN}")


GH_USERNAME = os.getenv("GH_USERNAME")
GH_TOKEN = os.getenv("GH_TOKEN")


PACKAGE_REQUIREMENTS = [
    "PyYAML==6.0",
    "pysftp==0.2.9",
    "boto3==1.34.51",
    "wheel"
]

DEV_REQUIREMENTS = [
    "pytest == 7.1.3",
    "pandas == 1.5.0",
    "pytest-cov == 3.0.0",
    "python-dotenv == 1.0.0",
    "pyspark == 3.3.0"
]


current_dir = pathlib.Path(__file__).parent.resolve()
#long_description = (current_dir / 'README.md').read_txt(encoding="utf-8")
long_description = "test project "
#os.environ["PROJ_BASE_DIR"] = str(current_dir)
#print(f"current_dir value is :::: {current_dir}")
#b=25
#sprint(f"value of b is :::: {b}")




setuptools.setup(
    name="e-python-proj-with-basic-function-and-class-definitions",
    version="1.0.0",
    author="ABC Team",
    author_email = "sekher.talupula@gmail.com,sekhar.jagadeesh9@gmail.com",
    description = "contains code for basic function and class definitions ",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    packages = setuptools.find_packages(exclude=["test_*","**/test/*"]),
    python_requires = ">=3.9",
    setup_requires = ["setuptools" , "wheel"],
    install_requires = PACKAGE_REQUIREMENTS,
    extras_require = { "dev" : DEV_REQUIREMENTS },
    classifiers= [
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    package_data = {
        'me.personal.core': ['*.csv' , '*.json'],
        'me.personal.basic-function-examples': ['*.csv' , '*.json'],
    }
)


