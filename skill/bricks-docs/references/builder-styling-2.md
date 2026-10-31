# Global Variables Manager

Source: https://academy.bricksbuilder.io/builder/styling/global-variables-manager/

*Manage reusable design tokens in Bricks with Global Variables Manager for consistent spacing, sizing, and color values.*

The Global Variables Manager lets you create and maintain reusable CSS custom properties in Bricks.

Use global variables for values that should stay consistent across controls, classes, templates, and pages: spacing sizes, typography sizes, radii, layout widths, color values, shadows, or any repeated design token.

For example, instead of typing `clamp(1rem, 2vw, 1.5rem)` into several controls, create a variable named `text-m` and use `var(--text-m)` wherever that value is needed.

https://www.youtube.com/watch?v=K-c6OFHVhpQ

## Accessing the Variable Manager

To access the Variable Manager, click the **Style Manager** icon in the builder toolbar. Then select the **Variables** tab.

The **Categories** column lists your variable categories next to **All** and **Uncategorized**. Color palettes from the [Color Manager](https://academy.bricksbuilder.io/builder/features/color-manager/) appear there too, marked with a **COLORS** badge, because every palette color is also a CSS variable (for example `moss` for `var(--moss)`).

![Style Manager Variables tab with the categories All, Uncategorized, Radius, Shadows, Layout and two color palettes, next to the variable list.](https://academy.bricksbuilder.io/assets/bricks-style-manager-variables-categories.webp)

You can disable the Variable Manager under `Bricks > Settings > General > Disable CSS variables manager`.

The variable picker value display can be hidden under `Bricks > Settings > Builder > Variable dropdown: Hide value`.

## The mental model

Global variables are stored as site-level Bricks data. A variable has:

- An internal ID.
- A name, stored without the leading `--`.
- A value.
- An optional category.

On the frontend, Bricks outputs variables as CSS custom properties with the `--` prefix:

```css
:root {
  --text-m: clamp(1rem, 2vw, 1.5rem);
}
```

In a Bricks control or CSS field, use the variable like this:

```css
var(--text-m)
```

Bricks only outputs variables that have a name and a non-empty value.

## Create a variable

1. Open **Style Manager > Variables**.
2. Optional: select the category the variable belongs to. A new variable is added to the selected category. To create a category, type its name into **New category name** below the list and press `Enter`; the new category is selected right away.
3. In the **New variable name** field, enter a name without the leading `--`, such as `space-m`. Bricks adds the `--` prefix for you.
4. In the **Value** field, enter the value, such as `clamp(1rem, 2vw, 2rem)`.
5. Press `Enter` or click the save icon at the end of the row.
6. Click **Save** in the Style Manager toolbar to store your changes.

If you paste a name that starts with `--` or `var(--...)`, Bricks normalizes it to the stored variable name.

Variable names must be unique. Bricks also prevents duplicate variable names that conflict with variable-based colors in the Color Manager.

![](https://academy.bricksbuilder.io/assets/bricks-css-variables-manager.png)

## Use variables in controls

Many builder controls include a variable picker: the small CSS icon at the end of the field. Open the picker and select a variable to insert it into the active control.

The picker has a search field and groups the variables by category, including **Uncategorized** and your color palettes. Open a group to see its variables.

The picker inserts a `var(--name)` reference. If the sides of a control are linked, such as the four corners of **Border > Radius**, picking a variable for one side sets all linked sides. You can also type `var(--name)` manually in controls that accept CSS values.

<div className="screenshot screenshot--control-panel">

![Border settings of an image. The radius fields show var(--radius-card), and the open variable picker lists the groups Uncategorized, Radius, Shadows, Layout, Default and Fernlow.](https://academy.bricksbuilder.io/assets/bricks-variable-picker-categories.webp)

</div>

Variables are useful in:

- Element ID styles.
- Global class styles.
- Theme Styles.
- Page settings.
- Custom CSS fields.
- Other Bricks-managed style settings that accept CSS values.

## Update, rename, duplicate, and delete variables

Click a variable in the list to select it. A selected variable's name and value become editable in place: change them and press `Enter`. Clicking the same row again clears the selection.

To select several variables, click the first one and `Shift`-click the last one, or use the select-all checkbox in the list header. With more than one variable selected, an **Edit** panel opens next to the list with three tabs:

- **Rename**: rename the selected variables at once with **Find** and **Replace with**, **Add prefix**, or **Add suffix**. The **Preview** shows the new names before you click **Rename**.
- **Categorize**: move the selected variables into a category. Choose it under **Category** and click **Update**. This tab appears once at least one category exists.
- **Duplicate**: create copies of the selected variables.

The list header also has icons to export the selected variables, move them to the trash, and clear the selection. You can reorder variables by drag and drop.

![Variables tab with card-shadow and card-shadow-hover selected. The Edit panel shows the Rename tab with Find card-shadow, Replace with shadow-card, and the preview of the new names.](https://academy.bricksbuilder.io/assets/bricks-variables-bulk-rename.webp)

When a variable is renamed, Bricks updates Bricks-managed references from `var(--old-name)` to `var(--new-name)` in builder data. This update runs in the builder and again on save.

> **Note**
>
> Variable rename updates apply to Bricks-managed data. A `var(--old-name)` typed into an element's **Custom CSS** field keeps the old name, and so does CSS written outside Bricks-managed settings. Update those references manually.

## Categories

Categories organize variables in the manager and picker. They do not change the variable name by themselves.

You can:

- Create categories.
- Rename categories.
- Reorder categories.
- Filter variables by category.
- Export categories with selected variables.

If a variable has no category, or its category no longer exists, Bricks treats it as uncategorized.

## Search, sorting, and usage filters

Use the manager header to narrow the variable list:

- **Name (Include)** shows only variables whose names contain the text.
- **Name (Exclude)** hides variables whose names contain the text. Combine both, for example `shadow` included and `hover` excluded.
- **Sort** orders the list alphabetically.
- **Filter** shows only the variables **Used on this page** or **Unused on this page**. A selected filter appears as a tag in the field; click its remove icon to clear it.

![](https://academy.bricksbuilder.io/assets/bricks-css-variables-manager-subheader.png)

Usage filters are helpful for cleanup, but review before deleting. A variable can be unused on the current page and still be used elsewhere.

## Scales and utility classes

Style Manager scales use variable categories. A typography or spacing scale is stored as a variable category with scale settings.

A scale can generate variables such as:

```text
text-xs
text-s
text-m
text-l
space-xs
space-s
space-m
space-l
```

Scale categories can also define utility class patterns. For example:

```text
Class name: text-*
CSS property: font-size
```

For a variable named `text-m`, Bricks can generate:

```css
.text-m {
  font-size: var(--text-m);
}
```

If a class pattern does not contain `*`, Bricks appends the scale step name to the class pattern.

Generated utility classes are part of the Style Manager CSS output and are also reflected in the builder preview.

## CSS output

Global variables with non-empty values are output as `:root` CSS custom properties.

Bricks also generates a Style Manager CSS file when relevant Style Manager data changes. That file can contain:

- Color palette variables.
- Color utility classes.
- Variables from scale categories.
- Utility classes generated from scale categories.

If the Style Manager CSS file exists, Bricks enqueues it on the frontend. If file generation fails because of filesystem permissions, cache configuration, or another environment issue, regenerate Bricks CSS files and check the site's file permissions.

## Exporting and importing variables

Export and import variables to reuse the same set across Bricks sites.

### Exporting variables

You have two options for exporting variables:

1. **Export all:** Click the export button at the top of the manager to export all variables and categories.

![](https://academy.bricksbuilder.io/assets/bricks-css-variables-manager-export-all.png)

2. **Export selected:** Select one or more variables and click the export-selected icon in the variables column.

![](https://academy.bricksbuilder.io/assets/bricks-css-variables-manager-export-selected-1024x682.png)

Selected exports include the categories used by the selected variables.

### Importing variables

You can import variables in three ways:

**Importing via JSON file:** In the import popup, drag and drop a JSON file containing exported variables.

![](https://academy.bricksbuilder.io/assets/bricks-css-variables-manager-import-1024x682.png)

![](https://academy.bricksbuilder.io/assets/bricks-css-variables-manager-import-file-1024x682.png)

When importing a JSON file, Bricks adds variables that do not already exist by name. If the file includes categories, Bricks can also import categories that do not already exist by name.

**Manual text entry:** You can manually enter variables into a textarea. This is useful for quickly importing variables from a child theme, custom plugin, stylesheet, or snippet.

The expected format is a semicolon-separated list of CSS variable definitions:

```css
--bricks-color-primary: #ffd64f;
--bricks-color-secondary: #fc5778;
--bricks-text-dark: #212121;
```

![](https://academy.bricksbuilder.io/assets/bricks-css-variables-manager-import-textarea-1024x682.png)

Manual imports add variables that do not already exist by name.

**Importing from remote templates:** When inserting a remote template, Bricks can offer to import variables from the remote source. Remote template variables are matched by name. New variables can be imported; existing local variables with the same name are not duplicated.

Remote template variable categories are not imported with the template variables, so imported variables may appear uncategorized.

## Best practices

- Name variables by purpose: `space-m`, `radius-card`, `text-step-2`.
- Use variables for repeated values, not every one-off value.
- Keep values valid CSS for the controls where you plan to use them.
- Prefer scale-generated variables for typography and spacing systems.
- Avoid renaming variables casually on production sites with lots of custom CSS.
- After large variable changes, regenerate Bricks CSS files and review important templates.

## Troubleshooting

### A variable does not appear in the picker

Check whether the variable exists, has a valid name, and whether the current control supports variable insertion.

### A variable exists but does not output CSS

Check whether it has a non-empty value. Bricks skips variables with empty values.

### A renamed variable still appears in custom CSS

Bricks updates Bricks-managed `var(--old-name)` references. External stylesheets, child theme CSS, custom plugin CSS, or manually written code outside Bricks-managed data may still need manual updates.

### Imported variables are uncategorized

Remote template variable imports do not import variable categories. JSON imports can import categories when the file includes them and you confirm the category import.

### Utility classes are missing

Check that the variable category is a scale, that utility classes are configured for that scale, and that Bricks can generate and enqueue the Style Manager CSS file.

---

# Gradients & Overlays

Source: https://academy.bricksbuilder.io/builder/styling/gradients-overlays/

*Create gradients and overlays in Bricks to add layered backgrounds, image treatments, and color effects.*

Spice up your site's design by adding background, overlay, and text gradients to any element. When editing an element, the Gradients & Overlays control group is under the Style tab.

https://youtu.be/U0x0vCAzuc0

## Available controls:

- **Apply to**: Select the type of content you want to add a gradient to (text, background, overlay).
- **CSS selector**: To target a specific HTML within an element.
- **Colors**: Add at least two colors to see a gradient. When you apply the gradient to an overlay make sure to reduce the color transparency in order to see through it.
- **Type**: Choose the gradient type—linear, radial, or conic.
- **Repeat (since 1.9.4)**: Allows the gradient to repeat across the element. Define 'stops' to control the transition points of each color, using units like percentages or pixels.

### Linear gradient controls:

- **Angle in °**: Set a specific angle for your linear gradient between 0 to 360°.

### Radial gradient controls:

- **Shape**: Choose between 'circle' or 'ellipse'.
- **Size**: Select from 'closest-side', 'farthest-side', 'closest-corner', 'farthest-corner'. For details on these settings, see the [Mozilla Documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/gradient/radial-gradient#size).
- **Position**: Define the central point of the gradient.

### Conic gradient controls:

- **Starting angle in °**: Specify the starting angle of the gradient between 0 to 360°.
- **Position**: Set the gradient's center.

---

# Hover Styles

Source: https://academy.bricksbuilder.io/builder/styling/hover-styles/

*Style hover states in Bricks so links, buttons, cards, and other interactive elements respond consistently.*

Bring your site to life and boost visitor engagement by styling the hover state of any interactive element.

In the builder, select the element or class you want to style. Open the pseudo-class menu and choose `:hover`. Any styles you add while `:hover` is active are saved to that hover state instead of the default state.

Use the same pseudo-class workflow for global classes, element ID styles, and other supported states. Learn more in [Styling Element States & Parts](https://academy.bricksbuilder.io/builder/styling/pseudo-classes/).

---

# Understanding The Layout

Source: https://academy.bricksbuilder.io/builder/styling/layout/

*Understand the Bricks layout model so you know when to use sections, containers, blocks, divs, flexbox, and grid.*

Bricks has four layout elements (since 1.5) to group & lay out your content in a fast, predictable, and streamlined approach:

- **Section**: Use to structure/divide your page (think: one topic per section)
- **Container**: Contain elements at 1100px width (centered)
- **Block**: Flexbox with 100% width (e.g. column)
- **Div**: Plain, unstyled div (grows according to inner elements)

![](https://academy.bricksbuilder.io/assets/bricks-layout-elements-1024x626.png)

<figcaption>

Two-column layout inside a section

</figcaption>

If you are new to web design, we recommend using the Section, Container, and Block element. As they come with presets that work well out-of-the-box without having to configure commonly used settings for every layout element.

![](https://academy.bricksbuilder.io/assets/Bricks-1.5-Layout-Elements.png)

**The Section, Container, & Block element are just Divs with some presets**. By default they use the [flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox) layout model. So you can easily direct, align, and space out elements inside of them.

**The Div element is the most basic element to group & lay out your content.** In Bricks the Div is plain (no predefined styles). So you can style it any way you want.

All layout elements expose a **Display** control. You can keep the flex defaults, switch to `grid` to use CSS grid controls, or use `block`, `inline-block`, `inline`, or `none` when the layout calls for it.

You can customize the defaults of any layout element in your [Theme Styles](https://academy.bricksbuilder.io/builder/styling/theme-styles/).

Quick overview of the main properties of each layout element:

| **Element ** | ** Tag** | **Display** | **Width** | **Where To Use** |
| --- | --- | --- | --- | --- |
| Section | `section` | flex | 100% | Root level |
| Container | `div` | flex | 1100px | Inside Section |
| Block | `div` | flex | 100% | Inside Section or Container |
| Div | `div` | No Bricks display preset | - | Anywhere |

## Section {#section}

Use sections as the outermost building block. To separate & space out individuals parts of your page.

A section takes up 100% of the available width. It adjusts in height according to its content. Sections are stacked on top of one another.

When adding a new Section, a "Container" element is automatically added inside the section.

You can remove this Container if you don't need to "contain" any other elements inside of it. As we did in the following hero section example:

![](https://academy.bricksbuilder.io/assets/bricks-hero-section-1024x576.jpg)

<figcaption>

Example: Hero Section (height: 100vh)

</figcaption>

You can overwrite the section defaults under Style Manager → Theme Styles → Element - Section.

To space out your sections, you can set the `margin` or `padding` to your liking. You can also change the default `display` and `height` values.

*Learn more: [Section element](https://academy.bricksbuilder.io/builder/elements/layout/section/)*

## Container {#container}

A Container is automatically centered, and has a default width of 1100px. Which you can customize under Style Manager → Theme Styles → Element - Container.

Place your Container inside a Section. And Block / Div elements inside your Container for a multi-column or multi-row layout.

The following screenshot shows a Container (with 60px `padding`) inside a Section (with `background-image`):

![](https://academy.bricksbuilder.io/assets/bricks-container-inside-section-1024x576.jpg)

*Learn more: [Container element](https://academy.bricksbuilder.io/builder/elements/layout/container/)*

## Block {#block}

The Block element provides the same controls as the Container (layout, query loop, etc.). The difference is that the Block uses a default width of 100% instead of a predefined 1100px width like the Container.

Use the Block element to create equal column/row layouts inside a Section or Container.

*Learn more: *[Block element](https://academy.bricksbuilder.io/builder/elements/layout/block/)

### How To Create Multi-Column Layouts {#columns}

To create a three-column layout inside a Container:

1. Select the Container
2. Change "Direction" to "Horizontal"
3. Click the little "+" icon on the canvas 3x to insert 3 Block elements.

The result should look like this:

![](https://academy.bricksbuilder.io/assets/bricks-blocks-inside-container-1024x459.jpg)

<figcaption>

Section > Container > 3 Blocks: 3-column-layout

</figcaption>

The fastest way to create a multi-column layout is to select the Container, click the little "column" layout icon on the canvas, and select the pre-defined column layout of your choice:

![](https://academy.bricksbuilder.io/assets/bricks-insert-layout-tool-1024x293.jpg)

<figcaption>

"Insert Layout" Tool

</figcaption>

[By default](#default), the inserted layout consists of "Block" elements. The "Column" label is just that: a label. It's still a Block element. Visible by the icon in the structure panel. You can also see the element name when you hover over the element icon in the structure panel:

![](https://academy.bricksbuilder.io/assets/bricks-3-column-block-layout-1024x256.jpg)

## Div {#div}

The Div element is the most generic element to group and lay out your content.

In contrast to the other layout elements, **the Div element in Bricks is completely unstyled**. Giving you 100% freedom regarding its markup & styling.

When used inside one of the other layout elements the Div grows and shrinks according to the elements it contains.

*Learn more: *[Div element](https://academy.bricksbuilder.io/builder/elements/layout/div/)

## How to Insert, Wrap, and Convert layout elements {#actions}

You can right-click on any layout element to reveal the context menu. From there you can "Insert", "Wrap", and "Convert" layout elements with one click.

The screenshot below shows how to convert a root Container to a Section by right-clicking on the "Hero" Container in the structure panel, and then selecting the "Section" icon under "Convert":

![](https://academy.bricksbuilder.io/assets/bricks-1.5-context-menu-convert-to-section-1024x550.jpg)

<figcaption>

Context menu: Convert "Container" into a "Section"

</figcaption>

When editing a layout element, you can insert any other layout element by hovering over the "+" icon on the canvas, which provides you with "Container", "Block", "Div" options.

Hold down "CMD / CRTL" to insert an element after the active element.

![](https://academy.bricksbuilder.io/assets/bricks-1.5-element-action-insert.png)

### Element actions: Setting the default element {#default}

Under "Bricks → Settings → Builder → Element actions" you can change the layout element that's being used by default for "Insert", "Wrap", and the "Layout" tool:

![](https://academy.bricksbuilder.io/assets/bricks-1.5-setting-element-actions-1024x363.png)

### Optional: Converting your Container-based layout

To convert your existing "Container"-based site to use the new "Section" & "Block" elements, you can run the Converter with the **'Convert "Container" to new "Section" & "Block" elements'** option enabled:

![](https://academy.bricksbuilder.io/assets/bricks-1.5-convert-container-to-section-block-1024x192.png)

<figcaption>

Located under: Bricks > Settings > General > Converter

</figcaption>

## Masonry layout {#masonry}

Starting at Bricks 1.11.1 you can enable the "Masonry layout" for all layout elements under `Style > Layout > Masonry`. Learn more at [/builder/styling/masonry-layout/](https://academy.bricksbuilder.io/builder/styling/masonry-layout/)

---

# Masonry Layout

Source: https://academy.bricksbuilder.io/builder/styling/masonry-layout/

*Create masonry-style layouts in Bricks and understand the current options and constraints for staggered grids.*

Starting with version 1.11.1, you can easily apply a masonry layout to any layout element in Bricks.

The new Masonry Layout controls are available under `Style > Layout > Masonry` for all layout elements (Section, Container, Block, Div).

![](https://academy.bricksbuilder.io/assets/masonry-layout-controls.png)

Bricks utilizes the [IsotopeJS](https://isotope.metafizzy.co/) library to create the masonry layout, which it also uses for the **Image Gallery** and **Posts** elements, for optimal performance.

## How It Works {#how-it-works}

When the Masonry layout is enabled, all direct child elements become masonry items.

You can customize the number of columns and adjust spacing for different breakpoints to achieve a responsive layout.

> **Note**
>
> **Tip:** Ensure that no conflicting CSS styles are applied to the masonry-enabled element, as they may interfere with the masonry layout. It’s best to clear all custom styles for the element to allow the masonry effect to work smoothly.

You can also use the masonry layout to wrap items in a **query loop** for a dynamic grid effect. This is particularly useful for layouts with posts, products, or any repeated content, enabling you to display query items in a visually engaging, staggered grid format.

![](https://academy.bricksbuilder.io/assets/masonry-layout-example-query-loop.png)

## Use Bricks Interaction Animation

If you want to apply custom animations using the **Interactions** panel (e.g., setting an **Entry Viewport Trigger** and **Start Animation** for masonry children), you can disable the default masonry animations by setting **Transition: Duration** to `0`.

This prevents any overlap between the default masonry transitions and your custom animations, ensuring a smoother effect.

![](https://academy.bricksbuilder.io/assets/masonry-layout-disable-animation.png)

## Troubleshooting {#troubleshoot}

### Custom CSS Conflicts

If the masonry columns don’t align with your settings, inspect the CSS styles applied to the child elements. Styles such as **width**, **flex-basis** or **align-self** within flex layouts can override the masonry column settings. Adjust or remove these styles to ensure the masonry layout functions as expected.

### Dynamic Content Updates via Custom JavaScript/AJAX

If you have custom code/plugins that adds masonry child nodes via JavaScript or AJAX, it’s likely that the masonry layout may not update correctly. To fix this, you can manually refresh the masonry instance by running the following JavaScript.

```php
bricksUtils.updateIsotopeInstance('BRICKS_ID');

```

Replace `'BRICKS_ID'` with the specific ID of your masonry element. This function will reinitialize the masonry layout to accommodate the new nodes, ensuring the layout remains intact.

![](https://academy.bricksbuilder.io/assets/masonry-copy-bricks-id-2.png)

---

# Styling Element States & Parts

Source: https://academy.bricksbuilder.io/builder/styling/pseudo-classes/

*Style different element states and parts in Bricks with pseudo-classes, pseudo-elements, and responsive variants.*

Bricks lets you apply different styles to an element depending on its state (such as on mouse `:hover` or a `:visited` link) via pseudo-classes.

You can also apply different styles to specific parts of an element via pseudo-elements. Such as the `::first-letter` or the `::first-line`.

The video below shows how to work with pseudo-classes & pseudo-elements in Bricks (1.3.5+) and how you can add pseudo keywords yourself to Bricks:

https://youtu.be/38tXZSkw40U

<figcaption>

How to work with pseudo-classes & pseudo-elements in Bricks.

</figcaption>

> **Note**
>
> You can style pseudo-classes and pseudo-elements on individual elements, global classes, and in Theme Styles.

## How to edit a specific element state or part of an element

Click the cursor icon (**Selectors**) next to the selector field in the Element panel to toggle the pseudo-class menu:

![](https://academy.bricksbuilder.io/assets/toggle-pseudo-classes-1.png)

Click the text input to reveal all available pseudo-classes & pseudo-elements:

![](https://academy.bricksbuilder.io/assets/default-pseudo-classes.png)

## How to create your own pseudo-classes & pseudo-elements

By default, Bricks shows `:hover`, `:active` and `:focus` pseudo-classes, but you can add other pseudo-classes or pseudo-elements yourself.

Simply type out the pseudo-class or pseudo-element you want to create (such as `:visited`) and press enter or click the little save icon:

![](https://academy.bricksbuilder.io/assets/adding-other-pseudo-classes.png)

## Edit styles for element states or parts

Click the **Selectors** icon next to the selector field to open the pseudo-class menu. Another click inside the text input reveals all available pseudo-classes & -elements. Select the one you want to edit.

![](https://academy.bricksbuilder.io/assets/edit-styles.png)

The "active" pseudo keyword will now show highlighted in the right corner. The **Selectors** icon will appear highlighted as well, indicating you're now editing the styles for a pseudo-class or pseudo-element:

![](https://academy.bricksbuilder.io/assets/edit-states-styles.png)

At this point, changing the styles controls will only affect the active pseudo-class or pseudo-element. To leave the state, open the Selectors menu and click it again. Avoid using X if you want to keep editing the active global class: X also deselects the class, so further changes apply to the element ID.

After that, you'll notice the input will show a little indicator of how many pseudo-classes or pseudo-elements are configured to this element or theme style:

![](https://academy.bricksbuilder.io/assets/pseudo-classes-assigned.png)

To clear the styles associated with a pseudo-class or a pseudo-element, open the dropdown list where you'll notice a little dot indicator for the states that have styles associated with them. To clear the styles of a specific state, click the dot indicator:

![](https://academy.bricksbuilder.io/assets/clear-styles-pseudo-classes.png)

## Deleting pseudo keywords

You can delete custom-added pseudo-classes or pseudo-elements (except the ones Bricks adds by default).

To do so, open the pseudo-class menu, reveal the dropdown, hover with your mouse over the pseudo keyword you want to delete. Then click the "bin" icon.

![](https://academy.bricksbuilder.io/assets/delete-pseudo-class.png)

> **Note**
>
> Deleting a custom pseudo keyword removes it from the list site-wide. Existing styles are kept. Add the keyword again to edit those styles.

## Example 1: Style a child class when a parent is hovered

Let's say there's a Div having a Heading element and that the heading has a class called `text--blue` with blue color text. Now you want to change the heading text to a different color when the Div is hovered.

For this:

1. Set a padding of say 40px all around for the Div element so the end result can be seen.
2. Select the Div.
3. Click the **Selectors** icon.
4. Click in the input field.
5. Type `:hover .text--blue` and hit return or click the Save (floppy) icon.
6. With the Div element still as the current element that is selected, go to STYLE → TYPOGRAPHY, click the Color control's circle and set your desired color.

Save and check the frontend. Hovering the Div should change the heading color.

Resources (list of available pseudo keywords):

[https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes)

[https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements)

---

# Scroll Snap

Source: https://academy.bricksbuilder.io/builder/styling/scroll-snap/

*Use CSS Scroll Snap in Bricks to create scroll-controlled sections, sliders, and other snapping layouts.*

With the introduction of scroll snapping in Bricks 1.9.3, enhancing your web pages with sophisticated scrolling effects has never been easier.

In our latest video, we provide a step-by-step guide on using scroll snap in Bricks, including how to set it up on a page and fine-tune it for individual elements.

https://www.youtube.com/watch?v=LoKCda8uDNw

## Page-level scroll snap

Open the page settings and use the **Scroll snap** controls to set the page scroll snap **Type**. Bricks applies `scroll-snap-type` to `html` and, by default, applies snap alignment to `.brxe-section`.

You can change the **Snapping elements selector** if your snap items are not sections. The **Align**, **Margin**, **Padding**, and **Stop** controls let you fine-tune the snapping behavior.

## Element-level scroll snap

Layout elements also expose scroll snap controls under their layout settings. Use these when a specific element should become its own scroll snap container or when you need element-level snap alignment, margin, or stop behavior.

> **Note**
>
> Scroll snap is disabled inside the builder preview. Check the page on the frontend to verify the actual snapping behavior.

For an in-depth look at the CSS properties behind this feature, such as `scroll-snap-align`, `scroll-snap-type`, and more, please visit [https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_scroll_snap](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_scroll_snap)

---

# Shape Dividers

Source: https://academy.bricksbuilder.io/builder/styling/shape-dividers/

*Add and style shape dividers in Bricks to separate sections with SVG-based visual transitions.*

Give your design an edge by adding an unlimited number of shape dividers such as tilts, drops, grids, clouds, strokes, triangles, waves, etc. to layout elements: Section, Container, Block, and Div.

Shape dividers are available in the element style panel under **Shape Dividers**. You can add multiple dividers, choose a bundled shape or custom SVG, and control fill color, front/back placement, flipping, overflow, size, rotation, alignment, and offsets.

https://youtu.be/rXhgQ5fsKDc

---

# Theme Styles

Source: https://academy.bricksbuilder.io/builder/styling/theme-styles/

*Set up Bricks theme styles so colors, typography, buttons, forms, and other defaults stay consistent across the site.*

Theme Styles are site-level style defaults in Bricks. Use them to define the baseline look for pages, templates, and elements: typography, links, colors, contextual spacing, buttons, forms, images, layout elements, popups, and other element defaults.

Theme Styles are not a replacement for global classes or element styles. They are the broadest styling layer. More specific styles can override them.

Use Theme Styles for defaults that should apply to a context. Use global classes for reusable patterns. Use element ID styles for one-off exceptions.

## Access Theme Styles

Open the builder, click the **Style Manager** icon, and select **Theme Styles**.

To create a Theme Style:

1. Open the Theme Styles selector.
2. Type a name.
3. Press `Enter` or click the save icon.
4. Select the Theme Style.
5. Add conditions.
6. Configure the style groups.

https://youtu.be/SgTBp34J3CQ

## The mental model

A Theme Style has two important parts:

- Conditions: where the Theme Style applies.
- Settings: which defaults it outputs.

On each frontend request, Bricks checks the Theme Style conditions against the current context. Matching Theme Styles become active. Bricks then generates CSS from the active Theme Style settings.

The builder also calculates the active Theme Style for the page you are editing, so the Theme Styles panel can show active styles separately from other styles.

## Style hierarchy

Theme Styles are baseline styles. They are output before more specific Bricks-managed CSS such as global classes, page settings, template content, element settings, and popup styles.

Practical result:

- Theme Style sets the default.
- Global class styles can override matching Theme Style defaults.
- Page settings can override matching Theme Style defaults.
- Element ID styles can override matching Theme Style defaults.
- Custom CSS with stronger selectors or later output can override Theme Styles.

Example:

1. Theme Style sets all buttons to black text.
2. A global class `.button--primary` sets button text to white.
3. A specific button ID sets text to red.

The specific button ID wins for that button because it is more specific and output later.

## Conditions {#conditions}

Open the **Conditions** control group to tell Bricks where on your site this Theme Style should be used.

To apply a Theme Style to your entire website, open **Conditions**, click **Add Condition**, and select **Entire website**. When you create the first Theme Style on a site, Bricks adds the **Entire website** condition for you.

You can set as many Theme Style conditions as you want.

For example, to apply a Theme Style to two specific landing pages and your home page:

1. Add a condition for the individual landing pages.
2. Add another condition for **Front page**.

The Theme Style matches when any non-excluded condition matches the current context.

### Exclude condition {#exclude}

Since Bricks 1.3.6 you can set exclude conditions for any Theme Style. To exclude a specific condition, toggle the exclude control. If the exclude condition applies, Bricks does not use that Theme Style for the current context.

![](https://academy.bricksbuilder.io/assets/theme-style-exclude-condition.png)

<figcaption>

Use this Theme Style everywhere except for the Privacy Policy page

</figcaption>

## Active Theme Style resolution

When multiple Theme Styles match a page, Bricks scores the matching conditions by specificity.

Common specificity order:

- Entire Website: broadest match.
- Archive or generic archive conditions.
- Post type conditions.
- Specific archive, term, search, error, or child conditions.
- Front page.
- Specific post/page IDs: most specific common match.

The exact match can depend on the current request, preview context, archive type, taxonomy, post type, multilingual translation, and custom condition filters.

By default, Bricks loads only the most specific matching Theme Style.

For example:

- Theme Style A targets **Entire Website**.
- Theme Style B targets **Pages**.
- Theme Style C targets a specific page.

On that specific page, Theme Style C is the most specific match and is the one Bricks loads by default.

## Loading Method {#loading-method}

Configure the Theme Styles loading method under `WordPress Admin > Bricks > Settings > General > Theme Styles: Loading Method`.

Options:

- **Most specific**: Default. Bricks loads only the most specific matching Theme Style.
- **Load all matching theme styles**: Bricks loads every Theme Style whose conditions match the current page.

Use **Most specific** when each context should have one complete Theme Style.

Use **Load all matching theme styles** when you intentionally stack Theme Styles, such as:

- A global typography Theme Style for the entire site.
- A blog Theme Style for posts.
- A landing-page Theme Style for a small set of pages.

When loading all matching Theme Styles, Bricks keeps the matching styles ordered by condition specificity. If multiple active Theme Styles set the same property, the normal CSS cascade decides the final result. Avoid accidental overlaps by keeping each Theme Style focused.

## Style groups

The available groups depend on the active Bricks version, registered elements, and integrations. Core groups include:

- **Conditions:** where the Theme Style applies.
- **Stylesheet:** custom CSS for this Theme Style.
- **General:** broad site defaults.
- **Colors:** default color values.
- **Links:** link defaults and optional additional link selectors.
- **Contextual spacing:** spacing rules and default margin/padding cleanup.
- **Content:** content margin defaults.
- **Typography:** HTML and text defaults.
- **Popup:** popup defaults.
- **Elements:** defaults for supported elements such as Section, Container, Block, Div, Button, Heading, Image, List, Nav Menu, Post Content, Text, Video, and others.

Integrations can register additional Theme Style groups.

> **Note**
>
> If a group does not appear, the related element or integration may not be registered in your installation.

## Stylesheet group

The **Stylesheet** group lets you add custom CSS as part of a Theme Style.

This CSS is output with that Theme Style. It is not breakpoint-aware in the same way as generated control CSS, so use normal CSS and media queries when needed.

Use the Stylesheet group for CSS that belongs to the same Theme Style context. Use global custom CSS for site-wide code that should not depend on Theme Style conditions.

## Typography notes

Theme Styles can set typography defaults for HTML, body text, headings, links, and element-specific typography controls.

When multiple typography controls apply, Bricks orders the generated typography CSS so more specific heading settings can override broader heading settings.

If Style Manager scales are configured, the Style Manager can use the Theme Style HTML font size as the auto value for rem-based scale calculations unless Style Manager settings override it.

## Pseudo classes

Theme Styles can store pseudo-class settings, such as hover or focus states, for supported style groups.

Use pseudo-class settings for broad defaults. Use global classes when the state belongs to a reusable component pattern. Use element ID styles when the state is unique to one element.

## Export {#export}

1. Inside the builder, open **Style Manager > Theme Styles**.
2. Select the Theme Style you want to export.
3. Click the export icon.
4. Download the generated JSON file.

## Import {#import}

1. Inside the builder, open **Style Manager > Theme Styles**.
2. Click the import icon.
3. Select the Theme Style JSON file.
4. Upload it.

If a Theme Style with the same ID already exists in your installation, Bricks skips the import for that style. Rename or duplicate the source Theme Style before exporting if you need to import it as a separate style.

## Page Settings and Theme Styles

Page Settings apply to the current page or template and are output after Theme Styles. Use Page Settings for page-specific settings such as one-page navigation, page-level code, SEO/social values, or page-specific styling.

If a style should become the default for a group of pages, use Theme Styles. If it should affect one page or template, use Page Settings.

## Style Manager and Theme Styles

Theme Styles are one part of the Style Manager. They work alongside:

- Color Manager.
- Global Variables Manager.
- Global Class Manager.
- Style Manager settings and scales.

Theme Styles define broad defaults. Variables and color palettes provide reusable values. Global classes provide reusable patterns.

## Best practices

- Always add conditions. A Theme Style without conditions will not become active.
- Start with an Entire Website Theme Style for baseline typography, links, and broad element defaults.
- Use more specific Theme Styles only when a context really needs different defaults.
- Avoid setting the same property in many stacked Theme Styles unless you understand the cascade.
- Keep component-specific styling in global classes when the style belongs to a reusable pattern.
- Use the Stylesheet group for context-specific CSS, not unrelated global CSS.
- Test specific pages, archives, templates, and multilingual versions after changing conditions.

## Troubleshooting

### A Theme Style is not active

Check whether it has at least one condition, whether an exclude condition applies, and whether another Theme Style is more specific under the **Most specific** loading method.

### A broad Theme Style disappeared on a specific page

That is expected in **Most specific** mode when a more specific Theme Style matches the page. Switch to **Load all matching theme styles** only if you want styles to stack.

### A Theme Style control does not affect an element

Check whether the element has a global class, element ID style, page setting, or custom CSS overriding the same property.

### A group or control is missing

Theme Style groups depend on registered elements and integrations. If an element or integration is unavailable, its Theme Style group may not be shown.

### Custom CSS in the Stylesheet group is not responsive

The Stylesheet group is plain CSS. Add your own media queries if the CSS needs breakpoint-specific behavior.
