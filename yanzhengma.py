import requests
import os
import time
from lxml import etree

def get_Page(url,headers):
  response = requests.get(url,headers = headers)
  if response.status_code == 200:
    #print(response.text)
    return response.text
  return None
def parse_Page(html,headers):
  heml_lxml = etree.HTML(html)
  datas = html_lxml.xpath('.//div[@class = "captcha_images_left"]|.//div[@class = "captcha_images_right"]')
  item = {}
  #创建保存验证码文件夹
  file = 'D:/******'
  if os.path.exists(file):
    os.chdir(file)
  else:
    os.mkdir(file)
    os.chdir(file)
    for data in datas:
      #验证码名称
      name = data.xpath('.//h3')
      #print(len(name))
      #验证码链接
      src = data.xpath('.//div/img/src')
      #print(len(src))
      count = 0
      for i in range(len(name)):
        #验证码图片文件名
        filename = name[i].text + '.jpg'
        img_url = 'https://captcha.com/' + src[i]
        response = requests.get(img_url,headers = headers)
        if response.status_code == 200:
          image = response.content
          with open(filename,'wb') as f:
            f.write(image)
            count += 1
            print('保存第{}张脸验证码成功'.format(count))
            time.sleep(1)
def main():
  url = 'https://captcha.com/captcha-examples.html?cst=corg'
  headers = {usewegefhedghef}
  html = get_Page(html,headers)
  parse_page(html,headers)
if __name__ == '__main__':
  main()
        
        
