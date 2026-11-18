*Display an inline search form or an icon that opens a search overlay, with separate input, submit, and close controls.*

The Search element displays a search form or an icon that opens a search overlay. Set **Type** to **Input** for an inline form or **Icon & Overlay** for an overlay. **Input** is the default.

## Settings

- **Action URL**: Where the form submits. Leave it empty to use your site's home URL.
- **Additional parameters**: Add hidden fields to the submitted search request.

In Bricks 2.5, the controls are grouped by the part of the search form they affect. The overlay's opening icon, submit button, and close button have separate controls.

<div className="screenshot screenshot--control-panel">

![Search controls in Icon & Overlay mode, with Keep open while styling enabled and separate Icon, Input, Overlay, Submit button, and Close button groups.](https://academy.bricksbuilder.io/assets/builder/release-2.5/search-controls-panel.webp)

</div>

## Input

Use **Input** to style the search field in either mode. Set its height, width, placeholder, background, border, box shadow, and typography. The default placeholder is “Search ...”.

Enable **Show label** to display a label above the field, then set **Label text** and **Label typography**.

## Inline submit button

With **Type** set to **Input**, open **Submit button** to set the button's text, icon, size, spacing, colors, border, box shadow, and typography.

If the button uses an icon without visible text, provide an **aria-label** that describes its action, such as `Search`.

## Icon and overlay

With **Type** set to **Icon & Overlay**, choose the opening icon under **Icon**. Its **aria-label**, such as `Open search`, names the button for screen-reader users.

Enable **Keep open while styling** to keep the overlay visible in the Builder while adjusting its controls. This preview setting does not force the overlay open on the frontend.

![The Search overlay visible on the Builder canvas with a Search Atelier North title, search field, submit button, and close icon.](https://academy.bricksbuilder.io/assets/builder/release-2.5/search-overlay-builder.webp)

### Overlay layout and title

Under **Overlay**, set the form direction, gap, title, title tag, title typography, and background.

The default title is **Search site**, using an `h4` tag. Enable **Hide title** to remove the visible title. The overlay and search field keep their accessible names when the title is hidden.

### Overlay submit button

Open **Submit button** to set the overlay form's submit text, icon, **aria-label**, and styling. These controls affect the button inside the overlay, separately from the icon that opens it.

For example, use a magnifying-glass icon to open the overlay and a text button labelled `Search` to submit the form.

### Close button

Open **Close button** to choose its icon, **aria-label**, size, spacing, colors, background, border, and box shadow. Bricks uses a close icon and the accessible name **Close search** when you leave those settings empty.

### Existing search elements

Existing opening icons and button styles retain their saved values. After updating to Bricks 2.5, review any custom CSS targeting the search form, especially rules that style every button in the overlay. Use the separate control groups when each button needs different styling.

> **Developer reference**
>
> See the [Search Schema](https://academy.bricksbuilder.io/developer/schema/elements/search/) for the full JSON schema of this element's settings and controls.