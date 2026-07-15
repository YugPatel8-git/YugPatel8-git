# -*- coding: utf-8 -*-
"""Depth pass part 2: HUD panels docking the illustrations + project cards."""
from gen_depth import svg, panel_shell, cut_rect, C, B, V, M, G, D, P, P2, MONO

# telemetry micro-rows helper
def telem(x, y, rows, w=118):
    out = f'<g transform="translate({x},{y})" {MONO} font-size="8" letter-spacing="1">'
    for i, (k, v_, col) in enumerate(rows):
        yy = i * 16
        out += (f'<text x="0" y="{yy+8}" fill="{B}" opacity="0.9">{k}</text>'
                f'<text x="{w}" y="{yy+8}" fill="{col}" text-anchor="end">{v_}</text>'
                f'<path d="M0 {yy+12} H{w}" stroke="{B}" stroke-width="0.5" opacity="0.3"/>')
    return out + '</g>'


# ============ PANEL 1: IDENTITY — biometric profile scan (460x220) ============
W, H = 460, 220
inner = panel_shell('pi', W, H, 'IDENTITY.SCAN', 'ID.CORE//YP-06') + f'''
<circle cx="120" cy="118" r="62" fill="none" stroke="{B}" stroke-width="1" opacity="0.3" stroke-dasharray="3 5"/>
<g fill="none" stroke="{C}" stroke-width="1.5" filter="url(#pigl)">
<circle cx="120" cy="118" r="50"/>
<circle cx="120" cy="118" r="42" opacity="0.4" stroke-dasharray="10 6">
<animateTransform attributeName="transform" type="rotate" from="0 120 118" to="360 120 118" dur="24s" repeatCount="indefinite"/></circle>
</g>
<g fill="none" stroke="{C}" stroke-width="1.6">
<circle cx="120" cy="102" r="13"/>
<path d="M96 142 a24 18 0 0 1 48 0" />
</g>
<rect x="66" y="60" width="108" height="4" fill="{M}" opacity="0.55">
<animate attributeName="y" values="64;168;64" dur="8s" repeatCount="indefinite"/></rect>
<g stroke="{V}" stroke-width="1.5" fill="none" opacity="0.9">
<path d="M56 66 v-10 h10 M184 66 v-10 h-10 M56 170 v10 h10 M184 170 v10 h-10"/></g>
<path d="M170 118 H236" stroke="{C}" stroke-width="1.5"/>
<path d="M236 118 h8 l6 -6 h60" stroke="{C}" stroke-width="1.5" fill="none"/>
<circle r="2.4" fill="{C}"><animateMotion path="M170 118 h66 l14 -6 h60" dur="4.5s" repeatCount="indefinite"/></circle>
{telem(310, 52, [('HANDLE','YUG PATEL',C),('ROLE','DEVELOPER',C),('BASE','ASU // CS',B),('FOCUS','AI + WEB',V),('STATE','BUILDING',G)], 128)}
<text x="238" y="150" {MONO} font-size="8" fill="{B}" letter-spacing="2" opacity="0.9">SCAN INTEGRITY</text>
<rect x="238" y="156" width="130" height="5" fill="{P}" stroke="{B}" stroke-width="0.6"/>
<rect x="238" y="156" width="0" height="5" fill="{C}"><animate attributeName="width" values="0;130" dur="6s" fill="freeze"/></rect>
<text x="238" y="178" {MONO} font-size="8" fill="{G}" letter-spacing="2">MATCH CONFIRMED ▸ ACCESS GRANTED</text>'''
svg('panel-identity', W, H, 'Identity scan panel',
    'Biometric profile scan interface with rotating rings, scan beam and identity telemetry.', inner, 'pi')

# ============ PANEL 2: BUILDS — active process dashboard (460x220) ============
inner = panel_shell('pb', W, H, 'PROC.MONITOR', 'SYS.02//EXEC') + f'''
<rect x="22" y="40" width="230" height="150" fill="{D}" stroke="{B}" stroke-width="1" opacity="0.9"/>
<rect x="22" y="40" width="230" height="14" fill="{P2}" stroke="{B}" stroke-width="1"/>
<circle cx="31" cy="47" r="2.6" fill="{M}"/><circle cx="40" cy="47" r="2.6" fill="#FFB020"/><circle cx="49" cy="47" r="2.6" fill="{G}"/>
<g {MONO} font-size="9" fill="{C}">
<text x="30" y="72">&gt; run stat-updates --live</text>
<text x="30" y="90" fill="{G}">  ▸ match feed streaming…</text>
<text x="30" y="108">&gt; run local-ai --experiment</text>
<text x="30" y="126" fill="{V}">  ▸ model session active</text>
<text x="30" y="144">&gt; run automation --daemon</text>
<text x="30" y="162" fill="{B}">  ▸ scripts scheduled ✓</text>
</g>
<rect x="30" y="170" width="8" height="10" fill="{C}"><animate attributeName="opacity" values="1;0;1" dur="1.6s" repeatCount="indefinite"/></rect>
<g transform="translate(280,48)">
<text x="0" y="0" {MONO} font-size="8" letter-spacing="2" fill="{B}">PROCESS LOAD</text>
<g>
<rect x="0" y="10" width="150" height="7" fill="{P}" stroke="{B}" stroke-width="0.6"/><rect x="0" y="10" height="7" fill="{C}" width="112"><animate attributeName="width" values="96;126;112" dur="7s" repeatCount="indefinite"/></rect>
<rect x="0" y="30" width="150" height="7" fill="{P}" stroke="{B}" stroke-width="0.6"/><rect x="0" y="30" height="7" fill="{V}" width="80"><animate attributeName="width" values="64;98;80" dur="9s" repeatCount="indefinite"/></rect>
<rect x="0" y="50" width="150" height="7" fill="{P}" stroke="{B}" stroke-width="0.6"/><rect x="0" y="50" height="7" fill="{G}" width="120"><animate attributeName="width" values="104;136;120" dur="8s" repeatCount="indefinite"/></rect>
</g>
<g {MONO} font-size="7" fill="{B}" opacity="0.9">
<text x="0" y="26">STAT UPDATES</text><text x="0" y="46">LOCAL AI</text><text x="0" y="66">AUTOMATION</text>
</g>
<path d="M0 84 h150" stroke="{B}" stroke-width="0.5" opacity="0.4"/>
<path d="M0 118 L18 108 36 120 54 100 72 112 90 96 108 116 126 104 150 110" fill="none" stroke="{C}" stroke-width="1.5" filter="url(#pbgl)"/>
<circle cx="150" cy="110" r="2.6" fill="{M}"><animate attributeName="opacity" values="1;0.3;1" dur="2.4s" repeatCount="indefinite"/></circle>
<text x="0" y="140" {MONO} font-size="8" letter-spacing="2" fill="{B}">THROUGHPUT ▸ NOMINAL</text>
</g>'''
svg('panel-builds', W, H, 'Active process dashboard',
    'Terminal window with running build processes, load bars and throughput graph.', inner, 'pb')

# ============ PANEL 3: AI CORE — wide neural interface (880x200) ============
W3, H3 = 880, 200
mesh_l = ''.join(f'<path d="M120 100 C{200} {40+i*30}, {280} {40+i*30}, 360 {55+i*30}"/>' for i in range(4))
mesh_r = ''.join(f'<path d="M760 100 C{680} {40+i*30}, {600} {40+i*30}, 520 {55+i*30}"/>' for i in range(4))
nodes_l = ''.join(f'<circle cx="360" cy="{55+i*30}" r="4" fill="{B}"><animate attributeName="opacity" values="0.5;1;0.5" dur="4s" begin="{i*0.7}s" repeatCount="indefinite"/></circle>' for i in range(4))
nodes_r = ''.join(f'<circle cx="520" cy="{55+i*30}" r="4" fill="{V}"><animate attributeName="opacity" values="0.5;1;0.5" dur="4s" begin="{i*0.7+0.4}s" repeatCount="indefinite"/></circle>' for i in range(4))
inner = panel_shell('pa', W3, H3, 'AGENT.CORE', 'NEURAL//v4') + f'''
<g fill="none" stroke="{B}" stroke-width="1" opacity="0.28">{mesh_l}{mesh_r}
<path d="M360 55 H520 M360 85 H520 M360 115 H520 M360 145 H520"/></g>
{nodes_l}{nodes_r}
<g fill="none" stroke="{C}" stroke-width="1.6" filter="url(#pagl)">
<circle cx="440" cy="100" r="40"/>
<circle cx="440" cy="100" r="30" opacity="0.5" stroke-dasharray="8 6">
<animateTransform attributeName="transform" type="rotate" from="360 440 100" to="0 440 100" dur="18s" repeatCount="indefinite"/></circle>
<circle cx="440" cy="100" r="52" opacity="0.3" stroke-dasharray="2 8">
<animateTransform attributeName="transform" type="rotate" from="0 440 100" to="360 440 100" dur="30s" repeatCount="indefinite"/></circle>
</g>
<g fill="none" stroke="{M}" stroke-width="1.5" opacity="0.9">
<path d="M425 92 h10 v16 h-10 M455 92 h-8 v16 h8 M440 84 v-6 M440 116 v6 M424 100 h-8 M456 100 h8"/>
</g>
<circle cx="440" cy="100" r="6" fill="{C}"><animate attributeName="r" values="5;8;5" dur="3.5s" repeatCount="indefinite"/></circle>
<circle cx="120" cy="100" r="10" fill="{P}" stroke="{C}" stroke-width="1.5"/>
<circle cx="760" cy="100" r="10" fill="{P}" stroke="{C}" stroke-width="1.5"/>
<g {MONO} font-size="8" letter-spacing="2" fill="{B}">
<text x="120" y="128" text-anchor="middle">INPUT.STREAM</text>
<text x="760" y="128" text-anchor="middle">ACTION.OUT</text>
<text x="440" y="176" text-anchor="middle" fill="{V}" letter-spacing="4">AGENTIC TOOLING ▸ PLANNING ▸ EXECUTION</text>
</g>
<circle r="3" fill="{C}"><animateMotion path="M130 100 C240 30, 300 30, 400 92" dur="5s" repeatCount="indefinite"/></circle>
<circle r="3" fill="{M}"><animateMotion path="M480 108 C580 170, 660 170, 750 100" dur="5s" begin="2.5s" repeatCount="indefinite"/></circle>'''
svg('panel-brain', W3, H3, 'AI core neural interface',
    'Wide neural network interface: input stream flowing through a rotating AI core to action output.', inner, 'pa')

# ============ PANEL 4: SECURITY RACK — 4 bays (880x150) ============
W4, H4 = 880, 150
def bay(x, label, art):
    return f'''<g transform="translate({x},34)">
<path d="{cut_rect(0,0,180,86,10)}" fill="{D}" stroke="{B}" stroke-width="1" opacity="0.95"/>
{art}
<text x="90" y="80" {MONO} font-size="7" letter-spacing="2" fill="{B}" text-anchor="middle">{label}</text>
</g>'''
shield = f'''<g transform="translate(90,36)"><path d="M0 -22 L18 -14 V4 C18 16, 0 24, 0 24 C0 24, -18 16, -18 4 V-14 Z" fill="none" stroke="{C}" stroke-width="1.6" filter="url(#psgl)"/><path d="M-7 0 l5 6 10 -12" stroke="{G}" stroke-width="2" fill="none"/><animateTransform attributeName="transform" type="translate" values="90 36;90 33;90 36" dur="5s" repeatCount="indefinite"/></g>'''
padlock = f'''<g transform="translate(90,38)"><rect x="-14" y="-6" width="28" height="24" fill="none" stroke="{C}" stroke-width="1.6"/><path d="M-8 -6 v-6 a8 8 0 0 1 16 0 v6" fill="none" stroke="{V}" stroke-width="1.6"/><circle cx="0" cy="5" r="3" fill="{M}"><animate attributeName="opacity" values="1;0.35;1" dur="3s" repeatCount="indefinite"/></circle></g>'''
virus = f'''<g transform="translate(90,36)"><circle r="11" fill="none" stroke="{M}" stroke-width="1.6"/><g stroke="{M}" stroke-width="1.5"><path d="M0 -11 v-7 M0 11 v7 M-11 0 h-7 M11 0 h7 M-8 -8 l-5 -5 M8 8 l5 5 M8 -8 l5 -5 M-8 8 l-5 5"/></g><circle r="4" fill="{M}" opacity="0.6"><animate attributeName="r" values="3;5;3" dur="4s" repeatCount="indefinite"/></circle><animateTransform attributeName="transform" type="rotate" from="0 90 36" to="360 90 36" dur="40s" repeatCount="indefinite"/></g>'''
warn = f'''<g transform="translate(90,36)"><path d="M0 -18 L20 16 H-20 Z" fill="none" stroke="#FFB020" stroke-width="1.8" stroke-linejoin="round"/><path d="M0 -6 v10" stroke="#FFB020" stroke-width="2.4"/><circle cx="0" cy="10" r="1.8" fill="#FFB020"/><animate attributeName="opacity" values="1;0.45;1" dur="2.8s" repeatCount="indefinite"/></g>'''
inner = panel_shell('ps', W4, H4, 'SEC.RACK', 'DEFENSE//GRID') + f'''
<path d="M30 122 H850" stroke="{B}" stroke-width="1" opacity="0.35"/>
{bay(52,'SHIELD.ACTIVE',shield)}{bay(262,'ENCRYPTION',padlock)}{bay(472,'THREAT.WATCH',virus)}{bay(682,'ALERT.SYS',warn)}
<g stroke="{C}" stroke-width="1.2" opacity="0.7">
<path d="M232 77 h30 M442 77 h30 M652 77 h30"/></g>
<circle r="2" fill="{C}"><animateMotion path="M232 77 h30" dur="2.2s" repeatCount="indefinite"/></circle>
<circle r="2" fill="{C}"><animateMotion path="M442 77 h30" dur="2.2s" begin="0.7s" repeatCount="indefinite"/></circle>
<circle r="2" fill="{C}"><animateMotion path="M652 77 h30" dur="2.2s" begin="1.4s" repeatCount="indefinite"/></circle>'''
svg('panel-security', W4, H4, 'Security rack panel',
    'Hardware rack with four linked security bays: shield, encryption, threat watch and alert system.', inner, 'ps')

# ============ PANEL 5: TECH CORE — chip grid + rotating core (460x220) ============
chips = ''
for r in range(3):
    for c_ in range(3):
        x, y = 268 + c_*58, 52 + r*52
        chips += f'''<g transform="translate({x},{y})"><rect width="40" height="34" fill="{D}" stroke="{B}" stroke-width="1"/><rect x="8" y="7" width="24" height="20" fill="none" stroke="{C}" stroke-width="1" opacity="0.75"/><g stroke="{B}" stroke-width="1" opacity="0.7"><path d="M6 -4 v4 M20 -4 v4 M34 -4 v4 M6 34 v4 M20 34 v4 M34 34 v4"/></g></g>'''
inner = panel_shell('pc', W, H, 'TECH.CORE', 'ARSENAL//HW') + f'''
<g fill="none" stroke="{C}" stroke-width="1.6" filter="url(#pcgl)">
<circle cx="130" cy="118" r="52"/>
<circle cx="130" cy="118" r="40" stroke-dasharray="14 8" opacity="0.6">
<animateTransform attributeName="transform" type="rotate" from="0 130 118" to="360 130 118" dur="16s" repeatCount="indefinite"/></circle>
<circle cx="130" cy="118" r="27" stroke="{V}" stroke-dasharray="6 6" opacity="0.7">
<animateTransform attributeName="transform" type="rotate" from="360 130 118" to="0 130 118" dur="12s" repeatCount="indefinite"/></circle>
</g>
<rect x="118" y="106" width="24" height="24" fill="{P}" stroke="{M}" stroke-width="1.5" transform="rotate(45 130 118)"/>
<circle cx="130" cy="118" r="4" fill="{C}"><animate attributeName="r" values="3;5.4;3" dur="3s" repeatCount="indefinite"/></circle>
<path d="M182 118 h40 v-38 h36" fill="none" stroke="{C}" stroke-width="1.5"/>
<path d="M182 130 h30 v52 h46" fill="none" stroke="{B}" stroke-width="1.5" opacity="0.7"/>
<circle r="2.4" fill="{C}"><animateMotion path="M182 118 h40 v-38 h36" dur="4s" repeatCount="indefinite"/></circle>
<circle r="2.4" fill="{G}"><animateMotion path="M182 130 h30 v52 h46" dur="5s" repeatCount="indefinite"/></circle>
{chips}
<text x="130" y="196" {MONO} font-size="8" letter-spacing="3" fill="{B}" text-anchor="middle">POWER CORE ▸ STABLE</text>'''
svg('panel-core', W, H, 'Tech arsenal core panel',
    'Rotating power core wired into a grid of hardware chips.', inner, 'pc')

# ============ PROJECT CARDS (3 × 290x190) ============
def card(name, pid, title, desc1, desc2, status, scol, art):
    Wc, Hc = 290, 190
    inner = f'''<path d="{cut_rect(1.5,1.5,Wc-3,Hc-3,12)}" fill="url(#{pid}bg)" stroke="{C}" stroke-width="1.5"/>
<path d="{cut_rect(1.5,1.5,Wc-3,Hc-3,12)}" fill="url(#{pid}gr)"/>
<path d="{cut_rect(1.5,1.5,Wc-3,Hc-3,12)}" fill="url(#{pid}sc)"/>
<path d="M14 1.5 H{Wc-14}" stroke="{scol}" stroke-width="3" opacity="0.5"/>
{art}
<text x="20" y="118" {MONO} font-size="13" letter-spacing="2" fill="{C}" font-weight="bold">{title}</text>
<path d="M20 126 H{Wc-20}" stroke="{B}" stroke-width="0.6" opacity="0.5"/>
<g {MONO} font-size="9" fill="#B8C4E8">
<text x="20" y="142">{desc1}</text><text x="20" y="156">{desc2}</text></g>
<rect x="20" y="166" width="7" height="7" fill="{scol}"><animate attributeName="opacity" values="1;0.25;1" dur="2.8s" repeatCount="indefinite"/></rect>
<text x="32" y="173" {MONO} font-size="8" letter-spacing="2" fill="{scol}">{status}</text>
<g stroke="{V}" stroke-width="1.5" fill="none" opacity="0.9"><path d="M8 28 v-14 M8 14 h14 M{Wc-8} {Hc-28} v14 M{Wc-8} {Hc-14} h-14"/></g>
<rect x="{Wc/2-5}" y="{Hc-8}" width="10" height="6" fill="{P}" stroke="{C}" stroke-width="1.2"/>
<rect x="{Wc/2-5}" y="2" width="10" height="6" fill="{P}" stroke="{C}" stroke-width="1.2"/>'''
    svg(name, Wc, Hc, f'{title} project module', f'Dashboard card for {title}: {desc1} {desc2}', inner, pid)

art_stat = f'''<g transform="translate(20,26)">
<rect width="250" height="70" fill="{D}" stroke="{B}" stroke-width="0.8" opacity="0.9"/>
<g fill="{C}" opacity="0.9">
<rect x="14" y="40" width="12" height="22"><animate attributeName="height" values="22;36;22" dur="4s" repeatCount="indefinite"/><animate attributeName="y" values="40;26;40" dur="4s" repeatCount="indefinite"/></rect>
<rect x="34" y="30" width="12" height="32" fill="{B}"><animate attributeName="height" values="32;18;32" dur="5s" repeatCount="indefinite"/><animate attributeName="y" values="30;44;30" dur="5s" repeatCount="indefinite"/></rect>
<rect x="54" y="22" width="12" height="40" fill="{V}"/>
</g>
<path d="M84 52 L110 36 136 46 162 28 188 40 214 24 238 34" fill="none" stroke="{G}" stroke-width="1.5"/>
<circle cx="238" cy="34" r="2.6" fill="{M}"><animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite"/></circle>
<text x="14" y="16" {MONO} font-size="8" letter-spacing="2" fill="{B}">MATCH FEED ▸ LIVE</text>
</g>'''
card('card-stat', 'k1', '⚽ STAT UPDATES', 'Live match dashboard —', 'real-time scores &amp; stats.', 'STATUS ▸ LIVE', G, art_stat)

art_ai = f'''<g transform="translate(20,26)">
<rect width="250" height="70" fill="{D}" stroke="{B}" stroke-width="0.8" opacity="0.9"/>
<g fill="none" stroke="{B}" stroke-width="1" opacity="0.5">
<path d="M40 35 L95 18 M40 35 L95 35 M40 35 L95 52 M95 18 L160 27 M95 35 L160 27 M95 52 L160 45 M95 35 L160 45 M160 27 L215 35 M160 45 L215 35"/></g>
<g><circle cx="40" cy="35" r="5" fill="{V}"/><circle cx="95" cy="18" r="4" fill="{B}"/><circle cx="95" cy="35" r="4" fill="{B}"/><circle cx="95" cy="52" r="4" fill="{B}"/><circle cx="160" cy="27" r="4" fill="{C}"/><circle cx="160" cy="45" r="4" fill="{C}"/><circle cx="215" cy="35" r="5" fill="{M}"><animate attributeName="r" values="4;6;4" dur="3s" repeatCount="indefinite"/></circle></g>
<circle r="2.2" fill="{C}"><animateMotion path="M40 35 L95 35 L160 27 L215 35" dur="3.5s" repeatCount="indefinite"/></circle>
<text x="14" y="16" {MONO} font-size="8" letter-spacing="2" fill="{V}">INFERENCE GRAPH</text>
</g>'''
card('card-localai', 'k2', '🤖 LOCAL AI', 'Assistant experiments —', 'local model tooling.', 'STATUS ▸ EXPERIMENTAL', V, art_ai)

art_auto = f'''<g transform="translate(20,26)">
<rect width="250" height="70" fill="{D}" stroke="{B}" stroke-width="0.8" opacity="0.9"/>
<g transform="translate(50,38)" fill="none" stroke="{C}" stroke-width="1.6">
<circle r="13"/><g stroke-width="2"><path d="M0 -13 v-5 M0 13 v5 M-13 0 h-5 M13 0 h5 M-9 -9 l-4 -4 M9 9 l4 4 M9 -9 l4 -4 M-9 9 l-4 4"/></g>
<animateTransform attributeName="transform" type="rotate" from="0 50 38" to="360 50 38" dur="14s" repeatCount="indefinite"/></g>
<g transform="translate(105,38)" fill="none" stroke="{B}" stroke-width="1.4">
<circle r="9"/><g stroke-width="1.6"><path d="M0 -9 v-4 M0 9 v4 M-9 0 h-4 M9 0 h4"/></g>
<animateTransform attributeName="transform" type="rotate" from="360 105 38" to="0 105 38" dur="10s" repeatCount="indefinite"/></g>
<g {MONO} font-size="8" fill="{G}">
<text x="140" y="26">▸ job.scheduler OK</text><text x="140" y="42">▸ dash.refresh OK</text><text x="140" y="58">▸ script.daemon OK</text></g>
<text x="14" y="16" {MONO} font-size="8" letter-spacing="2" fill="{B}">TASK ENGINE</text>
</g>'''
card('card-automation', 'k3', '⚙ AUTOMATION', 'Dashboards &amp; scripts —', 'self-running workflows.', 'STATUS ▸ ACTIVE', C, art_auto)

print('--- panels + cards done ---')
