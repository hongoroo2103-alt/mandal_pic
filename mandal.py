#!/usr/bin/env python3
"""Generate free 1080x1350 Mongolian Facebook image posts using Pillow."""
from pathlib import Path
from datetime import datetime, timedelta, date
from zoneinfo import ZoneInfo
from PIL import Image, ImageDraw, ImageFont
import math, json, argparse

ROOT=Path(__file__).parent
POSTS=[
("МАНДАЛ ЗУРХАЙ","Өөрийн доторх ертөнцийг нээ","Та ямар орд вэ?","✨ Мандал Зурхай хуудсанд тавтай морил. Бид орд, хайр, зан чанар, өөрийгөө таних талаар сонирхолтой постууд хуваалцана.\n\n💬 Та ямар орд вэ? Сэтгэгдэлд бичээрэй!\n\n#МандалЗурхай #Зурхай"),
("ЗУРХАЙН 4 МАХБОД","Гал • Газар • Агаар • Ус","Аль нь танд ойр вэ?","✨ Зурхайд ордуудыг Гал, Газар, Агаар, Ус гэсэн 4 махбодод хуваадаг. Энэ бол шинжлэх ухааны баталгаа биш, өөрийгөө эргэцүүлэх бэлгэдлийн арга юм.\n\n💬 Та ямар орд вэ? #МандалЗурхай"),
("ХАЙРЫН ХЭЛ","Халамж • Сайхан үг • Хамт байх","Та хайраа хэрхэн илэрхийлдэг вэ?","💛 Хайрыг хүн бүр өөр өөрөөр илэрхийлдэг. Зурхайн нийцэл сонирхолтой ч сайн харилцаанд ойлголцол хамгийн чухал.\n\n💬 Та хайраа яаж илэрхийлдэг вэ? #МандалЗурхай"),
("МӨНГӨНИЙ 3 ЗУРШИЛ","Төлөвлө • Хадгал • Эргэн хар","Аль зуршлаас эхлэх вэ?","💰 Орлого, зарлагаа бич. Боломжтой бага дүнгээр хуримтлуул. Сар бүр зорилгоо хар. Одноос илүү бодит зуршил нөлөөлнө.\n\n💬 Та аль зуршлаас эхлэх вэ? #МандалЗурхай"),
("САРНЫ ТЭМДЭГЛЭЛ","Өнөөдрийн бодлоо бичээд үз","Таны өнөөдрийн нэг үг?","🌙 Өнөөдөр юу баярлуулав? Юу хэцүү байсан бэ? Маргааш юуг өөрчлөх вэ? Сарны бэлгэдлийг өөрийгөө таних тэмдэглэл болгож болно.\n\n💬 Өнөөдрийн нэг үг? #МандалЗурхай"),
("ТАНЫ ХҮЧТЭЙ ТАЛ","Зориг • Тэвчээр • Бүтээлч байдал","Өөрийн нэг давуу талаа бич","⭐ Давуу талаа анзаарч, өдөр бүр хөгжүүлээрэй. Зурхайн тайлбар нь зөвхөн өөрийгөө эргэцүүлэх нэг арга.\n\n💬 Таны нэг давуу тал юу вэ? #МандалЗурхай"),
("ӨӨРТӨӨ ЦАГ ГАРГА","Өдөр бүр 10 минут өөртөө","Та өнөөдөр амарсан уу?","🌿 Өөртөө зориулсан багахан цаг ч үнэ цэнтэй. Өнөөдөр 10 минут утсаа холдуулаад амьсгалаа ажиглаарай.\n\n💬 Та яаж амардаг вэ? #МандалЗурхай"),
("ШИНЭ ЭХЛЭЛ","Жижиг алхмаас эхэл","Таны энэ долоо хоногийн зорилго?","✨ Амжилт жижиг алхмаас эхэлдэг. Энэ долоо хоногт хийж болох нэг зорилго сонгоорой.\n\n💬 Ямар зорилго тавьсан бэ? #МандалЗурхай"),
("ХАРИЛЦААНЫ НУУЦ","Сонсох нь ойлголцлын эхлэл","Та сайн сонсогч мөн үү?","💛 Нөгөө хүнээ таслалгүй сонсох нь хайр, нөхөрлөлийг сайжруулдаг.\n\n💬 Та юуг хамгийн их үнэлдэг вэ? #МандалЗурхай"),
("ӨДРИЙН НЭГ АСУУЛТ","Би өнөөдөр юунд талархав?","Талархах нэг зүйлээ бич","🌙 Өнөөдөр талархах гурван зүйлээ тэмдэглээд үзээрэй.\n\n💬 Нэгийг нь энд хуваалцаарай! #МандалЗурхай")
]
def font(size,bold=False):
 paths=(['/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'] if bold else ['/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'])
 for p in paths:
  if Path(p).exists():return ImageFont.truetype(p,size)
 return ImageFont.load_default()
def render(day):
 index=(day-date(2026,11,13)).days%len(POSTS)
 title,subtitle,question,caption=POSTS[index]
 W,H=1080,1350;gold='#b08d57';dark='#3d302b';ivory='#f8f3e9'
 image=Image.new('RGB',(W,H),ivory); d=ImageDraw.Draw(image)
 d.rounded_rectangle((45,45,1035,1305),radius=35,outline='#d3bb94',width=4)
 d.text((100,103),'МАНДАЛ ЗУРХАЙ',font=font(42,True),fill=dark)
 d.text((103,167),'MANDALA ASTRO',font=font(24),fill=gold)
 cx,cy=540,450
 for r in (195,165,118):d.ellipse((cx-r,cy-r,cx+r,cy+r),outline=gold,width=4 if r==195 else 2)
 for i in range(12):
  a=math.pi*i/6
  x,y=cx+181*math.cos(a),cy+181*math.sin(a)
  d.ellipse((x-5,y-5,x+5,y+5),fill=gold)
 # abstract celestial star
 for i in range(16):
  a=math.pi*i/8
  r=98 if i%2==0 else 52
  d.line((cx,cy,cx+r*math.cos(a),cy+r*math.sin(a)),fill=gold,width=4)
 d.ellipse((cx-30,cy-30,cx+30,cy+30),fill=ivory,outline=gold,width=3)
 def wrap(txt,maxpx,ft):
  words=txt.split();lines=[];line=''
  for w in words:
   test=(line+' '+w).strip()
   if d.textbbox((0,0),test,font=ft)[2]>maxpx and line:
    lines.append(line);line=w
   else:line=test
  if line:lines.append(line)
  return lines
 def center(lines,start,ft,fill,step):
  for j,line in enumerate(lines):
   bb=d.textbbox((0,0),line,font=ft);d.text(((W-(bb[2]-bb[0]))/2,start+j*step),line,font=ft,fill=fill)
 center(wrap(title,910,font(64,True)),690,font(64,True),dark,86)
 center(wrap(subtitle,930,font(35)),885,font(35),dark,53)
 d.rounded_rectangle((100,1085,980,1195),radius=24,fill='#eee1ce')
 center(wrap(question,810,font(32,True)),1113,font(32,True),dark,42)
 d.text((103,1248),'ӨӨРИЙН ДОТОРХ ЕРТӨНЦИЙГ НЭЭ',font=font(22),fill=gold)
 (ROOT/'images').mkdir(exist_ok=True);(ROOT/'captions').mkdir(exist_ok=True)
 name=day.isoformat(); image.save(ROOT/'images'/f'{name}.png',optimize=True)
 (ROOT/'captions'/f'{name}.txt').write_text(caption+'\n',encoding='utf-8')
 print(name, title)
if __name__=='__main__':
 p=argparse.ArgumentParser(); p.add_argument('--days',type=int,default=15); a=p.parse_args()
 today=datetime.now(ZoneInfo('Asia/Ulaanbaatar')).date()
 for i in range(a.days):
  day=today+timedelta(days=i)
  if day.weekday()<5:render(day)
