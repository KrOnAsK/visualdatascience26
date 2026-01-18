"""
Colorblind-Friendly Palette Module

This module provides centralized, colorblind-safe color palettes for data visualization,
specifically designed to be accessible for people with red/green color blindness
(deuteranopia and protanopia).

Author: Visual Data Science Team
Date: 2026-01-18
"""

# Okabe-Ito categorical palette (colorblind-safe)
# Source: https://jfly.uni-koeln.de/color/
OKABE_ITO = [
    "#E69F00",  # Orange
    "#56B4E9",  # Sky Blue
    "#009E73",  # Bluish Green
    "#F0E442",  # Yellow
    "#0072B2",  # Blue
    "#D55E00",  # Vermillion
    "#CC79A7",  # Reddish Purple
    "#000000",  # Black
]

# ColorBrewer Dark2 palette (colorblind-friendly)
COLORBREWER_DARK2 = [
    "#1B9E77",  # Teal
    "#D95F02",  # Orange
    "#7570B3",  # Purple
    "#E7298A",  # Magenta
    "#66A61E",  # Green
    "#E6AB02",  # Yellow
    "#A6761D",  # Brown
    "#666666",  # Gray
]

# Paul Tol's vibrant palette (colorblind-safe)
PAUL_TOL_VIBRANT = [
    "#EE7733",  # Orange
    "#0077BB",  # Blue
    "#33BBEE",  # Cyan
    "#EE3377",  # Magenta
    "#CC3311",  # Red
    "#009988",  # Teal
    "#BBBBBB",  # Gray
]

# Paul Tol's muted palette (colorblind-safe, professional)
PAUL_TOL_MUTED = [
    "#CC6677",  # Rose
    "#332288",  # Indigo
    "#DDCC77",  # Sand
    "#117733",  # Green
    "#88CCEE",  # Cyan
    "#882255",  # Wine
    "#44AA99",  # Teal
    "#999933",  # Olive
    "#AA4499",  # Purple
]

# Sequential colormaps (all colorblind-friendly)
CONTINUOUS_COLORMAPS = [
    "viridis",    # Blue to yellow
    "plasma",     # Purple to yellow
    "inferno",    # Black to yellow
    "magma",      # Black to white
    "cividis",    # Blue to yellow (optimized for colorblind)
    "blues",      # Light to dark blue
    "oranges",    # Light to dark orange
    "purples",    # Light to dark purple
]

# Diverging colormaps (colorblind-friendly)
DIVERGING_COLORMAPS = [
    "BrBG",       # Brown to blue-green (ColorBrewer)
    "PuOr",       # Purple to orange (ColorBrewer)
    "coolwarm",   # Blue to red (but distinguishable)
]


def get_categorical_palette(name='okabe_ito', n=None):
    """
    Get a categorical color palette by name.
    
    Parameters
    ----------
    name : str, optional
        Name of the palette. Options: 'okabe_ito', 'colorbrewer_dark2', 
        'paul_tol_vibrant', 'paul_tol_muted'. Default is 'okabe_ito'.
    n : int, optional
        Number of colors to return. If None, returns all colors in palette.
        If n is larger than palette size, cycles through palette.
    
    Returns
    -------
    list of str
        List of hex color codes
    
    Examples
    --------
    >>> palette = get_categorical_palette('okabe_ito', n=4)
    >>> print(palette)
    ['#E69F00', '#56B4E9', '#009E73', '#F0E442']
    """
    palettes = {
        'okabe_ito': OKABE_ITO,
        'colorbrewer_dark2': COLORBREWER_DARK2,
        'paul_tol_vibrant': PAUL_TOL_VIBRANT,
        'paul_tol_muted': PAUL_TOL_MUTED,
    }
    
    if name not in palettes:
        raise ValueError(f"Unknown palette '{name}'. Available: {list(palettes.keys())}")
    
    palette = palettes[name]
    
    if n is None:
        return palette
    elif n <= len(palette):
        return palette[:n]
    else:
        # Cycle through palette if n is larger
        return [palette[i % len(palette)] for i in range(n)]


def get_continuous_colormap(name='viridis'):
    """
    Get the name of a continuous colormap.
    
    Parameters
    ----------
    name : str, optional
        Name of the colormap. Default is 'viridis'.
    
    Returns
    -------
    str
        Colormap name for use with matplotlib, seaborn, etc.
    
    Examples
    --------
    >>> cmap = get_continuous_colormap('viridis')
    >>> plt.imshow(data, cmap=cmap)
    """
    if name not in CONTINUOUS_COLORMAPS:
        raise ValueError(f"Unknown colormap '{name}'. Available: {CONTINUOUS_COLORMAPS}")
    return name


def apply_matplotlib_palette(ax=None, palette_name='okabe_ito'):
    """
    Apply a colorblind-friendly palette to matplotlib axes.
    
    Parameters
    ----------
    ax : matplotlib.axes.Axes, optional
        Axes object to apply palette to. If None, applies globally via rcParams.
    palette_name : str, optional
        Name of the palette to apply. Default is 'okabe_ito'.
    
    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> apply_matplotlib_palette()  # Apply globally
    >>> plt.plot(x, y)
    
    >>> fig, ax = plt.subplots()
    >>> apply_matplotlib_palette(ax=ax, palette_name='paul_tol_muted')
    """
    try:
        import matplotlib.pyplot as plt
        from cycler import cycler
    except ImportError:
        raise ImportError("matplotlib and cycler are required for this function")
    
    palette = get_categorical_palette(palette_name)
    
    if ax is None:
        # Apply globally
        plt.rcParams['axes.prop_cycle'] = cycler(color=palette)
    else:
        # Apply to specific axes
        ax.set_prop_cycle(cycler(color=palette))


def set_seaborn_palette(palette_name='okabe_ito'):
    """
    Set a colorblind-friendly palette for seaborn.
    
    Parameters
    ----------
    palette_name : str, optional
        Name of the palette to apply. Default is 'okabe_ito'.
    
    Examples
    --------
    >>> import seaborn as sns
    >>> set_seaborn_palette('paul_tol_muted')
    >>> sns.scatterplot(data=df, x='x', y='y', hue='category')
    """
    try:
        import seaborn as sns
    except ImportError:
        raise ImportError("seaborn is required for this function")
    
    palette = get_categorical_palette(palette_name)
    sns.set_palette(palette)


def set_plotly_palette(palette_name='okabe_ito'):
    """
    Set a colorblind-friendly palette for plotly.
    
    Parameters
    ----------
    palette_name : str, optional
        Name of the palette to apply. Default is 'okabe_ito'.
    
    Examples
    --------
    >>> import plotly.express as px
    >>> set_plotly_palette('paul_tol_vibrant')
    >>> fig = px.scatter(df, x='x', y='y', color='category')
    """
    try:
        import plotly.express as px
    except ImportError:
        raise ImportError("plotly is required for this function")
    
    palette = get_categorical_palette(palette_name)
    px.defaults.color_discrete_sequence = palette


def get_altair_scale(palette_name='okabe_ito'):
    """
    Get an Altair color scale with a colorblind-friendly palette.
    
    Parameters
    ----------
    palette_name : str, optional
        Name of the palette to use. Default is 'okabe_ito'.
    
    Returns
    -------
    alt.Scale
        Altair Scale object with the specified palette
    
    Examples
    --------
    >>> import altair as alt
    >>> scale = get_altair_scale('okabe_ito')
    >>> chart = alt.Chart(df).mark_point().encode(
    ...     x='x:Q',
    ...     y='y:Q',
    ...     color=alt.Color('category:N', scale=scale)
    ... )
    """
    try:
        import altair as alt
    except ImportError:
        raise ImportError("altair is required for this function")
    
    palette = get_categorical_palette(palette_name)
    return alt.Scale(range=palette)


def set_global_palettes(
    palette_name='okabe_ito',
    matplotlib_enabled=True,
    seaborn_enabled=True,
    plotly_enabled=False
):
    """
    Set colorblind-friendly palettes globally for multiple libraries.
    
    Parameters
    ----------
    palette_name : str, optional
        Name of the palette to apply. Default is 'okabe_ito'.
    matplotlib_enabled : bool, optional
        Whether to set matplotlib palette. Default is True.
    seaborn_enabled : bool, optional
        Whether to set seaborn palette. Default is True.
    plotly_enabled : bool, optional
        Whether to set plotly palette. Default is False (requires explicit opt-in).
    
    Examples
    --------
    >>> set_global_palettes('paul_tol_muted')
    >>> # Now all matplotlib and seaborn plots will use the palette
    """
    if matplotlib_enabled:
        try:
            apply_matplotlib_palette(palette_name=palette_name)
        except ImportError:
            pass
    
    if seaborn_enabled:
        try:
            set_seaborn_palette(palette_name=palette_name)
        except ImportError:
            pass
    
    if plotly_enabled:
        try:
            set_plotly_palette(palette_name=palette_name)
        except ImportError:
            pass


# Utility function to generate CSS variables
def generate_css_variables(palette_name='okabe_ito', prefix='color'):
    """
    Generate CSS variable definitions for a palette.
    
    Parameters
    ----------
    palette_name : str, optional
        Name of the palette. Default is 'okabe_ito'.
    prefix : str, optional
        Prefix for CSS variable names. Default is 'color'.
    
    Returns
    -------
    str
        CSS variable definitions
    
    Examples
    --------
    >>> css = generate_css_variables('okabe_ito')
    >>> print(css)
    --color-1: #E69F00;
    --color-2: #56B4E9;
    ...
    """
    palette = get_categorical_palette(palette_name)
    lines = []
    for i, color in enumerate(palette, 1):
        lines.append(f"  --{prefix}-{i}: {color};")
    return "\n".join(lines)


if __name__ == "__main__":
    # Example usage and testing
    print("Okabe-Ito palette:")
    print(get_categorical_palette('okabe_ito'))
    print("\nCSS variables for Okabe-Ito:")
    print(generate_css_variables('okabe_ito'))
