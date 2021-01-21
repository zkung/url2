## Url2
Crawler series tool set.

--------
## Install
```
pip install url2
```
--------
## Parameter
```python
url2(url, headers={'User-Agent':'Mozolla/5.0'}, encode=False, verify=True, cdx=True, form_data=None)
```
## Usage

**url2html**

```python
from url2 import url2

url = 'https://www.huya.com/669166'
html = url2(url).html
print(html)
```
result:
```
<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="ie6" lang="zh-cmn-Hans"> <![endif]-->
<!--[if IE 7]>         <html class="ie7" lang="zh-cmn-Hans"> <![endif]-->
<!--[if IE 8]>         <html class="ie8" lang="zh-cmn-Hans"> <![endif]-->
<!--[if IE 9]>         <html class="ie9" lang="zh-cmn-Hans"> <![endif]-->
<!--[if gt IE 9]><!--> <html lang="zh-cmn-Hans"><!--<![endif]-->
<head>
    <meta charset="utf-8">
    <title>虎牙直播-技术驱动娱乐-弹幕式互动直播平台</title>
    <meta name="Keywords" content="lol直播,英雄联盟直播,dota2直播,dnf直播,cf直播,绝地求生直播，王者荣耀直播，球球大作战直播，游戏直播,赛事直播,YY直播,美女直播,户外直播,视频直播,虎牙直播"/>
    <meta name="Description" content="虎牙直播是以游戏直播为主的弹幕式互动直播平台，累计注册用户2亿，提供热门游戏直播、电竞赛事直播与游戏赛事直播，手游直播等。包含英雄联盟lol，王者荣耀，绝地求生，和平精英等游戏直播，lol、dota2、dnf等热门游戏直播以及单机游戏、手游等游戏直播。"/>
......
.....
....
...
..
.
```
--------
**url2xpath**

```python
from url2 import url2

url = 'https://www.huya.com/669166'
xp = url2(url).xpath
hrefs = xp('//@href')
print(hrefs)
```
result:
```
['https://www.huya.com/guanzongo', 'https://a.msstatic.com/huya/main3/common/headerStyle_694cd.css', 'https://a.msstatic.com/huya/main3/app/room_normal_9e1d4.css', 'https://a.msstatic.com/huya/h5player/room/2010221757/vplayer.css', 'https://a.msstatic.com/huya/h5player/room/2010221757/vplayer.js', 'https://www.huya.com/', 'https://www.huya.com/', 'https://www.huya.com/l', 'https://www.huya.com/g', 'https://www.huya.com/m', 'http://v.huya.com', 'https://www.huya.com/g/100023', 'https://www.huya.com/g/lol', 'http://v.huya.com/u/20020995', '//www.huya.com/download/', '#', '#', '#', 'https://www.huya.com/myfollow', 'https://www.huya.com/l', 'https://www.huya.com/m', 'https://www.huya.com/g/100023', 'https://www.huya.com/g/100002', 'https://www.huya.com/g/100022', 'https://www.huya.com/g/100004', 'https://hd.huya.com/pc/2019zhubo/pages/index.html', 'https://www.huya.com/myfollow', 'https://www.huya.com/l', 'https://www.huya.com/660000', 'https://www.huya.com/660006', 'https://www.huya.com/kpl', 'https://www.huya.com/660004', 'https://www.huya.com/660006', '//www.huya.com/m', 'https://www.huya.com/g/100023'
......
.....
....
...
..
.
```
--------
**url2soup**

```python
from url2 import url2

url = 'https://www.huya.com/669166'
soup = url2(url).soup
as_ = soup.find_all("a",href=True)
hrefs = [a.get('href') for a in as_]
print(hrefs)
```
result:
```
['https://www.huya.com/', 'https://www.huya.com/', 'https://www.huya.com/l', 'https://www.huya.com/g', 'https://www.huya.com/m', 'http://v.huya.com', 'https://www.huya.com/g/100023', 'https://www.huya.com/g/1', 'http://v.huya.com/u/20020995', '#', '//www.huya.com/download/', '#', '#', 'https://www.huya.com/myfollow', 'https://www.huya.com/l', 'https://www.huya.com/m', 'https://www.huya.com/g/100023', 'https://www.huya.com/g/100002', 'https://www.huya.com/g/100022', 'https://www.huya.com/g/100004', 'https://hd.huya.com/pc/2019zhubo/pages/index.html', 'https://www.huya.com/myfollow', 'https://www.huya.com/l', 'https://www.huya.com/660000', 'https://www.huya.com/660006', 'https://www.huya.com/s', 'https://www.huya.com/lck', 
......
.....
....
...
..
.
```
--------
**url2post**

```python
from url2 import url2

url = 'https://fanyi.baidu.com/sug'
content = '你好'
data = f'kw:{content}'
x = url2(url, form_data=data).html
print(x)
```
result:
```
{'errno': 0,
 'data': [{'k': '你好', 'v': '[nǐ hǎo] how do you do; how are you; hello;'},
  {'k': '你好，陌生人', 'v': '网络 Hello Stranger; knowing me knowing you;'},
  {'k': '你好吗', 'v': 'How are you; How are you doing; How do you do;'}]}
```
--------
**build/auto**

```python
base = url2('https://top.chinaz.com/diqu/index_GuangDong_ShenZhen.html')
base.build({'web_name':['腾讯网'], 'url':['qq.com']})
base.auto('https://top.chinaz.com/diqu/index_GuangDong_ZhuHai.html')
```
result:
```
{'web_name': ['魅族官网',
  '5118站长大数据',
  '学信网',
  '魅族Flyme官网',
  '时代互联',
  '有问必答健康网健康知识数据中心',
  '格力',
  '北京师范大学珠海分校',
  '汤臣倍健',
  '周易天地',
  '中国摄影在线',
  '珠海人力资源网',
  '中国珠海',
  '天堂纪念网',
  '爱词霸英语沙龙',
  '魅族官网',
  '耐思尼克',
  '格力官网',
  'Flyme社区',
  '全志科技',
  'iBS语言学校',
  '魅族社区',
  '李锦记',
  '淘域网',
  '紫金论坛',
  '紫金论坛',
  'WPS海外版官网',
  '北京理工大学珠海学院',
  '仪表展览网',
  '格力商城'],
 'url': ['www.meizu.com',
  'www.5118.com',
  'account.chsi.com.cn',
  'flyme.cn',
  'now.cn',
  'tag.120ask.com',
  'gree.com',
  'bnuz.edu.cn',
  'by-health.com',
  '64gua.com',
  'cphoto.net',
  'zh-hr.com',
  'zhuhai.gov.cn',
  'waheaven.com',
  'news.iciba.com',
  'meizu.cn',
  'iisp.com',
  'www.gree.com.cn',
  'bbs.flyme.cn',
  'allwinnertech.com',
  'zhibs.net',
  'bbs.meizu.cn',
  'lkk.com',
  'b08.com',
  'gdzijin.com',
  'bbs.gdzijin.com',
  'wps.com',
  'zhbit.com',
  '18show.cn',
  'mall.gree.com']}
```
--------
