# Visual Data Science 2026 - Climate Agriculture Dashboard

An interactive dashboard visualizing global agriculture data and climate patterns across different crops, with a focus on accessibility and colorblind-friendly design.

## Overview

This project presents an interactive Vega-Lite visualization dashboard that explores the relationships between:
- Agricultural yield and climate change
- Production trends over time
- Climate regime classifications
- Country-level trajectories

## Features

- **Interactive Crop Selection:** Switch between MAIZE, RICE, SOYBEAN, and WHEAT
- **Brush & Filter:** Select regions of interest to filter other views
- **Climate Regime Visualization:** Categorizes countries into 4 regimes based on yield and climate factors
- **Continent-based Analysis:** Track agricultural trajectories by continent
- **Colorblind-Friendly Palettes:** All visualizations use accessible color schemes

## Accessibility

This project prioritizes accessibility for people with color vision deficiencies. All color palettes are carefully selected to be distinguishable for people with red/green color blindness (deuteranopia and protanopia).

**Key accessibility features:**
- Okabe-Ito and Paul Tol colorblind-safe palettes
- Centralized palette management via `viz/palettes.py`
- CSS color variables in `assets/palette.css`
- Comprehensive testing with Color Oracle recommended

See [ACCESSIBILITY.md](ACCESSIBILITY.md) for detailed information about our accessibility approach, palette choices, and testing procedures.

## Getting Started

### View the Dashboard

Simply open `index.html` in a modern web browser. The visualization uses Vega-Lite with embedded data and requires no server setup.

### Using the Palette Module (Python)

If you're creating additional visualizations:

```python
from viz.palettes import get_categorical_palette, set_global_palettes

# Set colorblind-friendly palettes globally
set_global_palettes('okabe_ito')

# Or get specific colors
colors = get_categorical_palette('okabe_ito', n=4)
```

See `viz/palettes.py` for complete API documentation.

## File Structure

```
.
├── index.html              # Main dashboard (Vega-Lite visualization)
├── viz/
│   └── palettes.py        # Centralized colorblind-safe palette module
├── assets/
│   └── palette.css        # CSS color variables for web styling
├── ACCESSIBILITY.md        # Detailed accessibility documentation
└── README.md              # This file
```

## Color Palettes

### Climate Regimes (4 categories)
- **Orange** (#E69F00) - Vulnerable / Subsistence
- **Sky Blue** (#56B4E9) - Developing / Low-Input
- **Bluish Green** (#009E73) - Emerging / Mid-Scale
- **Blue** (#0072B2) - Efficient / High-Yield

### Continents (6 categories)
- **Blue** (#0072B2) - Africa
- **Orange** (#E69F00) - Asia
- **Bluish Green** (#009E73) - Europe
- **Vermillion** (#D55E00) - North America
- **Reddish Purple** (#CC79A7) - South America
- **Yellow** (#F0E442) - Oceania

All palettes are from the Okabe-Ito collection, designed specifically for colorblind accessibility.

## Testing for Colorblindness

We recommend testing visualizations with:
- **Color Oracle:** Real-time screen simulation (https://colororacle.org/)
- **Coblis:** Online image simulation (https://www.color-blindness.com/coblis-color-blindness-simulator/)
- **Chrome DevTools:** Built-in vision deficiency emulation

## Contributing

When adding new visualizations:
1. Use palettes from `viz/palettes.py` or `assets/palette.css`
2. Test with colorblindness simulation tools
3. Ensure colors work in grayscale
4. Update documentation if adding new palette options

## Dependencies

- Modern web browser with JavaScript enabled
- Vega, Vega-Lite, and Vega-Embed (loaded via CDN)

For Python palette module:
- Optional: `matplotlib`, `seaborn`, `plotly`, or `altair` (depending on usage)
- Optional: `cycler` (for matplotlib color cycles)

## License

This project is created for educational purposes as part of Visual Data Science 2026.

## References

- **Okabe-Ito Palette:** Okabe, M. and Ito, K. (2008) Color Universal Design (CUD)
- **Paul Tol's Palettes:** https://personal.sron.nl/~pault/
- **ColorBrewer:** https://colorbrewer2.org/
- **Vega-Lite:** https://vega.github.io/vega-lite/

---

**Last Updated:** January 18, 2026
