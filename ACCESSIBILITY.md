# Accessibility: Colorblind-Friendly Visualizations

## Overview

This repository uses colorblind-friendly palettes to ensure that all visualizations are accessible to people with color vision deficiencies, particularly red/green color blindness (deuteranopia and protanopia), which affects approximately 8% of men and 0.5% of women of Northern European descent.

## Why Colorblind-Friendly Palettes Matter

Traditional red-green color schemes are problematic because:
- Red and green appear similar or indistinguishable to people with deuteranopia or protanopia
- This makes it difficult or impossible to interpret visualizations that rely on these color differences
- Approximately 1 in 12 men (8%) and 1 in 200 women (0.5%) have some form of color blindness

## Palettes Used

### Okabe-Ito Palette (Primary)

The Okabe-Ito palette is specifically designed to be colorblind-safe and distinguishable by people with all forms of color vision deficiency.

**Colors:**
- `#E69F00` - Orange
- `#56B4E9` - Sky Blue
- `#009E73` - Bluish Green
- `#F0E442` - Yellow
- `#0072B2` - Blue
- `#D55E00` - Vermillion
- `#CC79A7` - Reddish Purple
- `#000000` - Black

**Source:** Okabe, M. and Ito, K. (2008) Color Universal Design (CUD): How to make figures and presentations that are friendly to color blind people. https://jfly.uni-koeln.de/color/

### Paul Tol's Palettes (Secondary)

We also use Paul Tol's muted and vibrant palettes for additional variety, all of which are colorblind-safe.

### Sequential Colormaps

For continuous data, we use:
- **Viridis** (default): Blue to yellow, perceptually uniform
- **Plasma**: Purple to yellow
- **Cividis**: Blue to yellow, optimized specifically for colorblind viewers

## Implementation

### Climate Regimes (4 Categories)

**Old palette (problematic):**
- Red (#d7191c) → Orange (#fdae61) → Light Green (#a6d96a) → Dark Green (#1a9641)
- ❌ Red and green are indistinguishable to colorblind viewers

**New palette (accessible):**
- Orange (#E69F00) → Sky Blue (#56B4E9) → Bluish Green (#009E73) → Blue (#0072B2)
- ✅ All colors are distinguishable with any form of color blindness

### Continents (6 Categories)

**Old palette (problematic):**
- Includes red (#d62728) and green (#2ca02c) which are confusing for colorblind viewers

**New palette (accessible):**
- Blue (#0072B2) - Africa
- Orange (#E69F00) - Asia  
- Bluish Green (#009E73) - Europe
- Vermillion (#D55E00) - North America
- Reddish Purple (#CC79A7) - South America
- Yellow (#F0E442) - Oceania

## Using the Palettes

### Python Scripts

```python
from viz.palettes import get_categorical_palette, set_global_palettes

# Get palette colors
colors = get_categorical_palette('okabe_ito', n=4)

# Apply globally to matplotlib/seaborn
set_global_palettes('okabe_ito')

# Use with matplotlib
import matplotlib.pyplot as plt
from viz.palettes import apply_matplotlib_palette

apply_matplotlib_palette(palette_name='okabe_ito')
plt.plot(x, y)

# Use with seaborn
import seaborn as sns
from viz.palettes import set_seaborn_palette

set_seaborn_palette('paul_tol_muted')
sns.scatterplot(data=df, x='x', y='y', hue='category')

# Use with plotly
import plotly.express as px
from viz.palettes import set_plotly_palette

set_plotly_palette('okabe_ito')
fig = px.scatter(df, x='x', y='y', color='category')

# Use with altair
import altair as alt
from viz.palettes import get_altair_scale

chart = alt.Chart(df).mark_point().encode(
    x='x:Q',
    y='y:Q',
    color=alt.Color('category:N', scale=get_altair_scale('okabe_ito'))
)
```

### Web/CSS

Include the palette CSS file:

```html
<link rel="stylesheet" href="assets/palette.css">
```

Use CSS variables:

```css
.my-element {
  background-color: var(--color-okabe-1);
  border-color: var(--regime-1);
}
```

### Vega-Lite/Altair

```javascript
{
  "color": {
    "scale": {
      "range": ["#E69F00", "#56B4E9", "#009E73", "#F0E442"]
    }
  }
}
```

## Testing for Colorblindness

We recommend testing visualizations with colorblindness simulation tools:

### Color Oracle (Recommended)
- **Website:** https://colororacle.org/
- **Platforms:** Windows, Mac, Linux
- **Features:** Real-time screen simulation of deuteranopia, protanopia, and tritanopia
- **Usage:** 
  1. Download and install Color Oracle
  2. Open your visualization
  3. Press Ctrl+Cmd+O (Mac) or Ctrl+Windows+O (Windows) to cycle through simulations
  4. Verify all colors are distinguishable

### Coblis (Online)
- **Website:** https://www.color-blindness.com/coblis-color-blindness-simulator/
- **Platforms:** Web browser
- **Features:** Upload images to see how they appear with different types of color blindness
- **Usage:**
  1. Take a screenshot of your visualization
  2. Upload to Coblis
  3. Select different color blindness types to test

### Other Tools
- **Chrome DevTools:** Built-in vision deficiency emulation (F12 → Rendering → Emulate vision deficiencies)
- **Pilestone Color Blind Simulator:** Mobile app (iOS/Android)

## Contrast Ratio Guidelines

For text and UI elements, we follow WCAG 2.1 guidelines:

- **Level AA (minimum):** 4.5:1 contrast ratio for normal text, 3:1 for large text
- **Level AAA (enhanced):** 7:1 contrast ratio for normal text, 4.5:1 for large text

Check contrast ratios using:
- **WebAIM Contrast Checker:** https://webaim.org/resources/contrastchecker/
- **Chrome DevTools:** Built-in contrast ratio checker

## Additional Best Practices

1. **Don't rely on color alone:** Use patterns, labels, or shapes in addition to color
2. **Use sufficient contrast:** Ensure colors are distinguishable in grayscale
3. **Test with simulations:** Always verify with colorblindness simulation tools
4. **Provide legends:** Clear labels help users understand the meaning of colors
5. **Use texture/patterns:** When possible, add patterns to fill areas (e.g., hatching in bar charts)

## Resources

- **Color Universal Design (CUD):** https://jfly.uni-koeln.de/color/
- **Paul Tol's Notes:** https://personal.sron.nl/~pault/
- **ColorBrewer:** https://colorbrewer2.org/ (select "colorblind safe")
- **WCAG Guidelines:** https://www.w3.org/WAI/WCAG21/quickref/
- **Datawrapper Guide:** https://blog.datawrapper.de/colorblind-check/

## Verification Checklist

Before finalizing visualizations:

- [ ] Color palette is from a colorblind-safe source (Okabe-Ito, Paul Tol, ColorBrewer)
- [ ] Tested with Color Oracle or similar tool
- [ ] Colors are distinguishable in grayscale
- [ ] No red-green combinations are used for critical distinctions
- [ ] Text has sufficient contrast (4.5:1 minimum)
- [ ] Legends and labels are provided
- [ ] Alternative visual cues (patterns, shapes) are used where appropriate

## Contact

For questions or suggestions about accessibility improvements, please open an issue or contact the maintainers.

---

**Last Updated:** January 18, 2026
