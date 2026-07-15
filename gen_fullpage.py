# -*- coding: utf-8 -*-
import re, io, random
random.seed(7)
A = 'assets'
CY, BL, PU, VI = '#00E5FF', '#3B82F6', '#7C3AED', '#A78BFA'
BG, BG2, LN, DIM, TXT = '#0B0E1A', '#0E1424', '#1B2440', '#8B99BB', '#B8C4E0'
MONO = "Consolas,'Courier New',monospace"

def esc(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

def cut_rect(x,y,w,h,c=10,**kw):
    at=' '.join('%s="%s"'%(k.replace('_','-'),v) for k,v in kw.items())
    return ('<path d="M%s %s H%s L%s %s V%s L%s %s H%s L%s %s V%s Z" %s/>'
            %(x+c,y, x+w-c, x+w,y+c, y+h-c, x+w-c,y+h, x+c, x,y+h-c, y+c, at))

def defs(idp):
    return ('<defs>'
      '<pattern id="g%s" width="28" height="28" patternUnits="userSpaceOnUse">'
      '<path d="M28 0H0V28" fill="none" stroke="%s" stroke-width="0.6" opacity="0.5"/></pattern>'
      '<pattern id="s%s" width="4" height="4" patternUnits="userSpaceOnUse">'
      '<rect width="4" height="1" fill="#FFFFFF" opacity="0.02"/></pattern>'
      '<linearGradient id="swp%s" x1="0" y1="0" x2="1" y2="0">'
      '<stop offset="0" stop-color="%s" stop-opacity="0"/>'
      '<stop offset="0.5" stop-color="%s" stop-opacity="0.10"/>'
      '<stop offset="1" stop-color="%s" stop-opacity="0"/></linearGradient>'
      '<linearGradient id="hdr%s" x1="0" y1="0" x2="1" y2="0">'
      '<stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient>'
      '</defs>')%(idp,LN,idp,idp,CY,CY,CY,idp,BG2,BG)

def led(x,y,c=CY,d='2s'):
    return ('<circle cx="%s" cy="%s" r="3" fill="%s"><animate attributeName="opacity" '
            'values="1;0.25;1" dur="%s" repeatCount="indefinite"/></circle>'
            '<circle cx="%s" cy="%s" r="6" fill="none" stroke="%s" stroke-width="0.8" opacity="0.5"/>')%(x,y,c,d,x,y,c)

def sweep(idp,x,y,w,h,dur='9s'):
    return ('<rect x="%s" y="%s" width="46" height="%s" fill="url(#swp%s)" opacity="0.55">'
            '<animate attributeName="x" values="%s;%s;%s" dur="%s" repeatCount="indefinite"/></rect>')%(x,y,h,idp,x,x+w-46,x,dur)

def svg(w,h,body,title):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %s %s" width="%s" height="%s" '
            'role="img" aria-label="%s">%s</svg>')%(w,h,w,h,esc(title),body)

def txt(x,y,s,size=12,fill=TXT,ls='2',anchor='start',weight='400'):
    return ('<text x="%s" y="%s" font-family="%s" font-size="%s" fill="%s" '
            'letter-spacing="%s" text-anchor="%s" font-weight="%s">%s</text>')%(x,y,MONO,size,fill,ls,anchor,weight,esc(s))

def flowdot(path,dur,c=CY,r=2.2,begin='0s'):
    return ('<circle r="%s" fill="%s"><animateMotion dur="%s" begin="%s" '
            'repeatCount="indefinite" path="%s"/></circle>')%(r,c,dur,begin,path)

W=1200

def module_header(fname, sysno, name, sub, ledc=CY):
    h=70; idp=fname.replace('-','')
    b=[defs(idp)]
    b.append(cut_rect(2,2,W-4,h-4,12,fill='url(#hdr%s)'%idp,stroke=CY,stroke_width='1.4'))
    b.append('<rect x="2" y="2" width="%s" height="%s" fill="url(#g%s)" opacity="0.5"/>'%(W-4,h-4,idp))
    b.append('<rect x="2" y="2" width="%s" height="%s" fill="url(#s%s)"/>'%(W-4,h-4,idp))
    b.append(cut_rect(14,14,190,h-28,8,fill=BG,stroke=PU,stroke_width='1'))
    b.append(txt(28,h/2+5,sysno,15,CY,'3','start','700'))
    b.append(led(188,h/2,ledc))
    b.append(txt(228,h/2-3,name,19,'#EAF6FF','4','start','700'))
    b.append(txt(228,h/2+16,sub,10,DIM,'2.5'))
    b.append('<path d="M%s %s H%s" stroke="%s" stroke-width="1" stroke-dasharray="6 4"/>'%(W-330,h/2,W-40,LN))
    for i in range(6):
        x=W-320+i*48
        b.append(('<rect x="%s" y="%s" width="3" height="14" fill="%s" opacity="0.8">'
                  '<animate attributeName="opacity" values="0.9;0.25;0.9" dur="%.1fs" repeatCount="indefinite"/></rect>')
                 %(x,h/2-7,CY if i%2==0 else PU,2+i*0.4))
    b.append(flowdot('M%s %s H%s'%(W-330,h/2,W-40),'5s',CY))
    b.append(txt(W-28,h/2+4,'OK',11,CY,'2','end','700'))
    b.append(sweep(idp,6,6,W-12,h-12))
    io.open('%s/%s.svg'%(A,fname),'w',encoding='utf-8').write(svg(W,h,''.join(b),'%s %s section header'%(sysno,name)))

module_header('section-identity','SYS.01','IDENTITY // OPERATOR PROFILE','origin: tempe.az // clearance: public')
module_header('section-build','SYS.02','PROC.MONITOR // ACTIVE BUILDS','live processes // build daemon attached')
module_header('section-projects','SYS.03','EXEC // PROJECT MODULES','deployed units // source linked')
module_header('section-automation','SYS.04','AGENT.LOOP // AUTOMATION LAB','agentic workflows // ai-first pipeline',PU)
module_header('section-stack','SYS.05','STACK.MANIFEST // INVENTORY','scan complete // all drivers loaded')
module_header('section-tech','SYS.05','STACK.MANIFEST // TOOLING','inventory scan // drivers loaded')
module_header('section-learning','SYS.06','UPGRADE.QUEUE // LEARNING','scheduled installs // priority ordered',VI)
module_header('section-activity','SYS.07','TELEMETRY // RUNTIME STATS','sampling interval: continuous')
module_header('section-connect','SYS.08','UPLINK // COMM CHANNELS','handshake ready // signal stable')

def hero():
    h=320; idp='hero'; b=[defs(idp)]
    b.append('<rect width="%s" height="%s" fill="%s"/>'%(W,h,BG))
    b.append('<rect width="%s" height="%s" fill="url(#g%s)" opacity="0.55"/>'%(W,h,idp))
    b.append('<rect width="%s" height="%s" fill="url(#s%s)"/>'%(W,h,idp))
    b.append(cut_rect(3,3,W-6,h-6,14,fill='none',stroke=CY,stroke_width='1.6'))
    b.append(cut_rect(9,9,W-18,h-18,10,fill='none',stroke=LN,stroke_width='0.8'))
    b.append('<path d="M20 34 H%s" stroke="%s" stroke-width="1"/>'%(W-20,LN))
    b.append(txt(24,26,'YUG.PATEL // PERSONAL COMMAND INTERFACE',11,CY,'3','start','700'))
    b.append(txt(W-24,26,'STATUS: ONLINE',11,'#22C55E','2','end','700'))
    b.append(led(W-160,21,'#22C55E'))
    b.append(txt(34,120,'YUG PATEL',46,'#EAF6FF','8','start','700'))
    b.append('<rect x="36" y="134" width="330" height="3" fill="%s"><animate attributeName="opacity" values="1;0.4;1" dur="3s" repeatCount="indefinite"/></rect>'%CY)
    b.append(txt(36,164,'AI-FIRST DEVELOPER // CS @ ARIZONA STATE UNIVERSITY',14,VI,'3'))
    b.append(txt(36,190,'> agentic tooling . automation . shipping useful things',13,TXT,'1.5'))
    b.append('<rect x="36" y="204" width="9" height="16" fill="%s"><animate attributeName="opacity" values="1;0;1" dur="1.1s" repeatCount="indefinite"/></rect>'%CY)
    for i,(lab,c) in enumerate([('MODE: AI-FIRST',PU),('LOOP: BUILD-SHIP-REPEAT',CY),('SECTOR: AZ.US',BL)]):
        x=36+i*250
        b.append(cut_rect(x,238,230,34,7,fill=BG2,stroke=c,stroke_width='1'))
        b.append(txt(x+16,260,lab,11,c,'2','start','700'))
        b.append(led(x+212,255,c,'%ss'%(2+i)))
    px,py,pw,ph=830,52,340,236
    b.append(cut_rect(px,py,pw,ph,10,fill=BG2,stroke=PU,stroke_width='1.2'))
    b.append(txt(px+14,py+22,'PROC.MONITOR',11,VI,'3','start','700'))
    b.append('<path d="M%s %s H%s" stroke="%s" stroke-width="1"/>'%(px+10,py+32,px+pw-10,LN))
    procs=[('agent.loop',82,CY),('build.daemon',64,BL),('learn.queue',47,VI),('uplink.svc',91,PU)]
    for i,(nm,pc,c) in enumerate(procs):
        y=py+52+i*34
        b.append(txt(px+16,y+4,nm,10,TXT,'1'))
        b.append('<rect x="%s" y="%s" width="180" height="10" fill="%s" stroke="%s" stroke-width="0.7"/>'%(px+130,y-6,BG,LN))
        b.append(('<rect x="%s" y="%s" width="%s" height="10" fill="%s" opacity="0.85">'
                  '<animate attributeName="width" values="%s;%s;%s" dur="%ss" repeatCount="indefinite"/></rect>')
                 %(px+130,y-6,180*pc//100,c,180*pc//100,180*max(pc-18,8)//100,180*pc//100,4+i))
    pts=' '.join('%s,%s'%(px+16+i*10.5,py+205-random.randint(0,26)) for i in range(30))
    b.append(('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.4" opacity="0.9">'
              '<animate attributeName="opacity" values="0.9;0.45;0.9" dur="3.5s" repeatCount="indefinite"/></polyline>')%(pts,CY))
    b.append(txt(px+16,py+226,'signal.trace // nominal',9,DIM,'1.5'))
    b.append('<path d="M660 240 H790 V170 H830" fill="none" stroke="%s" stroke-width="1.2"/>'%LN)
    b.append(flowdot('M660 240 H790 V170 H830','4s',CY))
    b.append(sweep(idp,6,6,W-12,h-12,'11s'))
    io.open('%s/hero-banner.svg'%A,'w',encoding='utf-8').write(svg(W,h,''.join(b),'Yug Patel - personal command interface hero console'))
hero()

src=io.open('README.md',encoding='utf-8').read()
def badges_between(a_marker,b_marker):
    i=src.find(a_marker)
    if i<0: return []
    j=src.find(b_marker,i+1)
    seg=src[i:j if j>0 else len(src)]
    labs=re.findall(r'img\.shields\.io/badge/([^-]+)-',seg)
    out=[]
    for l in labs:
        l=l.replace('_',' ').replace('%20',' ')
        if l not in out and 0<len(l)<22: out.append(l)
    return out
stack=badges_between('section-tech','section-learning') or badges_between('section-stack','section-learning')
learn=['Applied AI/ML','Advanced TypeScript','Frontend Architecture','Data & API Design']
print('STACK:',stack)
print('LEARN:',learn)

def about():
    h=250; idp='abt'; b=[defs(idp)]
    b.append(cut_rect(2,2,W-4,h-4,12,fill=BG,stroke=CY,stroke_width='1.3'))
    b.append('<rect x="2" y="2" width="%s" height="%s" fill="url(#g%s)" opacity="0.45"/>'%(W-4,h-4,idp))
    b.append('<rect x="2" y="2" width="%s" height="36" fill="%s"/>'%(W-4,BG2))
    b.append('<path d="M2 38 H%s" stroke="%s" stroke-width="1"/>'%(W-2,CY))
    for i,c in enumerate(['#FF5F56','#FFBD2E','#22C55E']):
        b.append('<circle cx="%s" cy="20" r="5.5" fill="%s"/>'%(24+i*20,c))
    b.append(txt(W/2,24,'operator@yugpatel:~/identity',12,TXT,'1.5','middle'))
    b.append(txt(W-20,24,'TTY.01',10,DIM,'2','end'))
    lines=[('> whoami','#22C55E'),
           ('  yug.patel - computer science student @ arizona state university',TXT),
           ('> cat mission.txt','#22C55E'),
           ('  build ai-first developer tooling. automate the boring. ship real, useful software.',TXT),
           ('> cat focus.txt','#22C55E'),
           ('  agentic workflows / web engineering / systems that run while i sleep',TXT)]
    y=66
    for s,c in lines:
        b.append(txt(28,y,s,13,c,'0.5')); y+=28
    b.append('<rect x="28" y="%s" width="9" height="15" fill="%s"><animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></rect>'%(y-12,CY))
    b.append(txt(W-20,h-16,'session persistent // no idle timeout',9,DIM,'1.5','end'))
    b.append(sweep(idp,6,42,W-12,h-52,'10s'))
    io.open('%s/panel-about.svg'%A,'w',encoding='utf-8').write(svg(W,h,''.join(b),'About terminal: identity, mission and focus'))
about()

def inventory():
    chips=stack[:16]
    if not chips: chips=['Python','JavaScript','TypeScript','Tailwind CSS','Node.js','MySQL','Git','GitHub']
    cols=4; rows=(len(chips)+cols-1)//cols
    h=76+rows*56+14; idp='inv'
    b=[defs(idp)]
    b.append(cut_rect(2,2,W-4,h-4,12,fill=BG,stroke=PU,stroke_width='1.3'))
    b.append('<rect x="2" y="2" width="%s" height="%s" fill="url(#g%s)" opacity="0.4"/>'%(W-4,h-4,idp))
    b.append(txt(24,32,'INVENTORY.SCAN',12,VI,'3','start','700'))
    b.append(txt(W-24,32,'%s UNITS REGISTERED // 0 FAULTS'%len(chips),10,CY,'2','end'))
    b.append('<path d="M20 44 H%s" stroke="%s" stroke-width="1" stroke-dasharray="5 4"/>'%(W-20,LN))
    cw=(W-48-3*14)/4.0
    for i,cname in enumerate(chips):
        r,c=divmod(i,cols); x=24+c*(cw+14); y=60+r*56
        col=[CY,BL,VI,PU][c%4]
        b.append(cut_rect(int(x),y,int(cw),44,7,fill=BG2,stroke=col,stroke_width='1'))
        b.append('<rect x="%s" y="%s" width="4" height="20" fill="%s" opacity="0.9"/>'%(int(x)+10,y+12,col))
        b.append(txt(int(x)+26,y+20,cname.upper(),11,'#EAF6FF','1.5','start','700'))
        pc=random.randint(55,96)
        b.append('<rect x="%s" y="%s" width="%s" height="5" fill="%s" stroke="%s" stroke-width="0.5"/>'%(int(x)+26,y+28,int(cw)-60,BG,LN))
        b.append(('<rect x="%s" y="%s" width="%.0f" height="5" fill="%s" opacity="0.8">'
                  '<animate attributeName="opacity" values="0.85;0.4;0.85" dur="%.1fs" repeatCount="indefinite"/></rect>')
                 %(int(x)+26,y+28,(cw-60)*pc/100,col,3+(i%5)*0.7))
        b.append(led(int(x+cw)-14,y+22,col,'%ss'%(2+(i%4))))
    b.append(sweep(idp,6,50,W-12,h-60,'12s'))
    io.open('%s/panel-stack.svg'%A,'w',encoding='utf-8').write(svg(W,int(h),''.join(b),'Tech stack inventory panel'))
inventory()

def queue():
    items=learn[:6]
    if not items: items=['Next.js','TypeScript']
    h=64+len(items)*46+14; idp='lq'
    b=[defs(idp)]
    b.append(cut_rect(2,2,W-4,h-4,12,fill=BG,stroke=VI,stroke_width='1.3'))
    b.append('<rect x="2" y="2" width="%s" height="%s" fill="url(#g%s)" opacity="0.4"/>'%(W-4,h-4,idp))
    b.append(txt(24,32,'UPGRADE.QUEUE // SCHEDULED INSTALLS',12,VI,'3','start','700'))
    b.append(txt(W-24,32,'PRIORITY: FIFO',10,DIM,'2','end'))
    b.append('<path d="M20 44 H%s" stroke="%s" stroke-width="1" stroke-dasharray="5 4"/>'%(W-20,LN))
    for i,it in enumerate(items):
        y=58+i*46; pc=[68,52,38,27,18,12][i%6]
        col=VI if i%2 else CY
        b.append(cut_rect(24,y,W-48,36,6,fill=BG2,stroke=LN,stroke_width='0.9'))
        b.append(txt(40,y+23,'%02d'%(i+1),12,CY,'2','start','700'))
        b.append(txt(78,y+23,'installing :: %s'%it.lower(),12,'#EAF6FF','1.5'))
        b.append('<rect x="%s" y="%s" width="300" height="9" fill="%s" stroke="%s" stroke-width="0.6"/>'%(W-420,y+13,BG,LN))
        b.append(('<rect x="%s" y="%s" width="%s" height="9" fill="%s" opacity="0.85">'
                  '<animate attributeName="width" values="%s;%s;%s" dur="%ss" repeatCount="indefinite"/></rect>')
                 %(W-420,y+13,300*pc//100,col,300*pc//100,300*min(pc+14,98)//100,300*pc//100,5+i))
        b.append(txt(W-96,y+23,'%s%%'%pc,11,col,'1','start','700'))
        b.append(led(W-44,y+18,col,'%.1fs'%(2+i*0.5)))
    b.append(sweep(idp,6,50,W-12,h-60,'11s'))
    io.open('%s/panel-learning.svg'%A,'w',encoding='utf-8').write(svg(W,int(h),''.join(b),'Learning queue panel with progress bars'))
queue()

def telem():
    h=110; idp='tm'; b=[defs(idp)]
    b.append(cut_rect(2,2,W-4,h-4,10,fill=BG,stroke=CY,stroke_width='1.2'))
    b.append('<rect x="2" y="2" width="%s" height="%s" fill="url(#g%s)" opacity="0.45"/>'%(W-4,h-4,idp))
    b.append(txt(24,30,'TELEMETRY.FEED',11,CY,'3','start','700'))
    b.append(txt(24,50,'sampling github runtime metrics...',10,DIM,'1.5'))
    pts=' '.join('%s,%s'%(300+i*16,78-random.randint(4,40)) for i in range(28))
    b.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.4"/>'%(pts,CY))
    b.append('<path d="M300 82 H%s" stroke="%s" stroke-width="1"/>'%(300+27*16,LN))
    b.append(flowdot('M300 78 H%s'%(300+27*16),'6s',PU,2.5))
    cx,cyy=880,55
    for r_ in (14,26,38):
        b.append('<circle cx="%s" cy="%s" r="%s" fill="none" stroke="%s" stroke-width="0.8"/>'%(cx,cyy,r_,LN))
    b.append(('<path d="M%s %s L%s %s" stroke="%s" stroke-width="1.5" opacity="0.9">'
              '<animateTransform attributeName="transform" type="rotate" from="0 %s %s" to="360 %s %s" dur="6s" repeatCount="indefinite"/></path>')
             %(cx,cyy,cx+38,cyy,CY,cx,cyy,cx,cyy))
    b.append(led(cx+22,cyy-14,PU,'3s'))
    b.append(txt(W-30,40,'GRAPH.FEED: LIVE',10,VI,'2','end','700'))
    b.append(txt(W-30,60,'UNITS: COMMITS / STARS',9,DIM,'1.5','end'))
    b.append(sweep(idp,6,6,W-12,h-12,'9s'))
    io.open('%s/panel-telemetry.svg'%A,'w',encoding='utf-8').write(svg(W,h,''.join(b),'Telemetry feed strip'))
telem()

def uplink():
    h=150; idp='up'; b=[defs(idp)]
    b.append(cut_rect(2,2,W-4,h-4,12,fill=BG,stroke=PU,stroke_width='1.3'))
    b.append('<rect x="2" y="2" width="%s" height="%s" fill="url(#g%s)" opacity="0.4"/>'%(W-4,h-4,idp))
    b.append(txt(24,34,'UPLINK.CONSOLE',12,VI,'3','start','700'))
    b.append(txt(24,56,'open channels below // response time: human-scale',10,DIM,'1.5'))
    cx=1080
    b.append('<path d="M%s 118 V70 L%s 44 M%s 70 L%s 44" stroke="%s" stroke-width="1.6" fill="none"/>'%(cx,cx-14,cx,cx+14,CY))
    for i,r_ in enumerate((10,20,30)):
        b.append(('<circle cx="%s" cy="38" r="%s" fill="none" stroke="%s" stroke-width="1" opacity="0.7">'
                  '<animate attributeName="opacity" values="0.8;0.1;0.8" dur="3s" begin="%.1fs" repeatCount="indefinite"/></circle>')%(cx,r_,CY,i*0.5))
    chans=[('MAIL','mail.channel',CY),('GITHUB','repo.uplink',BL),('REPOS','browse.index',VI)]
    for i,(nm,sub,c) in enumerate(chans):
        x=40+i*300
        b.append(cut_rect(x,76,270,50,8,fill=BG2,stroke=c,stroke_width='1.1'))
        b.append(txt(x+18,98,nm,13,c,'3','start','700'))
        b.append(txt(x+18,116,sub,9,DIM,'1.5'))
        b.append(led(x+248,100,c,'%ss'%(2+i)))
        if i<2:
            b.append('<path d="M%s 101 H%s" stroke="%s" stroke-width="1.2" stroke-dasharray="4 3"/>'%(x+310,x+340,LN))
            b.append(flowdot('M%s 101 H%s'%(x+310,x+340),'2.5s',c,2))
    b.append('<path d="M950 101 H%s" stroke="%s" stroke-width="1.2" stroke-dasharray="4 3"/>'%(cx-10,LN))
    b.append(flowdot('M950 101 H%s'%(cx-10),'3s',PU,2.2))
    b.append(sweep(idp,6,6,W-12,h-12,'10s'))
    io.open('%s/panel-uplink.svg'%A,'w',encoding='utf-8').write(svg(W,h,''.join(b),'Uplink communication console'))
uplink()
print('assets generated OK')
