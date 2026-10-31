# Integration: Adobe Fonts

Source: https://academy.bricksbuilder.io/builder/styling/adobe-fonts/

*Connect Adobe Fonts to Bricks so your project can use synced Typekit fonts inside the builder and on the frontend.*

## How to use Adobe Fonts with Bricks

All you need to do is provide Bricks with your Adobe Fonts "Project ID".

First, visit the "web projects" section inside your Adobe Fonts account: [https://fonts.adobe.com/my_fonts#web_projects-section](https://fonts.adobe.com/my_fonts#web_projects-section)

Each of your web projects contains a unique "Project ID".

Copy the project ID of the web project whose fonts you want to use on your Bricks site.

![](https://academy.bricksbuilder.io/assets/bricks-adobe-fonts-web-project-id.png)

<figcaption>

Copy the project ID into your clipboard

</figcaption>

Next, inside your WordPress dashboard, go to `Bricks > Settings > API keys` and paste the project ID into the "Adobe fonts (Project ID)" input field. Then save your settings.

![](https://academy.bricksbuilder.io/assets/bricks-adobe-fonts-project-id-saved.png)

<figcaption>

Click "Sync fonts" to fetch all fonts of this project

</figcaption>

Next to the project ID input, a "Sync fonts" button should now be visible. Click it to fetch the Adobe fonts of this project. A success message should appear & the "Published Adobe fonts" counter should reflect the number of published fonts.

![](https://academy.bricksbuilder.io/assets/bricks-adobe-fonts-synced.png)

<figcaption>

Fonts are now synced & available in the builder

</figcaption>

Those fonts are now available inside the builder in any `font-family` dropdown:

![](https://academy.bricksbuilder.io/assets/bricks-adobe-fonts-in-bricks.png)

Syncing an Adobe Fonts project only makes its fonts available in Bricks typography controls. To apply and load an Adobe font on the frontend, select it in a typography setting, such as an element, global class, Theme Style, page setting, or template setting.

Bricks loads the Adobe Fonts project CSS only when an Adobe font from the synced project is detected in the generated page CSS.

> **Note**
>
> NOTE: Bricks recognizes when you use an Adobe font that is also available as a Google font. Bricks will load only the Adobe font to prevent loading this font from Google as well.

## Variable fonts {#font-variation-settings}

Bricks also provides a new `font-variation-settings`. This CSS property allows you to control the four-letter axis names of a variable Adobe font. Such as the `wght`, `wdth`, `slnt`, and `ital`.

For more information about the specifics please visit [https://developer.mozilla.org/en-US/docs/Web/CSS/font-variation-settings](https://developer.mozilla.org/en-US/docs/Web/CSS/font-variation-settings)

![](https://academy.bricksbuilder.io/assets/bricks-adobe-fonts-variable-font-variation-settings.png)

<figcaption>

Variable Adobe font with a custom font-weight (axis: "wght") of 535

</figcaption>

You can view available variable Adobe fonts by selecting "Variable Fonts" under "Font technology on [https://fonts.adobe.com/fonts](https://fonts.adobe.com/fonts).

> **Note**
>
> NOTE: This new `font-variation-settings` is also available for [custom fonts](https://academy.bricksbuilder.io/builder/styling/custom-fonts/). For Google Fonts, Bricks can collect multiple variation axes from the selected font and your typography settings; the available axes depend on the font and the Google Fonts API.

---

# Build a Design System in Bricks

Source: https://academy.bricksbuilder.io/builder/styling/build-a-design-system/

*Build a design system in Bricks from an unstyled page: color palette and shades, fluid type and spacing scales, variables, a theme style, classes, and components.*

A design system is a set of decisions you make once and reuse everywhere: your colors, font sizes, spacing, the default look of plain elements, and the patterns and blocks that repeat. In Bricks, those decisions live in the Style Manager, in a theme style, in global classes, and in components. Once they are in place, a new page needs no new styles, and changing one value updates every page that uses it.

This article builds a design system for a small coffee roaster's website, starting from a page with content and no styling. It follows the same steps as the video.

https://youtu.be/lo2L313Cpko

## The four layers

Each layer builds on the one below it:

| Layer | In Bricks | Example |
| --- | --- | --- |
| Values | Colors and variables in the [Style Manager](https://academy.bricksbuilder.io/builder/features/style-manager/) | `var(--brand)`, `var(--heading-xl)`, `var(--space-m)` |
| Rules | A [theme style](https://academy.bricksbuilder.io/builder/styling/theme-styles/) | Body text, headings, buttons, section padding |
| Classes | [Global classes](https://academy.bricksbuilder.io/builder/styling/global-css-classes/) | `.eyebrow` for the small label above a heading |
| Components | [Components](https://academy.bricksbuilder.io/builder/features/components/) | A product card |

A component uses classes, and classes use variables. When a value changes, everything above it follows.

## Starting point

The example starts with a header template, a footer template, and a home page with its content in place. Nothing is styled yet: default fonts, default colors, no spacing.

You could style this page element by element. A second page would then mean doing it all again and keeping both pages in sync by hand. The steps below put every decision in one place first.

{/* screenshot: The unstyled home page in the Builder: header and footer templates, hero, product cards and panels with Bricks default styles. */}

## 1. Colors

Open the Style Manager and select **Colors**. See [Color Manager](https://academy.bricksbuilder.io/builder/features/color-manager/) for every setting.

1. Create a palette for the site.
2. Add the brand color and name it `brand`, not `orange`. If the brand color changes later, the name is still correct.
3. Enable **Light shades** and **Dark shades**. Bricks generates ten steps of each from the base color and names them after it: `brand-d-1` is one step darker than `brand`, `brand-l-9` is a soft tint for backgrounds.
4. Add the neutrals: `ink` for text, `ink-muted` for quieter text, and `paper` for the page background.
5. Add the colors that only serve one purpose. The example uses six pastels for the product cards (`blush`, `butter`, `lilac`, `mint`, `sky`, `clay`).
6. For the pastels, enable the `background-color` utility class. Bricks then creates a global class for each color, such as `bg-butter`.

Only enable utility classes for colors you will apply as classes. Each one adds a global class per shade.

{/* screenshot: Color Manager with the brand color expanded, light and dark shades enabled and the generated shade strips visible. */}

## 2. Typography and spacing scales

Open **Typography** in the Style Manager and create a scale for headings:

1. Give the scale the prefix `heading-`.
2. Set a base size and a ratio for the minimum (mobile) and another pair for the maximum (desktop). The example uses 20 px at 1.25 for mobile and 24 px at 1.5 for desktop.
3. Generate the variables.

Bricks turns every step into a `clamp()` value, from `--heading-2xs` to `--heading-2xl`. A heading grows with the screen instead of jumping at breakpoints. See [Fluid Typography](https://academy.bricksbuilder.io/builder/styling/fluid-typography/) for how the values are calculated.

Create a second scale with the prefix `text-` for body sizes.

Spacing works the same way. Open **Spacing** and create a scale with the prefix `space-`, from `--space-2xs` to `--space-2xl`.

{/* screenshot: Typography scale "Headings" with prefix heading-, minimum and maximum values and the generated preview rows. */}

## 3. Variables and categories

A few values are not part of a scale. Add them in **Variables** and give each group its own category:

| Category | Variable | Value |
| --- | --- | --- |
| Layout | `container` | `1240px` |
| Shape | `radius-s` | `10px` (buttons) |
| Shape | `radius-m` | `24px` (cards) |

The scales already sit in their own categories, so the variable picker stays readable as the list grows. See [Global Variables Manager](https://academy.bricksbuilder.io/builder/styling/global-variables-manager/).

Name variables by role or step, like `radius-s` and `radius-m`. A name like `radius-24` is wrong the moment you change the value.

Values do nothing until something uses them. The page still looks the same after this step.

## 4. Theme style

The theme style sets the defaults for every element, so plain headings, text and buttons never need their own settings.

Create a theme style. A new theme style applies to the entire website by default. Then set:

| Group | Setting | Value |
| --- | --- | --- |
| Typography | Body | Figtree, `var(--text-m)`, `var(--ink)` |
| Typography | Headings | Fraunces, `var(--brand)` |
| Typography | H1 / H2 / H3 | `var(--heading-2xl)` / `var(--heading-l)` / `var(--heading-m)` |
| Elements > Button | Background, text color, border radius | `var(--brand)`, `var(--brand-d-8)`, `var(--radius-s)` |
| Elements > Section | Padding | `var(--space-2xl)` top and bottom, `var(--space-m)` left and right |
| Elements > Container | Width | `var(--container)` |
| Elements > Container and Block | Row gap | `var(--space-s)` |

The row gap on Container and Block gives stacked headings and text even space without a single margin.

Save, and the whole page changes, including the header and footer templates. Switch to the mobile breakpoint: headings and section padding shrink with the screen, without any breakpoint-specific setting.

{/* screenshot: Theme style Typography group with Body and Headings set, live preview of the styled home page on the right. */}

## 5. Classes

A theme style styles headings, text and buttons. It does not know the small label above a heading or the quieter line under a title. Those are patterns, and patterns need [global classes](https://academy.bricksbuilder.io/builder/styling/global-css-classes/).

1. Select the label above the hero heading and add a class named `eyebrow`.
2. Style it once: `var(--text-s)`, uppercase, a little letter spacing, and `var(--brand-d-4)`.
3. Add the same class to the other labels.
4. Add `text-l` for intro paragraphs and `text-muted` for quieter text.

Name classes by purpose, in lowercase with hyphens. `text-muted` still makes sense when the color changes; `grey-text` does not.

In the [Global Class Manager](https://academy.bricksbuilder.io/builder/styling/global-class-manager/), put the three classes into a category called **Typography**. Layout classes such as `card-grid` (below) go into a second category, **Layout**.

## 6. Components

The coffee card repeats eight times on the home page. That makes it a component.

1. Style one card first: `var(--space-m)` as padding and `var(--radius-m)` as border radius. In the variable picker, open the **Shape** category to find the radius quickly.
2. Give the origin the `eyebrow` class, the tasting notes `text-muted`, and the name a darker brand shade.
3. Right-click the card in the Structure panel, choose **Save as component**, and name it `Coffee card`.
4. Add a property for everything that changes from card to card (image, origin, name, notes, price) and connect each one to its element. See [Property types](https://academy.bricksbuilder.io/builder/features/components/#property-types).

A component has no color property type, but it has a [global classes property](https://academy.bricksbuilder.io/builder/features/components/#global-classes). Create one named `Color`, add an option for each pastel, assign each option its `bg-*` class, and connect the property to the card's root element. Each instance now only asks for its content and a color.

Give the row of cards a class too:

```css
/* card-grid: as many columns as fit, four on a desktop */
display: grid;
grid-template-columns: repeat(auto-fit, minmax(22rem, 1fr));
gap: var(--space-m);
```

The numbered section headings and the café panel become components the same way: `Section head`, and `Feature panel` with a `Style` option (global classes property) for a soft or a bold background.

{/* screenshot: Coffee card component with its properties in the panel, the Color property dropdown open with the pastel options. */}

## 7. Build a new page

On a new page, the header and footer are already there because they are templates.

1. Add a heading and an intro. They pick up the theme style without a single setting.
2. Insert a `Section head`, then a Block with the `card-grid` class and `Coffee card` instances. Fill in the content and pick a color.
3. Add a `Feature panel` with its own image and text.

The page has no new styles. Everything on it comes from the system.

{/* screenshot: The finished shop page on the frontend, built only from components, classes and the theme style. */}

## Change the brand color

Open the Color Manager and change `brand` to a new color. Bricks regenerates the shades from it, and headings, buttons, labels and panels follow on every page, in the header and in the footer.

## Related

- [Style Manager](https://academy.bricksbuilder.io/builder/features/style-manager/)
- [Color Manager](https://academy.bricksbuilder.io/builder/features/color-manager/)
- [Fluid Typography](https://academy.bricksbuilder.io/builder/styling/fluid-typography/)
- [Global Variables Manager](https://academy.bricksbuilder.io/builder/styling/global-variables-manager/)
- [Theme Styles](https://academy.bricksbuilder.io/builder/styling/theme-styles/)
- [Global Class Manager](https://academy.bricksbuilder.io/builder/styling/global-class-manager/)
- [Components](https://academy.bricksbuilder.io/builder/features/components/)

---

# Cascade layer

Source: https://academy.bricksbuilder.io/builder/styling/cascade-layer/

*Use CSS cascade layers in Bricks to control style order more predictably across theme styles, classes, and custom code.*

The specificity of default Bricks styles has always been a balancing act. While we aim to keep these styles as non-intrusive as possible, providing a blank canvas for users to build upon, achieving this solely through selector specificity has its limitations. In some cases, it’s been challenging for users to override specific selectors, even when desired.

Bricks 1.12 introduces a promising solution to this longstanding issue through [CSS cascade layers](https://developer.mozilla.org/en-US/docs/Web/CSS/@layer), which as of December 2024 reach an impressive 96% browser support and "Widely available" Baseline.

Since Bricks 2.0, this feature has been **enabled by default**. You can disable it from **Bricks Settings > Performance > Cascade layer**, though it is not recommended.

This feature leverages cascade layers to define how Bricks' default styles interact with other styles on the page.

## How it works

This feature introduces a Bricks layer stack:

- **`bricks.reset`** (a lower-priority layer): This sublayer is empty, providing a safety net for advanced users. Bricks itself does not apply any styles in this layer.
- **`bricks`**: This layer contains Bricks' default styles and element CSS, making them easier to override using un-layered styles or styles in higher-priority user-defined layers.
- **Additional Bricks layers**: Some frontend assets use more specific layers such as `bricks.gutenberg`, `bricks.icons`, or `bricks.libs` so related reset, editor, icon, or library styles can keep their intended order.

Here’s an example to illustrate the problem and the solution:

### The problem: Selector specificity

In the default Bricks styles, a common pattern might look like this:

```php
[class*="brxe-"] {
    max-width: 100%;
}
```

If you tried to override this with a general element selector, such as:

```php
div {
    max-width: 400px;
}
```

…the override wouldn't work because the attribute selector `[class*="brxe-"]` has a higher specificity then the `div`.

One potential workaround could be wrapping Bricks' attribute selectors in `:where()` to reduce specificity:

```php
:where([class*="brxe-"]) {
    max-width: 100%;
}
```

However, this approach would require wrapping every selector, which is not only complex but also impractical at scale.

### The solution: Cascade layers

With cascade layers, we can simply define the default styles within a layer named `bricks`.

Styles outside this layer (un-layered) or in a higher-priority layer automatically precede the default Bricks styles.

Here's how the layers are structured:

```php
@layer bricks.reset;

@layer bricks {
    [class*="brxe-"] {
        max-width: 100%;
    }
    /* Other default Bricks styles */
}
```

Now, when you add your own styles outside the `bricks` layer, like this:

```php
div {
    max-width: 400px;
}
```

…they will precede the default Bricks styles because un-layered styles and higher-priority layers take precedence, regardless of the selector.

### The role of `bricks.reset` {#bricks-reset}

The `bricks.reset` sublayer ensures flexibility when overriding default Bricks styles.

Normally, styles in the `bricks` layer are easy to override, but if a default style uses `!important`, the cascade order flips, making it harder to override with un-layered styles or higher-priority layers. You can learn more about this behaviour [here](https://css-tricks.com/css-cascade-layers/#aa-establishing-a-layer-order).

The `bricks.reset` layer, being lower priority, provides a fallback for safely defining custom styles in these rare cases. While we aim to avoid using `!important` in our default styles unless absolutely required, this sublayer is there as a safeguard.

## Why this matters

By moving default Bricks styles into a dedicated cascade layer, we ensure:

1. **Easier overrides**: Un-layered or higher-priority layered styles can override the default Bricks styles without battling selector specificity.
2. **Simplified maintenance**: Instead of manually tweaking every selector's specificity, cascade layers offer a clean, scalable solution.

## Resources

- **Kevin Powell's YouTube video on cascade layers**: [A look at CSS Cascade Layers](https://www.youtube.com/watch?v=NDNRGW-_1EE)
- **In-depth guide on CSS cascade layers**: [CSS-Tricks: Cascade Layers Guide](https://css-tricks.com/css-cascade-layers/)

---

# Contextual Spacing

Source: https://academy.bricksbuilder.io/builder/styling/contextual-spacing/

*Apply contextual spacing in Bricks to create more consistent rhythm between elements without manually tweaking every margin.*

https://youtu.be/X8Brq1epsfk

Bricks 2.0 introduces **Contextual spacing** to give you full control over vertical spacing (margin) between elements like headings, paragraphs, and lists within embedded content.

Contextual spacing automatically applies to elements within:

- Rich text element
- Post content element (source: WordPress)
- WooCommerce embedded content (excluding Checkout)

Out-of-the-box, Bricks tries to apply various top margins (`margin-block-start`) to elements like headings and paragraphs depending on their context.

If you want to override these defaults, you had to manually remove browser spacing, undo Bricks' built-in styles, and then define your own margins.

Contextual spacing simplifies this process. You can now reset those margins and visually define custom spacing rules under **[Theme Styles](https://academy.bricksbuilder.io/builder/styling/theme-styles/) →** Contextual Spacing.

Whether you are styling embedded content, working with dynamic layouts, or creating utility-based wrappers, this feature gives you consistent and flexible control over spacing.

## How to use contextual spacing

You can enable Contextual spacing inside the builder under **Style Manager → Theme Styles → Contextual Spacing**. The Style Manager preview updates while you change the values.

![Contextual spacing settings in a theme style: Heading var(--space-xl), Paragraph and Fallback spacing var(--space-s), and an additional target for list items with a top margin of 0, next to the live preview of a blog post.](https://academy.bricksbuilder.io/assets/contextual-spacing-theme-style-settings.webp)

**Remove default margins**: Lets you select the HTML tags from which you want to remove the default margins (i.e. Heading, Paragraph, Lists, etc.). This creates a clean starting point for spacing that fits your layout needs, without interference from inherited or default styles.

**Remove default padding**: Lets you remove default padding from selected tags such as `ul`, `ol`, `blockquote`, and `button`.

> **Note**
>
> The remove-default selectors are output exactly as selected. Broad tag selections such as `p`, `ul`, or `h1,h2,h3,h4,h5,h6` reset every matching element in the generated Theme Style CSS, not only the embedded-content selectors used by the spacing rules. Use more specific custom selectors if the reset should be narrower.

> **Note**
>
> **Contextual spacing:** Only applies margins when an element is preceded by another. This prevents extra spacing at the very top while maintaining consistent spacing between elements.

## Settings overview

| Setting | Description |
| --- | --- |
| **Remove default margins** | Resets margins on the selected or manually entered HTML tags. |
| **Remove default padding** | Resets padding on the selected or manually entered HTML tags. |
| **Heading** | Applies top margin to `h1` through `h6` elements when they are preceded by another element. |
| **Paragraph** | Applies top margin to `p` elements when they are preceded by another element. |
| **Fallback spacing** | Applied to any element that does not match a heading, paragraph, or target elements, or when those targets have no spacing value defined. |
| **Additional target elements** | Define spacing rules for elements like `ul`, `blockquote`, or any custom selector. Lets you block margin (top, bottom) and inline padding (left, right). |
| **Apply spacing inside** | Extend contextual spacing to other parts of your layout by targeting wrapper selectors such as `.contextual-spacing`. |

### Use spacing variables

The Heading, Paragraph, Fallback spacing and target fields accept variables. Pick them with the variable picker next to each field, for example `var(--space-xl)` for headings and `var(--space-s)` for paragraphs. If the variables come from a fluid spacing scale ([Style Manager → Spacing](https://academy.bricksbuilder.io/builder/features/style-manager/#spacing)), the spacing between text blocks grows and shrinks with the screen like the rest of your layout.

## Additional target elements

Use the **Additional target elements** repeater to extend Contextual spacing to more than headings and paragraphs.

You can choose from predefined elements:

- Unordered list (ul)
- Ordered list (ol)
- List item (li)
- Figure (figure)
- Blockquote (blockquote)

Or enter your own custom selectors like `.my-class`, `code`, or `div`.

For each, you can set:

- Top and bottom margin (`margin-block`)
- Start and end padding (`padding-inline`)

This gives you spacing consistency across all types of content.

> **Note**
>
> Fallback spacing applies to every element that follows another element inside the content, including list items. If the items of a list drift apart after you set a fallback, add a target for **List item (li)** and set **Margin: Top** to `0`.

## Apply to more content areas

> **Note**
>
> By default, Contextual spacing only targets Rich Text, Post Content, and WooCommerce content. But you can easily extend it by defining **Apply spacing inside** selectors to apply Contextual spacing to any wrapper of your choice, such as `.contextual-spacing, .brxe-shortcode`.

Add these utility classes to wrappers (i.e. Container, Div, Block elements) that hold a mix of content elements, and Bricks will apply your Contextual spacing settings to them.

![Apply spacing inside set to .contextual-spacing in the theme style, with the preview of a block of separate Heading and Basic Text elements that now follows the contextual spacing.](https://academy.bricksbuilder.io/assets/contextual-spacing-apply-spacing-inside.webp)

Inside a selector from **Apply spacing inside**, the rules work slightly differently than inside Rich Text and Post Content:

- **Heading** spacing applies to `h1` through `h6` elements that are not the first child.
- **Paragraph** spacing applies to `p` elements that are not the first child. A **Basic Text** element renders a `div` by default, so it takes the fallback spacing instead.
- **Fallback spacing** applies to direct children of the wrapper that follow another child.
- **Additional target elements** apply to matching elements anywhere inside the wrapper when they follow another element.

> **Caution**
>
> Margins add to the wrapper's gap. If the wrapper has a row gap, clear it, or the space between elements becomes gap plus margin. Clear the gap before you add the class: once a class is added, the panel edits the class, not the element, so the element's own gap would stay.

### Why not apply spacing to all headings and paragraphs by default?

In most Bricks layouts, especially when using **Heading** and **Basic text** elements in combination with other elements, spacing is typically handled using the **gap** property between containers.

Because of that, applying a single spacing rule to all headings and paragraphs wouldn't make sense in every context.

Contextual spacing gives you the flexibility to apply spacing only where it's needed, using selectors and utility classes.

## Example use case 1: Embedded post content

You’re building a single post template using a **Post Content** element (source: WordPress).
Before enabling Contextual spacing, the post displays the default spacing added by Bricks.

When **Remove default margins** is enabled, Bricks removes both its own default spacing and the browser's default margins. You can then define your own spacing values using the Contextual spacing controls.

When you enable **Remove default margins**, then set spacing values. For example:

- **Heading**: `2rem`
- **Paragraph**: `1.25rem`
- **Fallback**: `1rem`

Bricks then applies spacing only between elements where needed. The first element inside the post has no margin above it, but elements that follow each other are spaced consistently.

![](https://academy.bricksbuilder.io/assets/bricks-contextual-spacing-enable-scaled.png)

![](https://academy.bricksbuilder.io/assets/bricks-contextual-spacing-example-values-scaled.png)

**Result:** Clean layout, no spacing at the top, full control over vertical rhythm.

![](https://academy.bricksbuilder.io/assets/bricks-contextual-spacing-use-case-1-1-1024x791.png)

![](https://academy.bricksbuilder.io/assets/bricks-contextual-spacing-use-case-1-2-1024x1017.png)

![](https://academy.bricksbuilder.io/assets/bricks-contextual-spacing-use-case-1-3-1024x1012.png)

![](https://academy.bricksbuilder.io/assets/bricks-contextual-spacing-use-case-1-4-926x1024.png)

## Example use case 2: Mixed content layout

You've created a custom template that includes a container with the following elements:

- A **Heading** element
- A **Basic text** element (with a `p` tag)
- An **Image** element (with a `figure` tag)
- A **Post Content** element (source: WordPress)

Because these use different systems for spacing, the result may feel inconsistent.

To unify the layout:

1. Under Theme Styles > Contextual Spacing > Enable **Remove default margins**
2. Set spacing values. For example:
  - Heading: `2rem`
  - Paragraph: `1.25rem`
  - Fallback: `1rem`
3. Clear the container's row gap, so it does not add to the margins
4. Add a global class like `.contextual-spacing` to the container
5. Enter `.contextual-spacing` under **Apply spacing inside**

![](https://academy.bricksbuilder.io/assets/bricks-contextual-spacing-utility-class-scaled.png)

![](https://academy.bricksbuilder.io/assets/bricks-contextual-spacing-apply-to-utility-class-scaled.png)

**Result**: All elements within that wrapper now follow your contextual spacing rules.

---

# CSS Grid Layout

Source: https://academy.bricksbuilder.io/builder/styling/css-grid-layout/

*Build CSS Grid layouts in Bricks and control columns, rows, placement, and alignment directly from the builder.*

Available since Bricks 1.6.1 CSS grid allows you to create two-dimensional layouts (columns & rows). Whereas CSS flexbox, which Bricks uses as the default layout model, is designed for one-dimensional layouts (either column or row).

## Creating a grid layout

You can turn any layout element (section, container, block, div) into a CSS grid layout by setting the **Display** value to `grid`. This element is your **Grid Container**.

Every direct child element of your Grid container is a **Grid Item**, with additional settings for **Grid column** & **Grid row** to place an item it within the grid.

When editing a grid container in the builder a grid overlay becomes visible indicating the [grid cells](https://developer.mozilla.org/en-US/docs/Glossary/Grid_Cell). Clicking the little four-square element action icon lets to show/hide this overlay.

![](https://academy.bricksbuilder.io/assets/bricks-css-grid.jpg)

<figcaption>

Grid container (display: grid) with 6 grid items (direct children) and 20px gap

</figcaption>

As you can see in the screenshot above grid items are laid out in rows by default, covering the full width of the grid container. Which in itself doesn't unlock the true power of CSS grid, until you start ...

## Visual Grid Builder {#visual-grid-builder}

When a layout element's **Display** value is set to `grid`, Bricks adds a Visual Grid Builder action to the grid control. Open it to create and adjust columns, rows, and gaps visually instead of writing every `grid-template-columns` or `grid-template-rows` value by hand.

The Visual Grid Builder shows the grid panel, row and column controls, breakpoint controls, undo/redo history, and actions such as filling or resetting the grid. Column, row, and gap values are saved back to the grid controls. Grid item placement is saved to child grid controls where possible; for query loop items, active class styling, non-nestable elements, or component roots, Bricks writes generated placement CSS into the selected grid's custom CSS between Visual Grid Builder markers.

## Setting up column & row tracks (explicit grid)

Once we've created our grid container it is time to define our grid column & row [tracks](https://developer.mozilla.org/en-US/docs/Glossary/Grid_Tracks).

We can do this explicitly via the **Grid template columns** ([`grid-template-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-template-columns)) & **Grid template rows** ([`grid-template-rows`](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-template-rows)) settings of our grid container.

Let's explore a few examples together ...

`***grid-template-columns: 200px 1fr 2fr***`

Each value of the `grid-template-columns` property creates a column track.

The example above creates a three-column grid layout.

Column 1 has a fixed width of 200px. Column 2 is `1fr` a column 3 is `2fr` wide.

`**fr**` is a new flexible unit, called the fractional unit, which takes up x parts of the available space.

How is `fr` calculated?

Let's say our grid container has a width of 1100px (the container's default width).

We first need to subtract all non-fr values and gaps: So minus the fixed 200px width of column 1 the remaining available width is 900px.

We have 3 fractional units in total (1fr from column 2 plus 2fr from column 3) to allocate the remaining space towards.

Meaning 1fr equals 300px (= 900px / 3). So column 2 is 300px wide (= 1fr x 300px), and column 3 is 600px (= 2fr x 300px) wide.

`***grid-template-rows: 100px 300px***`

Each value of the `grid-template-row`s property creates a row track.

The example above explicitly defines the first two rows. Row 1 is 100px high, and row 2 is 300px high.

As we only explicitly defined the height for the first two rows, the height of any row after row 2 is determined by the height of its content by default. We can change this behaviour by creating an implicit grid ...

### Implicit grid

The grid container automatically generates additional (column & row) tracks for grid items that fall outside of your explicitly defined grid. This is called the implicit grid.

You can define the column & row sizes of this implicit grid via the **Grid auto columns** (`grid-auto-columns`) and **Grid auto rows** (`grid-auto-rows`) settings of your grid container.

### Min & max grid track sizes

The [`minmax`](https://developer.mozilla.org/en-US/docs/Web/CSS/minmax) CSS function lets you set a minimum and maximum track size.

It accepts two arguments. The first one is the minimum value, and the second one is the maximum value of your grid track.

`grid-template-columns: repeat(3, minmax(200px, 1fr))`

Creates an explicit 3-column grid where each grid item has a min. width of 200px, and a max. width of 1fr.

The problem is this sort of explicit grid is that is it not responsive. It overflows when the viewport is less than 600px wide (3 columns of min. 200px), and the number of columns doesn't adjust to different breakpoints out of the box.

### auto-fill & auto-fit keywords

We can use the `auto-fill` or `auto-fit` keywords to address those responsive issues. Allowing us to create responsive grid layouts without media queries.

So instead of setting an explicit 3 column grid, we use the `auto-fill` or `auto-fit` keyword like this:

`grid-template-columns: repeat(auto-fill, minmax(200px, 1fr))`

Which keyword to use depends on the desired behavior. `auto-fit` expands grid items to fill the available space. While `auto-fill` does not (it keeps the available space).

### Repeat track sizes

The [repeat](https://developer.mozilla.org/en-US/docs/Web/CSS/repeat) CSS function lets you define a repeating track size pattern in a compact format.

It accepts two arguments. The first one is the number of times the track should repeat and the second one is the definition of the tracks.

`grid-template-columns: repeat(3, 1fr)`
Creates an explicit 3-column grid.

`grid-template-rows: 100px repeat(2, 1fr) 200px`
Creates an explicit 4-row grid. Where row 1 is 100px high, row 2 & 3 are 1fr each, and row 4 is 200px high.

## Placing grid items (by line number)

[Grid lines](https://developer.mozilla.org/en-US/docs/Glossary/Grid_Lines) mark the start or end of a column or row track. The count starts at 1.

We can use those line numbers to place a grid item onto the grid.

The example below shows an explicit three column grid layout, whose grid items cover three rows.

![](https://academy.bricksbuilder.io/assets/bricks-css-grid-lines.jpg)

That means this grid has 4 column lines and 4 row lines.

When inspecting the grid layout of any website by clicking the little blue `grid` button next to the element node in the browser, in this case Chrome, shows you the grid lines as well:

![](https://academy.bricksbuilder.io/assets/bricks-css-grid-lines-browser-scaled.jpg)

In our example above we positioned **Grid Item 2** via the Grid column ([`grid-column`](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-column)) and Grid row ([`grid-row`](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-row)) settings like this, so it takes up two columns and two rows:

![](https://academy.bricksbuilder.io/assets/bricks-css-grid-column-grid-row.jpg)

The **Grid column** & **Grid row** settings are available for all grid items (direct children of the grid container).

Syntax: The first value specifies the starting line number. Followed by a forward slash (`/`). Followed by the second value, which specifies the end line number.

In our example above we've set the Grid column to "2 / 4". Telling the grid we want Grid Item 2 to start at column line 2 and end at column line 4. The Grid row is set to "1 / 3", meaning Grid Item 2 starts at row line 1 and ends at row line 3.

We could have achieved the same layout by setting the grid column & Grid row setting to "`span 2`". `span` is a keyword that tells the grid layout how many columns or rows the item should span.

## Notes

Named grid areas ([`grid-template-areas`](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-template-areas)) have to be defined via custom CSS.

Placing grid items inside a query loop are best done via `nth-child` custom CSS.

This article is meant to provide an overview of CSS grid, and not a complete reference. We recommend following the resources linked below to learn more about CSS grid.

### Additional resources

- [A Complete Guide to CSS Grid](https://css-tricks.com/snippets/css/complete-guide-grid/) (by CSS tricks)
- [learncssgrid.com](https://learncssgrid.com/) (comprehensive CSS grid overview)
- [cssgrid.io](https://cssgrid.io/) (free CSS grid course by Wes Bos)

---

# Custom Fonts

Source: https://academy.bricksbuilder.io/builder/styling/custom-fonts/

*Upload and manage custom fonts in Bricks so they can be used across theme styles, classes, and element typography.*

Your website typography has a huge impact on how your site is perceived, and it'll pay off to spend some time to get this aspect right.

Bricks allows you to add any font you want. From web-safe fonts to Google fonts, and of course, uploading your own custom fonts in your WordPress dashboard under **Bricks > Custom Fonts**. The latter which we are going to have a more in-depth look at now.

> **Note**
>
> **Bricks 2.0 introduces the [Font Manager](https://academy.bricksbuilder.io/builder/styling/font-manager/) for uploading and managing custom fonts directly inside the builder. This is the recommended workflow for Bricks 2.0 and newer. The legacy Bricks > Custom Fonts screen remains available in the WordPress dashboard.**

You can also preload uploaded custom fonts under **Bricks > Settings > Performance > Preload custom fonts** to help avoid FOUT (Flash of unstyled text).

## How To Create & Upload Custom Fonts

https://youtu.be/6QB84hoycgw

To create a new custom font go to **Bricks > Custom Fonts** in your WordPress dashboard, and click **Add New**.

First, let's give your custom font a title. This title shows in the *font-family* dropdown control when editing the typography in the builder.

Now your can start uploading your font files for all the font variants (*font-weight* and *font-style*) you plan to use on your site:

![](https://academy.bricksbuilder.io/assets/doce-custom-fonts-edit-font-variants-1024x786.png)

<figcaption>

Editing your custom font and managing all its font files and variant.

</figcaption>

You can see in the example above that we've uploaded a .WOFF and .WOFF2 font file for the standard font-weight (400) and a "Normal" font style.

If we'd have font files for font-weight 700 (bold) and font-style "Italic" we'd click the "Add a font variant" button. Select the font-weight value "700" and the font-style "Italic", and then upload the correct font files for this variant.

Once you've created all relevant font variants and uploaded all font files accordingly, you can save your fonts. Your new custom font is now available in the builder.

Uploading a custom font only makes it available in Bricks typography controls. To use it on the frontend, select the font in a typography setting, such as an element, global class, Theme Style, page setting, or template setting.

When a custom font has multiple weights or styles, select the matching font family and weight/style together in the same typography control. This lets Bricks match the setting to the correct saved variation, especially when **Preload custom fonts** is enabled.

You can also see a font preview when editing your font or on the "Custom Fonts" page.

> **Note**
>
> If your custom fonts are not showing correctly, please check your [WordPress URL settings](https://academy.bricksbuilder.io/builder/setup/known-issues/#custom-fonts).

## Supported Font Formats

The following font formats are enabled by default:

- **WOFF (Web Open Font Format)**: This is the recommend font format used by all modern browsers. Font data is compressed and therefore loads faster than the same font provided via TrueType or OpenType files. Full support for IE9+.
- **WOFF2 (Web Open Font Format 2.0)**: TrueType/OpenType font with even better compression than WOFF 1.0. No IE browser support.
- **TTF (TrueType Font)**: Uncompressed font data, but partial IE9+ support.

The recommended font format is WOFF, with a current [browser](https://caniuse.com/woff)[support of 98.26%](https://caniuse.com/woff), and full support for IE9+.

## How To Enable More Font Formats

If you need to support IE8 you can programatically enable the EOT font format (or any other font format) by adding the following code to your Bricks child theme:

```php
add_filter( 'bricks/custom_fonts/mime_types', function( $mime_types ) {
  // Enable EOT font format for <IE9 browser support
  array_unshift( $mime_types, ['eot' => 'font/eot'] );

  return $mime_types;
} );
```

Once you've created at least one custom font a "Custom Fonts" section with all your custom fonts will show underneath the "Standard Fonts" in any "font-family" control:

![](https://academy.bricksbuilder.io/assets/docs-custom-fonts-control.png)

#### Pro Tip: How To Become GDPR Compliant By Hosting Google Fonts Yourself {#google-fonts}

When using a Google Font on your website, you have to get consent from your website visitors before displaying the font.

You can avoid this whole issue by downloading all relevant font variants for the Google Fonts you want to use on your site, and then upload them as "Custom fonts" in Bricks.

> **Note**
>
> The "[Google Webfonts Helper](https://gwfh.mranftl.com/fonts)" project is a great resource to directly download all `.eot`, `.woff`, `.woff2`, `.svg`, `.ttf` files of a Google font.

Bricks 1.4 allows you to “Disable Google Fonts” altogether via the Bricks settings under “Performance”:

![](https://academy.bricksbuilder.io/assets/bricks-1.4-disable-google-fonts-setting-1024x944.png)

<figcaption>

Bricks > Settings > Performance: Disable Google Fonts

</figcaption>

### Free Fonts Resources

- [fontsquirrel.com](https://www.fontsquirrel.com)
- [reedesignresources.net/category/free-fonts](https://freedesignresources.net/category/free-fonts)
- [awwwards.com/awwwards/collections/free-fonts](https://www.awwwards.com/awwwards/collections/free-fonts)

---

# Fluid Spacing

Source: https://academy.bricksbuilder.io/builder/styling/fluid-spacing/

*Create a fluid spacing scale in Bricks and use its variables for padding, margins and gaps that grow smoothly from small to large screens.*

A fluid spacing scale replaces fixed padding, margin and gap values with CSS variables that grow with the screen. Each variable uses a `clamp()` value: its minimum on small screens, its maximum on large screens, and a smooth transition in between. One spacing variable can replace a padding value and the separate values you would otherwise set on each breakpoint.

https://youtu.be/plfRsthxOXI

## Accessing fluid spacing {#access}

Open the **Style Manager** from the builder toolbar, then select **Spacing** in the Style Manager sidebar. From there you can create and edit spacing scales.

The minimum and maximum screen widths and the HTML font-size used for rem calculations are set once in the [Style Manager settings](https://academy.bricksbuilder.io/builder/features/style-manager/#settings) and apply to all spacing and typography scales (default: `360px` and `1440px`).

![Style Manager Spacing tab with a scale named Spacing: prefix space-, scale type T-shirt, baseline step m, minimum and maximum settings, and steps from space-2xs to space-4xl with their minimum and maximum values.](https://academy.bricksbuilder.io/assets/bricks-style-manager-spacing-scale.webp)

## Creating a spacing scale {#create-scale}

Every spacing scale is a variable category. Enter a scale name, for example `Spacing`, and click **Create**. A new scale starts with these settings:

- **Variable prefix:** `space-`
- **Scale type:** T-shirt, with seven steps from `2xs` to `2xl`
- **Baseline step:** `m`
- **Minimum (Mobile):** base size `16px`, scale ratio 1.25
- **Maximum (Desktop):** base size `20px`, scale ratio 1.333

With these settings, `space-m` runs from `16px` on small screens to `20px` on large screens, and every other step is calculated from it with the scale ratio.

The prefix, scale type, baseline step and ratios work the same way as in the typography scale generator. See [Fluid Typography](https://academy.bricksbuilder.io/builder/styling/fluid-typography/#controls-overview) for each control.

## Generating variables {#generating-variables}

Changes to the scale settings are previewed in the list first. Click **Regenerate variables** to create or update the variables of the category (without pending changes, the button reads **Generate variables**).

Generating replaces all variables of the category, and Bricks asks you to confirm this when the category already has variables. As long as the number of steps and the scale type stay the same, the names stay the same too, so every `var(--space-l)` in your design picks up the new value.

Generated variables appear in the variable picker of every spacing and size control, grouped by their category.

## Adding larger steps for section padding {#add-steps}

With the default settings, the largest step, `space-2xl`, ends at about `47px`. That is usually too small for the padding of a section.

Hover over the last row of the list and click **+** to add a larger step (`3xl`, then `4xl`, `5xl` and so on). With the default settings, `space-5xl` runs from about `61px` on small screens to `112px` on large screens. Hover over the first row to add a smaller step instead. To remove the smallest or largest step, hover over the first or last row and click **−**.

## Using spacing in a theme style {#theme-style}

To give every section the same padding, set it once in a [theme style](https://academy.bricksbuilder.io/builder/styling/theme-styles/) instead of on each section: **Theme styles** > your theme style > **Elements** > **Section** > **Padding**.

Each side has its own variable picker. With **Opposites linked** turned on, setting the top value also sets the bottom value, and setting the left value also sets the right value. For example, use `var(--space-5xl)` for top and bottom and `var(--space-l)` for the sides. The **Container** group in the same theme style has its own padding, row gap and column gap.

<div className="screenshot screenshot--control-panel">

![Theme style Section settings: the Padding control with var(--space-5xl) on top and bottom and var(--space-l) on the left and right, opposites linked.](https://academy.bricksbuilder.io/assets/bricks-theme-style-section-padding-variables.webp)

</div>

To make a whole page tighter or roomier later, change the step in the theme style, for example from `var(--space-5xl)` to `var(--space-4xl)`. Every section that follows the theme style updates on every page.

## Clearing padding on elements {#clear-element-padding}

Padding set directly on an element, including padding set on a breakpoint, takes precedence over the theme style. Clear it on the sections that should follow the theme style.

To clear several sections at once, select them in the Structure panel. Click the first section, then Shift-click the last one to select all sections in between, or hold `CMD` (macOS) or `CTRL` (Windows/Linux) and click to add single elements. The panel switches to **Bulk edit** and shows how many elements are selected. Clearing a field clears it on all of them. If the sections have their own padding on a breakpoint, switch to that breakpoint and clear it there as well.

![Bulk edit of five selected sections in the Builder: the cleared Padding fields show the inherited theme style values as placeholders.](https://academy.bricksbuilder.io/assets/bricks-structure-bulk-edit-section-padding.webp)

For an element that should deliberately differ, pick another step of the same scale instead of typing a value.

## Utility classes {#utility-classes}

Below the list, the spacing scale can generate utility classes such as `gap-m` or `p-l`. Only generate the classes you actually use.

---

# Fluid Typography

Source: https://academy.bricksbuilder.io/builder/styling/fluid-typography/

*Create fluid typography in Bricks so text scales smoothly across viewport sizes instead of changing only at breakpoints.*

Starting with Bricks 2.1, the **Fluid Typography Generator** lets you create pixel-perfect & responsive font sizes (through CSS variables using `clamp`) that scale smoothly between defined minimum and maximum values, ensuring consistent readability across all screen sizes and devices. Simplifying the process of managing font sizes while maintaining flexibility and precision in your design.

https://youtu.be/wsxOmDqjfaQ

## Accessing fluid typography {#access}

Open the **Style Manager** from the builder toolbar, then select **Typography** in the Style Manager sidebar. From there you can create and edit fluid typography scales.

Global scale settings, including the HTML font-size used for rem calculations and the minimum and maximum screen widths, are available in the Style Manager settings.

Spacing scales for padding, margins and gaps work the same way in the **Spacing** tab. See [Fluid Spacing](https://academy.bricksbuilder.io/builder/styling/fluid-spacing/).

## Fluid typography categories {#adding-category}

Bricks lets you create unlimited Fluid Typography Scales for your Headings, Text, etc. through categories.

So, **every Category is a Fluid Typography Scale**, that stores all its scale settings alongside it.

You can keep it simple and just create a `Headings` and `Text` category for those two scales as we did in the following screenshot:

![](https://academy.bricksbuilder.io/assets/bricks-fluid-typo-category-text-empty.png)

## Fluid typography variables {#generating-variables}

Fluid typography variables can be generated with the Scale Generator on the right-hand side.

Scale changes are previewed in the list first. Click **Regenerate variables** to create or update the variables of the category (without pending changes, the button reads **Generate variables**). The icon in the Style Manager header, **Regenerate variables and save**, does both in one step.

Whenever variables are generated, all existing variables within the selected category are deleted and replaced with the newly created variables. If the category already has variables, Bricks asks you to confirm this first. The number of variables is the same as in the previous set, but the names and values will be regenerated. So, any manual edits made to variable names or values are lost once the variables are regenerated. As long as the number of steps and the scale type stay the same, the names stay the same too, so every place that uses a variable (for example `var(--heading-xl)`) picks up the new value.

## Scale controls {#controls-overview}

### Prefix {#control-prefix}

The prefix determines how variable names are structured. For instance, setting the prefix to `text-` results in variables being named `--text-m` or `--text-xl`, depending on the scale. It is recommended to use a prefix that is both unique and descriptive to maintain clarity and avoid conflicts.

### Scale type {#control-scale-type}

The scale type specifies the naming convention used for fluid typography variables. There are three available options:

1. **T-shirt:** Generates variable names based on standard t-shirt sizes, such as `2xs, xs, s, m, l, xl, 2xl`. An example output would be `--text-m`.
2. **Numeric:** Generates variable names using numbers, typically ranging from 1 through 6. An example output would be `--text-4`.
3. **Custom:** Allows complete manual control over the naming convention. For example, scale names such as `small, medium, large, title` could be entered, resulting in variable names such as `--text-medium`.

### Custom scale type {#control-custom-scale-type}

This control only shows when the scale type is set to **Custom**. It provides the ability to define custom scale names, offering flexibility in aligning the naming convention with project-specific requirements.

### Baseline step {#control-baseline-step}

The baseline step acts as the foundation of the scale. The baseline variable will directly reflect the minimum and maximum font sizes defined, and all other scale steps will be calculated relative to this baseline. Proper definition of the baseline ensures accurate scaling across all steps.

### HTML font-size {#control-px-to-rem}

The Style Manager **HTML font-size** setting defines the rem baseline used for scale generation. You can set it explicitly to `10px` or `16px`, or leave it on auto so Bricks resolves the value from Theme Styles where possible and otherwise falls back to the default.

### Base font size (px) {#control-base-font-size}

The scale settings have two groups, **Minimum (Mobile)** and **Maximum (Desktop)**. Each has its own base font size and type scale ratio (defaults: `16px` with 1.25, and `20px` with 1.333). The two base font sizes establish the minimum and maximum values for the baseline step. Font sizes for all other steps will be calculated automatically based on the defined **Type Scale Ratio**.

### Screen width (px) {#control-screen-width}

The minimum and maximum screen widths are set once in the Style Manager settings and apply to all scales (default: `360px` and `1440px`). At the minimum width every step uses its minimum size, at the maximum width its maximum size. Outside these widths, font sizes stay constant.

### Type scale ratio {#control-type-scale-ratio}

This control defines the ratio by which font sizes increase or decrease in relation to the next adjacent variable. For example, with a baseline of 16px and a scale ratio of 1.5, the next step above the baseline will be calculated as 24px. Ratios are applied upward and downward, generating consistent scaling in both directions. Because the minimum and maximum have their own ratio, a larger ratio for large screens gives more contrast between headings on desktop while keeping them compact on phones. Steps below the baseline then shrink more on large screens, so for the smallest steps the maximum value can end up below the minimum.

For advanced use cases, it is possible to enter a custom ratio. A new control for defining custom values becomes available only when the **Custom** option is selected. This allows precise manual control over how each step in the scale is calculated.

## Editing variables {#editing-variables}

Once generated, variables are displayed in the central panel. These variables may be managed in several ways.

![](https://academy.bricksbuilder.io/assets/bricks-fluid-typo-category-text-generated.png)

### Adding variables {#add-variables}

Hover over the first or the last step in the list. A **+** button on its left edge adds a step: above the first row it adds a smaller step, below the last row a larger one (for example `3xl` after `2xl`).

The new step is inserted at the appropriate position, either above or below the baseline. Both the variable name and value are automatically generated.

In cases where the **Custom** scale type is used, variable names may need to be updated manually, or additional values can be added directly in the custom scale definition.

**Note:** If you used the **Custom** scale type, then you will need to update the variable name, or even better, add new value to the **Custom** scale directly.

### Deleting variables {#delete-and-export}

To remove the smallest or the largest step, hover over the first or last row and click the **−** button. Bricks prevents removing the baseline step because the other steps depend on it.

### Editing variables {#manually-editing}

Variable names and values can be directly edited by selecting them in the center column. Manual edits apply only to the selected variable and do not affect any calculations. This allows fine-tuned adjustments while maintaining overall scale consistency.

## Using the variables {#using-variables}

Generated variables appear in the variable picker of every size control, grouped by their category. To give all headings of the same level one size across the site, set them in a theme style: **Theme Styles** > **Typography** > **Heading H1** (H2, H3 …) > **Typography** > **Font size**, then pick the variable, for example `var(--heading-xl)` for H2.

A font size set directly on an element, including a size set on a breakpoint, takes precedence over the theme style. Clear those sizes on the elements that should follow the theme style. For an element that should deliberately differ, such as a larger hero headline, pick another step of the same scale instead of typing a value.

## Typography preview {#typography-preview}

The list in the center shows every step of the scale with its minimum and maximum size, each rendered as a line of preview text. Changes to the scale settings are previewed in this list right away. They reach the variables only after you click **Regenerate variables**.

The `eye` icon in the Style Manager header toggles the canvas preview, so you can see the page next to the Style Manager while you work.

![Style Manager Typography tab with a Headings scale: prefix heading-, minimum and maximum settings, and steps from heading-2xs to heading-3xl with their minimum and maximum preview.](https://academy.bricksbuilder.io/assets/bricks-fluid-typo-scale-list.webp)

---

# Font Manager

Source: https://academy.bricksbuilder.io/builder/styling/font-manager/

*Manage project fonts in Bricks, including uploads, font organization, and how fonts are exposed throughout the builder.*

https://youtu.be/6QB84hoycgw

The Font Manager is the central place to browse, favorite, download, upload, edit, and remove the fonts available in Bricks typography controls.

Use it when you want to:

- Upload custom font files.
- Download Google Fonts and serve them locally.
- Mark frequently used fonts as favorites.
- Search and preview available fonts.
- Restore or permanently delete custom fonts from the Font Manager trash.

The Font Manager affects which fonts are available in builder typography controls. It does not automatically apply fonts to your site. After adding or favoriting a font, select it in an element, global class, Theme Style, page setting, template setting, or another typography control.

![](https://academy.bricksbuilder.io/assets/bricks-font-manager-scaled.png)

## How Font Manager works

Font Manager groups fonts by source:

| Font source | What it means |
| --- | --- |
| Favorites | Fonts you marked with the heart icon. |
| Custom | Fonts stored on your site as custom font records and font files. |
| Google | Google Fonts available to preview and optionally download locally. |
| Standard | System font-family options available without loading font files. |
| Adobe | Fonts synced from the Adobe Fonts project ID in Bricks settings. |

Custom fonts are stored as Bricks custom font records. Each custom font has a font family name and one or more variations. A variation is a file plus metadata such as font weight, font style, and optional unicode range.

When custom fonts are available, Bricks generates `@font-face` rules for them and makes those fonts available in the builder and on the frontend. Custom font output uses `font-display: swap`.

> **Note**
>
> Font Manager access depends on the **Access font manager** builder permission. Users without this permission will not see the Font Manager entry or the font-family action icon.

## Opening Font Manager

You can open the Font Manager by going to **Settings > Font Manager** in the builder toolbar, or by clicking the **gear icon** next to any font-family control.

This opens a popup where you can manage all available fonts (Google fonts, Adobe fonts, Standard fonts, and Custom fonts).

## Browsing and previewing fonts

The Font Manager sidebar lets you switch between font sources. The search field filters the current source by family name, category, or type.

Each font card shows:

- The display name.
- The source type.
- The category, when available.
- The number of available styles or variants, when available.
- A preview line using the current preview text.

Use the preview icon in the header to enter custom preview text. The default preview text is `The quick brown fox jumps over the lazy dog`.

Google font previews load only when the font card becomes visible. This keeps the popup lighter, but it means previewing Google Fonts can still make browser requests to Google. Downloading a Google Font converts it into a custom font stored on your site.

## Favorites and font-family controls

Click the heart icon on any font to add or remove it from Favorites.

Favorites are stored differently depending on the source:

- Custom fonts are favorited by custom font ID.
- Google, Adobe, and Standard fonts are favorited by source and family name.

Favorites affect the font-family control:

- If no favorites are saved, the font-family dropdown shows all available fonts.
- If favorites exist, they appear at the top of the dropdown.
- Under **Bricks > Settings > Builder > Font family: Options**, you can choose **Show favorites only**.

When **Show favorites only** is enabled, Bricks still shows the currently selected font in the dropdown if that font is not a favorite. This prevents existing typography settings from becoming invisible while editing.

## Creating a custom font

1. Open Font Manager.
2. Click the **Add** icon.
3. Enter the font family name.
4. Add one or more font variations.
5. Save the builder.

When you click **Add**, Bricks creates an empty draft custom font record. If you close the editor without a font family name and without uploaded variations, Bricks deletes that empty draft.

### Add a single variation

Inside a custom font, click **Add** to create a variation row.

![](https://academy.bricksbuilder.io/assets/bricks-font-manager-add-993x1024.png)

For each variation, set:

- **Font file**: Choose a supported font file from the Media Library.
- **Font weight**: 100 through 900.
- **Font style**: Normal, Italic, or Oblique.
- **Unicode range**: Optional. Use this when a variation should only load for a specific character range.

Supported upload formats are:

- `.woff2`
- `.woff`
- `.ttf`

Bricks validates the file by extension and MIME type. The user also needs WordPress upload permissions.

### Import multiple variations

Click **Import** to upload multiple `.woff2`, `.woff`, or `.ttf` files at once. Bricks processes the files and tries to detect font weight and style from the file metadata.

![](https://academy.bricksbuilder.io/assets/bricks-font-manager-import-988x1024.png)

If Bricks cannot detect the weight or style, the variation falls back to `400` and `normal`. Review imported variations before saving, especially when the font family has multiple weights or italic styles.

Bricks warns when variations overlap. Two variations overlap when they share the same weight and style and either have no unicode range or have the same unicode range.

## Downloading Google Fonts locally

The Google tab lists Google Fonts unless Google Fonts are disabled in Bricks settings.

To download a Google Font locally:

1. Open the **Google** source.
2. Find the font.
3. Click the download icon.
4. Wait for the success message.

Bricks fetches the Google Fonts CSS, downloads the referenced font files, creates a custom font record, saves the files in WordPress, and adds the font to the Custom source. After download, the Google font card shows that it has already been downloaded.

Downloaded Google Fonts are custom fonts. Edit them from the Custom source if you need to inspect or adjust the stored variations.

> **Tip**
>
> If you want to avoid external Google Fonts requests on the frontend, download the Google Font locally and use the custom font version in your typography controls.

## Adobe and Standard fonts

Adobe fonts appear when an Adobe Fonts project ID is configured and synced in Bricks settings. The Font Manager shows Adobe font names, but the actual CSS family used in typography controls can be the Adobe slug or one of the synced CSS names.

Standard fonts are system font-family options. They do not require uploading files or loading external font CSS.

## Editing custom fonts

Custom fonts and downloaded Google Fonts can be edited.

In the custom font editor, you can:

- Rename the font family.
- Add, remove, or replace variation files.
- Change variation weight or style.
- Add or edit unicode ranges.
- Mark the font as a favorite.
- Move the font to trash.

Renaming a custom font changes the family name used by that custom font record. Review existing typography settings after renaming, especially if the old name was used in custom CSS.

When you edit variation files, Bricks updates the custom font data and regenerates custom font-face CSS on save so the updated font can be used in the builder and frontend.

## Trash, restore, and permanent delete

Moving a custom font to trash removes it from the active Custom font list and removes it from Favorites.

To review trashed fonts, click the trash icon in Font Manager. From there you can:

- **Restore**: Move the font out of trash and publish it again.
- **Delete permanently**: Delete the custom font record and its stored font file attachments.

Permanent deletion cannot be undone from Font Manager. Use it only when you are sure the font is no longer needed.

## Loading behavior

Custom fonts are available because Bricks generates `@font-face` rules from the saved variations. For each variation, Bricks uses the saved font family, weight, style, optional unicode range, and file URLs. WOFF2 files are preferred first in generated source lists when available.

Bricks avoids loading a Google Font from Google when a custom font with the same family name exists. This prevents a locally stored custom font from being overwritten by a Google font with the same name.

### Preloading custom fonts

Under **Bricks > Settings > Performance**, enable **Preload custom fonts** to add preload tags for custom fonts that Bricks detects in the active page output.

When this setting is enabled, Bricks scans active Theme Styles, header, content, footer, page settings, template settings, global class settings, and component instance settings for custom font usage. It then preloads matching `.woff2`, `.woff`, or `.ttf` files.

For automatic preloading, the custom font family and the relevant weight/style need to be set together in Bricks typography settings. Bricks does not resolve every possible inherited CSS combination. For example, if an element inherits the custom font family from a parent but sets only `font-weight: 700` on itself, Bricks may not preload the 700 font file automatically. Set the family and weight/style explicitly in the typography control when that specific variation should be preloaded.

Preloading can improve perceived loading for important above-the-fold fonts, but it should be used carefully. Preloading too many font files can hurt performance.

### Webfont loading method

For webfonts such as Google Fonts, Bricks settings include a webfont loading method option. The default is stylesheet loading. The Webfont Loader option can hide page content until webfonts are loaded to reduce flashes of unstyled text.

This setting is separate from custom font preloading.

## Troubleshooting

### The Font Manager icon is missing

Check the user's builder permissions. The user needs **Access font manager**.

### A Google Font does not appear

Google Fonts may be disabled in Bricks settings. If Google Fonts are disabled, the Google source in Font Manager shows a disabled message instead of the font list.

### A downloaded Google Font still appears in the Google list

That is expected. The Google source remains a browser of Google Fonts. Once downloaded, the local version is available in the Custom source and the Google card shows the downloaded state.

### A custom font does not appear in a typography control

Check that the font has a family name, at least one saved variation, and that the builder was saved after the change. Also confirm that the font was not moved to trash.

### A variation loads as the wrong weight or style

Edit the custom font and review each variation. Bulk import tries to detect weight and style from font metadata, but you may need to set them manually.

### Font files cannot be uploaded

Confirm that the file is `.woff2`, `.woff`, or `.ttf`, that the current user has upload permissions, and that the site allows those MIME types through the Font Manager permission path.

### The wrong Google Font loads instead of a custom font

If a custom font and a Google Font share the same family name, Bricks skips the Google font when generating frontend webfont links. If you still see an unexpected font, check for custom CSS or third-party font loading outside Bricks.

---

# Global class import manager

Source: https://academy.bricksbuilder.io/builder/styling/global-class-import-manager/

*Import global classes into Bricks and control how shared class libraries are brought into a project.*

The global class import manager addresses a key challenge in managing imported classes. Previously, conflicting classes were always automatically discarded, and users had no way to prepare or organize classes before importing them.

This feature provides a clear and structured way to handle imported classes, giving users the ability to resolve conflicts, categorize classes, and maintain a clean workflow. To further streamline the process, we’ve included a setting that lets users decide when they’d like to be prompted, ensuring the feature suits their workflow.

![](https://academy.bricksbuilder.io/assets/bricks-class-import-manager.png)

## When does this show up?

The global class import manager opens whenever global classes are imported into the builder. This includes importing a global classes JSON file, pasting elements, or importing a template. Depending on your settings, it can open for specific situations, such as new classes, conflicting classes, or both.

## Types of classes in the import manager

The import manager displays two types of classes:

- **New classes**: These are classes that do not exist in the current site. Users can choose to import and categorize these classes before they are added to the site.
- **Conflicting classes**: These are classes that either share the same name or the same internal ID as an existing local class, but have different settings. Conflicting classes are highlighted in red, and users must resolve each conflict before completing the import. Conflicts can be resolved by:
  - **Overriding the local class**: Replace the existing class with the imported one.
  - **Discarding the conflicting class**: Skip importing the conflicting class.

![](https://academy.bricksbuilder.io/assets/bricks-class-import-manager-override-zoomed.png)

![](https://academy.bricksbuilder.io/assets/bricks-class-import-manager-import-zoomed.png)

## Configuring when the import manager opens

You can control when the global class import manager opens by navigating to **WordPress admin > Bricks Settings > Builder > Global class import manager**. The available options are:

- **Show for class conflicts (default)**: The manager opens only when conflicts are detected. New classes are imported automatically.
- **Show for new classes**: The manager opens for all new classes, allowing users to review and manage them, while conflicting classes are automatically discarded.
- **Show for new & conflicting classes**: The manager opens for both new and conflicting classes, providing full control over the import process.
- **Never**: The manager is disabled. New classes are imported automatically, and conflicting classes are automatically discarded.

---

# Global Class Manager

Source: https://academy.bricksbuilder.io/builder/styling/global-class-manager/

*Create, organize, and maintain CSS classes directly in Bricks with Global Class Manager.*

The Global Class Manager is the central place to maintain your reusable CSS classes in Bricks. It is different from the class selector on an element: the element panel is for assigning and editing classes while you work on a specific element; the Class Manager is for editing custom CSS, organizing, importing, exporting, locking, deleting, and reviewing the whole class library.

Use the Class Manager when your site has more than a few reusable classes or when you maintain a design system across pages, templates, and imported layouts.

For the element-level workflow of assigning and styling classes while editing an element, see [Global CSS Classes](https://academy.bricksbuilder.io/builder/styling/global-css-classes/).

## Accessing the class manager

To access the Class Manager, click the **Style Manager** icon in the builder toolbar. Then select the **Classes** tab.

![](https://academy.bricksbuilder.io/assets/bricks-2.2-style-manager-class-manager-scaled.png)

The Class Manager can be disabled under `Bricks > Settings > General > Disable global class manager`.

Access is also permission-based. A user may be able to use the builder without having permission to access the Class Manager, create classes, edit classes, delete classes, lock classes, or copy and paste class styles.

## What the Class Manager stores

A global class is a site-level record. It can contain:

- A class ID.
- A class name.
- Style settings.
- Breakpoint-specific custom CSS.
- Custom selectors and pseudo-state settings.
- A category.

Bricks also tracks lock state, trash/restore data, and import conflict metadata around those class records so the manager can protect classes and resolve imports safely.

Elements that use a class store a reference to the class. This is why class imports and conflicts matter: a class name is what you see, but Bricks also needs to keep element references mapped correctly.

## Class Manager vs element class selector

Use the element class selector when you want to:

- Add a class to the selected element.
- Remove a class from the selected element.
- Select the active class and edit its styles through element controls.
- Work with element-specific pseudo states and custom selectors.

Use the Class Manager when you want to:

- Create or rename classes without selecting a specific element.
- Edit custom CSS for one selected class.
- Organize classes into categories.
- Bulk rename or duplicate classes.
- Lock or unlock multiple classes.
- Move classes to trash, restore them, or delete them permanently.
- Export and import classes.
- Review usage, conflicts, and imported classes.

## Create and edit classes

In the Class Manager, use the new-class input at the bottom of the class list to create a class.

You can also select one or more classes and use the editor column to:

- Rename one class.
- Bulk rename multiple classes with find/replace, prefix, or suffix.
- Duplicate classes with find/replace, prefix, or suffix.
- Assign selected classes to a category.
- Lock or unlock selected classes.

If you rename or duplicate a class, Bricks checks for duplicate class names and skips names that would conflict.

![](https://academy.bricksbuilder.io/assets/bricks-classes-manager.png)

## Edit custom CSS for a class

Starting in Bricks 2.4, you can edit a class's custom CSS directly in the Class Manager. You do not need to find an element that uses the class first.

Select one class to open its **Custom CSS** editor in the editor column. Use `%root%` to target the selected class:

```css
%root% {
  color: firebrick;
}
```

The breakpoint navigation above the editor lets you add CSS for each responsive breakpoint. An indicator shows which breakpoints contain a value. Changes appear in the canvas preview while you edit, and the indicator on the Class Manager save button shows that the class has unsaved changes.

![](https://academy.bricksbuilder.io/assets/global-class-manager-custom-css.webp)

Click the Class Manager save button to save the CSS with the class. When global class synchronization is enabled, custom CSS changes use the same conflict checks as other class changes.

Renaming or duplicating the class preserves its custom CSS. If the stored CSS contains the previous class root selector, Bricks updates that selector for the renamed or duplicated class. CSS written outside Bricks-managed class settings is not changed.

## Categories

Categories help you organize large class libraries. They do not change CSS output by themselves; they are an organizational layer in the builder.

You can:

- Create categories.
- Rename categories.
- Reorder categories.
- Filter the class list by category.
- Export categories with the classes that belong to them.

If a class has no category, or its stored category no longer exists, Bricks treats it as uncategorized.

## Search, sorting, and filters

Use the Class Manager header to reduce the class list before editing or exporting.

Available filters include:

- Text include/exclude filters.
- Alphabetical sorting.
- Used on this site.
- Unused on this site.
- Used on this page.
- Unused on this page.
- Has styles.
- Has no styles.
- Locked.
- Unlocked.

Usage filters are useful for cleanup, but review results carefully before deleting classes. A class can be unused on the current page and still be used elsewhere.

![](https://academy.bricksbuilder.io/assets/bricks-classes-manager-subheader.png)

## Lock classes

Locking protects classes from accidental changes. A locked class can still exist in the class library and can still be assigned where permissions allow, but its styles and custom CSS cannot be edited until it is unlocked.

If a selection contains a locked class, Bricks also blocks rename and delete actions for that selection. Unlock the class before renaming it, moving it to trash, or deleting it permanently.

Use locks for foundational design-system classes such as layout wrappers, button bases, typography classes, or generated utility classes that should not be changed casually.

Locking is permission-based. Users without lock/unlock permission cannot change the lock state.

## Trash, restore, and permanent delete

Deleting a class from the active list moves it to trash. Trashed classes can be restored from the trash view.

When a class is restored, Bricks attempts to restore it to its previous position. If a class with the same name already exists, Bricks may rename the restored class to avoid the name conflict.

Permanent delete removes the class from the trash. Use permanent delete only after verifying that the class should not be restored.

> **Note**
>
> Moving a class to trash is not the same as removing a class from one element. Removing a class from an element only removes that element's assignment. Moving a class to trash removes the class from the active class library.

## Exporting and importing classes

The Global Class Manager facilitates the exporting and importing of CSS classes, making it easier to maintain a consistent styling framework across various Bricks projects.

### Exporting classes

You have two options for exporting classes:

1. **Export all:** Click the export button at the top of the manager to export the current class library.

![](https://academy.bricksbuilder.io/assets/bricks-classes-manager-export-all-1024x682.png)

2. **Export selected:** Select one or more classes and click the export-selected icon in the classes column.

![](https://academy.bricksbuilder.io/assets/bricks-classes-manager-export-selected-1024x682.png)

Exports include category metadata for classes that belong to a category.

### Importing classes

In the import popup, drag and drop a JSON file containing exported classes.

![](https://academy.bricksbuilder.io/assets/bricks-classes-manager-import-1024x682.png)

![](https://academy.bricksbuilder.io/assets/bricks-classes-manager-import-file.png)

## Import conflicts

When importing classes, Bricks checks for conflicts by class ID and class name.

A conflict can happen when:

- The imported class has the same ID as a local class but different data.
- The imported class has the same name as a local class.
- A template or pasted layout references a class that already exists locally.

Depending on the global class import setting, Bricks can:

- Add new classes automatically and show only conflicts for review.
- Ask you to review new classes.
- Skip conflicting classes.
- Ask you to review both new and conflicting classes.
- Map imported class IDs to existing local class IDs so inserted elements keep a valid class reference.

When reviewing an import, you can accept, reject, rename, duplicate, categorize, lock, or mark conflicting classes to override local classes.

If you're importing global classes and need to handle **conflicts** or organize new classes before they are added to your project, check out the [Global Class Import Manager](https://academy.bricksbuilder.io/builder/styling/global-class-import-manager/). This feature, introduced in Bricks 1.12, provides a structured way to resolve conflicts and categorize imported classes, ensuring a smooth and controlled workflow.

## Template and paste imports

Templates, remote templates, copied elements, and converted layouts can bring global classes with them.

When Bricks inserts content that references imported classes, it must keep the element's class references valid. If the imported class is identical to an existing class, Bricks can map the imported class to the existing one. If the class differs, Bricks can route the class through the import review workflow.

This is why reviewing class imports matters: accepting a class can change the class library, while mapping a class can make the inserted content reuse an existing local class.

## Generated CSS lifecycle

Bricks does not output every class record on every page just because it exists in the Class Manager.

Global class CSS is generated for classes that are used by elements in the current rendered context. Bricks also generates class CSS per element type so element-specific controls can output the correct selectors for that class.

Starting in Bricks 2.4, the **Output global class CSS in Class Manager order** setting under [Bricks settings](https://academy.bricksbuilder.io/builder/setup/settings/#miscellaneous) can make generated global class CSS follow the class order shown in the Class Manager. This affects same-specificity class overrides. It does not make unused classes output CSS.

This has a few practical effects:

- An unused class can exist in the Class Manager without producing frontend CSS on a page.
- A class with no styles can be assigned but may not output useful CSS.
- A class can output different generated rules depending on the element types that use it.
- If a site uses external CSS files, class changes may require Bricks to regenerate CSS files.

## Conflict detection while saving

If global class synchronization/conflict checking is enabled, Bricks can detect when another user changed global classes after your builder session loaded.

The save flow can report:

- Classes added by another user.
- Classes modified by another user.
- Classes deleted or trashed by another user.
- True conflicts where both your session and another session changed the same class.

Resolve the notification before continuing. This protects shared class systems on teams.

## Best practices

- Use clear class names that describe purpose, not only appearance.
- Keep foundational classes locked once they are stable.
- Use categories for large systems such as layout, typography, buttons, cards, utilities, and components.
- Avoid deleting classes based only on the current page's usage filter.
- Review imports before accepting them on client sites.
- Keep utility classes small and predictable.
- Avoid creating several classes that set the same property in conflicting ways.

## Troubleshooting

### A class is in the manager but has no visible effect

Check whether the class is assigned to an element, has styles, and is not overridden by element ID styles or custom CSS.

### I cannot edit a class

The class may be locked, your user role may not have the required permission, or the Class Manager may be disabled.

### I restored a class and its name changed

That can happen when a class with the same name already exists. Rename the restored class if you need a different convention.

### Imported content does not look like the source site

Check whether imported classes were accepted, mapped to local classes, or rejected. Also check whether required variables, color palettes, or theme styles were imported.

---

# Global CSS Classes

Source: https://academy.bricksbuilder.io/builder/styling/global-css-classes/

*Use global CSS classes in Bricks to apply shared styles across multiple elements and keep designs easier to maintain.*

A global CSS class is a reusable Bricks style target. Instead of styling one element's ID only, you create a class, assign it to one or more elements, and edit the class visually with the same controls you use for element styling.

Use global classes for repeated design decisions: buttons, cards, grids, spacing wrappers, headings, badges, form rows, or any element pattern that should stay consistent across a page or site.

https://youtu.be/V9bzI6poe-Y

## The mental model

Every element in Bricks has an element ID. When no global class is selected, visual style controls apply to that element ID only.

When a global class is selected as the active selector, style controls apply to the class instead. Any element that uses that class can receive the same class styles.

Think of the selector field at the top of the element panel as the current styling target:

- `#my-element`: you are styling only that element.
- `.card`: you are styling the global class named `card`.
- `.card:hover`, `.card::before`, or another selector/pseudo state: you are styling that state or selector for the class.

The important part is the active class state. Adding a class to an element and selecting that class are related, but not identical:

- Assigned class: the element uses the class on the frontend.
- Active class: the builder controls currently write styles to that class.

If you add `.card` to an element, then deselect the class, you are back to styling the element ID. If you select `.card`, your style changes update the class.

## Class styles vs element ID styles

Element ID styles are more specific than global class styles. If the same CSS property is set on both the element ID and a global class, the element ID style usually wins.

Use that on purpose:

- Put shared defaults on the class.
- Put one-off overrides on the element ID.
- If a style is meant to be reusable, avoid leaving the same property on the element ID.

> **Note**
>
> If a class appears not to work, check whether the selected element already has the same property set on its element ID, page settings, or custom CSS.

## How to create a global class

![](https://academy.bricksbuilder.io/assets/adding-global-classes-bricks.png)

1. Select any element by clicking on it in the canvas or via the structure panel.
2. Click the selector input that shows the element's ID under its name in the left panel.
3. Type a class name in the class input.
4. Press `Enter` or click the save icon.
5. Select the class so it becomes the active selector.
6. Change style controls as needed.

Bricks accepts class names with or without a leading dot. The builder stores the class name without the dot and displays it as `.class-name`.

You can enter more than one class name separated by spaces or commas when creating classes. Bricks creates the missing classes and reuses existing classes with the same name.

## Assign an existing class to an element

1. Select the element.
2. Open the selector/class dropdown at the top of the element panel.
3. Search for the class name.
4. Click the class to add it to the element.

The class then appears in the element's active class list. Click the class chip to make it active for editing. Click the close icon on the chip to remove it from the element.

Removing a class from an element does not delete the global class. It only removes that class assignment from the selected element.

## Deselect a class before styling the element itself

When a global class is active, the style controls edit the class. To return to the element ID:

1. Click the active selector field.
2. Choose the element ID entry, or click the clear icon.
3. Confirm the selector field shows the element ID instead of the class name.

This is the safest way to avoid accidentally changing every element that uses the class.

## Multiple classes on one element

An element can have multiple global classes. This lets you separate responsibilities:

```text
.button
.button--primary
.margin-top-l
```

A common pattern is:

- One base class for structure and default styling.
- One modifier class for a variation.
- One utility class for a single property such as spacing or color.

When two classes set the same property with similar specificity, normal CSS cascade rules decide the final value. Avoid relying on conflicting class definitions as your main workflow. It is clearer to keep each class focused.

Starting in Bricks 2.4, admins can enable **Output global class CSS in Class Manager order** under [Bricks settings](https://academy.bricksbuilder.io/builder/setup/settings/#miscellaneous). When enabled, same-specificity global class rules follow the class order in the Class Manager. When disabled, Bricks uses the previous output order based on how classes are encountered on rendered elements.

## Pseudo classes and custom selectors

Global classes can have pseudo-class and custom-selector styles.

Use pseudo classes for states such as:

```text
:hover
:focus
:active
```

Use custom selectors when you need to style a child or related selector from the class context. For example, you might style an icon inside a card class, or a nested heading inside a reusable wrapper.

When a selector starts with `:`, Bricks attaches it directly to the class selector. Other selectors are treated as nested selectors.

> **Tip**
>
> Use class selectors for reusable states and child styling. Use element ID selectors only for one-off exceptions.

## Copy, paste, reset, and rename class styles

The class selector actions let you work with styles without manually copying CSS:

- Copy styles from an element ID or class.
- Paste styles into an element ID or class.
- Reset styles on an element ID.
- Reset styles on a class.
- Rename the element CSS ID or the active class.

When a class is renamed, Bricks updates the class name and also updates custom CSS stored inside that class where the old class root selector is used.

Renaming a class does not rename unrelated CSS that you wrote outside Bricks-managed class settings.

## Locked classes

Locked classes cannot be edited until they are unlocked. This protects shared design-system classes from accidental changes while still allowing them to be assigned where permissions allow.

If a class is locked and you cannot edit it, check whether your user role has permission to lock, unlock, and edit global classes.

## Bulk editing

When multiple elements are selected, the global classes panel shows classes that all selected elements have in common. You can add or remove a class across the selected elements.

Bulk editing is useful for applying a shared utility or layout class to multiple elements. It is not the right place to do detailed per-element cleanup.

## Permissions and disabled interface

Administrators can control access to global class features. Depending on your permissions, you may be able to:

- Create global classes.
- Edit global classes.
- Assign or unassign classes.
- Delete global classes.
- Lock or unlock classes.
- Copy and paste global class styles.

Administrators can also disable the Global Class Manager under `Bricks > Settings > General > Disable global class manager`. That hides the manager tab. Element-panel class actions are controlled by the global-class permissions above.

## Relationship to Class Manager

The element panel is where you apply a class and edit the active class while working on an element.

The Global Class Manager is where you maintain the class library: custom CSS for a selected class, categories, bulk renaming, locks, trash, import/export, usage filters, and conflict review.

You can create and use classes from either workflow, but they serve different jobs:

- Element panel: "Use or edit this class on this element."
- Class Manager: "Maintain the whole class system."

## Relationship to utility classes

Some Style Manager features can generate utility classes from colors or variable scales. Those utility classes are stored as global classes too, so they can appear in the class list and be assigned like other classes.

Generated utility classes are best used as small, single-purpose classes. Avoid editing them into large component classes unless that is intentional.

## Troubleshooting

### The class is assigned, but the style does not show

Check these first:

1. Is the class selected as the active selector when you edit it?
2. Does the element ID already set the same property?
3. Is the class locked?
4. Does the class have styles for the current element type?
5. Is the class output affected by custom CSS with higher specificity?

### I changed a class and many elements changed

That is expected. A global class is reusable. If only one element should change, clear the active class and style the element ID instead, or create a more specific modifier class.

### I cannot create or edit a class

Check your builder permissions and whether the Global Class Manager is disabled in Bricks settings.

### A class from an imported template conflicts with an existing class

Bricks tracks classes by ID and name. If an imported class has the same ID or name as a local class, Bricks may map it to the existing class or ask you to review the conflict, depending on your import settings.

Review conflicts before accepting imports on production sites, especially when classes are part of a design system.
