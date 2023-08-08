import urllib.request as urllib2
import pprint
import http.cookiejar as cookielib
import lxml.html
from io import BytesIO
import lxml.html
from PIL import Image
import base64
import pytesseract
import requests
import io

def load_captcha(html):
   tree = lxml.html.fromstring(html)
   img_data = tree.cssselect('cssselectorforcaptchaimg')[0]
   img_data=img_data.get('src')
   img_data = img_data.partition(',')[-1]
   binary_img_data= base64.b64decode(img_data)
   img=BytesIO(binary_img_data)
   response = requests.get(aspx_image_url)
   if response.status_code == 200:
    img = Image.open(io.BytesIO(response.content))
    PNG_buffer = io.BytesIO()
    img.save(PNG_buffer, format='PNG')
    img.save('captcha_original.png')
   return img


aspx_image_url = 'captchaimgurl'
REGISTER_PAGE_URL = 'yourwebpageurl'

ckj = cookielib.CookieJar()
browser = urllib2.build_opener(urllib2.HTTPCookieProcessor(ckj))
html = browser.open(REGISTER_PAGE_URL).read()
img = load_captcha(html)
captcha=pytesseract.image_to_string(img)
print(captcha)

