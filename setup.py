from setuptools import setup, find_packages

setup(
    name="EmotionDetection",
    version="1.0.0",
    description="A Python package for emotion detection using Watson NLP",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="KHAN Vuthy",
    author_email="khanvuthy800@gmail.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.6",
)