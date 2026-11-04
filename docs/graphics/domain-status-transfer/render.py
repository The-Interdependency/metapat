"""Render the domain-status transfer card (MPL-2.0).

Usage: python render.py --out-dir /tmp/domain-status-transfer
Owner: The Interdependency. GPT generated; context and prompt Erin Spencer.
This optional documentation tool writes PNG/PDF, previews, and validation JSON
only beneath the selected output directory. It uses no network or credentials.
The pinned source statements and proposed clarification remain separate from canon.
Validation checks one finite conjugacy, a broken-map falsifier, contrast, and text
layout. The displayed algebra supplies the general argument under its assumptions.
Rollout is manual; rollback removes this folder and its two README index links.
"""
import argparse
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle
from PIL import Image, ImageOps

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--out-dir', type=Path, default=Path('build/domain-status-transfer'))
OUT = parser.parse_args().out_dir.resolve()
OUT.mkdir(parents=True, exist_ok=True)
INK = '#17232F'
MUTED = '#4D5C68'
BLUE = '#075B83'
LINE = '#C6CED5'
PANEL = '#F3F6F8'
AMBER = '#704A16'
AMBER_BG = '#FAF5EB'
WHITE = '#FFFFFF'
W, H = 1000, 1414
plt.rcParams.update({
    'font.family': 'DejaVu Sans', 'font.size': 11,
    'mathtext.fontset': 'stix', 'pdf.fonttype': 42, 'ps.fonttype': 42,
    'svg.fonttype': 'none', 'text.color': INK,
})
fig = plt.figure(figsize=(8.2677, 11.6929), dpi=180, facecolor=WHITE)
ax = fig.add_axes([0, 0, 1, 1])
ax.set(xlim=(0,W), ylim=(H,0))
ax.set_axis_off()
texts=[]

def text(x,y,s,size=11,color=INK,weight='normal',ha='left',va='top',family=None,linespacing=1.4,url=None):
    t=ax.text(x,y,s,fontsize=size,color=color,fontweight=weight,ha=ha,va=va,
              family=family,linespacing=linespacing,url=url,zorder=5)
    texts.append(t)
    return t

def line(x1,y1,x2,y2,color=LINE,width=0.8):
    ax.plot([x1,x2],[y1,y2],color=color,lw=width,zorder=2)

def arrow(x1,y1,x2,y2,color=INK,width=1.25):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=11,
                                linewidth=width,color=color,zorder=3))

def box(x,y,w,h,fill):
    ax.add_patch(Rectangle((x,y),w,h,facecolor=fill,edgecolor='none',zorder=0))

text(62,43,'METAPAT  /  CHAPTER ZERO',9.1,BLUE,'bold')
text(938,43,'EXPLANATORY CARD 01  |  04 NOV 2026',8.2,MUTED,ha='right')
text(60,94,'When status crosses\na domain boundary',29,INK,family='DejaVu Serif',linespacing=1.15)
text(62,218,'Standing follows the justification preserved by the mapping.',12.0,INK)
line(62,258,938,258,color=INK,width=1.1)

text(62,282,'01  /  VERIFY WHAT THE CLAIM DEPENDS ON',9.4,BLUE,'bold')
text(62,315,'Preserve the transition. Carry the invariant.',16.1,INK,'bold')
text(62,353,'A sufficient formal case: a bijection preserves the state transition.',10.8,MUTED)

box(62,393,876,263,PANEL)
text(359,414,'CURRENT STATE',8.5,MUTED,'bold',ha='center')
text(742,414,'NEXT STATE',8.5,MUTED,'bold',ha='center')
text(86,469,'SYSTEM A',9.3,INK,'bold',va='center')
text(86,603,'SYSTEM B',9.3,INK,'bold',va='center')
text(359,469,r'$x$',25,INK,ha='center',va='center')
text(742,469,r'$T_A(x)$',25,INK,ha='center',va='center')
text(359,603,r'$f(x)$',25,INK,ha='center',va='center')
text(742,603,r'$T_B(f(x))$',25,INK,ha='center',va='center')
arrow(422,469,657,469)
arrow(422,603,636,603)
text(537,452,r'$T_A$',12.5,ha='center',va='bottom')
text(530,586,r'$T_B$',12.5,ha='center',va='bottom')
arrow(359,496,359,575,BLUE)
arrow(742,496,742,575,BLUE)
text(333,536,r'$f$',15,BLUE,ha='right',va='center')
text(766,536,r'$f$',15,BLUE,va='center')
text(550,531,'BOTH ROUTES AGREE',8.6,BLUE,'bold',ha='center',va='center')

text(62,679,r'For a bijection $f:A\to B$ and transitions $T_A,T_B$, require:',10.7)
text(500,718,r'$f(T_A(x))=T_B(f(x))\quad (\forall x\in A)$',20,BLUE,ha='center')
text(62,772,r'An invariant is an unchanged quantity: $I_A(T_A(x))=I_A(x)$.',10.5)
text(62,805,r'Define $I_B=I_A\circ f^{-1}$. For $y=f(x)$, the proof carries across:',10.5)
text(500,846,r'$I_B(T_B(y))=I_A(T_A(x))=I_A(x)=I_B(y)$',16.3,INK,ha='center')

line(62,902,938,902)
text(62,926,'02  /  WHAT CAN CARRY ACROSS',9.4,BLUE,'bold')
text(62,963,'SOURCE BASIS',8.8,MUTED,'bold')
text(352,963,'TARGET STANDING',8.8,MUTED,'bold')
line(62,988,938,988)
rows=[
 (1004,'Structural proof','Mapped conclusion follows under\nthe preserved hypotheses.'),
 (1065,'Empirical finding','Applicability needs evidence;\nsource uncertainty remains.'),
 (1126,'Resemblance','Candidate correspondence;\ntarget validity remains unresolved.'),
]
for y,left,right in rows:
    text(62,y,left,10.7,INK,'bold')
    text(352,y,right,10.6,INK,linespacing=1.25)
    line(62,y+49,938,y+49)

box(62,1197,876,103,AMBER_BG)
text(80,1212,'hmmm  /  CURRENT IMPLEMENTATION [2]',9.4,AMBER,'bold')
text(80,1240,'The classifier stores a proof ID without checking the proof.',10.0)
text(80,1265,'Transfer flags stay false, even for SAME_STRUCTURE.',10.0)

repo='https://github.com/The-Interdependency/metapat/blob/7480d6d6d42cded74a9d69aeac975e590368c097/'
text(62,1320,'[1] Chapter Zero, Theorem 7.',8.3,MUTED,url=repo+'CHAPTER_ZERO.md#seventh-theorem-domain-terms-do-not-transfer-by-structure-alone')
text(391,1320,'[2] Structural recurrence, verification and limits.',8.3,MUTED,url=repo+'docs/structural-recurrence.md#verification-and-limits')
text(62,1343,'Source: metapat @ 7480d6d6d42c. This card proposes a clarification; canon is unchanged.',8.0,MUTED)
text(62,1372,'GPT generated; context and prompt: Erin Spencer.',8.3,INK)
text(938,1372,'Formal example derived here.',8.3,MUTED,ha='right')

# Meaningful verification: exact finite conjugacy, invariant, and one falsifier.
f={0:2,1:0,2:3,3:1}
inv={v:k for k,v in f.items()}
ta={0:1,1:0,2:3,3:2}
tb={f[x]:f[ta[x]] for x in f}
ia=lambda x:x//2
ib=lambda y:ia(inv[y])
assert all(f[ta[x]]==tb[f[x]] for x in f)
assert all(ia(ta[x])==ia(x) for x in f)
assert all(ib(tb[y])==ib(y) for y in inv)
bad=dict(tb)
bad[f[0]]=f[2]
assert f[ta[0]] != bad[f[0]]
assert ib(bad[f[0]]) != ib(f[0])

def luminance(h):
    rgb=[int(h[i:i+2],16)/255 for i in (1,3,5)]
    lin=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in rgb]
    return .2126*lin[0]+.7152*lin[1]+.0722*lin[2]
contrasts={}
for fg,bg in [(INK,WHITE),(MUTED,WHITE),(BLUE,WHITE),(BLUE,PANEL),(INK,PANEL),(AMBER,AMBER_BG),(INK,AMBER_BG)]:
    a,b=sorted([luminance(fg),luminance(bg)])
    ratio=(b+.05)/(a+.05)
    assert ratio>=4.5,(fg,bg,ratio)
    contrasts[fg+'/'+bg]=round(ratio,2)

# Verify typography boundaries and unintended overlapping text before rendering.
fig.canvas.draw()
renderer=fig.canvas.get_renderer()
issues=[]
for i,t in enumerate(texts):
    b=t.get_window_extent(renderer)
    if b.x0<0 or b.x1>fig.bbox.width or b.y0<0 or b.y1>fig.bbox.height:
        issues.append(('bounds',t.get_text()))
    for q in texts[i+1:]:
        bq=q.get_window_extent(renderer)
        if b.overlaps(bq):
            issues.append(('overlap',t.get_text(),q.get_text()))
if issues:
    raise AssertionError(issues)

basename='domain-status-transfer-card'
pdf=OUT/(basename+'.pdf')
png=OUT/(basename+'.png')
fig.savefig(pdf,format='pdf',metadata={'Title':'When status crosses a domain boundary','Author':'GPT generated; context and prompt: Erin Spencer','Subject':'Proposed explanation of justified status transfer, with a formal invariant proof and current METAPAT boundary.'})
fig.savefig(png,format='png',dpi=300,metadata={'Title':'When status crosses a domain boundary','Description':'A sufficient mathematical transfer example uses a bijection f preserving transitions. An invariant then carries across. Structural proofs need preserved hypotheses; empirical findings need an applicability bridge; resemblance supports a candidate mapping. The current METAPAT recurrence classifier does not verify its proof IDs.','Author':'GPT generated; context and prompt: Erin Spencer'})
preview=OUT/'domain-card-preview.png'
im=Image.open(png)
im.thumbnail((1240,1754))
im.save(preview)
gray=ImageOps.grayscale(im).convert('RGB')
gray.save(OUT/'domain-card-grayscale.png')
report={'finite_conjugacy':'passed','invariant_transport':'passed','broken_mapping_falsifier':'passed','text_layout':'passed','contrast_ratios':contrasts,'sources_commit':'7480d6d6d42cded74a9d69aeac975e590368c097','files':[str(png),str(pdf)]}
(OUT/'domain-card-validation.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
