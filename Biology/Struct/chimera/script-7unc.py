from chimerax.core.commands import run
from datetime import datetime
import os

script_path = os.path.dirname(os.path.abspath(__file__))
baseName = 'rewrap'

# Setting defaults
run (session, 'close session')
run (session, 'window 1000 1000')
run (session, f'cd {script_path}')
run (session, f'open {script_path}/models/7unc.cif')
run (session, 'hide atoms')
run (session, 'show cartoons')
run (session, 'cartoon style protein modeHelix default arrows false xsection oval width 1 thickness 1')
run (session, 'cartoon style strand modeHelix default arrows true xsection rectangle width 2 thickness 0.5')
run (session, 'cartoon style  nucleic xsect oval width 4 thick 4')
run (session, 'cartoon style  protein modeh tube rad 2 sides 24')
run (session, 'lighting  intensity 0.1 ambientIntensity 1.6 depthCue true multiShadow 64 msMapSize 128')
run (session, 'dssp')
run (session, f'name {baseName} #1')
run (session, 'graphics sil true width 2')

# Finding correct orientation
run (session, 'turn y -90')
run (session, 'turn x -90')
run (session, 'turn z 5')
run (session, 'view clip false')

# Assign name to chains
run (session, 'name CTR9 #1/Q')
run (session, 'name WDR61 #1/W')
run (session, 'name TFIIS #1/O')
run (session, 'name PAF1 #1/V')
run (session, 'name RTF1 #1/R')
run (session, 'name SPT5 #1/Z')
run (session, 'name SPT6 #1/M')
run (session, 'name LEO1 #1/U')
run (session, 'name RNA #1/P')
run (session, 'name Template #1/T')
run (session, 'name Non-template #1/N')
run (session, 'name H2A #1/c,g')
run (session, 'name H2B #1/d,h')
run (session, 'name H3 #1/a,e')
run (session, 'name H4 #1/b,f')

# Colouring chains
run (session, 'colour #1 #999999')
colours = {
    'CTR9': '#FF9500',
    'WDR61': '#139F9F',
    'TFIIS': '#FEDD14',
    'PAF1': '#9ACB56',
    'RTF1': '#E90E8B',
    'SPT5': '#036A39',
    'SPT6': '#303997',
    'LEO1': '#F34BE9',
    'RNA': '#BD202E',
    'H2A': '#F0E926',
    'H2B': '#DB1F26',
    'H3': '#4B86C6',
    'H4': '#75C043',
}
for chain, colour in colours.items():
    run (session, f'colour {chain} {colour}')
run (session, 'rainbow Template target c palette ^PuBu-5')
run (session, 'rainbow Non-template target c palette PuBu-5')
run (session, 'transparency protein 50 target c')

# Saving figures
now = datetime.now()
dt_string = now.strftime("%Y-%m-%d_%H-%M")
# run	(session, 'save {n}_{d}.png width 2000 height 2000 supersample 4 transparentBackground false'.format(n = baseName, d = dt_string))
