*The SVG element displays SVG graphics from files, dynamic data, custom code, or icon sets.*

The SVG element displays SVG graphics from files, dynamic data, custom code, or icon sets.

## Settings

- **Source** (select) - SVG source type. Options: `file` (default), `dynamicData`, `code`, `iconSet`.

- **File** (svg upload) - Upload an SVG file from your computer. Available when source is "file".

- **Icon set** (icon) - Select an SVG from custom icon libraries. Available when source is "iconSet".

- **Dynamic data** (text with dynamic data) - Load SVG from dynamic data. Supported field types: File, Image, SVG code, URL. Available when source is "dynamicData".

- **Code** (code editor) - Paste SVG code directly. Only available to users with code execution permissions. Ensure SVG code is safe and doesn't contain malicious code. Consider using an SVG cleaner like svgomg.net. Available when source is "code".

### Styling

- **Height** (number with units) - SVG height.

- **Width** (number with units) - SVG width.

- **Stroke width** (number) - Width of SVG stroke lines. Minimum: 1.

- **Stroke color** (color) - Color of SVG stroke elements (excludes elements with `stroke="none"`).

- **Fill** (color) - Fill color for SVG shapes (excludes elements with `fill="none"`).

- **Link** (link) - Make the SVG clickable by adding a link.

## Label a linked SVG

To give a linked SVG a link label without custom code:

1. Add an SVG element, set **Source** to **File**, and select your SVG file.
2. Open **Link**, select **Custom URL**, and enter your homepage URL.
3. In the Link control's **aria-label** field, enter `Site home`.

Bricks adds `aria-label="Site home"` to the surrounding `<a>` element.

[Custom attributes](https://academy.bricksbuilder.io/builder/features/custom-attributes/) added under **Style > Attributes** apply to the `<svg>` element, including when it has a link. Use **Link > aria-label** to set the label directly on the link.

For example, if you also add a custom attribute named `data-icon` with the value `home`, the relevant HTML is:

```html
<a href="https://academy.bricksbuilder.io/" class="bricks-link-wrapper" aria-label="Site home">
  <svg data-icon="home" viewBox="0 0 24 24">
    <!-- SVG shapes -->
  </svg>
</a>
```

This example uses `/` as the homepage URL and omits generated SVG IDs and classes.

> **Developer reference**
>
> See the [SVG Schema](https://academy.bricksbuilder.io/developer/schema/elements/svg/) for the full JSON schema of this element's settings and controls.