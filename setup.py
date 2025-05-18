from setuptools import setup, find_packages

setup(
    name="kadoBossBot",
    version="1.0.0",
    author="Raphakado",
    author_email="raphakado@gmail.com",
    description="Bot autônomo para campanhas de marketing e monetização",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # Dependências essenciais
        "requests",
        "openai",
        "python-telegram-bot",
        "selenium",
        "flask",
        "python-dotenv",
        "pillow",
        "moviepy",
        "beautifulsoup4",
        "lxml",
        "fake-useragent",
        "schedule",
        "yagmail",
        "urllib3",
        "numpy"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
