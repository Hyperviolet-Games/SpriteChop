import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="spritechop",
    version="0.0.1",
    install_requires=[
        "Pillow>=7.0.0"
    ],
    python_requires=">=3.6",
)
