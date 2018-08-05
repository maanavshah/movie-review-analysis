from PIL import Image
import time
import os

sentiment = Image.open("output/sentiment_analysis.png")
sentiment.show()
time.sleep( 6 )
sentiment.close()
os.system("kill $(ps aux | grep 'display' | awk '{print $2}')")