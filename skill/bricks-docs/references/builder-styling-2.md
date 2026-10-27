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
