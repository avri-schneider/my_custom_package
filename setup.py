from setuptools import setup
import os

# Print an environment variable
print("MY_ENV_VAR:", os.environ.get("MY_ENV_VAR", "Not Found"))

setup(
    name='mypackage',
    version='0.1',
    description='A custom package to print environment variables',
    packages=['mypackage'],
)

