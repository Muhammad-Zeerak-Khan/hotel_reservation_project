from setuptools import find_packages, setup

with open("requirements.txt", "r") as file:
    reqs: list[str] = file.read().splitlines()


setup(
    name="HOTEL-RESERVATION",
    version="0.0.1",
    author="Muhammad Zeerak Khan",
    packages=find_packages(),
    install_requires=reqs,
)
