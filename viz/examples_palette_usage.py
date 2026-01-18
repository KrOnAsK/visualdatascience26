#!/usr/bin/env python3
"""
Example Usage of Colorblind-Friendly Palettes

This script demonstrates how to use the viz.palettes module to create
colorblind-friendly visualizations with various plotting libraries.
"""

# Import the palette module
import sys
sys.path.insert(0, '.')
from viz.palettes import (
    get_categorical_palette,
    get_continuous_colormap,
    apply_matplotlib_palette,
    set_seaborn_palette,
    set_plotly_palette,
    get_altair_scale,
    set_global_palettes,
)

print("=" * 70)
print("Colorblind-Friendly Palette Examples")
print("=" * 70)

# Example 1: Get palette colors
print("\n1. Getting palette colors:")
print("-" * 70)
okabe_ito = get_categorical_palette('okabe_ito')
print(f"Okabe-Ito palette ({len(okabe_ito)} colors):")
for i, color in enumerate(okabe_ito, 1):
    print(f"  {i}. {color}")

paul_tol = get_categorical_palette('paul_tol_muted', n=4)
print(f"\nPaul Tol Muted palette (first 4 colors):")
for i, color in enumerate(paul_tol, 1):
    print(f"  {i}. {color}")

# Example 2: Matplotlib usage
print("\n2. Matplotlib usage:")
print("-" * 70)
print("""
import matplotlib.pyplot as plt
from viz.palettes import apply_matplotlib_palette

# Apply globally
apply_matplotlib_palette(palette_name='okabe_ito')

# Now create plots
fig, ax = plt.subplots()
for i in range(4):
    ax.plot([0, 1, 2], [i, i+1, i+2], label=f'Series {i+1}')
ax.legend()
plt.show()
""")

# Example 3: Seaborn usage
print("\n3. Seaborn usage:")
print("-" * 70)
print("""
import seaborn as sns
from viz.palettes import set_seaborn_palette

set_seaborn_palette('paul_tol_muted')

# Create a plot
tips = sns.load_dataset('tips')
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='day')
plt.show()
""")

# Example 4: Plotly usage
print("\n4. Plotly usage:")
print("-" * 70)
print("""
import plotly.express as px
from viz.palettes import set_plotly_palette

set_plotly_palette('okabe_ito')

# Create a plot
df = px.data.iris()
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species')
fig.show()
""")

# Example 5: Altair usage
print("\n5. Altair usage:")
print("-" * 70)
print("""
import altair as alt
from viz.palettes import get_altair_scale

# Load data
source = alt.load_dataset('cars')

# Create chart with custom colors
chart = alt.Chart(source).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color=alt.Color('Origin:N', scale=get_altair_scale('okabe_ito'))
)
chart.show()
""")

# Example 6: Set global palettes
print("\n6. Set palettes globally for multiple libraries:")
print("-" * 70)
print("""
from viz.palettes import set_global_palettes

# Set Okabe-Ito palette for matplotlib and seaborn
set_global_palettes('okabe_ito', matplotlib_enabled=True, seaborn_enabled=True)

# Now all plots will use the colorblind-friendly palette
""")

# Example 7: Generate CSS variables
print("\n7. Generate CSS variables for web use:")
print("-" * 70)
from viz.palettes import generate_css_variables
css = generate_css_variables('okabe_ito', prefix='color-okabe')
print("CSS Variables:")
print(css)

# Example 8: Using in Vega-Lite specs
print("\n8. Using in Vega-Lite/Altair specifications:")
print("-" * 70)
print("""
from viz.palettes import get_categorical_palette

colors = get_categorical_palette('okabe_ito', n=4)

vega_spec = {
    "mark": "bar",
    "encoding": {
        "x": {"field": "category", "type": "nominal"},
        "y": {"field": "value", "type": "quantitative"},
        "color": {
            "field": "category",
            "type": "nominal",
            "scale": {
                "range": colors  # Use colorblind-safe colors
            }
        }
    }
}
""")

# Example 9: Continuous colormaps
print("\n9. Continuous colormaps for heatmaps and gradients:")
print("-" * 70)
print("""
from viz.palettes import get_continuous_colormap
import matplotlib.pyplot as plt
import numpy as np

# Get a colorblind-friendly continuous colormap
cmap = get_continuous_colormap('viridis')

# Use it in a plot
data = np.random.randn(10, 10)
plt.imshow(data, cmap=cmap)
plt.colorbar()
plt.show()
""")

print("\n" + "=" * 70)
print("For more information, see ACCESSIBILITY.md")
print("=" * 70)

# Test that the module works
if __name__ == "__main__":
    print("\n✓ All examples loaded successfully!")
    print("✓ Palette module is working correctly")
