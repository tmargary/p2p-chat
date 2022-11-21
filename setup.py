from setuptools import setup, find_packages

VERSION = "0.0.1"

setup(
    name="p2p-chat",
    version=VERSION,
    description="Peer to peer console application.",
    author="Tigran Margaryan",
    author_email="tigranmargarian@outlook.com",
    packages=find_packages(),
    entry_points={"console_scripts": ["p2p_demo=p2p_chat.main:main"]},
    # install_requires=[
    # ],
)
