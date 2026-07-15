# -*- coding: utf-8 -*-
"""Network linkage pass: upgraded spine connector, dock wires, micro traces."""
import io

C, B, V, M, G = '#00E5FF', '#4D8AFF', '#7C3AED', '#FF2D95', '#22E06C'
D, P = '#0B0E1A', '#101530'


def write(name, svg):
    io.open(f'assets/{name}.svg', 'w', encoding='utf-8', newline='\n').write(svg)
    print(name, len(svg), 'B')


# ---- 1) Upgraded main data spine connector (replaces old divider-connector) ----
# Full-width junction: central bus, angled branch traces, ports, corner brackets,
# one slow packet traveling the bus, one pulsing junction node.
spine = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 56" role="img" aria-labelledby="t d" preserveAspectRatio="xMidYMid meet">
<title id="t">Data spine junction</title><desc id="d">Circuit bus connecting sections with a traveling data packet.</desc>
<g stroke="{V}" stroke-width="1" opacity="0.5">
<path d="M60 10 L60 22 L110 22" fill="none"/>
<path d="M820 46 L820 34 L770 34" fill="none"/>
</g>
<path id="bus" d="M20 28 H360 L380 14 H500 L520 28 H860" fill="none" stroke="{C}" stroke-width="1.5" opacity="0.85"/>
<path d="M20 28 H360 L380 14 H500 L520 28 H860" fill="none" stroke="{C}" stroke-width="4" opacity="0.08"/>
<g fill="{P}" stroke="{C}" stroke-width="1.5">
<rect x="14" y="24" width="8" height="8"/>
<rect x="858" y="24" width="8" height="8"/>
</g>
<rect x="436" y="9" width="10" height="10" fill="{P}" stroke="{B}" stroke-width="1.5" transform="rotate(45 441 14)"/>
<circle cx="441" cy="14" r="2" fill="{B}"><animate attributeName="opacity" values="1;0.25;1" dur="3s" repeatCount="indefinite"/></circle>
<g stroke="{B}" stroke-width="1.5" fill="none" opacity="0.8">
<path d="M110 18 v8 M114 18 v8"/>
<path d="M770 30 v8 M766 30 v8"/>
</g>
<g fill="none" stroke="{V}" stroke-width="1.5" opacity="0.7">
<path d="M6 8 h10 M6 8 v10"/>
<path d="M874 48 h-10 M874 48 v-10"/>
</g>
<circle r="3" fill="{C}"><animateMotion dur="9s" repeatCount="indefinite"><mpath href="#bus"/></animateMotion></circle>
<circle r="2" fill="{M}" opacity="0.9"><animateMotion dur="13s" repeatCount="indefinite" keyPoints="1;0" keyTimes="0;1"><mpath href="#bus"/></animateMotion></circle>
</svg>'''
write('connector', spine)

# ---- 2) Dock wire: short vertical drop that plugs illustrations into content ----
wire = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 46" role="img" aria-labelledby="t d">
<title id="t">Dock wire</title><desc id="d">Vertical connector wire with a descending data pulse.</desc>
<rect x="8" y="2" width="8" height="5" fill="{P}" stroke="{C}" stroke-width="1.2"/>
<line x1="12" y1="7" x2="12" y2="39" stroke="{C}" stroke-width="1.5" opacity="0.85"/>
<line x1="12" y1="7" x2="12" y2="39" stroke="{C}" stroke-width="4" opacity="0.08"/>
<path d="M8 39 h8 l-4 5 z" fill="{P}" stroke="{B}" stroke-width="1.2"/>
<circle cx="12" r="2" fill="{C}"><animate attributeName="cy" values="9;37" dur="3.5s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.15;0.85;1" dur="3.5s" repeatCount="indefinite"/></circle>
</svg>'''
write('wire-drop', wire)

# ---- 3) Micro trace: tiny horizontal circuit run linking card icon -> badge ----
trace = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44 12" role="img" aria-labelledby="t d">
<title id="t">Circuit trace</title><desc id="d">Short horizontal circuit trace with flowing signal.</desc>
<circle cx="4" cy="6" r="2.5" fill="none" stroke="{V}" stroke-width="1.2"/>
<line x1="7" y1="6" x2="37" y2="6" stroke="{B}" stroke-width="1.5" stroke-dasharray="4 4" opacity="0.9"><animate attributeName="stroke-dashoffset" values="0;-16" dur="2.4s" repeatCount="indefinite"/></line>
<path d="M37 3 l5 3 -5 3 z" fill="{C}"/>
</svg>'''
write('trace-h', trace)
