import os

from distutils.core import setup


base_path = os.path.dirname(os.path.abspath(__file__))
requirements_path = os.path.join(base_path, "docs", "setup", "requirements.txt")
reqs = [line.strip() for line in open(requirements_path)]


setup(
    name="sentiment-analysis-movie-reviews",
    version="0.1",
    description="Sentiment Analysis on Movie Reviews",
    author="Maanav Shah",
    packages=["sentiment_analysis"],
    install_requires=reqs,
    scripts=["scripts/execute.py"]
)
