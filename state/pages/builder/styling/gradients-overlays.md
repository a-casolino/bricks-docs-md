*Create gradients and overlays in Bricks to add layered backgrounds, image treatments, and color effects.*

Use gradients for element backgrounds, overlays, or text. Select an element and open **Style > Gradient / Overlay** to configure them.

https://youtu.be/U0x0vCAzuc0

## Available controls:

- **Apply to**: Select the type of content you want to add a gradient to (text, background, overlay).
- **CSS selector**: To target a specific HTML within an element.
- **Colors**: Define the color stops for a linear, radial, or conic gradient. Use transparent colors when an overlay should reveal the image beneath it.
- **Type**: Choose linear, radial, or conic. Since Bricks 2.5, **Custom** accepts a complete gradient value or a CSS variable that contains one.
- **Repeat**: Repeats a linear, radial, or conic gradient. Define color stops to control the repeating pattern. This control is hidden for **Custom**.

### Linear gradient controls:

- **Angle in °**: Set a specific angle for your linear gradient between 0 to 360°.

### Radial gradient controls:

- **Shape**: Choose between 'circle' or 'ellipse'.
- **Size**: Select from 'closest-side', 'farthest-side', 'closest-corner', 'farthest-corner'. For details on these settings, see the [Mozilla Documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/gradient/radial-gradient#size).
- **Position**: Define the central point of the gradient.

### Conic gradient controls:

- **Starting angle in °**: Specify the starting angle of the gradient between 0 to 360°.
- **Position**: Set the gradient's center.

## Change one setting at a breakpoint {#responsive-overrides}

Since Bricks 2.5, you can change an individual Gradient / Overlay setting at another breakpoint without recreating the whole gradient. Settings you leave unset inherit from the preceding applicable breakpoint.

For example:

1. At the base breakpoint, create a linear gradient with two colors and **Angle in °** set to `90`.
2. Switch to Mobile portrait.
3. Set only **Angle in °** to `0`.

The mobile gradient uses the inherited colors with the new angle. You do not need to add those colors again. Reset the local angle to return to its inherited value.

A breakpoint-specific **Colors** list replaces the inherited list as a whole. If you want different colors at that breakpoint, define the complete color list there.

The local **Colors** list can appear empty at the selected breakpoint while the canvas still uses the inherited colors:

![Mobile portrait Builder canvas shows a gradient using inherited colors, with only Angle in degrees set locally to 0.](https://academy.bricksbuilder.io/assets/builder/release-2.5/gradient-mobile-context.webp)

<div className="screenshot screenshot--control-panel">

![Gradient / Overlay controls with a local angle of 0 and no colors repeated in the local Colors list.](https://academy.bricksbuilder.io/assets/builder/release-2.5/gradient-mobile-panel.webp)

</div>

## Custom gradients {#custom-gradients}

Choose **Type > Custom** to reuse a gradient from a CSS variable or paste a complete CSS gradient function.

The **Value** field expects the value of `background-image`, such as:

```css
var(--hero-gradient)
```

Or enter the gradient directly:

```css
linear-gradient(135deg, #152238 0%, #4263eb 100%)
```

Enter only the value, without `background-image:` or a trailing semicolon. Bricks uses this value directly instead of building a gradient from the color controls.

**Colors**, **Angle**, **Repeat**, and the radial or conic controls are hidden for **Custom**. Define the angle, stops, and repeating behavior in the value itself. **Apply to** and **CSS selector** remain available, so the same custom gradient can be used for a background, overlay, or text.