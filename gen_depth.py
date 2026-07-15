# -*- coding: utf-8 -*-
"""Premium depth pass: section connectors, HUD panels, project dashboard cards.
Layered translucent panels, cut-corner frames, grids, scanlines, glow, slow SMIL."""
import io

C, B, V, M, G = '#00E5FF', '#4D8AFF', '#7C3AED', '#FF2D95', '#22E06C'
D, P, P2 = '#0B0E1A', '#101530', '#131A36'
MONO = 'font-family="Consolas, Courier New, monospace"'


def write(name, body):
    io.open(f'assets/{name}.svg', 'w', encoding='utf-8', newline='\n').write(body)
    print(f'{name}.svg', len(body), 'B')


def defs(pid, extra=''):
    return f'''<defs>
<linearGradient id="{pid}bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{P2}"/><stop offset="1" stop-color="{D}"/></linearGradient>
<pattern id="{pid}gr" width="24" height="24" patternUnits="userSpaceOnUse"><path d="M24 0H0V24" fill="none" stroke="{B}" stroke-width="0.5" opacity="0.16"/></pattern>
<pattern id="{pid}sc" width="6" height="4" patternUnits="userSpaceOnUse"><rect width="6" height="1" fill="{C}" opacity="0.05"/></pattern>
<filter id="{pid}gl" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="2.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
{extra}</defs>'''


def cut_rect(x, y, w, h, cut=12):
    """Octagonal cut-corner panel path."""
    return (f'M{x+cut} {y} H{x+w-cut} L{x+w} {y+cut} V{y+h-cut} L{x+w-cut} {y+h} '
            f'H{x+cut} L{x} {y+h-cut} V{y+cut} Z')


def panel_shell(pid, w, h, title, sysid, cut=14):
    """Layered shell: bg gradient + grid + scanlines + frame + title tab + brackets."""
    p = cut_rect(1.5, 1.5, w-3, h-3, cut)
    return f'''<path d="{p}" fill="url(#{pid}bg)" stroke="{C}" stroke-width="1.5"/>
<path d="{p}" fill="url(#{pid}gr)"/>
<path d="{p}" fill="url(#{pid}sc)"/>
<path d="M{cut+1.5} 1.5 H{w-cut-1.5}" stroke="{C}" stroke-width="3" opacity="0.35"/>
<g fill="none" stroke="{V}" stroke-width="1.5" opacity="0.8">
<path d="M8 {h-26} v18 M8 {h-8} h18"/><path d="M{w-8} 26 v-18 M{w-8} 8 h-18"/>
</g>
<g transform="translate(14,4)"><rect width="{10+len(title)*7.4}" height="16" fill="{D}" stroke="{C}" stroke-width="1"/>
<text x="{5+len(title)*3.7}" y="12" {MONO} font-size="10" letter-spacing="2" fill="{C}" text-anchor="middle">{title}</text></g>
<text x="{w-14}" y="15" {MONO} font-size="8" letter-spacing="1" fill="{B}" text-anchor="end" opacity="0.9">{sysid}</text>
<rect x="{w-26}" y="{h-14}" width="6" height="6" fill="{G}"><animate attributeName="opacity" values="1;0.2;1" dur="2.6s" repeatCount="indefinite"/></rect>
<text x="{w-32}" y="{h-8}" {MONO} font-size="7" fill="{G}" text-anchor="end" letter-spacing="1">ONLINE</text>'''


def svg(name, w, h, title, desc, inner, pid, extra_defs=''):
    write(name, f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="{pid}t {pid}d" preserveAspectRatio="xMidYMid meet">
<title id="{pid}t">{title}</title><desc id="{pid}d">{desc}</desc>
{defs(pid, extra_defs)}
{inner}
</svg>''')


# ================= CONNECTORS (7 distinct, engineered) =================
CW, CH = 880, 78

def conn(name, title, desc, inner, pid):
    svg(name, CW, CH, title, desc, inner, pid)

# faint background trace layer shared by connectors (depth: bg dim, fg bright)
def bglayer(pid, d1, d2):
    return f'''<g fill="none" stroke="{B}" stroke-width="1" opacity="0.22">
<path d="{d1}"/><path d="{d2}"/></g>'''

# -- 1. IDENTITY: biometric scan sweep --
inner = bglayer('cs', 'M0 18 H880', 'M0 60 H880') + f'''
<path id="csb" d="M20 39 H360 M520 39 H860" stroke="{C}" stroke-width="1.5" fill="none" opacity="0.9"/>
<g fill="none" stroke="{C}" stroke-width="1.5" filter="url(#csgl)">
<circle cx="440" cy="39" r="24" opacity="0.9"/><circle cx="440" cy="39" r="17" opacity="0.5"/>
<path d="M431 32 a12 12 0 0 1 18 0 M428 39 a12 12 0 0 1 24 0" stroke="{M}" opacity="0.9"/>
<path d="M433 45 a9 9 0 0 1 14 0" stroke="{M}" opacity="0.7"/>
</g>
<g stroke="{V}" stroke-width="1.5" fill="none" opacity="0.8"><path d="M404 15 h-12 v10 M476 63 h12 v-10"/></g>
<rect x="14" y="35" width="8" height="8" fill="{P}" stroke="{C}" stroke-width="1.5"/>
<rect x="858" y="35" width="8" height="8" fill="{P}" stroke="{C}" stroke-width="1.5"/>
<text x="440" y="74" {MONO} font-size="8" letter-spacing="3" fill="{B}" text-anchor="middle" opacity="0.9">BIOMETRIC LINK VERIFIED</text>
<rect x="0" y="8" width="3" height="62" fill="{C}" opacity="0.6"><animate attributeName="x" values="20;857;20" dur="14s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;0.5;0.08;0.5;0" dur="14s" repeatCount="indefinite"/></rect>
<circle r="3" fill="{C}"><animateMotion dur="8s" repeatCount="indefinite"><mpath href="#csb"/></animateMotion></circle>'''
conn('conn-scan', 'Biometric scan divider', 'Fingerprint scan node on a data line with a sweeping beam.', inner, 'cs')

# -- 2. PROJECTS: branching trunk into three drop ports --
inner = bglayer('cb', 'M0 14 H880', 'M60 64 H820') + f'''
<path id="cbt" d="M20 26 H860" stroke="{C}" stroke-width="1.5" fill="none"/>
<path d="M20 26 H860" stroke="{C}" stroke-width="5" opacity="0.08" fill="none"/>
<g stroke="{C}" stroke-width="1.5" fill="none">
<path d="M180 26 v22 M440 26 v22 M700 26 v22"/>
</g>
<g fill="{P}" stroke="{B}" stroke-width="1.5">
<path d="M174 48 h12 l-6 9 z"/><path d="M434 48 h12 l-6 9 z"/><path d="M694 48 h12 l-6 9 z"/>
</g>
<g fill="{P}" stroke="{C}" stroke-width="1.5">
<rect x="175" y="21" width="10" height="10" transform="rotate(45 180 26)"/>
<rect x="435" y="21" width="10" height="10" transform="rotate(45 440 26)"/>
<rect x="695" y="21" width="10" height="10" transform="rotate(45 700 26)"/>
</g>
<g {MONO} font-size="7" fill="{B}" text-anchor="middle" letter-spacing="2">
<text x="180" y="70">MOD.01</text><text x="440" y="70">MOD.02</text><text x="700" y="70">MOD.03</text>
</g>
<rect x="14" y="22" width="8" height="8" fill="{P}" stroke="{C}" stroke-width="1.5"/>
<rect x="858" y="22" width="8" height="8" fill="{P}" stroke="{C}" stroke-width="1.5"/>
<circle r="3" fill="{C}"><animateMotion dur="7s" repeatCount="indefinite"><mpath href="#cbt"/></animateMotion></circle>
<g fill="{G}"><circle cx="180" cy="37" r="2"><animate attributeName="opacity" values="0;1;0" dur="3s" repeatCount="indefinite"/></circle>
<circle cx="440" cy="37" r="2"><animate attributeName="opacity" values="0;1;0" dur="3s" begin="1s" repeatCount="indefinite"/></circle>
<circle cx="700" cy="37" r="2"><animate attributeName="opacity" values="0;1;0" dur="3s" begin="2s" repeatCount="indefinite"/></circle></g>'''
conn('conn-branch', 'Branching module bus', 'Main bus branching into three module ports with signal drops.', inner, 'cb')

# -- 3. AGENTIC: neural mesh --
inner = f'''<g fill="none" stroke="{V}" stroke-width="1" opacity="0.35">
<path d="M20 39 C160 8, 280 70, 440 39 S 720 8, 860 39"/>
<path d="M20 39 C160 70, 280 8, 440 39 S 720 70, 860 39"/>
</g>
<path id="cnm" d="M20 39 C160 8, 280 70, 440 39 S 720 8, 860 39" fill="none"/>
<g fill="none" stroke="{C}" stroke-width="1.5" opacity="0.85">
<path d="M230 24 L340 54 L440 39 L540 24 L650 54"/>
</g>
<g filter="url(#cngl)">
<circle cx="230" cy="24" r="4" fill="{V}"><animate attributeName="r" values="3.4;5;3.4" dur="4s" repeatCount="indefinite"/></circle>
<circle cx="340" cy="54" r="4" fill="{B}"><animate attributeName="r" values="3.4;5;3.4" dur="4s" begin="0.8s" repeatCount="indefinite"/></circle>
<circle cx="440" cy="39" r="6" fill="{C}"><animate attributeName="r" values="5;7;5" dur="4s" begin="1.6s" repeatCount="indefinite"/></circle>
<circle cx="540" cy="24" r="4" fill="{B}"><animate attributeName="r" values="3.4;5;3.4" dur="4s" begin="2.4s" repeatCount="indefinite"/></circle>
<circle cx="650" cy="54" r="4" fill="{V}"><animate attributeName="r" values="3.4;5;3.4" dur="4s" begin="3.2s" repeatCount="indefinite"/></circle>
</g>
<text x="440" y="14" {MONO} font-size="8" letter-spacing="3" fill="{V}" text-anchor="middle">SYNAPTIC ROUTE</text>
<circle r="2.6" fill="{M}"><animateMotion dur="10s" repeatCount="indefinite"><mpath href="#cnm"/></animateMotion></circle>'''
conn('conn-neural', 'Neural mesh divider', 'Curved synaptic links with pulsing nodes and a traveling impulse.', inner, 'cn')

# -- 4. TECH: chip pin header --
pins = ''.join(f'<path d="M{80+i*36} 30 v18" />' for i in range(20))
pads = ''.join(f'<rect x="{77+i*36}" y="24" width="6" height="6"/>' for i in range(20))
inner = bglayer('cp', 'M0 12 H880', 'M0 66 H880') + f'''
<path id="cpb" d="M20 21 H860" stroke="{C}" stroke-width="1.5" fill="none"/>
<path d="M20 57 H860" stroke="{B}" stroke-width="1.5" fill="none" opacity="0.7"/>
<g stroke="{B}" stroke-width="1.5" opacity="0.75">{pins}</g>
<g fill="{P}" stroke="{C}" stroke-width="1">{pads}</g>
<rect x="404" y="28" width="72" height="22" fill="{P}" stroke="{C}" stroke-width="1.5"/>
<text x="440" y="43" {MONO} font-size="9" letter-spacing="2" fill="{C}" text-anchor="middle">CPU.BUS</text>
<circle r="3" fill="{C}"><animateMotion dur="8s" repeatCount="indefinite"><mpath href="#cpb"/></animateMotion></circle>
<circle r="2" fill="{G}"><animateMotion path="M860 57 H20" dur="12s" repeatCount="indefinite"/></circle>'''
conn('conn-pins', 'Chip pin header divider', 'PCB pin header bus with counter-flowing signals.', inner, 'cp')

# -- 5. LEARNING: data-transfer chevrons + progress --
chev = ''.join(f'<path d="M{120+i*60} 32 l14 7 -14 7" />' for i in range(11))
inner = bglayer('ct', 'M0 16 H880', 'M0 62 H880') + f'''
<path d="M20 39 H860" stroke="{B}" stroke-width="1.5" opacity="0.35" fill="none"/>
<g fill="none" stroke="{C}" stroke-width="2" stroke-linejoin="round" opacity="0.85">{chev}
<animate attributeName="opacity" values="0.4;0.95;0.4" dur="3.6s" repeatCount="indefinite"/></g>
<rect x="20" y="36" width="0" height="6" fill="{C}" opacity="0.35"><animate attributeName="width" values="0;840" dur="12s" repeatCount="indefinite"/></rect>
<text x="24" y="28" {MONO} font-size="8" letter-spacing="3" fill="{C}">TRANSFERRING KNOWLEDGE…</text>
<text x="856" y="28" {MONO} font-size="8" letter-spacing="2" fill="{G}" text-anchor="end">LINK STABLE</text>
<rect x="14" y="35" width="8" height="8" fill="{P}" stroke="{C}" stroke-width="1.5"/>
<rect x="858" y="35" width="8" height="8" fill="{P}" stroke="{C}" stroke-width="1.5"/>'''
conn('conn-transfer', 'Data transfer divider', 'Chevron data stream with an advancing transfer bar.', inner, 'ct')

# -- 6. TELEMETRY: radar node with sweep --
inner = bglayer('cr', 'M0 20 H880', 'M0 58 H880') + f'''
<path id="crb" d="M20 39 H395 M485 39 H860" stroke="{C}" stroke-width="1.5" fill="none"/>
<g fill="none" stroke="{C}" stroke-width="1.2" opacity="0.8">
<circle cx="440" cy="39" r="30"/><circle cx="440" cy="39" r="20" opacity="0.6"/><circle cx="440" cy="39" r="10" opacity="0.45"/>
<path d="M410 39 h60 M440 9 v60" opacity="0.3"/>
</g>
<path d="M440 39 L440 10 A29 29 0 0 1 462 15 Z" fill="{C}" opacity="0.3">
<animateTransform attributeName="transform" type="rotate" from="0 440 39" to="360 440 39" dur="7s" repeatCount="indefinite"/></path>
<circle cx="452" cy="28" r="2.4" fill="{M}"><animate attributeName="opacity" values="0;1;0" dur="7s" repeatCount="indefinite"/></circle>
<circle cx="428" cy="52" r="2" fill="{G}"><animate attributeName="opacity" values="0;1;0" dur="7s" begin="3s" repeatCount="indefinite"/></circle>
<text x="440" y="76" {MONO} font-size="8" letter-spacing="3" fill="{B}" text-anchor="middle">SIGNAL MONITORING ACTIVE</text>
<circle r="3" fill="{C}"><animateMotion dur="9s" repeatCount="indefinite"><mpath href="#crb"/></animateMotion></circle>'''
conn('conn-radar', 'Radar sweep divider', 'Radar node with rotating sweep and detected blips on a data line.', inner, 'cr')

# -- 7. CONNECT: waveform uplink --
inner = bglayer('cw', 'M0 14 H880', 'M0 64 H880') + f'''
<path d="M20 39 H300" stroke="{C}" stroke-width="1.5" fill="none"/>
<path d="M580 39 H860" stroke="{C}" stroke-width="1.5" fill="none"/>
<path d="M300 39 q17 -26 35 0 t35 0 t35 0 t35 0 t35 0 t35 0 t35 0 t35 0" fill="none" stroke="{C}" stroke-width="1.8" stroke-dasharray="240 320" filter="url(#cwgl)">
<animate attributeName="stroke-dashoffset" values="560;0" dur="9s" repeatCount="indefinite"/></path>
<g stroke="{V}" stroke-width="1.5" fill="none" opacity="0.9">
<path d="M440 20 v-8 m-6 4 l6 -6 6 6"/>
</g>
<text x="440" y="70" {MONO} font-size="8" letter-spacing="3" fill="{B}" text-anchor="middle">UPLINK CHANNEL OPEN</text>
<rect x="14" y="35" width="8" height="8" fill="{P}" stroke="{C}" stroke-width="1.5"/>
<rect x="858" y="35" width="8" height="8" fill="{P}" stroke="{C}" stroke-width="1.5"/>'''
conn('conn-wave', 'Uplink waveform divider', 'Transmission waveform flowing between two endpoints.', inner, 'cw')

print('--- connectors done ---')
