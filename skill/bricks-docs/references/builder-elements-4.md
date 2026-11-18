# Logo

Source: https://academy.bricksbuilder.io/builder/elements/media/logo/

*The Logo element displays your site logo with support for regular, inverse, and dark-mode logo variants, custom dimensions, and fallback text.*

The Logo element displays your site logo and can switch between logo variants for dark mode and sticky headers.

## Settings

- **Logo** (image) - Select the main logo image from the media library. Minimum dimension should be twice the logo height/width for proper retina display. For SVG logos, set height and width in px values.

- **Logo inverse** (image) - Alternative logo image for sticky scrolling headers. Only available when the main logo is set.

- **Logo dark mode** (image) - Alternative logo image used when dark mode is active. Only available when the main logo is set.

- **Height** (number with units) - Logo height. Maximum: 400. Default: `auto`. Only available when logo is set.

- **Width** (number with units) - Logo width. Maximum: 999. Default: `auto`. Only available when logo is set.

- **Text** (text) - Fallback text displayed if logo image isn't set or available. Default: Site name from WordPress settings.

- **Loading** (select) - Image loading behavior. Options: `eager`, `lazy`. Default: `eager`.

- **Link to** (link) - Configure where the logo links. Default: Site home page.

## Logo variants

Logo variants are available starting in Bricks 2.4. Add them in the Logo element settings under **Logo variants**.

When [dark mode](https://academy.bricksbuilder.io/builder/features/color-manager/#using-dark-mode) is active and **Logo dark mode** is configured, Bricks swaps the main logo image for the dark-mode logo. If no dark-mode logo is configured, the main logo stays visible.

If the Logo element is inside a sticky header and **Logo inverse** is configured, the inverse logo is used while the header is scrolling. This takes priority over the dark-mode logo during the sticky scrolling state.

> **Developer reference**
>
> See the [Logo Schema](https://academy.bricksbuilder.io/developer/schema/elements/logo/) for the full JSON schema of this element's settings and controls.

---

# Lottie

Source: https://academy.bricksbuilder.io/builder/elements/media/lottie/

*Add Lottie JSON or .lottie animations and control playback on load, visibility, hover, click, scroll, or through interactions.*

The **Lottie** element, available in Bricks 2.5, displays vector animations from Lottie JSON or `.lottie` files. Use it for an animated illustration or a small interaction such as an icon that plays when a card receives hover or keyboard focus.

## Add an animation

1. Add a **Lottie** element from the **Media** elements.
2. Choose a **Source**:
   - **File**: Select a Lottie JSON or `.lottie` attachment.
   - **External URL**: Enter a public animation URL. The server must allow cross-origin requests. Leaving the URL empty shows the bundled sample animation.
   - **Dynamic data**: Select media supplied by a dynamic-data tag.
3. Set **Width** and **Height** if the animation needs a specific size.
4. Choose when it should play, then save and check the frontend.

For a `.lottie` file containing several animations, enter the manifest's **Animation ID**. Leave it empty to use the first animation. The setting has no effect on JSON files.

Bricks enables JSON and `.lottie` uploads for users who can upload files in WordPress and have permission to add the Lottie element. Other site upload restrictions still apply. If an upload is rejected, check those permissions and the site’s allowed file types.

A remote URL must return the animation file itself, rather than a web page containing a player.

<div className="screenshot screenshot--control-panel">

![Lottie settings with External URL selected, the empty URL showing the Sample animation placeholder, and Play set to None (Interactions).](https://academy.bricksbuilder.io/assets/builder/release-2.5/lottie-source-panel.webp)

</div>

## Choose when to play

Use **Play** to choose the trigger:

| Play setting            | Behavior                                                                                                                                  |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **On page load**        | Start after the animation loads.                                                                                                          |
| **When visible**        | Play when the element enters the viewport. Choose **Reset and replay** or **Pause and resume** under **On leaving viewport**.             |
| **On hover or focus**   | Play when the trigger receives pointer hover or keyboard focus. **On mouse leave** can reset, pause, reverse, or finish the current play. |
| **On click**            | Choose **Play and pause**, **Play from start**, or **Play forward, then reverse**.                                                        |
| **Sync with scroll**    | Advance through the animation as the element moves through the viewport.                                                                  |
| **None (Interactions)** | Control playback through Bricks interactions.                                                                                             |

**Delay (ms)** postpones playback for **On page load** and **When visible**. The default is `0`. With **Pause and resume**, the delay applies to the initial start, not resuming playback. Use **Delay between loops** to pause between repeats.

For **When visible**, enable **Play once** to disable looping and automatic replay after completion until the page reloads.

For hover and click, **Trigger element** can be **Self**, **Parent**, or **CSS selector**. A custom selector uses the closest matching ancestor first, then the first matching element on the page. Use **Parent** when an illustration should respond to its containing card.

### Sync with scroll

**Start (%)** controls where the element's top edge starts playback, measured from the bottom of the viewport (`0`) to the top (`100`). **End (%)** controls where its bottom edge finishes playback. The defaults are `0` and `100`.

Scroll playback follows scroll progress. Loop, loop count, loop delay, and speed controls do not apply in this mode.

## Playback settings

- **Loop**: Repeat playback. Enabled by default.
- **Loop count**: Number of plays. Leave empty for continuous looping.
- **Delay between loops (ms)**: Pause between repeats.
- **Speed**: Playback multiplier, from `0.1` to `10`. The default is `1`.
- **Direction**: Play forward or in reverse.
- **Start frame** and **End frame**: Limit playback to a section of the animation. Leave empty to use its full length.
- **Frame when stopped**: Show the first or last frame before playback and after a reset.
- **Lazy load**: Load the animation near the viewport. Enabled by default. Global or page-level **Disable lazy load** settings override it.

## Control playback with interactions

To play an animation from a separate Button:

1. Set the Lottie element's **Play** to **None (Interactions)**.
2. Add a **Click** interaction to the Button.
3. Choose **Lottie: Playback** as the action.
4. Choose **Play**, **Pause**, **Play and pause**, **Stop**, or **Play from start**.
5. Target the Lottie element, or a wrapper containing it, through the interaction target controls.
6. Save and test the Button on the frontend.

Use separate play and pause controls if visitors need to control a repeating animation. See [Interactions](https://academy.bricksbuilder.io/builder/features/interactions/) for trigger and target setup.

<div className="screenshot screenshot--control-panel">

![Button Click interaction using Lottie: Playback, Play and pause, and a CSS selector that targets the Lottie element.](https://academy.bricksbuilder.io/assets/builder/release-2.5/lottie-playback-panel.webp)

</div>

## Accessibility and reduced motion

Add a **Text alternative** when the animation conveys information. Leave it empty for decorative animations. A Lottie element that uses itself as a hover or click trigger is keyboard focusable; give it a meaningful text alternative so its purpose is clear.

When a visitor prefers reduced motion, Bricks shows the selected **Frame when stopped** instead of playing the animation. Keep essential text and actions outside the animation so they remain available in that state.

## Troubleshooting

- **Animation could not be loaded**: Check that the URL returns a supported JSON or `.lottie` file and that a remote host permits cross-origin requests.
- **Wrong animation in a .lottie file**: Check **Animation ID** against the file's manifest.
- **Animation starts only after scrolling**: Check **Lazy load** and the selected **Play** trigger.
- **A card does not trigger playback**: Check **Trigger element** and the custom CSS selector. For a keyboard-triggered card, the card itself must be focusable.

---

# Slider (nestable)

Source: https://academy.bricksbuilder.io/builder/elements/media/slider-nested/

*Build sliders with nested content, continuous auto scroll, and accessible pause and play controls.*

The Slider (nestable) element lets you build slides from editable Bricks elements. It uses Splide for slide navigation, autoplay, and, since Bricks 2.5, continuous auto scroll.

## Settings

- **Children** (nestable) - Drag and drop elements to create slider slides.

### Options

- **Options type** (select) - Use default settings or provide custom JSON options. Options: `default`, `custom`.

- **Custom options** (code) - A [Splide options](https://splidejs.com/guides/options/) object in JSON format. Shown when Options type is **Custom**. This replaces the options generated by the default controls, so include any autoplay or auto scroll settings you need in that object.

- **Type** (select) - Slider behavior. Options: `loop`, `slide`, `fade`. Default: `loop`.

- **Direction** (select) - Slide direction. Options: `left to right`, `right to left`, `vertical`. Supports breakpoints.

- **Keyboard** (select) - Keyboard navigation. Options: `off`, `focused`, `global`. Default: `global`. Supports breakpoints.

- **Auto height** (checkbox) - Adjust height to content. May cause layout shift. Using "Auto height" might lead to CLS (Cumulative Layout Shift).

- **Height** (number with units) - Fixed slider height. Default: 50vh. Not available when auto height is enabled. Supports breakpoints.

- **Spacing** (number with units) - Gap between slides. Default: 0. Supports breakpoints.

- **Start index** (number) - Initial slide index. Default: 0.

- **Items to show** (number) - Number of slides visible at once. Default: 1. Supports breakpoints. Not available for fade type.

- **Items to scroll** (number) - Number of slides to scroll at once. Default: 1. Supports breakpoints. Not available for fade type.

- **Speed in ms** (number) - Transition speed. Default: 400. Supports breakpoints.

- **Focus** (number) - Determines which slide should be active if the carousel has multiple slides in a page. Number/"center". Supports breakpoints.

#### Autoplay

- **Autoplay** (checkbox) - Enable automatic slide progression.

- **Pause on hover** (checkbox) - Pause autoplay when hovering over slider.

- **Pause on focus** (checkbox) - Pause autoplay when slider is focused.

- **Interval in ms** (number) - Time between slides. Default: 3000.

#### Auto scroll {#auto-scroll}

Auto scroll moves slides continuously. Autoplay advances from one slide to the next after an interval. For a continuous row of reviews or logos, use **Auto scroll** with **Type → Loop** and leave Autoplay disabled.

Auto scroll controls appear under **Options** when **Options type** is **Default**.

| Setting | Behavior | Default |
| --- | --- | --- |
| **Auto scroll** | Enable continuous slide movement. | Disabled |
| **Speed** | Movement speed, adjustable in steps of `0.1`. Positive and negative values move in opposite directions; `0` stops movement. This is separate from **Speed in ms**, which controls slide transitions. | `1` |
| **Pause on hover** | Pause while the pointer is over the slider. | Disabled |
| **Pause on focus** | Pause while focus is inside the slider. | Disabled |

<div className="screenshot screenshot--control-panel">

![Auto scroll enabled with speed -0.6 and pause on hover and focus.](https://academy.bricksbuilder.io/assets/builder/release-2.5/slider-auto-scroll-settings.webp)

</div>

The slider's **Direction** setting selects the horizontal or vertical layout. **Fade** does not support auto scroll. The Auto scroll controls apply across screen sizes; they do not have separate breakpoint values. Custom JSON options can define breakpoint-specific behavior.

Autoplay and auto scroll stay off in the Builder so you can select and edit slide content. Save the page and view the frontend to check movement. This also applies when you use Custom options.

Add a [Playback control](#playback-control) so visitors can pause the slider. Pause on hover or focus alone does not provide a pause control for everyone.

#### Rewind

Available when type is not "loop":

- **Rewind** (checkbox) - Enable rewind functionality.

- **Rewind by drag** (checkbox) - Allow rewinding by dragging.

- **Speed in ms** (number) - Rewind transition speed.

### Playback control {#playback-control}

Since Bricks 2.5, **Playback control → Show playback control** adds a native pause/play button for autoplay and auto scroll. It is disabled by default. The button sits outside the moving slides and changes its label between **Pause** and **Play**.

Set your own labels in the **Pause** and **Play** fields. Use the controls in the same group to set typography, background, border, padding, and position.

<div className="screenshot screenshot--control-panel">

![Playback control enabled with Pause reviews and Play reviews labels.](https://academy.bricksbuilder.io/assets/builder/release-2.5/slider-playback-settings.webp)

</div>

![A continuous review slider with its native Pause reviews button outside the cards.](https://academy.bricksbuilder.io/assets/builder/release-2.5/slider-reviews.webp)

With the native control enabled, keyboard focus entering the slider pauses playback until the visitor chooses **Play**. A deliberate pause remains in place after hovering, resizing, or updating the slider. Hover pauses are temporary when **Pause on hover** is enabled.

Bricks stops automatic movement when the visitor requests reduced motion and hides the native button when playback is unavailable. A Play action does not override the reduced-motion preference.

To use your own button, add a [Slider playback interaction](https://academy.bricksbuilder.io/builder/features/interactions/#slider-playback) and target the slider. This can pause, resume, or toggle both autoplay and auto scroll.

### Slide

- **Padding** (spacing) - Padding inside slides.

- **Align horizontal** (align-items) - Horizontal alignment of slide content. Options: `flex-start`, `center`, `flex-end`.

- **Align vertical** (justify-content) - Vertical alignment of slide content. Options: `flex-start`, `center`, `flex-end`, `space-between`, `space-around`.

- **Background** (background) - Background styling for slides.

- **Border** (border) - Border styling for slides.

### Arrows

- **Show** (checkbox) - Display navigation arrows.

- **Height** (number with units) - Arrow button height. Default: 50px.

- **Width** (number with units) - Arrow button width. Default: 50px.

- **Background** (color) - Arrow button background color.

- **Border** (border) - Arrow button border styling.

- **Color** (color) - Arrow icon color.

- **Size** (number with units) - Arrow icon size.

- **Text shadow** (text-shadow) - Text shadow for arrow icons.

#### Disabled

- **Background** (color) - Background color for disabled arrows.

- **Border** (border) - Border styling for disabled arrows.

- **Color** (color) - Icon color for disabled arrows.

- **Opacity** (number) - Opacity for disabled arrows (0-1).

#### Prev arrow

- **Prev arrow** (icon) - Custom icon for previous arrow.

- **Top** (number with units) - Top position. Default: 50%.

- **Right** (number with units) - Right position.

- **Bottom** (number with units) - Bottom position.

- **Left** (number with units) - Left position.

- **Transform** (transform) - CSS transform for previous arrow.

#### Next arrow

- **Next arrow** (icon) - Custom icon for next arrow.

- **Top** (number with units) - Top position. Default: 50%.

- **Right** (number with units) - Right position.

- **Bottom** (number with units) - Bottom position.

- **Left** (number with units) - Left position.

- **Transform** (transform) - CSS transform for next arrow.

### Pagination

- **Show** (checkbox) - Display pagination dots. Default: enabled.

- **Margin** (spacing) - Margin around pagination dots. Default: 5px on all sides.

- **Height** (number with units) - Dot height. Default: 10px.

- **Width** (number with units) - Dot width. Default: 10px.

- **Color** (color) - Dot color and background color.

- **Border** (border) - Border styling for dots.

#### Active

- **Height** (number with units) - Height for active dot.

- **Width** (number with units) - Width for active dot.

- **Color** (color) - Color for active dot.

- **Border** (border) - Border styling for active dot.

> **Developer reference**
>
> See the [Slider (Nestable) Schema](https://academy.bricksbuilder.io/developer/schema/elements/slider-nested/) for the full JSON schema of this element's settings and controls.

---

# Slider

Source: https://academy.bricksbuilder.io/builder/elements/media/slider/

*The Slider element creates a full-width image slider with customizable slides containing titles, content, and buttons, using the Swiper library.*

The Slider element creates a full-width image slider with customizable slides containing titles, content, and buttons, using the Swiper library.

## Security scanner reports

Bricks 2.4 patches the legacy Swiper build used by the classic Slider element. The bundled asset is a Bricks-patched vendored Swiper 8 legacy build with the CVE-2026-27212 / GHSA-hmx5-qpq5-p643 mitigation backported.

Bricks keeps the Swiper 8 runtime behavior so existing sliders continue to behave as before, including loop configurations that depend on Swiper 8 duplicate slides. The public `bricks-swiper` script version is `bricks-cve-2026-27212-p1`, and the bundled file no longer reports stock `Swiper 8.4.4` in its header.

Some security scanners may still fingerprint the underlying minified Swiper 8 code and flag it. Use this VEX or exception note: `Bricks-patched vendored Swiper 8 legacy build with CVE-2026-27212 backport.`

## Settings

- **Slides** (repeater) - Add slider slides. Each slide has:
  - **Title** (text) - Slide title.
  - **Title Tag** (select) - HTML tag for title. Options: `h1`-`h6`. Default: `h3`.
  - **Content** (rich text) - Slide content.
  - **Button text** (text) - Call-to-action button text.
  - **Button style** (select) - Button style. Default: `light`.
  - **Button size** (select) - Button size.
  - **Button width** (number with units) - Button width.
  - **Button link** (link) - Button destination.
  - **Button background** (color) - Button background color.
  - **Button border** (border) - Button border styling.
  - **Button box shadow** (box-shadow) - Button shadow.
  - **Button typography** (typography) - Button text styling.
  - **Background** (background) - Slide background (color, image, gradient).
  - **Overlay** (color) - Overlay color over the background.

- **Slides to show** (number) - Number of slides visible at once. Default: 1.

- **Slides to scroll** (number) - Number of slides to advance per transition. Default: 1.

- **Spacing** (number) - Spacing between slides in pixels. Default: 0.

- **Height** (number with units) - Slider height. Default: 300px.

- **Effect** (select) - Transition effect. Options: `slide`, `fade`, `cube`, `coverflow`, `flip`. Default: `slide`.

- **Loop** (select) - Enable infinite loop. Options: `enable`, `disable`. Default: `enable`.

- **Center mode** (checkbox) - Center the active slide.

- **Disable lazy load** (checkbox) - Load all images immediately.

- **Autoplay** (checkbox) - Enable automatic sliding.

- **Pause on hover** (checkbox) - Pause autoplay on hover.

- **Stop on last slide** (checkbox) - Stop autoplay on the last slide.

- **Autoplay delay in ms** (number) - Delay between slides in milliseconds. Default: 3000.

- **Animation speed in ms** (number) - Transition speed in milliseconds. Default: 300.

### Title

- **Title margin** (spacing) - Margin around slide titles.

- **Title typography** (typography) - Font settings for slide titles.

### Content

- **Content width** (number with units) - Maximum width of slide content.

- **Content background** (color) - Background color for slide content.

- **Content typography** (typography) - Font settings for slide content.

- **Content margin** (spacing) - Margin around slide content.

- **Content padding** (spacing) - Padding inside slide content. Default: 30px top, 60px right, 30px bottom, 60px left.

- **Content align horizontal** (justify-content) - Horizontal alignment of content within slides.

- **Content align vertical** (align-items) - Vertical alignment of content within slides.

- **Content text align** (text-align) - Text alignment within slide content.

### Button

- **Button style** (select) - Global button style. Default: `light`.

- **Button size** (select) - Global button size.

- **Button width** (number with units) - Global button width.

- **Background** (color) - Global button background color.

- **Border** (border) - Global button border styling.

- **Box shadow** (box-shadow) - Global button shadow.

- **Typography** (typography) - Global button text styling.

### Background

- **Top** (number with units) - Background image top position.

- **Right** (number with units) - Background image right position.

- **Bottom** (number with units) - Background image bottom position.

- **Left** (number with units) - Background image left position.

## Arrows

- **Show arrows** (checkbox) - Display navigation arrows. Default: true.

- **Height** (number with units) - Arrow button height. Default: 50px.

- **Width** (number with units) - Arrow button width. Default: 50px.

- **Background** (color) - Arrow button background color.

- **Border** (border) - Arrow button border styling.

- **Typography** (typography) - Arrow button text styling.

### Prev arrow

- **Prev arrow** (icon) - Previous arrow icon. Default: `ion-ios-arrow-back`.

- **Top** (number with units) - Previous arrow top position. Default: 50%.

- **Right** (number with units) - Previous arrow right position.

- **Bottom** (number with units) - Previous arrow bottom position.

- **Left** (number with units) - Previous arrow left position. Default: 50px.

- **Transform** (transform) - Previous arrow transformations.

### Next arrow

- **Next arrow** (icon) - Next arrow icon. Default: `ion-ios-arrow-forward`.

- **Top** (number with units) - Next arrow top position.

- **Right** (number with units) - Next arrow right position.

- **Bottom** (number with units) - Next arrow bottom position.

- **Left** (number with units) - Next arrow left position.

- **Transform** (transform) - Next arrow transformations.

## Dots

- **Show dots** (checkbox) - Display pagination dots.

- **Dynamic dots** (checkbox) - Enable dynamic bullet pagination.

- **Vertical** (checkbox) - Display dots vertically.

- **Height** (number with units) - Dot height.

- **Width** (number with units) - Dot width.

- **Top** (number with units) - Dots container top position.

- **Right** (number with units) - Dots container right position.

- **Bottom** (number with units) - Dots container bottom position.

- **Left** (number with units) - Dots container left position.

- **Border** (border) - Dot border styling.

- **Color** (color) - Inactive dot color.

- **Active color** (color) - Active dot color.

- **Margin** (spacing) - Margin around individual dots.

> **Developer reference**
>
> See the [Slider Schema](https://academy.bricksbuilder.io/developer/schema/elements/slider/) for the full JSON schema of this element's settings and controls.

---

# SVG

Source: https://academy.bricksbuilder.io/builder/elements/media/svg/

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

> **Developer reference**
>
> See the [SVG Schema](https://academy.bricksbuilder.io/developer/schema/elements/svg/) for the full JSON schema of this element's settings and controls.

---

# Query results summary

Source: https://academy.bricksbuilder.io/builder/elements/query/query-results-summary/

*Display a query's reported starting position, ending position, and total result count, with updates for pagination, Load More, Infinite Scroll, and Query Filters.*

The Query Results Summary element, introduced in version 1.12.2, allows you to display a dynamic count of results within a query, helping users understand which items they are currently viewing in relation to the total number of results. This is particularly useful for search results, archive pages, and paginated lists where users navigate through multiple pages of content. It can be found in the elements panel under the "Query" category.

**Note:** If a third-party plugin disables Bricks Query history via the [`bricks/query/force_run`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-force_run/) hook, the results summary may display incorrect information.

## Compatibility

The **Query Results Summary** element updates with Bricks' native AJAX actions, including:

- AJAX Pagination
- Load More
- Infinite Scroll
- Query Filters

This ensures that the summary updates dynamically as users interact with query-based elements on the page.

Example:

![](https://academy.bricksbuilder.io/assets/query-results-summary-element-example.png)

## Settings

![](https://academy.bricksbuilder.io/assets/query-results-summary-element-controls.png)

### Query

Select the **target query** for which the summary should be displayed.

For a listing with synced map markers, select the results loop containing [Map Connectors](https://academy.bricksbuilder.io/builder/elements/general/map-connector/). The summary describes that loop's results. See [map queries and interactive listings](https://academy.bricksbuilder.io/builder/dynamic-content/query-loop/#map-queries).

### Format

Customize the summary text using placeholders:

- `%start%`: The numeric starting position reported by the query.
- `%end%`: The numeric ending position reported by the query.
- `%total%`: The total number of results.

Default format: `Results: %start% - %end% of %total% posts`

Example output: Results: 1 - 5 of 14 posts

Native post, term, and user queries normally report one-based positions. A query without a populated range, including a provider-backed ACF loop, can report `0` for the start or end position.

Developers can override the reported positions with [`bricks/query/result_start`](https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-result_start/) and [`bricks/query/result_end`](https://academy.bricksbuilder.io/developer/hooks/filters/bricks-query-result_end/). These filters change summary metadata only. They do not skip or limit items, change the total count, or fetch another page.

### Text: One Result

Define a custom message when the query returns exactly **one** result to handle singular/plural differences.

Default text: One post found

### Text: No Results

Specify a custom message when the query returns **zero** results.

Default text: No posts found

> **Developer reference**
>
> See the [Query Results Summary Schema](https://academy.bricksbuilder.io/developer/schema/elements/query-results-summary/) for the full JSON schema of this element's settings and controls.

---

# Add to cart

Source: https://academy.bricksbuilder.io/builder/elements/product/product-add-to-cart/

*Displays the Add to cart form for the current product, including quantity and variation handling for variable products.*

Displays the Add to cart form for the current product, including quantity and variation handling for variable products.

## Where this element works

Single Product templates (or product preview context).

## Key settings

- **Typography** (typography)
- **Background color** (color)
- **Border** (border)
- **Margin** (spacing)
- **Padding** (spacing)
- **Description typography** (typography)
- **Price typography** (typography)
- **Regular price typography** (typography)
- **Sale price typography** (typography)
- **Wrap** (select)

## Usage tips

- Use this element inside a Single Product template to guarantee a valid product context.
- Combine it with Product title, Product price, and Product gallery for complete product detail layouts.

---

# Product additional information

Source: https://academy.bricksbuilder.io/builder/elements/product/product-additional-information/

*Displays the product attributes table shown in WooCommerce under Additional information.*

Displays the product attributes table shown in WooCommerce under Additional information.

## Where this element works

Single Product templates (or product preview context).

## Key settings

- **Heading** (text)
- **Typography** (typography)
- **Width** (number)

## Usage tips

- Use this element inside a Single Product template to guarantee a valid product context.
- Combine it with Product title, Product price, and Product gallery for complete product detail layouts.

---

# Product content

Source: https://academy.bricksbuilder.io/builder/elements/product/product-content/

*Displays the full product description (main content) from the product editor.*

Displays the full product description (main content) from the product editor.

## Where this element works

Single Product templates (or product preview context).

## Key settings

- This element uses standard WooCommerce output and inherited style controls.

## Usage tips

- Use this element inside a Single Product template to guarantee a valid product context.
- Combine it with Product title, Product price, and Product gallery for complete product detail layouts.

---

# Product meta

Source: https://academy.bricksbuilder.io/builder/elements/product/product-meta/

*Displays product meta details such as SKU, categories, and tags.*

Displays product meta details such as SKU, categories, and tags.

## Where this element works

Single Product templates (or product preview context).

## Key settings

- **Direction** (direction)
- **Spacing** (number)
- **Separator** (text)
- **Separator color** (color)
- **Typography** (typography)
- **Fields** (repeater)

## Usage tips

- Use this element inside a Single Product template to guarantee a valid product context.
- Combine it with Product title, Product price, and Product gallery for complete product detail layouts.

---

# Product gallery

Source: https://academy.bricksbuilder.io/builder/elements/product/product-gallery/

*Displays the WooCommerce product gallery with main product image and thumbnail navigation.*

Displays the WooCommerce product gallery with main product image and thumbnail navigation.

## Settings

- **Product image size** (select) - Image size for the main product image. Default: woocommerce_single.
- **Thumbnail image size** (select) - Image size for thumbnail images. Default: woocommerce_gallery_thumbnail.
- **Lightbox image size** (select) - Image size for lightbox/fullscreen view. Default: woocommerce_single.
- **Thumbnail position** (select) - Position of thumbnail navigation relative to main image. Options: bottom, top, left, right. Default: bottom.
- **Thumbnail width** (number) - Width of thumbnail images in pixels.
- **Thumbnail height** (number) - Height of thumbnail images in pixels.
- **Thumbnail border** (border) - Border styling for thumbnail images.
- **Thumbnail border (Active)** (border) - Border styling for active/selected thumbnail image.
- **Slider** (checkbox) - Enable thumbnail slider functionality.
- **Slider: Height (px)** (number) - Maximum height of thumbnail slider when positioned left/right.
- **Slider: Gap (px)** (number) - Gap between thumbnail images in slider. Default: 30.
- **Max. items** (number) - Maximum number of thumbnail items shown in horizontal slider. Default: 4.
- **Prev arrow** (icon) - Icon for previous arrow navigation. Default: ti-angle-left.
- **Next arrow** (icon) - Icon for next arrow navigation. Default: ti-angle-right.
- **Background** (color) - Background color for navigation arrows.
- **Border** (border) - Border styling for navigation arrows.
- **Color** (color) - Icon color for navigation arrows.
- **Size** (number) - Font size for navigation arrow icons.
- **Height** (number) - Height of navigation arrow buttons.
- **Width** (number) - Width of navigation arrow buttons.

---

# Product price

Source: https://academy.bricksbuilder.io/builder/elements/product/product-price/

*Displays the WooCommerce product price, including regular price, sale price, and price range for variable products.*

Displays the WooCommerce product price, including regular price, sale price, and price range for variable products.

## Selected variation price (since 2.5) {#variation-price}

On a variable product, the Product price element updates to the selected variation's price as soon as a customer picks a variation. Clearing the selection shows the original price or price range again. This also works for products inside query loops and quick views.

If all variations have the same price, WooCommerce doesn't provide a separate variation price, so the element keeps showing the original price.

## Settings

- **Hide regular price** (checkbox) - Hide the regular price when a sale price is active.
- **Regular price typography** (typography) - Typography settings for the regular price text.
- **Sale price typography** (typography) - Typography settings for the sale price text.

---

# Product rating

Source: https://academy.bricksbuilder.io/builder/elements/product/product-rating/

*Displays the product star rating and review count for the current product.*

Displays the product star rating and review count for the current product.

## Where this element works

Single Product templates (or product preview context).

## Key settings

- **Star color** (color)
- **Empty star color** (color)
- **Hide reviews link** (checkbox)
- **Reviews link** (separator)
- **Text** (text)
- **No ratings** (separator)
- **Show empty stars** (checkbox)

## Usage tips

- Use this element inside a Single Product template to guarantee a valid product context.
- Combine it with Product title, Product price, and Product gallery for complete product detail layouts.

---

# Related products

Source: https://academy.bricksbuilder.io/builder/elements/product/product-related/

*Displays related products based on the current product context.*

Displays related products based on the current product context.

## Where this element works

Single Product templates (or product preview context).

## Key settings

- **Heading** (text)
- **Heading typography** (typography)
- **Max. products** (number)
- **Columns** (number)
- **Order by** (select)
- **Order** (select)
- **Gap** (number)
- **Align** (text-align)
- **Image height** (number)
- **Padding** (spacing)

## Usage tips

- Use this element inside a Single Product template to guarantee a valid product context.
- Combine it with Product title, Product price, and Product gallery for complete product detail layouts.

---

# Product reviews

Source: https://academy.bricksbuilder.io/builder/elements/product/product-reviews/

*Displays the WooCommerce reviews section for the current product.*

Displays the WooCommerce reviews section for the current product.

## Where this element works

Single Product templates (or product preview context).

## Key settings

- **Title** (typography)
- **Label** (typography)
- **Textarea** (select)
- **Author** (typography)
- **Date** (typography)
- **Description** (typography)
- **Size** (number)
- **Background color** (color)
- **Fill color** (color)

## Usage tips

- Use this element inside a Single Product template to guarantee a valid product context.
- Combine it with Product title, Product price, and Product gallery for complete product detail layouts.

---

# Product short description

Source: https://academy.bricksbuilder.io/builder/elements/product/product-short-description/

*Displays the WooCommerce product short description (excerpt) on single product pages.*

Displays the WooCommerce product short description (excerpt) on single product pages.

---

# Product stock

Source: https://academy.bricksbuilder.io/builder/elements/product/product-stock/

*Displays the WooCommerce product stock status and quantity information.*

Displays the WooCommerce product stock status and quantity information.

## Settings

### In stock
- **Custom text** (text) - Custom text to display when product is in stock.
- **Typography** (typography) - Typography settings for in stock text.
- **Background color** (color) - Background color for in stock status.

### Low stock / On backorder
- **Custom text** (text) - Custom text to display when product has low stock or is on backorder.
- **Typography** (typography) - Typography settings for low stock/backorder text.
- **Background color** (color) - Background color for low stock/backorder status.

### Out of stock
- **Custom text** (text) - Custom text to display when product is out of stock.
- **Typography** (typography) - Typography settings for out of stock text.
- **Background color** (color) - Background color for out of stock status.

---

# Product tabs

Source: https://academy.bricksbuilder.io/builder/elements/product/product-tabs/

*Displays WooCommerce product tabs such as description, additional information, and reviews.*

Displays WooCommerce product tabs such as description, additional information, and reviews.

## Where this element works

Single Product templates (or product preview context).

## Key settings

- **Direction** (direction)
- **Alignment** (justify-content)
- **Padding** (spacing)
- **Typography** (typography)
- **Background color** (color)
- **Border** (border)

## Usage tips

- Use this element inside a Single Product template to guarantee a valid product context.
- Combine it with Product title, Product price, and Product gallery for complete product detail layouts.

---

# Product title

Source: https://academy.bricksbuilder.io/builder/elements/product/product-title/

*Displays the title of the current WooCommerce product.*

Displays the title of the current WooCommerce product.

## Settings

- **HTML tag** (select) - HTML tag for the title. Options: h1, h2, h3, h4, h5, h6. Default: h1.
- **Prefix** (text) - Text to display before the title.
- **Prefix block** (checkbox) - Display prefix as block element.
- **Suffix** (text) - Text to display after the title.
- **Suffix block** (checkbox) - Display suffix as block element.
- **Link to product** (checkbox) - Make the title a link to the product.

---

# Product up/cross-sells

Source: https://academy.bricksbuilder.io/builder/elements/product/product-upsells/

*Displays up-sell and cross-sell products linked to the current product.*

Displays up-sell and cross-sell products linked to the current product.

## Where this element works

Single Product templates (or product preview context).

## Key settings

- **Type** (select)
- **Heading** (text)
- **Heading typography** (typography)
- **Max. products** (number)
- **Columns** (number)
- **Gap** (number)
- **Order by** (select)
- **Order** (select)
- **Padding** (spacing)
- **Background color** (color)

## Usage tips

- Use this element inside a Single Product template to guarantee a valid product context.
- Combine it with Product title, Product price, and Product gallery for complete product detail layouts.

---

# Block

Source: https://academy.bricksbuilder.io/builder/elements/layout/block/

*The Block element is one of the four layout elements in Bricks (1.5+).*

The Block element is one of the four [layout elements](https://academy.bricksbuilder.io/builder/styling/layout/) in Bricks (1.5+).

Introduced together with the Section & Div element, it provides the same powerful layout controls as the Container but uses a default width of 100% instead of the Container's fixed 1100px width.

This makes it the perfect element to use inside of a Container (e.g. column/row based layout). Or wherever you need to span the entire available width, plus quick access to direction & alignment settings. As the Block element uses `flex` by default.

Use blocks to create multi-column layouts, sidebars, or any layout where you want full-width flexbox behavior without the Container's width constraints. If you want your layout element to only take up the space of its content, use the Div element instead.

**Tip:** Blocks are ideal for creating column-based layouts. When you need multiple equal-width columns, insert blocks inside a container and set the direction to horizontal - they'll automatically distribute the available space equally.

## Settings

- **Grid column** (text) - CSS grid column span when parent uses grid layout. Controls `grid-column` property.

- **Grid row** (text) - CSS grid row span when parent uses grid layout. Controls `grid-row` property.

- **Query loop** - Enable query loop functionality for dynamic content. Available for Container, Block, Div, and Section elements.

- **Link** (link) - Link settings when using anchor tag. Required when HTML tag is set to 'a'.

- **HTML tag** (select) - HTML tag for the block element. Options: div, section, a [Link], article, nav, ol, ul, li, aside, address, figure, custom. Default: div.

- **Custom tag** (text) - Custom HTML tag when "custom" is selected. Without attributes. Required when HTML tag is 'custom'.

- **Display** (select) - CSS display property. Options: flex, grid, block, inline-block, inline, none. Default: flex.

### Grid Layout (when Display is grid)

- **Gap** (number with units) - Gap between grid items. Controls `grid-gap` property.

- **Grid template columns** (text) - CSS grid template columns. Supports dynamic data and variables.

- **Grid template rows** (text) - CSS grid template rows. Supports dynamic data and variables.

- **Grid auto columns** (text) - Grid auto columns size. Supports dynamic data and variables.

- **Grid auto rows** (text) - Grid auto rows size. Supports dynamic data and variables.

- **Grid auto flow** (select) - Grid auto flow direction. Options: row, column, dense.

- **Justify items** (justify-content) - Grid justify items alignment.

- **Align items** (align-items) - Grid align items alignment.

- **Justify content** (justify-content) - Grid justify content alignment.

- **Align content** (align-items) - Grid align content alignment.

### Flex Layout (when Display is flex)

- **Flex wrap** (select) - Flexbox wrapping behavior. Options: No wrap, Wrap, Wrap reverse.

- **Direction** (direction) - Flexbox direction (row/column). Controls `flex-direction` property.

- **Align self** (align-items) - Align self for this flex item. Controls `align-self` property with `!important`.

- **Align main axis** (justify-content) - Justify content alignment. Controls `justify-content` property.

- **Align cross axis** (align-items) - Align items alignment. Controls `align-items` property.

- **Column gap** (number with units) - Gap between flex columns. Controls `column-gap` property.

- **Row gap** (number with units) - Gap between flex rows. Controls `row-gap` property.

- **Flex grow** (number) - Flex grow factor. Minimum: 0. Controls `flex-grow` property. Default placeholder: 0.

- **Flex shrink** (number) - Flex shrink factor. Minimum: 0. Controls `flex-shrink` property. Default placeholder: 1.

- **Flex basis** (text) - Flex basis value. Supports dynamic data and variables. Controls `flex-basis` property. Default placeholder: auto.

### Order

- **Order** (number) - Flexbox order. Minimum: -999. Controls `order` property. Default placeholder: 0. Available when display is not 'none'.

## Style

These controls can be accessed under the **Style** tab in the element settings.

### Masonry

- **Masonry layout** (checkbox) - Enable masonry layout for child elements.
- **Columns** (number) - Number of masonry columns. Default: 3. Controls `--columns` CSS property.
- **Spacing** (number with units) - Spacing between masonry items. Default: 10px. Controls `--gutter` CSS property.
- **Horizontal order** (checkbox) - Enable horizontal ordering in masonry layout.
- **Transition: Duration** (number with units) - Animation duration for masonry transitions. Default: 0.4s. Set to "0" to disable default animations.
- **Reveal animation** (select) - Animation type for masonry items. Options: Scale, Fade, Slide from left, Slide from right, Skew. Default: Scale. Only applies to new items added to the DOM.

## Theme Style: Element – Block

You can change the following Block default settings in your theme styles under "Element – Block":

- `width`
- `min-width`
- `max-width`
- `margin`
- `padding`

## Background lazy loading

From Bricks 2.5, enable **Style > Background > Disable lazy load** to load this element's background images and videos without waiting for them to become visible. The checkbox is hidden when lazy loading is already disabled globally or for the page.

See [Lazy Loading](https://academy.bricksbuilder.io/builder/features/lazy-loading/) for setup steps and how this differs from the Image and Logo elements' Loading controls.

> **Developer reference**
>
> See the [Block Schema](https://academy.bricksbuilder.io/developer/schema/elements/block/) for the full JSON schema of this element's settings and controls.

---

# Container

Source: https://academy.bricksbuilder.io/builder/elements/layout/container/

*The Container element used to be the only layout element in Bricks until version 1.5. It has now been extended by the Section, Block, and Div element to provide.*

The Container element used to be the only layout element in Bricks until version 1.5. It has now been extended by the Section, Block, and Div element to provide a more maintainable & streamlined layout creation process.

The [Understanding the Layout](https://academy.bricksbuilder.io/builder/styling/layout/) article covers in more detail how to best use the layout elements in Bricks.

## How To Use The Container

The Container has a default width of 1100px, is centered, and uses the **flexbox** layout model. This provides various settings to easily direct, align, and space out the elements inside a Container.

We recommend using the Container at the root level or inside a Section.

When editing the Container, you can click the "column" layout icon on the canvas to quickly insert a pre-designed column-based layout:

![](https://academy.bricksbuilder.io/assets/bricks-insert-layout-tool-1024x293.jpg)

Let's explore the container capabilities and go over a few container layout examples in the video below:

https://www.youtube.com/watch?v=_dhKJdNNxLI

## Convert your pre-1.2 Bricks layout to Containers

If you've built your site prior to version 1.2 using the "old" section, row, and column layout, you first need to convert your data to the new container layout.

Bricks comes with a built-in **container migrator** that migrates your existing Bricks data to the new container layout with one-click. So you don't have to re-create your entire site from scratch.

As the new container layout is fully flexible and does NOT have a pre-defined concept of "sections", "rows" or "columns" you most likely have to make some manual adjustments after running the migrator.

After updating to Bricks 1.2 your old data will still be rendered on the frontend, but it's not a 100% accurate representation of your existing section layout.

Once you've updated to Bricks 1.2+, please convert your existing Bricks data as soon as possible as outlined in the step-by-step migration guide below.  
  
We highly recommend migrating your pages one by one, to ensure you don't miss reviewing any of your migrated pages.  
  
As an extra precaution, you can also clone your existing site or editing it on a staging server first, and perform the migration there (rather than on any live site).  
  
**The migrator does NOT delete any of your existing (section) Bricks data. If you feel Bricks 1.2 and the migrator are not ready for your site yet, you can always download a previous version of Bricks (like 1.1.3) from your Bricks account to roll back and continue using the section, row, column layout for now.**

https://youtu.be/3MrLHRQssrg

### STEP #1: View your un-migrated data on the post type screen

All un-migrated posts/pages/templates, etc. all marked as such by the "**(not migrated)**" label behind the title. As you can see in the screenshot below, we need to migrate a page named "Blank":

<figure>

![](https://academy.bricksbuilder.io/assets/bricks-container-migrator-step-1.png)

<figcaption>

Page "Blank" needs to be migrated

</figcaption>

</figure>

### STEP #2: Select your page and run the migrator

Now select the page you want to migrate, click on the "Bulk actions" dropdown. Select "Migrate Bricks Data" and click "Apply" to run the migrator:

<figure>

![](https://academy.bricksbuilder.io/assets/bricks-container-migrator-step-2.png)

<figcaption>

Select and apply the "Migrate Bricks Data" bulk action

</figcaption>

</figure>

### STEP #3: Review the migration result

To inspect the results of the one-click migrator, edit your migrated page with Bricks, and perform any necessary adjustments inside the builder. Then preview your changes on the frontend as well, to ensure your layout matches your expectations.

### Migration tips:

- Restore the default section margin-bottom of 30px under: Theme Styles > General > Root Container Margin
- Restore the default element margin-bottom of 15px under: Theme Styles > General > Element Margin

![](https://academy.bricksbuilder.io/assets/bricks-container-migrator-tips-1024x429.png)

## Settings

- **Grid column** (text) - CSS grid column span when parent uses grid layout. Controls `grid-column` property.

- **Grid row** (text) - CSS grid row span when parent uses grid layout. Controls `grid-row` property.

- **Query loop** - Enable query loop functionality for dynamic content. Available for Container, Block, Div, and Section elements.

- **Link** (link) - Link settings when using anchor tag. Required when HTML tag is set to 'a'.

- **HTML tag** (select) - HTML tag for the container element. Options: div, section, a [Link], article, nav, ol, ul, li, aside, address, figure, custom. Default: div.

- **Custom tag** (text) - Custom HTML tag when "custom" is selected. Without attributes. Required when HTML tag is 'custom'.

- **Display** (select) - CSS display property. Options: flex, grid, block, inline-block, inline, none. Default: flex.

### Grid Layout (when Display is grid)

- **Gap** (number with units) - Gap between grid items. Controls `grid-gap` property.

- **Grid template columns** (text) - CSS grid template columns. Supports dynamic data and variables.

- **Grid template rows** (text) - CSS grid template rows. Supports dynamic data and variables.

- **Grid auto columns** (text) - Grid auto columns size. Supports dynamic data and variables.

- **Grid auto rows** (text) - Grid auto rows size. Supports dynamic data and variables.

- **Grid auto flow** (select) - Grid auto flow direction. Options: row, column, dense.

- **Justify items** (justify-content) - Grid justify items alignment.

- **Align items** (align-items) - Grid align items alignment.

- **Justify content** (justify-content) - Grid justify content alignment.

- **Align content** (align-items) - Grid align content alignment.

### Flex Layout (when Display is flex)

- **Flex wrap** (select) - Flexbox wrapping behavior. Options: No wrap, Wrap, Wrap reverse.

- **Direction** (direction) - Flexbox direction (row/column). Controls `flex-direction` property.

- **Align self** (align-items) - Align self for this flex item. Controls `align-self` property with `!important`.

- **Align main axis** (justify-content) - Justify content alignment. Controls `justify-content` property.

- **Align cross axis** (align-items) - Align items alignment. Controls `align-items` property.

- **Column gap** (number with units) - Gap between flex columns. Controls `column-gap` property.

- **Row gap** (number with units) - Gap between flex rows. Controls `row-gap` property.

- **Flex grow** (number) - Flex grow factor. Minimum: 0. Controls `flex-grow` property. Default placeholder: 0.

- **Flex shrink** (number) - Flex shrink factor. Minimum: 0. Controls `flex-shrink` property. Default placeholder: 1.

- **Flex basis** (text) - Flex basis value. Supports dynamic data and variables. Controls `flex-basis` property. Default placeholder: auto.

### Order

- **Order** (number) - Flexbox order. Minimum: -999. Controls `order` property. Default placeholder: 0. Available when display is not 'none'.

## Style

These controls can be accessed under the **Style** tab in the element settings.

### Masonry

- **Masonry layout** (checkbox) - Enable masonry layout for child elements.
- **Columns** (number) - Number of masonry columns. Default: 3. Controls `--columns` CSS property.
- **Spacing** (number with units) - Spacing between masonry items. Default: 10px. Controls `--gutter` CSS property.
- **Horizontal order** (checkbox) - Enable horizontal ordering in masonry layout.
- **Transition: Duration** (number with units) - Animation duration for masonry transitions. Default: 0.4s. Set to "0" to disable default animations.
- **Reveal animation** (select) - Animation type for masonry items. Options: Scale, Fade, Slide from left, Slide from right, Skew. Default: Scale. Only applies to new items added to the DOM.

## Background lazy loading

From Bricks 2.5, enable **Style > Background > Disable lazy load** to load this element's background images and videos without waiting for them to become visible. The checkbox is hidden when lazy loading is already disabled globally or for the page.

See [Lazy Loading](https://academy.bricksbuilder.io/builder/features/lazy-loading/) for setup steps and how this differs from the Image and Logo elements' Loading controls.

> **Developer reference**
>
> See the [Container Schema](https://academy.bricksbuilder.io/developer/schema/elements/container/) for the full JSON schema of this element's settings and controls.

---

# Div

Source: https://academy.bricksbuilder.io/builder/elements/layout/div/

*The Div element is one of the four layout elements in Bricks (1.5+).*

The Div element is one of the four [layout elements](https://academy.bricksbuilder.io/builder/styling/layout/) in Bricks (1.5+).

Introduced together with the Section & Block element, it allows you to create flexible layouts in record time. The Div element in Bricks is a plain, unstyled div. It's the most generic element to group and lay out your content.

While you use the **Container** to "contain" other elements inside a preset width of 1100px, and the **Block** element with a 100% width, the **Div** element has no presets at all.

This makes it perfect to use inside other layout elements as it grows & shrinks according to its content, or to build Div-only class-based layouts. Use the Div element for grouping content, creating custom layouts, or when you need complete control over styling without any predefined properties.

**Tip:** The Div element's HTML tag setting allows you to transform it into any semantic HTML element (article, nav, ul, li, a (link), etc.) while keeping all the powerful layout and styling controls. This flexibility makes it a versatile building block that can adapt to different content structures and semantic requirements.

## Settings

- **Grid column** (text) - CSS grid column span when parent uses grid layout. Controls `grid-column` property.

- **Grid row** (text) - CSS grid row span when parent uses grid layout. Controls `grid-row` property.

- **Query loop** - Enable query loop functionality for dynamic content. Available for Container, Block, Div, and Section elements.

- **Link** (link) - Link settings when using anchor tag. Required when HTML tag is set to 'a'.

- **HTML tag** (select) - HTML tag for the div element. Options: div, section, a [Link], article, nav, ol, ul, li, aside, address, figure, custom. Default: div.

- **Custom tag** (text) - Custom HTML tag when "custom" is selected. Without attributes. Required when HTML tag is 'custom'.

- **Display** (select) - CSS display property. Options: flex, grid, block, inline-block, inline, none. Default: block.

### Grid Layout (when Display is grid)

- **Gap** (number with units) - Gap between grid items. Controls `grid-gap` property.

- **Grid template columns** (text) - CSS grid template columns. Supports dynamic data and variables.

- **Grid template rows** (text) - CSS grid template rows. Supports dynamic data and variables.

- **Grid auto columns** (text) - Grid auto columns size. Supports dynamic data and variables.

- **Grid auto rows** (text) - Grid auto rows size. Supports dynamic data and variables.

- **Grid auto flow** (select) - Grid auto flow direction. Options: row, column, dense.

- **Justify items** (justify-content) - Grid justify items alignment.

- **Align items** (align-items) - Grid align items alignment.

- **Justify content** (justify-content) - Grid justify content alignment.

- **Align content** (align-items) - Grid align content alignment.

### Flex Layout (when Display is flex)

- **Flex wrap** (select) - Flexbox wrapping behavior. Options: No wrap, Wrap, Wrap reverse.

- **Direction** (direction) - Flexbox direction (row/column). Controls `flex-direction` property.

- **Align self** (align-items) - Align self for this flex item. Controls `align-self` property with `!important`.

- **Align main axis** (justify-content) - Justify content alignment. Controls `justify-content` property.

- **Align cross axis** (align-items) - Align items alignment. Controls `align-items` property.

- **Column gap** (number with units) - Gap between flex columns. Controls `column-gap` property.

- **Row gap** (number with units) - Gap between flex rows. Controls `row-gap` property.

- **Flex grow** (number) - Flex grow factor. Minimum: 0. Controls `flex-grow` property. Default placeholder: 0.

- **Flex shrink** (number) - Flex shrink factor. Minimum: 0. Controls `flex-shrink` property. Default placeholder: 1.

- **Flex basis** (text) - Flex basis value. Supports dynamic data and variables. Controls `flex-basis` property. Default placeholder: auto.

### Order

- **Order** (number) - Flexbox order. Minimum: -999. Controls `order` property. Default placeholder: 0. Available when display is not 'none'.

## Style

These controls can be accessed under the **Style** tab in the element settings.

### Masonry

- **Masonry layout** (checkbox) - Enable masonry layout for child elements.
- **Columns** (number) - Number of masonry columns. Default: 3. Controls `--columns` CSS property.
- **Spacing** (number with units) - Spacing between masonry items. Default: 10px. Controls `--gutter` CSS property.
- **Horizontal order** (checkbox) - Enable horizontal ordering in masonry layout.
- **Transition: Duration** (number with units) - Animation duration for masonry transitions. Default: 0.4s. Set to "0" to disable default animations.
- **Reveal animation** (select) - Animation type for masonry items. Options: Scale, Fade, Slide from left, Slide from right, Skew. Default: Scale. Only applies to new items added to the DOM.

## Theme Style: Element – Div

You can change the defaults of the Div element in your theme styles under "Element – Div":

- `display`
- `flex-direction` (if display set to "flex")
- `justify-content` (if display set to "flex")
- `align-items` (if display set to "flex")
- `width`
- `min-width`
- `max-width`
- `margin`
- `padding`

## Background lazy loading

From Bricks 2.5, enable **Style > Background > Disable lazy load** to load this element's background images and videos without waiting for them to become visible. The checkbox is hidden when lazy loading is already disabled globally or for the page.

See [Lazy Loading](https://academy.bricksbuilder.io/builder/features/lazy-loading/) for setup steps and how this differs from the Image and Logo elements' Loading controls.

> **Developer reference**
>
> See the [Div Schema](https://academy.bricksbuilder.io/developer/schema/elements/div/) for the full JSON schema of this element's settings and controls.

---

# Divider

Source: https://academy.bricksbuilder.io/builder/elements/layout/divider/

*The Divider element creates horizontal or vertical separator lines with optional icons.*

The Divider element creates horizontal or vertical separator lines with optional icons.

## Settings

- **Height** (number with units) - The height/thickness of the divider line. Default: 1.

- **Width** (number with units) - The width/length of the divider line.

- **Style** (select) - The line style. Options: `solid`, `dashed`, `dotted`, `double`, `groove`, `ridge`, `inset`, `outset`. Default: `solid`.

- **Direction** (select) - Orientation of the divider. Options: `horizontal`, `vertical`. Default: `horizontal`.

- **Align** (justify-content) - Alignment of the divider within its container. Options: `flex-start`, `center`, `flex-end`.

- **Color** (color) - Color of the divider line and icon.

### Icon

- **Icon** (icon) - Add an icon that appears on the divider line.

- **Typography** (typography) - Style settings for the icon (size, font properties). Only available when an icon is selected.

> **Developer reference**
>
> See the [Divider Schema](https://academy.bricksbuilder.io/developer/schema/elements/divider/) for the full JSON schema of this element's settings and controls.

---

# List

Source: https://academy.bricksbuilder.io/builder/elements/layout/list/

*The List element creates customizable lists with icons, titles, meta information, descriptions, and optional highlight labels.*

The List element creates customizable lists with icons, titles, meta information, descriptions, and optional highlight labels.

## Settings

### List Items

- **List items** (repeater) - Add and configure list items. Each item has:
  - **Icon** (icon) - Optional icon for the list item
  - **Title** (text) - Main title text
  - **Link title** (link) - Make the title clickable
  - **Meta** (text) - Additional meta information (e.g., price, date)
  - **Description** (textarea) - Longer description text
  - **Highlight** (checkbox) - Mark this item as highlighted
  - **Highlight label** (text) - Custom label text for highlighted items. Only available when highlight is enabled.

### List Item

- **Justify content** (justify-content) - Horizontal alignment of list item content. Controls `justify-content` property for `.content` and `.description` selectors.

- **Align items** (align-items) - Vertical alignment of list item content. Options: `flex-start`, `center`, `flex-end`, `baseline`. Controls `align-items` property for `.content` and `.description` selectors. Excludes `stretch` option.

- **Margin** (spacing) - Margin around each list item. Controls `margin` property for `li` selector.

- **Padding** (spacing) - Padding inside each list item. Controls `padding` property for `li` selector.

- **Odd background** (color) - Background color for odd-numbered list items. Controls `background-color` property for `li:nth-child(odd)` selector.

- **Even background** (color) - Background color for even-numbered list items. Controls `background-color` property for `li:nth-child(even)` selector.

- **Border** (border) - Border styling for list items. Controls `border` property for `li` selector.

- **Auto width** (checkbox) - Enable automatic width for list items. Sets `justify-content` to `initial` for `.content` selector and `flex-grow` to `0` for `.separator` selector.

### Highlight

- **Block** (checkbox) - Display highlight label as block element. Controls `display` property for `li[data-highlight]::before` selector.

- **Padding** (spacing) - Padding for highlight label. Controls `padding` property for `li[data-highlight]::before` selector.

- **Background** (color) - Background color for highlight label. Controls `background-color` property for `li[data-highlight]::before` selector.

- **Border** (border) - Border styling for highlight label. Controls `border` property for `li[data-highlight]::before` selector.

- **Typography** (typography) - Typography settings for highlight label. Controls `font` property for `li[data-highlight]::before` selector.

- **Content** (separator) - Visual separator in the control panel.

- **Padding** (spacing) - Padding for highlighted item content. Controls `padding` property for `li[data-highlight] .content` selector.

- **Background** (color) - Background color for highlighted item content. Controls `background-color` property for `li[data-highlight] .content` selector.

- **Border** (border) - Border styling for highlighted item content. Controls `border` property for `li[data-highlight] .content` selector.

- **Text color** (color) - Text color for highlighted item content. Controls `color` property for `li[data-highlight] .content .title`, `li[data-highlight] .content .meta`, and `li[data-highlight] .content .description` selectors.

### Icon

- **Icon** (icon) - Default icon for all list items.

- **After title** (checkbox) - Position icon after the title instead of before.

- **Width** (number with units) - Width of the icon. Controls `width` property for `.icon` selector.

- **Height** (number with units) - Height of the icon. Controls `height` property for `.icon` selector.

- **Size** (number with units) - Font size of the icon. Controls `font-size` property for `.icon` selector, and `height`/`width` properties for `.icon svg` selector.

- **Color** (color) - Color of the icon. Controls `color` property for `.icon` selector.

- **Background color** (color) - Background color of the icon. Controls `background-color` property for `.icon` selector.

- **Border** (border) - Border styling for the icon. Controls `border` property for `.icon` selector.

- **Box shadow** (box-shadow) - Box shadow for the icon. Controls `box-shadow` property for `.icon` selector.

### Title

- **Margin** (spacing) - Margin around the title. Controls `margin` property for `.title` selector.

- **HTML tag** (text) - HTML tag for the title. Supports dynamic data. Default placeholder: `span`. Validates HTML tag format.

- **Typography** (typography) - Typography settings for the title. Controls `font` property for `.title` selector.

### Meta

- **Margin** (spacing) - Margin around the meta text. Controls `margin` property for `.meta` selector.

- **Typography** (typography) - Typography settings for the meta text. Controls `font` property for `.meta` selector.

### Description

- **Typography** (typography) - Typography settings for the description. Controls `font` property for `.description` selector.

### Separator

- **Disable** (checkbox) - Disable the separator line between items. Controls `display` property for `.separator` selector (sets to `none`). Triggers re-render.

- **Style** (select) - Border style for the separator. Options from border style control options. Controls `border-top-style` property for `.separator` selector. Only available when separator is not disabled.

- **Width** (number with units) - Width of the separator. Controls `flex-basis` property for `.separator` selector and sets `flex-grow` to `0`. Only available when separator is not disabled.

- **Height** (number with units) - Height/thickness of the separator. Controls `border-top-width` property for `.separator` selector. Only available when separator is not disabled.

- **Color** (color) - Color of the separator. Controls `border-top-color` property for `.separator` selector. Only available when separator is not disabled.

> **Developer reference**
>
> See the [List Schema](https://academy.bricksbuilder.io/developer/schema/elements/list/) for the full JSON schema of this element's settings and controls.

---

# Section

Source: https://academy.bricksbuilder.io/builder/elements/layout/section/

*The Section element allows you to structure/divide your page into self-containing areas (think: one topic per section).*

The Section element allows you to structure/divide your page into self-containing areas (think: one topic per section).

The [Understanding the Layout](https://academy.bricksbuilder.io/builder/styling/layout/) article covers in more detail how to best use the layout elements in Bricks.

The Section element is the outermost building block for structuring and dividing your page. Use sections to separate and space out individual parts of your page, such as hero sections, content areas, or footers.

The Section element has a default width of 100%, uses the `section` tag, and flexbox. Sections take up 100% of the available width and adjust in height according to their content. They are stacked vertically on top of each other.

It should be used at the root level to structure your page into self-containing areas. When adding a Section to the canvas, a Container element is added inside of the Section automatically. You can delete this Container if not needed. It's just the default behaviour to speed up your site creation process.

<figure>

![](https://academy.bricksbuilder.io/assets/bricks-1.5-section-element-1024x484.jpg)

<figcaption>

Example: Section > Container > Heading

</figcaption>

</figure>

**Tip:** Use sections as the root level elements in your page structure. They work great for creating distinct page sections with different backgrounds, spacing, and layouts.

## Settings

- **Grid column** (text) - CSS grid column span when parent uses grid layout. Controls `grid-column` property.

- **Grid row** (text) - CSS grid row span when parent uses grid layout. Controls `grid-row` property.

- **Query loop** - Enable query loop functionality for dynamic content. Available for Container, Block, Div, and Section elements.

- **Link** (link) - Link settings when using anchor tag. Required when HTML tag is set to 'a'.

- **HTML tag** (select) - HTML tag for the section element. Options: div, section, a [Link], article, nav, ol, ul, li, aside, address, figure, custom. Default: section.

- **Custom tag** (text) - Custom HTML tag when "custom" is selected. Without attributes. Required when HTML tag is 'custom'.

- **Display** (select) - CSS display property. Options: flex, grid, block, inline-block, inline, none. Default: flex.

### Grid Layout (when Display is grid)

- **Gap** (number with units) - Gap between grid items. Controls `grid-gap` property.

- **Grid template columns** (text) - CSS grid template columns. Supports dynamic data and variables.

- **Grid template rows** (text) - CSS grid template rows. Supports dynamic data and variables.

- **Grid auto columns** (text) - Grid auto columns size. Supports dynamic data and variables.

- **Grid auto rows** (text) - Grid auto rows size. Supports dynamic data and variables.

- **Grid auto flow** (select) - Grid auto flow direction. Options: row, column, dense.

- **Justify items** (justify-content) - Grid justify items alignment.

- **Align items** (align-items) - Grid align items alignment.

- **Justify content** (justify-content) - Grid justify content alignment.

- **Align content** (align-items) - Grid align content alignment.

### Flex Layout (when Display is flex)

- **Flex wrap** (select) - Flexbox wrapping behavior. Options: No wrap, Wrap, Wrap reverse.

- **Direction** (direction) - Flexbox direction (row/column). Controls `flex-direction` property.

- **Align self** (align-items) - Align self for this flex item. Controls `align-self` property with `!important`.

- **Align main axis** (justify-content) - Justify content alignment. Controls `justify-content` property.

- **Align cross axis** (align-items) - Align items alignment. Controls `align-items` property.

- **Column gap** (number with units) - Gap between flex columns. Controls `column-gap` property.

- **Row gap** (number with units) - Gap between flex rows. Controls `row-gap` property.

- **Flex grow** (number) - Flex grow factor. Minimum: 0. Controls `flex-grow` property. Default placeholder: 0.

- **Flex shrink** (number) - Flex shrink factor. Minimum: 0. Controls `flex-shrink` property. Default placeholder: 1.

- **Flex basis** (text) - Flex basis value. Supports dynamic data and variables. Controls `flex-basis` property. Default placeholder: auto.

### Order

- **Order** (number) - Flexbox order. Minimum: -999. Controls `order` property. Default placeholder: 0. Available when display is not 'none'.

### Style

These controls can be accessed under the **Style** tab in the element settings.

### Masonry

- **Masonry layout** (checkbox) - Enable masonry layout for child elements.
- **Columns** (number) - Number of masonry columns. Default: 3. Controls `--columns` CSS property.
- **Spacing** (number with units) - Spacing between masonry items. Default: 10px. Controls `--gutter` CSS property.
- **Horizontal order** (checkbox) - Enable horizontal ordering in masonry layout.
- **Transition: Duration** (number with units) - Animation duration for masonry transitions. Default: 0.4s. Set to "0" to disable default animations.
- **Reveal animation** (select) - Animation type for masonry items. Options: Scale, Fade, Slide from left, Slide from right, Skew. Default: Scale. Only applies to new items added to the DOM.

## Theme Style: Element – Section

You can change the section `width`, `min-width`, `max-width`, `margin`, and `padding` in your theme styles under the "Elements > Section" group.

## Background lazy loading

From Bricks 2.5, enable **Style > Background > Disable lazy load** to load this element's background images and videos without waiting for them to become visible. The checkbox is hidden when lazy loading is already disabled globally or for the page.

See [Lazy Loading](https://academy.bricksbuilder.io/builder/features/lazy-loading/) for setup steps and how this differs from the Image and Logo elements' Loading controls.

> **Developer reference**
>
> See the [Section Schema](https://academy.bricksbuilder.io/developer/schema/elements/section/) for the full JSON schema of this element's settings and controls.

---

# Author

Source: https://academy.bricksbuilder.io/builder/elements/single/author/

*Display the current post author in Bricks, including avatar, name, bio, and optional links to the author archive or website.*

Displays information about the post author.

## Settings

### Avatar
- **Show avatar** (checkbox) - Display author avatar. Default: true.
- **Avatar size** (number) - Avatar dimensions. Default: 60px.
- **Avatar position** (select) - Avatar placement. Options: Top, Right, Bottom, Left. Default: Left.
- **Avatar border** (border) - Avatar border settings.
- **Avatar box shadow** (box-shadow) - Avatar shadow settings.

### Name
- **Show name** (checkbox) - Display author name. Default: true.
- **Link to website** (checkbox) - Make name link to author website. Default: true.
- **Typography** (typography) - Name typography.
- **HTML tag** (text) - HTML tag for name. Default: h2.

### Bio
- **Show bio** (checkbox) - Display author biography. Default: true.
- **Typography** (typography) - Bio typography.

### Posts
- **Show link to author posts** (checkbox) - Display button linking to all author posts. Default: true.
- **Padding** (spacing) - Button padding.
- **Text** (text) - Button text. Default: "All author posts".
- **Size** (select) - Button size.
- **Style** (select) - Button style. Default: primary.
- **Background** (color) - Button background color.
- **Border** (border) - Button border.
- **Typography** (typography) - Button typography.

> **Developer reference**
>
> See the [Author Schema](https://academy.bricksbuilder.io/developer/schema/elements/post-author/) for the full JSON schema of this element's settings and controls.

---

# Comments

Source: https://academy.bricksbuilder.io/builder/elements/single/comments/

*The Comments element displays post comments and comment form. It offers two display modes: custom styling with full control over appearance, or default.*

The Comments element displays post comments and comment form. It offers two display modes: custom styling with full control over appearance, or default WordPress styling.

## Settings

### Source

- **Source** (select) - Choose comment display mode. Options: Bricks (custom styling), WordPress (WordPress default styling). Default: Bricks.

### Custom styling controls

When **Source** is set to "Bricks", the following controls are available for customizing the comment display and form:

#### Title

- **Show title** (checkbox) - Display comments section title. Default: true.

- **HTML tag** (select) - HTML tag for title. Options: div, h1-h6. Default: h3. Only available when Show title is enabled.

- **Typography** (typography) - Title typography. Controls `font` property for `.comments-title` selector. Only available when Show title is enabled.

#### Avatar

- **Show avatar** (checkbox) - Display commenter avatars. Default: true.

- **Size** (number with units) - Avatar dimensions. Default: 60px. Triggers re-render.

- **Border** (border) - Avatar border settings. Controls `border` property for `.avatar` selector.

- **Box shadow** (box-shadow) - Avatar shadow settings. Controls `box-shadow` property for `.avatar` selector.

#### Comment

- **Author: HTML tag** (select) - HTML tag for commenter names. Options: div, h1-h6. Default: h5. Triggers re-render.

- **Author: Typography** (typography) - Commenter name typography. Controls `font` property for `.comment-author .fn` selector.

- **Meta: Typography** (typography) - Comment meta typography. Controls `font` property for `.comment-meta` selector.

- **Content: Typography** (typography) - Comment content typography. Controls `font` property for `.comment-content` selector.

#### Form

##### Form title

- **Show** (checkbox) - Display comment form title. Default: true.

- **HTML tag** (select) - HTML tag for form title. Options: div, h1-h6. Default: h4. Triggers re-render. Only available when Show is enabled.

- **Text** (text) - Form title text. Default placeholder: "Leave your comment". Only available when Show is enabled.

##### Label

- **Show** (checkbox) - Display form field labels. Default: true.

- **Typography** (typography) - Label typography. Controls `font` property for `label` selector. Only available when Show is enabled.

- **Placeholder typography** (typography) - Placeholder text typography. Controls `font` property for `::placeholder` selector. Only available when Show is enabled.

##### Cookie consent

- **Show** (checkbox) - Display cookie consent checkbox.

- **Required** (checkbox) - Make cookie consent required. Only available when Show is enabled.

- **Text** (text) - Cookie consent text. Only available when Show is enabled.

##### Fields

- **Fields** (select, multiple) - Form fields to display. Options: Name, Email, Website. Default: Name, Email, Website.

##### Field styling

- **Background color** (color) - Form field background color. Controls `background-color` property for `.form-group input` and `.form-group textarea` selectors.

- **Border** (border) - Form field border settings. Controls `border` property for `.form-group input` and `.form-group textarea` selectors.

- **Typography** (typography) - Form field typography. Controls `font` property for `.form-group input` and `.form-group textarea` selectors.

- **Textarea: Resize** (select) - Textarea resize behavior. Options: None, Vertical, Horizontal, Both. Default: Vertical. Controls `resize` property for `.form-group textarea` selector.

#### Submit button

- **Text** (text) - Submit button text. Default placeholder: "Submit Comment". Supports dynamic data.

- **Size** (select) - Button size. Options from button sizes control options. Default placeholder: "Default".

- **Style** (select) - Button style. Options from styles control options. Default: primary.

- **Background** (color) - Button background color. Controls `background-color` property for `.bricks-button` selector.

- **Border** (border) - Button border settings. Controls `border` property for `.bricks-button` selector.

- **Typography** (typography) - Button typography. Controls `font` property for `.bricks-button` selector.

### WordPress default styling

When **Source** is set to "WordPress", the element uses your theme's default comment styling and form layout. No additional styling controls are available - WordPress handles all comment display through the standard `comments_template()` function.

> **Developer reference**
>
> See the [Comments Schema](https://academy.bricksbuilder.io/developer/schema/elements/post-comments/) for the full JSON schema of this element's settings and controls.

---

# Excerpt

Source: https://academy.bricksbuilder.io/builder/elements/single/excerpt/

*Displays the excerpt of the current post or page.*

Displays the excerpt of the current post or page.

## Settings

- **Excerpt length** (number) - Number of words to display. Default: 15.
- **More text** (text) - Text to append when excerpt is truncated. Default: "...".
- **Keep formatting** (checkbox) - Preserve HTML formatting in the excerpt.

> **Developer reference**
>
> See the [Excerpt Schema](https://academy.bricksbuilder.io/developer/schema/elements/post-excerpt/) for the full JSON schema of this element's settings and controls.

---

# Meta data

Source: https://academy.bricksbuilder.io/builder/elements/single/meta-data/

*Displays post meta information like author, date, comments, etc.*

Displays post meta information like author, date, comments, etc.

## Settings

- **Meta** (repeater) - Dynamic data fields to display. Default includes: `{author_name}`, `{post_date}`, `{post_comments}`.
- **Direction** (direction) - Flex direction for meta items layout.
- **Gap** (number) - Spacing between meta items. Default: 20px.
- **Separator** (text) - Text to display between meta items.
- **Separator color** (color) - Color of the separator text.

> **Developer reference**
>
> See the [Meta Data Schema](https://academy.bricksbuilder.io/developer/schema/elements/post-meta/) for the full JSON schema of this element's settings and controls.

---

# Post content

Source: https://academy.bricksbuilder.io/builder/elements/single/post-content/

*The Post Content element is a placeholder in the builder that tells Bricks to fetch the post content into the layout you're building.*

The **Post Content** element is a placeholder in the builder that tells Bricks to fetch the post content into the layout you're building.

Since Bricks 1.3.5 you can select the source from which to pull the content:

- WordPress Editor (Gutenberg/Classic editor)
- Bricks Data

The **Data Source** control is only visible when the Post Content element is used in Bricks templates.

If the **Post Content** element is placed in a Page/Post, etc. the WordPress content is fetched by default.

## How to use the Post Content element

Inside the builder, go to the Elements panel and look for the **Post Content** element in the Single elements group or use the element search bar in the panel header. Click or drag the Post Content element onto the canvas.

![](https://academy.bricksbuilder.io/assets/post-content-element.png)

If the element is inserted when editing a post or page, it will automatically show the WordPress editor content on the canvas unless there is no Page/Post content. That content is also shown on the front end.

This is useful when creating a **Single Post template** in which you want to show the WordPress content (e.g. a single blog post).

## Lightbox for Gutenberg images

Since Bricks 2.5, the **Lightbox** setting opens media-linked Gutenberg images in the Bricks lightbox. It is off by default and available when the Post Content element uses WordPress as its data source.

1. In the WordPress block editor, link the images in your Image or Gallery blocks to **Media file**.
2. In Bricks, select the **Post Content** element. If you are editing a template, set **Data source** to **WordPress**.
3. Enable **Lightbox** in the element's **Content** tab, save, and check the images on the frontend.

<div className="screenshot screenshot--control-panel">

![Post Content settings with Lightbox enabled for media-linked Gutenberg images.](https://academy.bricksbuilder.io/assets/post-content-lightbox.webp)

</div>

Images within each Gallery block are grouped together so visitors can navigate between them. Separate galleries stay in separate groups, and standalone Image blocks open individually.

The image must come from the WordPress Media Library and link to its full-size media file URL. Custom links, attachment-page links, and images without valid attachment dimensions keep their existing behavior. Unlinked images using WordPress's native **Expand on click** lightbox are unaffected.

This setting changes the rendered output without rewriting your saved Gutenberg blocks. It does not apply when **Data source** is **Bricks**. For more on working with both editors, see [Gutenberg integration](https://academy.bricksbuilder.io/integrations/gutenberg/).

## Fetching Bricks Data with the Post Content element

In certain scenarios, you'd like to edit each post with Bricks instead of using the WordPress editor such as when using more complex layouts that aren't possible with WordPress.

In this case, you need to set the **Data Source** to "Bricks" in the Post Content settings:

![](https://academy.bricksbuilder.io/assets/post-content-data-source.png)

## Creating different page layouts using the Post Content

When using a Bricks template as your page layout this template is rendered on the frontend instead of the individual page created with Bricks.

If you use the **Post Content** element and set the **Data Source** to Bricks, you can design different page templates and still fetch each page content built with Bricks.

A common use case would be to build a page template with two areas: the main area (which is populated with the page content), and a fixed sidebar for all the pages.

To get the Bricks-built content of each page, the Data Source of the Post Content element needs to be set to "Bricks":

<figure>

![](https://academy.bricksbuilder.io/assets/page-template-post-content-element-1024x636.png)

<figcaption>

Bricks Page Template using a Post Content element to fetch page bricks data

</figcaption>

</figure>

## Settings

- **Data source** (select) - Choose content source. Options: WordPress, Bricks. Default: WordPress. The select is only available for templates, since on pages it automatically uses WordPress as the source.
- **Lightbox** (checkbox) - Open media-linked Gutenberg images in the Bricks lightbox. Default: Off. Available for the WordPress data source. Each Gallery block forms its own group.

> **Developer reference**
>
> See the [Post Content Schema](https://academy.bricksbuilder.io/developer/schema/elements/post-content/) for the full JSON schema of this element's settings and controls.

---

# Post reading progress bar

Source: https://academy.bricksbuilder.io/builder/elements/single/post-reading-progress-bar/

*Shows a progress bar indicating how much of the post has been read.*

Shows a progress bar indicating how much of the post has been read.

## Settings

- **Content** (select) - Choose the content to track reading progress for. Options: post_content, post_excerpt, custom_content. Default: post_content.
- **Position** (select) - Position of the progress bar. Options: top, bottom. Default: top.
- **Height** (number) - Height of the progress bar in pixels. Default: 4.
- **Background color** (color) - Background color of the progress bar.
- **Progress color** (color) - Color of the progress indicator.
- **Show percentage** (checkbox) - Display the reading percentage as text.

> **Developer reference**
>
> See the [Reading Progress Bar Schema](https://academy.bricksbuilder.io/developer/schema/elements/post-reading-progress-bar/) for the full JSON schema of this element's settings and controls.

---

# Post navigation

Source: https://academy.bricksbuilder.io/builder/elements/single/post-navigation/

*Displays navigation links to previous and next posts.*

Displays navigation links to previous and next posts.

The element uses WordPress adjacent-post navigation. **Previous** points to the previous post according to WordPress's post-date order, and **Next** points to the next one. This can look reversed when visitors arrive from a posts list sorted by date in descending order.

## Settings

- **Direction** (direction) - Layout direction for navigation items.
- **Max. post width** (number) - Maximum width for post navigation items.
- **In same term** (checkbox) - Navigate within same taxonomy term.
- **Excluded terms** (select) - Terms to exclude from navigation.
- **Taxonomy** (select) - Taxonomy for same term navigation. Default: category.

### Label
- **Show label** (checkbox) - Display navigation labels. Default: true.
- **Prev label** (text) - Label for previous post. Default: "Previous post".
- **Next label** (text) - Label for next post. Default: "Next post".
- **Label typography** (typography) - Typography for navigation labels.

### Title
- **Show title** (checkbox) - Display post titles in navigation. Default: true.
- **Title tag** (text) - HTML tag for post titles. Default: h5.
- **Title typography** (typography) - Typography for post titles.
- **Alignment: Previous post** (justify-content) - Alignment for previous post section.
- **Alignment: Next post** (justify-content) - Alignment for next post section.

### Arrows
- **Prev arrow** (icon) - Icon for previous post navigation.
- **Next arrow** (icon) - Icon for next post navigation.
- **Typography** (typography) - Typography for arrow icons.

You can change the labels and arrows to match the wording used by your design. The element does not include a setting that reverses the underlying adjacent-post lookup. Changing that order requires custom PHP through WordPress's adjacent-post filters, or a custom navigation implementation.

### Image
- **Show image** (checkbox) - Display post featured images. Default: true.
- **Size** (select) - WordPress image size. Default: Thumbnail.
- **Height** (number) - Image height. Default: 60px.
- **Width** (number) - Image width. Default: 60px.
- **Border** (border) - Image border settings.

> **Developer reference**
>
> See the [Post Navigation Schema](https://academy.bricksbuilder.io/developer/schema/elements/post-navigation/) for the full JSON schema of this element's settings and controls.

---

# Post reading time

Source: https://academy.bricksbuilder.io/builder/elements/single/post-reading-time/

*Displays the estimated reading time for a post based on the selected content.*

Displays the estimated reading time for a post based on the selected content.

## Settings

- **Content** (select) - Choose the content to calculate reading time from. Options: post_content, post_excerpt, custom_content. Default: post_content.
- **Prefix** (text) - Text to display before the reading time. Default: "Reading time:".
- **Suffix** (text) - Text to display after the reading time. Default: "min".
- **Words per minute** (number) - Average reading speed in words per minute. Default: 200.
- **Calculation method** (select) - Method to use for calculation. Options: words, characters. Default: words.

> **Developer reference**
>
> See the [Reading Time Schema](https://academy.bricksbuilder.io/developer/schema/elements/post-reading-time/) for the full JSON schema of this element's settings and controls.

---

# Post title

Source: https://academy.bricksbuilder.io/builder/elements/single/post-title/

*Displays the title of the current post or page.*

Displays the title of the current post or page.

## Settings

- **HTML tag** (select) - HTML tag for the title. Options: h1, h2, h3, h4, h5, h6. Default: h1.
- **Type** (select) - Title type. Options: Hero, Lead.
- **Style** (select) - Title style from theme styles.
- **Link to post** (checkbox) - Make the title a link to the post.
- **Add context** (checkbox) - Add context to title on archive/search templates (for template use only).

### Prefix
- **Prefix** (text) - Text to display before the title.
- **Spacing** (number) - Spacing between prefix and title.
- **Block** (checkbox) - Display prefix as block element.
- **Typography** (typography) - Typography settings for prefix text.

### Suffix
- **Suffix** (text) - Text to display after the title.
- **Spacing** (number) - Spacing between title and suffix.
- **Block** (checkbox) - Display suffix as block element.
- **Typography** (typography) - Typography settings for suffix text.

> **Developer reference**
>
> See the [Post Title Schema](https://academy.bricksbuilder.io/developer/schema/elements/post-title/) for the full JSON schema of this element's settings and controls.

---

# Post table of contents

Source: https://academy.bricksbuilder.io/builder/elements/single/post-toc/

*Generates a table of contents based on the headings in the post content.*

Generates a table of contents based on the headings in the post content.

## Settings

- **Content** (select) - Choose the content to generate table of contents from. Options: post_content, post_excerpt, custom_content. Default: post_content.
- **Heading selectors** (text) - CSS selectors for headings to include. Default: "h1,h2,h3,h4,h5,h6".
- **List style** (select) - Style for the list items. Options: none, disc, circle, square, decimal, decimal-leading-zero, lower-roman, upper-roman, lower-greek, lower-latin, upper-latin, armenian, georgian, lower-alpha, upper-alpha. Default: none.
- **Item typography** (typography) - Typography settings for list items.
- **Item padding** (dimensions) - Padding for list items.
- **Item background color** (color) - Background color for list items.
- **Item border** (border) - Border settings for list items.
- **Active item typography** (typography) - Typography settings for active list items.
- **Active item background color** (color) - Background color for active list items.
- **Active item border** (border) - Border settings for active list items.

> **Developer reference**
>
> See the [Table Of Contents Schema](https://academy.bricksbuilder.io/developer/schema/elements/post-toc/) for the full JSON schema of this element's settings and controls.

---

# Related posts

Source: https://academy.bricksbuilder.io/builder/elements/single/related-posts/

*Displays posts related to the current post based on shared taxonomies.*

Displays posts related to the current post based on shared taxonomies.

## Settings

### Title
- **Title** (text) - Section title text.
- **HTML tag** (select) - HTML tag for title. Options: h2, h3, h4, h5, h6. Default: h2.
- **Margin** (spacing) - Title margin.
- **Typography** (typography) - Title typography.

### Query
- **Post type** (select) - Post type to query.
- **Max. related posts** (number) - Maximum number of related posts. Default: 3.
- **Order** (select) - Sort order. Default: Descending.
- **Order by** (select) - Sort criteria. Default: Random.
- **Common taxonomies** (select) - Taxonomies posts must share. Default: category, post_tag.

### Layout
- **Gap** (number) - Spacing between posts. Default: 30px.
- **Posts per row** (number) - Number of posts per row. Default: 3.

### Fields
- **Content** (repeater) - Dynamic data fields to display. Default includes: `{post_title:link}`, `{post_date}`, `{post_excerpt:20}`.
  - **Dynamic data** (text) - Dynamic data expression.
  - **HTML tag** (select) - HTML tag for field. Default: div.
  - **Margin** (spacing) - Field margin.
  - **Padding** (spacing) - Field padding.
  - **Background color** (color) - Field background color.
  - **Border** (border) - Field border.
  - **Typography** (typography) - Field typography.

### Image
- **Disable** (checkbox) - Hide post images.
- **Aspect ratio** (text) - Image aspect ratio.
- **Image size** (select) - WordPress image size.
- **Position** (select) - Image position. Options: Top, Right, Bottom, Left. Default: Top.
- **Height** (number) - Image height.
- **Width** (number) - Image width.
- **Margin** (spacing) - Image margin.

### Content
- **Width** (number) - Content area width.
- **Padding** (spacing) - Content area padding.
- **Background color** (color) - Content area background color.
- **Overlay content** (checkbox) - Overlay content on image.
- **Horizontal alignment** (align-items) - Content horizontal alignment (overlay mode).
- **Vertical alignment** (justify-content) - Content vertical alignment (overlay mode).

> **Developer reference**
>
> See the [Related Posts Schema](https://academy.bricksbuilder.io/developer/schema/elements/related-posts/) for the full JSON schema of this element's settings and controls.

---

# Social sharing

Source: https://academy.bricksbuilder.io/builder/elements/single/social-sharing/

*Displays social media sharing buttons for the current post.*

Displays social media sharing buttons for the current post.

## Settings

- **Share via** (repeater) - Social media services to include. Default includes: Facebook, X, LinkedIn, WhatsApp, Pinterest, Telegram, VKontakte, Bluesky, Viber (since Bricks 2.5), Email.
  - **Service** (select) - Social media platform.
  - **Excerpt** (checkbox) - Include post excerpt in share (WhatsApp only).
  - **Icon** (icon) - Custom icon for the service.
  - **Background** (color) - Button background color.
  - **Color** (color) - Button text/icon color.
- **Use brand colors** (checkbox) - Apply default brand colors to buttons. Default: true.
- **Direction** (direction) - Layout direction for sharing buttons.
- **Open in new tab** (checkbox) - Open sharing links in new tabs.
- **Rel attribute** (text) - Link rel attribute. Default: "nofollow".

> **Developer reference**
>
> See the [Social Sharing Schema](https://academy.bricksbuilder.io/developer/schema/elements/post-sharing/) for the full JSON schema of this element's settings and controls.
