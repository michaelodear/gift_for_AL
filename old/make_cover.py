from PIL import Image, ImageDraw, ImageFont

W,H = 1500,600
VOID=(8,11,15); PANEL=(14,22,32)
AMBER=(230,165,50); AMBER_DIM=(138,106,44)
DIM=(85,102,118); INK=(199,210,220); RED=(207,70,52)

img = Image.new("RGB",(W,H),VOID)
d = ImageDraw.Draw(img,"RGBA")

# vertical gradient (top a touch lit, cold)
for y in range(H):
    t = 1-abs(y-260)/H
    r=int(VOID[0]+ (14-VOID[0])*max(0,t)*0.9)
    g=int(VOID[1]+ (22-VOID[1])*max(0,t)*0.9)
    b=int(VOID[2]+ (32-VOID[2])*max(0,t)*0.9)
    d.line([(0,y),(W,y)],fill=(r,g,b))
# faint scanlines
for y in range(0,H,3):
    d.line([(0,y),(W,y)],fill=(0,0,0,26))
# vignette-ish darker top/bottom
for y in list(range(0,90))+list(range(H-90,H)):
    a=int(120*(1-min(y,H-1-y)/90))
    d.line([(0,y),(W,y)],fill=(0,0,0,max(0,a)))

def font(path,size): return ImageFont.truetype(path,size)
mono   = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
sans   = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
sansB  = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
condB  = "/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf"

def spaced(xy,text,f,fill,track):
    x,y=xy
    for ch in text:
        d.text((x,y),ch,font=f,fill=fill)
        x+=d.textlength(ch,font=f)+track
    return x
def spaced_w(text,f,track):
    return sum(d.textlength(ch,font=f)+track for ch in text)-track

CY=300  # safe-band center

# ---- seal (globe + crosshair), left ----
sx,sy,R=150,CY,58
d.ellipse([sx-R,sy-R,sx+R,sy+R],outline=INK,width=3)
d.ellipse([sx-R//2,sy-R,sx+R//2,sy+R],outline=INK,width=2)     # meridian
for dy in (-R//2,0,R//2):
    d.line([(sx-R,sy+dy),(sx+R,sy+dy)],fill=(199,210,220,150),width=1)
d.line([(sx,sy-R),(sx,sy+R)],fill=AMBER,width=2)               # amber axis
d.line([(sx,sy),(sx+R,sy+R//2)],fill=(230,165,50,140),width=1)
d.line([(sx,sy),(sx-R,sy+R//2)],fill=(230,165,50,140),width=1)

TX=250  # text block left

# ---- eyebrow: CASE FILE 0507 ----
fEy=font(mono,26)
spaced((TX,CY-92),"CASE FILE 0507",fEy,AMBER,6)

# ---- title: THE GROCER ----
fT=font(condB,96)
end=spaced((TX-2,CY-58),"THE GROCER",fT,INK,3)

# ---- RESTRICTED chip (to the right of the eyebrow) ----
fC=font(sansB,20)
ct="RESTRICTED"; cw=spaced_w(ct,fC,3)
cx0=TX+spaced_w("CASE FILE 0507",fEy,6)+28; cyy=CY-90
pad=12
d.rounded_rectangle([cx0,cyy-4,cx0+cw+pad*2+22,cyy+30],radius=5,outline=RED,width=2)
d.ellipse([cx0+11,cyy+9,cx0+21,cyy+19],fill=RED)
spaced((cx0+pad+22,cyy+2),ct,fC,RED,3)

# ---- baseline strip ----
fB=font(sans,19)
spaced((TX,CY+62),"OFFICE OF INTERNATIONAL INVESTIGATION",fB,DIM,3)
fB2=font(mono,17)
sub="EVIDENCE CONTROL   ·   MIRROR NODE 07 — LIVE"
spaced((TX,CY+92),sub,fB2,AMBER_DIM,2)

# amber rule under title
d.line([(TX,CY+48),(end,CY+48)],fill=(230,165,50,120),width=2)

# ---- redaction bars, right side (classified texture) ----
import random; random.seed(7)
bx=1080
for i,by in enumerate(range(CY-96,CY+110,26)):
    w=random.choice([120,190,250,160,210])
    col=(24,36,48,255) if i%3 else (207,70,52,60)
    d.rounded_rectangle([bx,by,bx+w,by+15],radius=3,fill=col)
    if i%3==0:
        d.rounded_rectangle([bx+w+12,by,bx+w+12+random.choice([70,110,90]),by+15],radius=3,fill=(24,36,48,255))

img.save("act2_cover.png")
print("saved act2_cover.png", img.size)
