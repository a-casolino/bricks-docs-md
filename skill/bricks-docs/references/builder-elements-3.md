# Offcanvas

Source: https://academy.bricksbuilder.io/builder/elements/general/offcanvas/

*The Offcanvas element is a nestable panel that slides (or offsets) in from a chosen edge of the viewport. Typical use: mobile navigation. Bricks suggests adding.*

The **Offcanvas** element is a **nestable** panel that slides (or offsets) in from a chosen edge of the viewport. Typical use: mobile navigation. Bricks suggests adding a [Toggle](https://academy.bricksbuilder.io/builder/elements/general/toggle/) elsewhere on the page that targets this Offcanvas (see the in-element info link to the menu builder article).

The default structure includes an inner **Block** (`.brx-offcanvas-inner`) for your content—often with starter **Text** and a **Toggle** labeled for closing—and a second **Block** acting as the **Backdrop** (`.brx-offcanvas-backdrop`), which you can remove if you do not want a backdrop.

https://youtu.be/Lhyh52twZoE

## Settings

- **Direction** (select) — `top`, `right`, `bottom`, or `left`. Default: left.

- **Effect** (select) — `slide` or `offset`.

- **Close on** (select) — `backdrop` (click), `esc`, `none`, or default: backdrop and ESC.

- **Width**, **Height** (number with units) — Size of the inner panel (`.brx-offcanvas-inner`).

- **Transition: Duration** (number with units) — Open/close animation; set to `0s` to disable.

- **Transition: Timing function** (text) — Easing, e.g. `cubic-bezier(0.25, 0, 0.25, 1)`.

- **aria-label** (text) — Root dialog label; defaults to “Offcanvas”.

- **Keep open while styling** (checkbox) — Builder helper class `brx-open` to keep the panel open while designing.

- **No scroll (body)** (checkbox) — Prevents body scrolling while open.

- **Scroll to top** (checkbox) — Scrolls to top when the Offcanvas opens.

- **Disable auto focus** (checkbox) — Skips auto-focusing the first focusable element when opening.

- **Open on page load** (checkbox) — Opens on the front end when the page loads (not applied in the builder).

## Build a mobile menu

This example replaces the menu element's built-in mobile menu with an Offcanvas, so the phone menu can have its own design and extra content such as contact details.

1. Open the header template, select the header section, and add an **Offcanvas**. It is hidden on the canvas until you select it.
2. Turn on **Keep open while styling**. Without it, the panel closes as soon as you select an element inside it.
3. Set **Direction**, **Width**, and **No scroll (body)** to suit the design, for example `Right` and `86%`.
4. Replace the starter Basic Text with your menu, for example a [Nav Menu](https://academy.bricksbuilder.io/builder/elements/wordpress/nav-menu/) element that uses the same WordPress menu as the desktop header. Set its **Show at breakpoint** to `Never`, so it always shows the links instead of its own menu button.
5. Add a **Toggle** to the header. Select the Offcanvas, hover the **b** icon at the top of the panel, and click **#** (Copy: CSS ID). Paste the ID into the Toggle's **CSS selector**.
6. On the Toggle's **Style** tab, set **Display** (Layout group) to `none` on desktop. Switch to the breakpoint where the menu should change, for example Tablet portrait, set the Toggle's Display to `flex`, and set the desktop menu's Display to `none`. Smaller breakpoints inherit both settings.
7. Save. Keep open while styling is a Builder helper: it is not saved and does not affect the frontend.

![Builder with the header template open: the Offcanvas is selected with Direction Right, Width 86%, and No scroll (body) on. The Structure panel shows the Offcanvas with Content (Toggle (Close), Nav Menu, Contact) and Backdrop.](https://academy.bricksbuilder.io/assets/offcanvas-builder-mobile-menu.webp)

<div className="screenshot screenshot--control-panel">

![Toggle settings with the Offcanvas CSS ID pasted into CSS selector. Attribute and Value keep their defaults, class and brx-open.](https://academy.bricksbuilder.io/assets/offcanvas-toggle-css-selector.webp)

</div>

> **Note**
>
> Without a CSS selector, a Toggle opens the first Offcanvas on the page. This includes the Toggles inside a [Nav (Nestable)](https://academy.bricksbuilder.io/builder/elements/general/nav-nested/) when the page also has an Offcanvas, for example one in the header template. Give each Toggle a CSS selector when a page has more than one element to toggle.

## Opening, closing, and keyboard focus

A Toggle opens the Offcanvas by adding the class `brx-open` to it. While the Offcanvas is open:

- Focus moves to the first focusable element inside it. Turn on **Disable auto focus** to skip this. If the close Toggle is the first element in Content, focus lands on it.
- **Tab** and **Shift+Tab** stay inside the panel: from the last focusable element, Tab wraps back to the first.
- With **No scroll (body)** on, the page behind the panel does not scroll.
- The Toggle that opened it has `aria-expanded="true"`.

The Offcanvas closes on a click on the backdrop, on **Esc**, or with a Toggle inside it. **Close on** limits this to the backdrop or Esc, or turns both off. When it closes, focus returns to the Toggle that opened it. While closed, the panel is hidden, so its links cannot be reached with Tab.

> **Developer reference**
>
> See the [Offcanvas Schema](https://academy.bricksbuilder.io/developer/schema/elements/offcanvas/) for the full JSON schema of this element's settings and controls.

---

# Pie chart

Source: https://academy.bricksbuilder.io/builder/elements/general/pie-chart/

*The Pie Chart element displays a circular progress chart with customizable percentage, colors, and content.*

The Pie Chart element displays a circular progress chart with customizable percentage, colors, and content.

## Settings

- **Percentage** (number) - The percentage value to display (0-100). Default: 60.

- **Chart size in px** (number) - Diameter of the chart in pixels. Default: 160.

- **Line width in px** (number) - Thickness of the progress line. Default: 8.

- **Line cap** (select) - Style of the line ends. Options: `butt`, `round`, `square`. Default: `square`.

- **Content** (select) - What to display in the center. Options: `percent`, `icon`, `text`. Default: `percent`.

- **Icon** (icon) - Icon to display in the center. Only shown when Content is set to "icon".

- **Text** (text) - Custom text to display in the center. Only shown when Content is set to "text".

- **Bar color** (color) - Color of the progress bar. Default: Primary theme color.

- **Track color** (color) - Color of the background track. Default: Light background color.

- **Scale length in px** (number) - Length of the scale marks.

- **Scale color** (color) - Color of the scale marks. Only shown when Scale length is set.

> **Developer reference**
>
> See the [Pie Chart Schema](https://academy.bricksbuilder.io/developer/schema/elements/pie-chart/) for the full JSON schema of this element's settings and controls.

---

# Pricing tables

Source: https://academy.bricksbuilder.io/builder/elements/general/pricing-tables/

*The Pricing Tables element creates responsive pricing table layouts with customizable headers, pricing information, feature lists, and call-to-action buttons.*

The Pricing Tables element creates responsive pricing table layouts with customizable headers, pricing information, feature lists, and call-to-action buttons.

## Settings

- **Pricing tables** (repeater) - Configure multiple pricing tables. Each table includes:

  - **Show under** (select) - Which tab to display the table under. Options: `Tab 1`, `Tab 2`. Default: `Tab 1`.

  - **Table background** (background) - Background styling for the table.

  - **Table border** (border) - Border styling for the table.

  - **Table box shadow** (box-shadow) - Shadow effect for the table.

  ### Header

  - **Title** (text) - Table title. Placeholder: `Title`.

  - **Subtitle** (text) - Table subtitle. Placeholder: `Subtitle`.

  - **Padding** (spacing) - Header padding.

  - **Background color** (color) - Header background color.

  - **Border** (border) - Header border styling.

  - **Title typography** (typography) - Title font settings.

  - **Subtitle typography** (typography) - Subtitle font settings.

  ### Pricing

  - **Padding** (spacing) - Pricing section padding.

  - **Price prefix** (text) - Text before price (e.g., currency symbol).

  - **Price** (text) - Main price amount.

  - **Price suffix** (text) - Text after price.

  - **Price meta** (text) - Additional pricing info (e.g., "per month").

  - **Meta typography** (typography) - Price meta font settings.

  - **Price typography** (typography) - Price font settings.

  - **Background color** (color) - Pricing section background.

  - **Border** (border) - Pricing section border.

  - **Original price** (text) - Strikethrough original price.

  - **Original price typography** (typography) - Original price font settings.

  ### Features

  - **Padding** (spacing) - Features section padding. Default: 10px top, 30px right, 10px bottom, 30px left.

  - **Features** (textarea) - Feature list, one per line.

  - **Alignment** (justify-content) - Feature text alignment. Default: `Center`.

  - **Icon** (icon) - Icon for features.

  - **Icon color** (color) - Feature icon color.

  - **Icon size** (number with units) - Feature icon size.

  - **Icon position** (select) - Icon placement. Options: `Right`, `Left`. Default: `Left`.

  - **Background color** (color) - Features section background.

  - **Border** (border) - Features section border.

  - **Typography** (typography) - Features text font settings.

  ### Footer

  - **Padding** (spacing) - Footer padding.

  - **Background color** (color) - Footer background color.

  - **Border** (border) - Footer border styling.

  ### Button

  - **Button text** (text) - Call-to-action button text. Placeholder: `Button text`.

  - **Link** (link) - Button destination. Placeholder: `https://yoursite.com`.

  - **Width** (number with units) - Button width.

  - **Size** (select) - Button size options.

  - **Style** (select) - Button style. Default: `None`.

  - **Background color** (color) - Button background color.

  - **Border** (border) - Button border styling.

  - **Typography** (typography) - Button text font settings.

  ### Additional info

  - **Additional info** (textarea) - Extra information below button.

  - **Typography** (typography) - Additional info font settings.

  ### Ribbon

  - **Text** (text) - Ribbon label text.

  - **Position** (select) - Ribbon placement. Options: `Left`, `Right`. Default: `Right`.

  - **Background color** (color) - Ribbon background color.

  - **Typography** (typography) - Ribbon text font settings.

- **Columns** (number) - Number of columns for table layout. Minimum: 1.

- **Spacing** (number with units) - Gap between tables. Default: 30px.

- **Align tables** (align-items) - Vertical alignment of tables. Default: `Stretch`.

## Tabs

- **Show tabs** (checkbox) - Enable tabbed pricing layout.

- **Tab 1 label** (text) - First tab label. Placeholder: `Monthly`.

- **Tab 2 label** (text) - Second tab label. Placeholder: `Yearly`.

- **Default tab** (select) - Initially active tab. Options: `Tab 1`, `Tab 2`. Default: `Tab 1`.

- **Alignment** (justify-content) - Tab alignment. Default: `Center`.

- **Margin** (spacing) - Tabs container margin.

- **Background** (color) - Tabs container background.

- **Border** (border) - Tabs container border.

- **Box shadow** (box-shadow) - Tabs container shadow.

### Tab

- **Width** (number with units) - Individual tab width.

- **Margin** (spacing) - Individual tab margin.

- **Padding** (spacing) - Individual tab padding.

- **Background** (color) - Tab background color.

- **Border** (border) - Tab border styling.

- **Box shadow** (box-shadow) - Tab shadow.

- **Typography** (typography) - Tab text font settings.

- **Active background** (color) - Active tab background color.

- **Active border** (border) - Active tab border styling.

- **Active box shadow** (box-shadow) - Active tab shadow.

- **Active typography** (typography) - Active tab text font settings.

> **Developer reference**
>
> See the [Pricing Tables Schema](https://academy.bricksbuilder.io/developer/schema/elements/pricing-tables/) for the full JSON schema of this element's settings and controls.

---

# Progress bar

Source: https://academy.bricksbuilder.io/builder/elements/general/progress-bar/

*The Progress Bar element displays animated progress bars with customizable labels, percentages, and styling.*

The Progress Bar element displays animated progress bars with customizable labels, percentages, and styling.

## Settings

- **Bars** (repeater) - Add multiple progress bars. Each bar has:
  - **Label** (text) - Text label for the progress bar.
  - **Percentage** (number) - Progress percentage (0-100). Supports dynamic data.
  - **Bar color** (color) - Color of the progress fill.

- **Height** (number with units) - Height of the progress bars. Default: 8px.

- **Spacing** (number with units) - Gap between progress bars. Default: 20px.

- **Show percentage** (checkbox) - Display percentage values next to labels. Default: checked.

- **Bar color** (color) - Default color for all progress bars.

- **Bar background color** (color) - Background color of the progress bar tracks.

- **Bar border** (border) - Border styling for the progress bars.

- **Label typography** (typography) - Font settings for the labels.

- **Percentage typography** (typography) - Font settings for the percentage values. Only shown when "Show percentage" is enabled.

> **Developer reference**
>
> See the [Progress Bar Schema](https://academy.bricksbuilder.io/developer/schema/elements/progress-bar/) for the full JSON schema of this element's settings and controls.

---

# Rating

Source: https://academy.bricksbuilder.io/builder/elements/general/rating/

*The Rating element displays a numeric score as a row of icons (default: stars). It supports fractional values (e.g. 3.5 on a 5-point scale) by filling whole.*

The **Rating** element displays a numeric score as a row of icons (default: stars). It supports **fractional** values (e.g. `3.5` on a 5-point scale) by filling whole icons, one partial icon with a width mask, and empty icons for the remainder.

This is separate from [Product rating](https://academy.bricksbuilder.io/builder/elements/product/product-rating/) (WooCommerce). Use **Rating** for static or dynamic review scores anywhere on the site.

## Settings

- **Rating** (number) — Current score. Min `0`, step `0.1`. Supports dynamic data. Default: `3.5`.

- **Max. rating** (number) — Scale maximum (e.g. `5`). Min `1`. Supports dynamic data.

- **Gap** (number with units) — Space between icons (`gap` on the root).

### Icon

- **Icon** (icon) — Optional custom icon; default is the built-in star SVG.

- **Icon color: Full** (color) — Filled / active portion.

- **Icon color: Empty** (color) — Empty / inactive portion.

- **Icon size** (number with units).

### Schema

Optional **schema.org** **Review** + **Rating** JSON-LD.

- **Generate review schema** (checkbox).

When enabled, the following are required:

- **Required: Reviewed item type** (text) — e.g. `Product`, `Service`.

- **Required: Reviewed item name** (text).

Optional:

- **Optional: Review author** (text).

- **Additional item reviewed properties** (repeater) — `Property name`, `Property value`, `Value type` (`Text`, `Number`, `Nested object`).

- **Additional review properties** (repeater) — Same shape; adds fields on the **Review** object (e.g. `reviewBody`, `datePublished`).

The structured data maps your **Rating** and **Max. rating** into a `Rating` node with `bestRating` `5` (normalized from your scale).

> **Developer reference**
>
> See the [Rating Schema](https://academy.bricksbuilder.io/developer/schema/elements/rating/) for the full JSON schema of this element's settings and controls.

---

# Slot

Source: https://academy.bricksbuilder.io/builder/elements/general/slot/

*The Slot element is used inside Bricks components as a placeholder: when you place a component instance on the canvas, the content you add into that instance is.*

The **Slot** element is used **inside Bricks components** as a **placeholder**: when you place a component instance on the canvas, the content you add into that instance is rendered in place of each Slot.

On the front end, the Slot outputs **nothing by itself**—it only renders the child elements assigned to that slot on the **component instance** (`slotChildren` for that Slot id). If there is no matching instance or no children, the Slot outputs nothing.

The element shows a single **info** control explaining that it acts as a placeholder for instance content.

> **Nestable**
>
> Slot uses the nestable builder UI (`bricks-nestable`) but does not ship with default nested children; structure is defined in your **component** template.

> **Developer reference**
>
> See the [Slot Schema](https://academy.bricksbuilder.io/developer/schema/elements/slot/) for the full JSON schema of this element's settings and controls.

---

# Tabs (nestable)

Source: https://academy.bricksbuilder.io/builder/elements/general/tabs-nested/

*Build tabbed content with nested elements and switch to an accordion layout at a chosen breakpoint.*

The Tabs (nestable) element groups content into tabs. Each title and content pane contains editable Bricks elements. Since Bricks 2.5, the same content can switch to an accordion layout on smaller screens.

## Settings

- **Direction** (direction) - Layout direction of the tabs. Controls the `flex-direction` CSS property. Set "ID" on tab menu "Div" to open a tab via anchor link (no spaces, no pound sign).

- **Open tab on** (select) - Trigger for opening tabs. Options: `click`, `hover`. Default: `click`.

- **Open tab index** (text) - Index of the tab to expand on page load, starting at 0. Default: 0. A matching custom ID set on a tab title opens that tab when used in the URL hash.

- **Accordion layout at breakpoint** (select) - Switch to an accordion below the selected breakpoint width. Default: **None**. Choose from the site's configured [breakpoints](https://academy.bricksbuilder.io/builder/interface/responsive-editing/).

## Accordion layout {#accordion-layout}

Select the Tabs (nestable) element and choose **Accordion layout at breakpoint**. For example, choose **Mobile landscape** to keep a horizontal menu on wider screens and place each title directly above its content on narrower screens.

![Tabs settings with Accordion layout at breakpoint set to Mobile landscape.](https://academy.bricksbuilder.io/assets/builder/release-2.5/tabs-accordion-settings.webp)

![Strategy, Design, and Development shown as tabs on a wide screen.](https://academy.bricksbuilder.io/assets/builder/release-2.5/tabs-desktop.webp)

The accordion applies strictly below the selected width. At that width and above, Bricks restores the tabs layout. For a breakpoint width of `767px`, the accordion appears below `767px`, and tabs appear at `767px` and above.

![The same services arranged as an accordion on a narrow screen, with Design open.](https://academy.bricksbuilder.io/assets/builder/release-2.5/tabs-mobile.webp)

Both layouts use the same titles and content. Selecting another title opens its pane and closes the previous one. The **Open tab index** sets the initial pane; you do not need to create separate mobile content.

In accordion layout, use `TAB` to move between titles and `ENTER` or `SPACE` to open a pane. Titles configured to open on hover remain operable by click and keyboard. Links and form controls nested inside a title keep their own behavior.

Keep the native **Tab menu** and **Tab content** structure, with matching title and pane counts. Panes must be direct children of Tab content for the accordion layout to work. Wrapping the panes in an extra element keeps the ordinary tabs layout.

## Styling

Title styles apply in both layouts. In accordion layout, **Content → Padding** applies inside each pane so it does not indent the titles.

### Title

- **Width** (number with units) - Width of tab titles. Default: `auto`.

- **Margin** (spacing) - Margin around tab titles.

- **Padding** (spacing) - Padding inside tab titles. Default: `20px` (top, right, bottom, left).

- **Background** (color) - Background color of tab titles.

- **Border** (border) - Border styling for tab titles.

- **Typography** (typography) - Font styling for tab titles.

#### Active

- **Background color** (color) - Background color of active tab titles. Default: `#dddedf`.

- **Border** (border) - Border styling for active tab titles.

- **Typography** (typography) - Font styling for active tab titles.

### Content

- **Margin** (spacing) - Margin around tab content.

- **Padding** (spacing) - Padding inside tab content. Default: `20px` (top, right, bottom, left).

- **Text color** (color) - Text color of tab content.

- **Background color** (color) - Background color of tab content.

- **Border** (border) - Border styling for tab content. Default: `1px solid` (all sides).

> **Developer reference**
>
> See the [Tabs (Nestable) Schema](https://academy.bricksbuilder.io/developer/schema/elements/tabs-nested/) for the full JSON schema of this element's settings and controls.

---

# Tabs

Source: https://academy.bricksbuilder.io/builder/elements/general/tabs/

*The Tabs element creates tabbed content with horizontal or vertical layouts and responsive accordion fallback.*

The Tabs element creates tabbed content with horizontal or vertical layouts and responsive accordion fallback.

## Settings

- **Tabs** (repeater) - Add tab items. Each tab has:
  - **Icon** (icon) - Optional icon for the tab.
  - **Icon position** (select) - Position of the icon relative to text. Options from iconPosition control options. Default: `Left`. Requires icon to be set.
  - **Title** (text) - The tab title.
  - **ID** (text) - Anchor ID for linking to the tab.
  - **Content** (editor) - The content shown when the tab is active.

- **Layout** (select) - Tab orientation. Options: `horizontal`, `vertical`. Default: `horizontal`.

- **Accordion layout at breakpoint** (select) - Switch to accordion layout below this breakpoint. Options from available breakpoints.

- **Open tab on** (select) - Trigger for opening tabs. Options: `click`, `hover`. Default: `click`.

- **Open tab index** (text) - Index of the tab to expand on page load, starting at 0. Default: 0.

### Title

- **Stretch** (checkbox) - Make tab titles stretch to fill available space (horizontal layout only). Sets `flex-grow: 1` on `.tab-title`.

- **Align** (justify-content) - Horizontal alignment of tab titles (horizontal layout only). Controls `justify-content` on `.tab-menu`.

- **Padding** (spacing) - Padding inside tab titles. Default: `20px` (top, right, bottom, left).

- **Background** (color) - Background color of tab titles.

- **Border** (border) - Border styling for tab titles. Default: `1px solid #dedede` (top, right, left only, no bottom).

- **Typography** (typography) - Font styling for tab titles.

- **Active background** (color) - Background color of active tab titles.

- **Active border** (border) - Border styling for active tab titles.

- **Active typography** (typography) - Font styling for active tab titles.

### Content

- **Padding** (spacing) - Padding inside tab content. Default: `20px` (top, right, bottom, left).

- **Text align** (text-align) - Text alignment for tab content.

- **Text color** (color) - Text color of tab content.

- **Background color** (color) - Background color of tab content.

- **Border** (border) - Border styling for tab content. Default: `1px solid #dedede` (all sides).

> **Developer reference**
>
> See the [Tabs Schema](https://academy.bricksbuilder.io/developer/schema/elements/tabs/) for the full JSON schema of this element's settings and controls.

---

# Template

Source: https://academy.bricksbuilder.io/builder/elements/general/template/

*The Template element allows including reusable Bricks templates (sections, content, or popups) within a page.*

The Template element allows including reusable Bricks templates (sections, content, or popups) within a page.

## Settings

- **Template** (select) - Select a published Bricks template to include. Options include section, content, and popup templates.

- **Render without wrapper** (checkbox) - Render the template content directly without the outer div wrapper. Note: Style settings won't apply when this is enabled.

> **Developer reference**
>
> See the [Template Schema](https://academy.bricksbuilder.io/developer/schema/elements/template/) for the full JSON schema of this element's settings and controls.

---

# Team members

Source: https://academy.bricksbuilder.io/builder/elements/general/team-members/

*The Team Members element displays a responsive grid of team member profiles with images, names, titles, and descriptions.*

The Team Members element displays a responsive grid of team member profiles with images, names, titles, and descriptions.

## Settings

### Team members

- **Team members** (repeater) - Add team member profiles. Each member has:
  - **Image** (image) - Profile photo.
  - **Title** (text) - Name of the team member.
  - **Subtitle** (text) - Job title or role.
  - **Content** (textarea) - Description or bio.

### Layout

- **Columns** (number) - Number of columns in the grid (1-6). Controls `grid-template-columns` with `repeat(%s, 1fr)`.

- **Gap** (number with units) - Spacing between team member cards. Controls `gap` property. Default placeholder: `20`.

- **Background** (color) - Background color of member cards. Applied to `.member` selector.

- **Border** (border) - Border styling for member cards. Applied to `.member` selector.

- **Box shadow** (box-shadow) - Shadow effect for member cards. Applied to `.member` selector.

### Image

- **Image position** (select) - Position of the image relative to content. Options: `top`, `right`, `left`, `bottom`. Default: `top`.

- **Image ratio** (select) - Aspect ratio for images. Options from swiper image ratio controls.

- **Width** (number with units) - Width of the images. Applied to `.image` selector.

- **Margin** (spacing) - Margin around the images. Applied to `.image` selector.

- **Border** (border) - Border styling for images. Applied to `.image` selector.

### Content

- **Padding** (spacing) - Padding inside the content area. Applied to `.content` selector. Default placeholder: `15px` (top), `0px` (right, bottom, left).

- **Text align** (text-align) - Text alignment for content. Applied to `.content` selector.

- **Title tag** (select) - HTML tag for member titles. Options: `h2`, `h3`, `h4`, `h5`, `h6`, `p`, `div`. Default: `h4`.

- **Title typography** (typography) - Font styling for member titles. Applied to `.title` selector.

- **Subtitle typography** (typography) - Font styling for member subtitles. Applied to `.subtitle` selector.

- **Description typography** (typography) - Font styling for member descriptions. Applied to `.description` selector.

> **Developer reference**
>
> See the [Team Members Schema](https://academy.bricksbuilder.io/developer/schema/elements/team-members/) for the full JSON schema of this element's settings and controls.

---

# Testimonials

Source: https://academy.bricksbuilder.io/builder/elements/general/testimonials/

*The Testimonials element displays testimonials in a swipeable carousel with images, names, titles, and content.*

The Testimonials element displays testimonials in a swipeable carousel with images, names, titles, and content.

## Settings

### Testimonials

- **Testimonials** (repeater) - Add testimonial entries. Each testimonial has:
  - **Content** (textarea) - The testimonial text.
  - **Name** (text) - Name of the person giving the testimonial.
  - **Title** (text) - Job title or role of the person.
  - **Image** (image) - Profile image of the person.

### Settings

- **Initial slide** (number) - Starting slide index. From swiper controls.

- **Slides to show** (number) - Number of testimonials visible at once. From swiper controls.

- **Slides to scroll** (number) - Number of slides to advance per swipe. From swiper controls.

- **Gutter** (number with units) - Spacing between slides. From swiper controls.

- **Align items** (justify-content) - Vertical alignment of testimonial items. Applied to `.repeater-item` selector. Excludes space options.

- **Text align** (text-align) - Text alignment for testimonials.

- **Effect** (select) - Transition effect. From swiper controls.

- **Infinite** (checkbox) - Enable infinite loop. From swiper controls.

- **Random order** (checkbox) - Display testimonials in random order.

- **Center mode** (checkbox) - Center the active slide. From swiper controls.

- **Disable lazy load** (checkbox) - Disable lazy loading of images. From swiper controls.

- **Autoplay** (checkbox) - Enable autoplay. From swiper controls.

- **Pause on hover** (checkbox) - Pause autoplay on hover. From swiper controls.

- **Autoplay speed** (number) - Autoplay delay in milliseconds. From swiper controls.

- **Speed** (number) - Transition speed in milliseconds. From swiper controls.

### Image

- **Image align** (align-items) - Vertical alignment of images. Applied to `.repeater-item` selector. Excludes stretch option.

- **Image position** (select) - Position of the image relative to content. Options: `top`, `right`, `bottom`, `left`. Default: `left`.

- **Image size** (number with units) - Size of the images. Controls both `width` and `height` of `.image` selector. Default placeholder: `60`.

- **Image border** (border) - Border styling for images. Applied to `.image` selector.

- **Image box shadow** (box-shadow) - Shadow effect for images. Applied to `.image` selector.

### Arrows

- **Arrows** (checkbox) - Show navigation arrows. From swiper controls.

- **Arrow height** (number with units) - Height of navigation arrows. From swiper controls.

- **Arrow width** (number with units) - Width of navigation arrows. From swiper controls.

- **Arrow background** (color) - Background color of navigation arrows. From swiper controls.

- **Arrow border** (border) - Border styling for navigation arrows. From swiper controls.

- **Arrow typography** (typography) - Font styling for navigation arrows. From swiper controls. Default color: body color.

- **Previous arrow** (text) - Custom previous arrow icon. From swiper controls.

- **Previous arrow position** - Top, right, bottom, left positioning for previous arrow. From swiper controls.

- **Next arrow** (text) - Custom next arrow icon. From swiper controls.

- **Next arrow position** - Top, right, bottom, left positioning for next arrow. From swiper controls.

### Dots

- **Dots** (checkbox) - Show pagination dots. From swiper controls.

- **Dynamic dots** (checkbox) - Enable dynamic pagination bullets. From swiper controls.

- **Vertical dots** (checkbox) - Display dots vertically. From swiper controls.

- **Dots height** (number with units) - Height of pagination dots. From swiper controls.

- **Dots width** (number with units) - Width of pagination dots. From swiper controls.

- **Dots position** - Top, right, bottom, left positioning for dots. From swiper controls.

- **Dots border** (border) - Border styling for pagination dots. From swiper controls.

- **Dots color** (color) - Color of inactive pagination dots. From swiper controls.

- **Active dots color** (color) - Color of active pagination dot. From swiper controls.

- **Dots spacing** (number with units) - Spacing between pagination dots. From swiper controls.

## Style

- **Testimonial** (typography) - Font styling for testimonial content. Applied to `.testimonial-content-wrapper` selector.

- **Name** (typography) - Font styling for testimonial names. Applied to `.testimonial-name` selector.

- **Title** (typography) - Font styling for testimonial titles. Applied to `.testimonial-title` selector.

> **Developer reference**
>
> See the [Testimonials Schema](https://academy.bricksbuilder.io/developer/schema/elements/testimonials/) for the full JSON schema of this element's settings and controls.

---

# Toggle - Mode

Source: https://academy.bricksbuilder.io/builder/elements/general/toggle-mode/

*The Toggle - Mode element (toggle-mode) lets visitors switch between light and dark color modes on the front end. It relies on dark variants defined in the.*

The **Toggle - Mode** element (`toggle-mode`) lets visitors switch between **light** and **dark** color modes on the front end. It relies on **dark variants** defined in the Bricks **color manager**; if no dark colors exist, the builder toolbar sun/moon control does not appear, and the same idea applies to how the front end behaves.

The element renders a **button** containing two icon areas (`.toggle.light` and `.toggle.dark`); CSS shows the correct icon for the active mode.

## Settings

An **info** control explains that in the **builder**, you switch light/dark using the toolbar icon when dark colors are configured.

### Mode: Light

- **Icon** (icon) — Optional; default is the built-in light-mode graphic.
- **Color** (color) — Icon color/fill for the light icon.
- **Size** (number with units) — Icon size for the light icon.

### Mode: Dark

- **Icon Dark** (icon) — Optional; default is the built-in dark-mode graphic.
- **Color** (color) — Icon color/fill for the dark icon.
- **Size** (number with units) — Icon size for the dark icon.

### Accessibility

- **aria-label** (text) — Defaults to “Toggle mode” if empty.

> **Developer reference**
>
> See the [Toggle Mode Schema](https://academy.bricksbuilder.io/developer/schema/elements/toggle-mode/) for the full JSON schema of this element's settings and controls.

---

# Toggle

Source: https://academy.bricksbuilder.io/builder/elements/general/toggle/

*The Toggle element outputs a button used to open and close other UI—most often an Offcanvas menu. You can use a custom icon or the built-in animated “hamburger”.*

The **Toggle** element outputs a **button** used to open and close other UI—most often an [Offcanvas](https://academy.bricksbuilder.io/builder/elements/general/offcanvas/) menu. You can use a **custom icon** or the built-in animated “hamburger” bars (with optional **Animation** presets).

Bricks shows an inline hint: copy the **element ID** (or a valid CSS selector) of the target into **CSS selector**—for example `.brxe-offcanvas` for an Offcanvas.

## Settings

### Icon (optional)

If you add an **Icon**, the bar animation is hidden and the icon is used instead.

- **Icon** (icon)
- **Color** (color) — Icon color/fill.
- **Size** (number with units) — Icon size.

### Toggle

- **CSS selector** (text) — Target node to toggle (e.g. `.brxe-offcanvas`). Placeholder: `.brxe-offcanvas`.
- **Attribute** (text) — HTML attribute to change (default behavior uses `class`). Placeholder: `class`.
- **Value** (text) — Value applied when toggling (e.g. open-state class). Placeholder: `brx-open`.

### Bar (when no custom icon)

- **Animation** (select) — Preset hamburger animation: `close (x)`, `arrow`, `arrow-r`, `arrowalt`, `arrowalt-r`, `arrowturn`, `arrowturn-r`, `minus`, `spin`, `spring`, `squeeze`, `vortex`, or none.
- **Scale** (number) — Bar scale via `--brxe-toggle-scale`.
- **Height**, **Radius** (number with units) — Bar dimensions.
- **Color** (color) — Bar color.

### Accessibility

- **aria-label** (text) — Defaults to “Open” (or “Close” when used as the nested close control inside certain structures such as Nav).

> **Developer reference**
>
> See the [Toggle Schema](https://academy.bricksbuilder.io/developer/schema/elements/toggle/) for the full JSON schema of this element's settings and controls.

---

# Filter checkbox

Source: https://academy.bricksbuilder.io/builder/elements/filter/filter-checkbox/

*Filter query results with multiple selections, include child-term counts, and show collapsible taxonomy branches with Show more/less controls.*

Creates a checkbox filter interface for AJAX-powered content filtering. Users can select multiple options to narrow down query results. Supports taxonomy terms, WordPress fields, and custom fields as filter sources.

For initial setup, see [Query Filters](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#setup).

## Settings

- **Target query** (query-list) - Select the post, term, or user query this filter should target. Available sources depend on the query type.
- **URL parameter** (text) - Define a unique, more readable URL parameter name for this filter.
- **Apply on** (select) - Choose when to apply the filter. Options: Input (immediate), Submit (requires button click). Default: Input.
- **Source** (select) - Data source for filter options. Options: Taxonomy, WordPress field, Custom field.
- **Field type** (select) - Type of field when using WordPress field or custom field source. Options: Post, Term, User.
- **Field** (select) - Specific field to filter by (varies based on field type).
- **Taxonomy** (select) - Taxonomy to use for filtering when source is taxonomy.
- **Order by** (select) - How to order taxonomy terms. Options: Name, Slug, Term ID, Description, Parent, Count, Include, Menu Order, Meta Value, Meta Value Num.
- **Order meta key** (text) - Meta key for ordering when using meta value ordering.
- **Order** (select) - Sort direction. Options: ASC, DESC. Default: ASC.
- **Terms: Include** (select) - Specific taxonomy terms to include in filter options.
- **Terms: Exclude** (select) - Specific taxonomy terms to exclude from filter options.
- **Top level terms only** (checkbox) - Display only top-level terms (parent = 0) when source is taxonomy.
- **Hide count** (checkbox) - Hide the result count for each option.
- **Count: Include children** (checkbox, Bricks 2.5) - Include descendant-term posts in parent taxonomy counts. Off by default. Requires a target query and a selected taxonomy. See [taxonomy child counts](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#taxonomy-child-counts).
- **Hide empty** (checkbox) - Hide options with zero results.
- **Hide count bracket** (checkbox) - Remove brackets around count values. Style count via .brx-option-count.
- **Provider** (select) - Custom field provider for integration (ACF, Meta Box, etc.).
- **Meta key** (text) - Custom field key for filtering.
- **Compare** (select) - Comparison operator for filtering. Options: IN, NOT IN, BETWEEN, NOT BETWEEN.
- **Mode** (select) - Display mode for checkboxes. Options: Default (traditional checkboxes), Button (modern button style).
- **Active filter** - Settings for active filter display.
  - **Prefix** (text) - Text to display before filter value.
  - **Suffix** (text) - Text to display after filter value.
  - **Title** (text) - Custom title attribute for filter links.

## Collapsible Taxonomy Branches {#collapsible-hierarchy}

Starting with **Bricks 2.5**, visitors can expand and collapse child branches in a hierarchical taxonomy Checkbox filter. This is useful for category lists where showing every nested term would make the filter too long.

1. Set **Target query**, choose **Taxonomy** as the source, and select a taxonomy with parent and child terms.
2. Open the **Hierarchy** control group and enable **Hierarchical**.
3. Turn on **Enable expand/collapse**.
4. Leave **Show expanded** off to start with branches collapsed, or enable it to show all branches expanded initially.
5. Save and check the frontend. Parent terms with visible children have a separate expand/collapse button beside the checkbox.

| Hierarchy setting | Behavior |
| --- | --- |
| Hierarchical | Arrange taxonomy terms under their parents. |
| Auto toggle child terms | Toggle child checkboxes when a parent checkbox changes. This is separate from expanding a branch. |
| Enable expand/collapse | Add buttons to open and close child branches. Off by default. |
| Show expanded | Expand all branches initially. Off by default. |
| Expand icon / Collapse icon | Choose the disclosure icons. Defaults are plus and minus. |
| Icon typography / Icon gap | Set the icon appearance and spacing. |
| Indent: Prefix / Indent: Gap | Set child-term indentation in the default display mode. |

The disclosure button opens or closes a branch without selecting its checkbox. Visitors can focus the button and use Enter or Space to toggle it. Selected child terms open their ancestor branches on page load, including selections loaded from URL parameters. Bricks preserves each element's expanded branches through AJAX updates and opens the path to selected terms when needed.

Only terms present in the filter's options can appear in a branch. **Top level terms only**, term exclusions, and **Hide empty** can remove child options. If a parent has no visible children, it has no expand/collapse button. Use [Count: Include children](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#taxonomy-child-counts) if parent counts should include posts assigned to descendants.

<div className="screenshot screenshot--control-panel">

![Hierarchy settings with expand/collapse enabled, Show expanded off, and plus and minus icons selected.](https://academy.bricksbuilder.io/assets/filter-checkbox-hierarchy-settings.webp)

</div>

### Show More/Less With Branches {#show-more-less}

In the **Show more / Show less** control group, set **Visible options limit** to limit the initial list. Leave it empty to show all options.

When **Enable expand/collapse** is on, this limit counts whole root branches, not individual child terms. For example, a limit of three shows the first three root branches. Expanding one of them reveals its children without using up another place in the limit. **Show more** reveals the remaining root branches; **Show less** returns to the initial limit.

A branch containing a selected term stays visible even beyond the limit, so the list can show more than the configured number of roots. **Show more: Text** accepts `%number%` for the number of hidden root branches. In the collapsed list, the Show more button is hidden when no additional branches remain hidden. Without expand/collapse, the limit counts individual options.

![The Hoodies child term remains visible under Clothing beyond the two-branch limit, with Show 1 more available and three matching products.](https://academy.bricksbuilder.io/assets/filter-checkbox-collapsible-branches.webp)

### Linked Desktop and Mobile Filters {#linked-hierarchies}

When using a [global filter](https://academy.bricksbuilder.io/builder/dynamic-content/global-filters-filter-manager/), **Hierarchical**, **Auto toggle child terms**, and **Count: Include children** are shared settings. Expand/collapse, Show expanded, icons, indentation, and Show more/less limits stay on each element.

Linked elements targeting the same query synchronize their checkbox selections. Each copy keeps its own expanded branches and Show more/less state, so a mobile filter can start collapsed while the desktop copy starts expanded.

## Default selection {#default-selection}

Starting with **Bricks 2.5**, this filter can apply a selection before the first query runs. Use **Default value** to preselect exact option values, separated by commas, such as `cotton, wool`. Use taxonomy slugs or raw stored values rather than display labels. Wrap a value containing a comma in double quotes. Dynamic data is supported.

<div className="screenshot screenshot--control-panel">

![A Checkbox filter's Default value set to cotton, wool.](https://academy.bricksbuilder.io/assets/query-filter-default-values.webp)

</div>

The default applies even with **Apply on** set to **Submit**. Filter URL selections take precedence, and **Reset** clears the selection instead of restoring the default. A fresh visit or reload without filter parameters applies it again. See [default filter values](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#default-values) for shared defaults, validation, and URL behavior.

> **Developer reference**
>
> See the [Filter - Checkbox Schema](https://academy.bricksbuilder.io/developer/schema/elements/filter-checkbox/) for the full JSON schema of this element's settings and controls.

---

# Filter active filters

Source: https://academy.bricksbuilder.io/builder/elements/filter/filter-active-filters/

*Display selected query filters as removable buttons and exclude filters from the active list.*

Displays the currently active or selected filters, allowing users to easily remove a filter with a single click for faster navigation. This element shows all active filters from the connected target query and provides quick access to clear individual filters.

**Tip:** Use this element alongside other filter elements to give users clear visibility of their current filter selections and easy ways to modify their search criteria.

## Settings

- **Target query** (query-list) - Select the query whose active filters should be displayed.
- **Global filter** (Bricks 2.5) - Reuse the shared behavior of another Active Filters configuration. The target query and styling remain local.
- **Exclude filter IDs** (text) - Enter filter element IDs, separated by commas, to exclude from the active filters list. From Bricks 2.5, accepts global filter IDs too. A linked element's ID excludes its shared filter for the target query.
- **Button** - Settings for the remove filter buttons.
  - **Padding** (spacing) - Padding for filter remove buttons.
  - **Gap** (number) - Gap between filter buttons.
  - **Size** (select) - Button size preset. Options: Default, Small, Medium, Large, Extra Large.
  - **Style** (select) - Button style. Options: None, Primary, Secondary, Success, Info, Warning, Danger, Dark, Light.
  - **Circle** (checkbox) - Make buttons circular.
  - **Outline** (checkbox) - Use outline button style.
  - **Background color** (color) - Custom background color for buttons.
  - **Border** (border) - Border styling for buttons.
  - **Typography** (typography) - Typography settings for button text.
- **Icon** - Settings for filter remove icons.
  - **Icon** (icon) - Icon to display on filter buttons.
  - **Color** (color) - Icon color.
  - **Size** (number) - Icon size.
  - **Gap** (number) - Gap between icon and text.
  - **Position** (select) - Icon position. Options: Left, Right. Default: Right.
- **Active filter** - Settings for active filter display.
  - **Prefix** (text) - Text to display before filter value.
  - **Suffix** (text) - Text to display after filter value.
  - **Title** (text) - Custom title attribute for filter links.

## Default selections

Starting with Bricks 2.5, [configured default values](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#default-values) appear as active selections on the first page load. Visitors can remove them like other selections. Removing a default does not immediately reapply it; a fresh visit or reload without filter parameters applies it again. Display exclusions still apply.

## Excluding a Global Filter

Starting with Bricks 2.5, use a [global filter](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#global-filters) ID or any linked element's ID in **Exclude filter IDs**. For example, exclude a shared results-per-page filter to keep it out of the active-filter list across desktop and mobile copies. This hides the entry without clearing its selection or changing the query.

Copy a definition ID from Filter manager, or use the Bricks ID from a linked element's panel. Do not use a target query ID or URL parameter name. This display exclusion is separate from a Reset button's exclusions, which preserve values when resetting.

> **Developer reference**
>
> See the [Filter - Active Filters Schema](https://academy.bricksbuilder.io/developer/schema/elements/filter-active-filters/) for the full JSON schema of this element's settings and controls.

---

# Filter datepicker

Source: https://academy.bricksbuilder.io/builder/elements/filter/filter-datepicker/

*Filter query results by a single date or date range, including events stored with separate start and end date fields.*

Use Filter - Datepicker to filter a Query Loop by post dates, user registration dates, or custom date fields. Visitors can select a single date or a date range, with optional time selection.

Enable [Query Filters](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#enable), add the element, and select its **Target query**. Starting with **Bricks 2.5**, date ranges can use separate start and end custom fields on posts, terms, or users, including supported ACF, Meta Box, and JetEngine fields.

## Settings

- **Target query** (query-list) - Select the Posts, Terms, or Users query this filter should target.
- **URL parameter** (text) - Define a unique, more readable URL parameter name for this filter.
- **Apply on** (select) - Choose when to apply the filter. Options: Input (immediate), Submit (requires button click). Default: Input.
- **Source** (select) - Data source for filter options. Options: WordPress field, Custom field.
- **Field type** (select) - Type of field when using WordPress field or custom field source. Options: Post, Term, User.
- **Field** (select) - Specific date field to filter by (post date, modified date, user registered date).
- **Provider** (select) - Custom field provider for integration (ACF, Meta Box, etc.).
- **Meta key** (text) - Custom field containing date values. For separate start and end fields, this is the start field. Enter a native meta key or use the selected provider's field picker.
- **End date meta key** (text, Bricks 2.5) - Optional separate end-date field from the same provider and object type as **Meta key**. Leave empty to compare both selected dates against **Meta key**. See [separate start and end fields](#separate-date-fields).
- **Enable time** (checkbox) - Add time selection capability to the date picker.
- **Date range** (checkbox) - Enable selection of date ranges instead of single dates.
- **Min/max date** (checkbox) - Use minimum and maximum dates from the index table for date picker limits.
- **Compare** (select) - Comparison operator for single-date filtering. Options: == (is), < (before), > (after).
- **Input** - Settings for the date input field.
  - **Placeholder** (text) - Placeholder text for the input field. Default: Date.
  - **Placeholder typography** (typography) - Typography for placeholder text.
  - **Language** (text) - Language code for date picker localization (de, es, fr, etc.).
  - **Datepicker format** (text) - Display format, defaulting to `Y-m-d`. **Enable time** appends `H:i`. This does not change how dates are stored in the database.
- **Active filter** - Settings for active filter display.
  - **Prefix** (text) - Text to display before filter value.
  - **Suffix** (text) - Text to display after filter value.
  - **Title** (text) - Custom title attribute for filter links.

## Separate start and end fields {#separate-date-fields}

Use **End date meta key** when each item in a Posts, Terms, or Users query stores its start and end dates in separate custom fields.

1. Set **Target query** to the results loop.
2. Set **Source** to **Custom field** and **Field type** to the objects in that loop: **Post**, **Term**, or **User**.
3. For native metadata, leave **Provider** at **WordPress**. For ACF, Meta Box, or JetEngine, enable [Custom fields integration](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#custom-fields-integration) and select the provider.
4. In **Meta key**, enter the native start field's key, such as `event_start`, or select the provider field using the dynamic data picker.
5. Enable **Date range**.
6. In **End date meta key**, enter the native end field's key, such as `event_end`, or use its picker to select the provider field.
7. Optionally enable **Min/max date** to limit the calendar to the indexed date bounds.
8. Save the builder and allow indexing to finish before testing the frontend.

For native metadata, enter literal keys without dynamic data braces. For provider fields, use the picker on each control. Bricks reads the selected field's definition; these references are not frontend dynamic data output. Both fields must belong to the same provider and object type, with compatible post type or taxonomy locations.

<div className="screenshot screenshot--control-panel">

![Datepicker controls using Post fields and ACF, with departure_date as the start field, return_date as the end field, and Date range and Min/max date enabled.](https://academy.bricksbuilder.io/assets/datepicker-acf-separate-date-fields.webp)

</div>

### Supported fields and storage {#supported-date-fields}

Each field must store one date or datetime value per object. These sources support field pairs on posts, terms, and users:

| Source | Supported date fields |
| --- | --- |
| WordPress metadata | Date strings such as `2027-03-09` or `20270309`, and ISO datetime strings such as `2027-03-09 10:00:00`. |
| ACF | Date Picker and Date Time Picker, including scalar fields inside ordinary Group fields. |
| Meta Box | Date and Datetime fields stored in native WordPress metadata, including numeric save formats such as `d/m/Y H:i:s` and timestamp storage. User and term fields require the corresponding Meta Box extensions. |
| JetEngine | Date and Datetime fields stored in native WordPress metadata, as strings or timestamps. |

Bricks resolves each field's storage separately. The start and end fields can use different supported formats or timestamp settings. ACF's Date Picker stores `Ymd` values; changing its return format or **Datepicker format** does not change how Bricks compares the stored dates.

Time-only fields, repeating or cloneable fields, serialized groups, and custom-table storage are not supported for separate start and end fields. The provider pickers limit choices to compatible date fields. ACF Group fields are supported only where each date is stored as its own metadata value, rather than inside a repeated or serialized structure.

If a provider is unavailable or a selected field is deleted or incompatible, Bricks reports a configuration error. Select a compatible replacement or clear **End date meta key** to return to one-field behavior. An invalid pair does not silently compare the start field twice.

### Example: ACF dates on taxonomy terms

If each term in an event taxonomy has ACF `event_start` and `event_end` Date Picker fields, target the **Terms** loop and set **Field type** to **Term** and **Provider** to **ACF**. Select `event_start` in **Meta key**, enable **Date range**, and select `event_end` in **End date meta key**. Both ACF fields must be available on the taxonomy being queried.

### Which events match?

Both conditions must be met:

- The event starts on or after the selected start date.
- The event ends on or before the selected end date.

For a selected range of **March 8–10, 2027**, with **Enable time** off:

| Event dates | Included? |
| --- | --- |
| March 8–10 | Yes, both boundaries are included. |
| March 9 | Yes, the event fits within the range. |
| March 9–12 | No, it ends after March 10. |
| March 7–9 | No, it starts before March 8. |

An event must fit entirely within the selection. An event that overlaps only part of the range is excluded. Both date fields must contain valid values, and the stored start must not be later than the stored end. Items with missing, empty, invalid, or reversed dates are excluded from filtered results and calendar bounds.

With **Enable time** off, the selection covers complete days, including the whole final day. With it on, the selected hours and minutes are part of the comparisons, and the final minute includes seconds through `:59`. A stored end field containing only a date represents the end of that day.

Select both endpoints to apply a range; selecting only the first date does not filter the query. Choose the same day for both endpoints to filter a single day. The range narrows the query's existing restrictions, including groups of conditions joined by **OR**.

Leave **End date meta key** empty to filter one field between the selected dates. Turning off **Date range** uses **Meta key** and the **Compare** setting; the separate end field is ignored.

Changing **Source**, **Provider**, or **Field type** clears the retained end-field selection. Select a compatible end field again after the change. The **WordPress field** source, such as Post date or User registered date, keeps its existing single-field behavior.

### Calendar limits and indexing

With a separate end field configured, Bricks indexes both dates from complete, valid intervals. **Min/max date** uses those indexed values, so a multi-day event's end date can extend the calendar's upper limit. It does not disable individual days without events inside those limits or select a particular opening month.

Adding, updating, or deleting either date field refreshes the affected post, term, or user's complete interval through the normal queue. If either value is removed or becomes invalid, neither date from that item contributes to the bounds. Upgrades and changes to the selected field definitions can queue an index rebuild. If the calendar limits appear stale, check the [filter indexing tools](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#filter-index) and allow pending jobs to finish.

### Shared Datepicker settings

When using a [Global Filter](https://academy.bricksbuilder.io/builder/dynamic-content/global-filters-filter-manager/), the provider, field type, and both field selections belong to the shared configuration. Linked Datepickers use those fields and one shared index while keeping their own target queries and styling. Linking to a global filter without an end key uses one-field behavior, even if the element previously had a local end key.

## Default selection {#default-selection}

Starting with **Bricks 2.5**, this filter can apply a selection before the first query runs. For a single date, enter **Default value** in `YYYY-MM-DD` format. With **Date range** enabled, provide both **Start date** and **End date** in that format, with the start no later than the end. These fields support dynamic data, which must return the same format regardless of the display or stored field format.

The default applies even with **Apply on** set to **Submit**. Filter URL selections take precedence, and **Reset** clears the selection instead of restoring the default. A fresh visit or reload without filter parameters applies it again. See [default filter values](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#default-values) for shared defaults, validation, and URL behavior.

> **Developer reference**
>
> See the [Filter - Datepicker Schema](https://academy.bricksbuilder.io/developer/schema/elements/filter-datepicker/) for the full JSON schema of this element's settings and controls.

---

# Filter Geolocation

Source: https://academy.bricksbuilder.io/builder/elements/filter/filter-geolocation/

*Filter posts, terms, or users by distance from an address, device location, or map center, and show nearby results on Google Maps or Leaflet.*

The **Filter - Geolocation** element, available in **Bricks 2.5**, finds results within a radius of a selected location. Use it for store locators, property listings, or directories where visitors need to find nearby places.

Visitors can search from an address, their device location, or the center of a connected map. A map is optional. The filter supports native **Posts**, **Terms**, and **Users** query loops.

Distance is measured along the earth's surface in a straight line, not along roads. It does not represent driving distance or travel time.

## Basic setup {#setup}

1. Enable **Enable query sort / filter / live search** under **Bricks > Settings > Query filters**.
2. Create a [Query Loop](https://academy.bricksbuilder.io/builder/dynamic-content/query-loop/) for your listing.
3. Add **Filter - Geolocation** from the **Filter** element group.
4. Set **Target query** to the listing's loop.
5. Under **Data source**, set **Object type** to **Post**, **Term**, or **User** to match the listing, then configure its [coordinate fields](#coordinates).
6. Enable **Search by address**, **Search by device location**, or both. Both are off by default.
7. Set the radius and distance unit. Enable **Radius dropdown** if visitors should choose the radius.
8. Save the builder and let indexing finish. Test the search on the frontend.

For example, a store directory can use a Posts query with `store_latitude` and `store_longitude` custom fields. Enable device-location search and offer 5, 10, 25, and 50 km radii. A visitor selects their location and 25 km, and the listing shows stores within that distance.

![A 25 km device-location search around Johor Bahru, with a removable active-filter label, a result showing its distance, and a Leaflet map showing the origin and radius.](https://academy.bricksbuilder.io/assets/academy-filter-geolocation-leaflet.webp)

## Coordinate fields {#coordinates}

Every result needs saved latitude and longitude values. Bricks indexes these coordinates for distance searches. It does not convert saved street addresses into coordinates during indexing.

### WordPress meta fields

Use the **WordPress** provider, or the native coordinate controls when custom-field integration is disabled.

| Coordinate format | Settings | Example saved values |
| --- | --- | --- |
| **Separate fields** (default) | **Latitude meta key** and **Longitude meta key** | `store_latitude`: `1.4927`; `store_longitude`: `103.7414` |
| **Combined field** | **Coordinates meta key** | `store_coordinates`: `1.4927,103.7414` |

Enter the meta key names, not dynamic data tags. For combined fields, latitude comes first. Bricks reads post, term, or user metadata according to **Object type**.

Latitude must be between -90 and 90, and longitude between -180 and 180. Missing or invalid coordinates are excluded from location searches. An item can appear in the unfiltered listing and disappear when a radius search is applied if its coordinates are missing.

### ACF and Meta Box map fields

1. Enable **Custom fields integration** under **Bricks > Settings > Query filters**.
2. Set **Provider** to **ACF** or **Meta Box** on the Geolocation filter.
3. Open the dynamic data picker in **Location field** and select an **ACF Google Map** or **Meta Box Map** field.

These integrations read the saved coordinates from the map field. The provider choices for this element are limited to ACF and Meta Box, even when other query-filter integrations are active.

After importing locations or changing the coordinate source, use **Regenerate filter index** under **Bricks > Settings > Query filters** if results are missing or outdated. See [Filter Index](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#filter-index) for background indexing controls.

### Coordinates from a custom storage format {#custom-coordinate-storage}

For integrations that store coordinates in another format, use the `bricks/query_filters/geolocation/coordinates` PHP filter. It runs while Bricks indexes each object, after the normal coordinate lookup, rather than on every visitor search.

The callback receives five arguments:

| Argument | Value |
| --- | --- |
| `$coordinates` | The resolved `['lat' => ..., 'lng' => ...]` array, or `false` when no valid coordinates were found. |
| `$object_id` | The post, term, or user ID being indexed. |
| `$object_type` | `post`, `term`, or `user`. |
| `$settings` | The Geolocation filter settings used for indexing. |
| `$filter_id` | The filter ID that owns the coordinate index. |

For example, suppose a `store` post type saves an array under `_directory_location`, with `latitude` and `longitude` keys. Configure the Geolocation filter with **Object type > Post**, **Combined field**, and **Coordinates meta key** set to `_directory_location`. Add this callback to your child theme or a custom plugin:

```php
add_filter( 'bricks/query_filters/geolocation/coordinates', function ( $coordinates, $object_id, $object_type, $settings, $filter_id ) {
    if (
        $object_type !== 'post' ||
        get_post_type( $object_id ) !== 'store' ||
        ( $settings['geoCoordinateSource'] ?? 'separate' ) !== 'combined' ||
        ( $settings['geoCoordinatesKey'] ?? '' ) !== '_directory_location'
    ) {
        return $coordinates;
    }

    $location = get_post_meta( $object_id, '_directory_location', true );

    if ( ! is_array( $location ) ) {
        return false;
    }

    return [
        'lat' => $location['latitude'] ?? null,
        'lng' => $location['longitude'] ?? null,
    ];
}, 20, 5 );
```

The scope checks preserve other filters and object types. Return the incoming value when your integration does not apply, or `false` to exclude that object's coordinates. Bricks validates the returned array again: latitude and longitude must be finite numbers within the ranges above. An invalid result is not indexed, and stale coordinates for that object are removed during reindexing.

After adding the callback or changing its stored data, [regenerate the filter index](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#filter-index) to update existing results. Integrations can also [request a rebuild from PHP](https://academy.bricksbuilder.io/developer/hooks/actions/bricks-query_filters-reindex/#request).

## Search methods {#search-methods}

### Address search

Enable **Search by address** to display an address field and Search button. Save a Google Maps API key under **Bricks > Settings > API keys**. The key needs access to **Maps JavaScript API** and **Geocoding API**, with billing and website restrictions configured for your site. Saving a key does not verify access to those services.

**Address autocomplete** adds suggestions while typing and additionally requires **Places API (New)**. If suggestions fail, visitors can still type an address and use Search. See [Google Maps API key setup](https://academy.bricksbuilder.io/integrations/how-to-set-up-your-google-maps-api-key/#geolocation).

- **Country codes** limits suggestions to up to 15 two-letter country codes, separated by commas or spaces. Leave it empty for all countries.
- **Autocomplete map area** can **Prefer map area** (default), **Limit to map area**, or **Ignore map area** when a map is connected.
- **Hide label** hides the address label visually while retaining its accessible name.
- **Hide search button** leaves Enter available to run a search.

Autocomplete restrictions affect address suggestions. The selected origin and radius determine which listing items match.

### Device-location search

Enable **Search by device location** to display a location button. Choose text, an icon, or both, and configure the enabled and clear states under **Device location button**.

Bricks requests location permission only after the visitor activates the button. The browser must support geolocation and permit it on the site, normally over HTTPS. If permission is denied or the location cannot be retrieved, the previous applied search remains in place.

Device-location search does not need a Google Maps API key. It works with a listing alone or a connected Leaflet map without Google services. Enabling address search still requires the Google APIs, including when the connected map uses Leaflet.

## Default location {#default-location}

Enable **Use default location** to apply a radius search before the first query runs. This works with Google Maps, Leaflet, or a listing without a map.

1. Set **Target query** and enable at least one visitor search method: **Search by address** or **Search by device location**.
2. Under **Default location**, enable **Use default location**.
3. Enter **Latitude** and **Longitude**, for example `3.1390` and `101.6869` for Kuala Lumpur.
4. Optionally enter a **Location label**, such as "Kuala Lumpur". An empty label displays "Default location".
5. Set **Default radius** and **Distance unit**, for example 25 km, then save and test a URL without filter parameters.

<div className="screenshot screenshot--control-panel">

![Use default location enabled with latitude 3.1390, longitude 101.6869, and Kuala Lumpur as the location label.](https://academy.bricksbuilder.io/assets/query-filter-default-location.webp)

</div>

Latitude, longitude, and label support dynamic data from the original page or template preview context. Coordinates must resolve to valid numbers. The label is display text, not an address that Bricks needs to geocode. It appears in Active Filters and the address input when address search is enabled. Submitting the unchanged label uses the existing coordinates.

The default applies immediately, including with **Apply on** set to **On submit**. It uses the configured radius and unit, does not derive coordinates from the map center, and does not request the visitor's device location. Device access still requires the visitor to activate its button.

Use one default location per target query. Duplicate desktop and mobile controls can share a default through one [global filter](https://academy.bricksbuilder.io/builder/dynamic-content/global-filters-filter-manager/). If independent Geolocation filters targeting the same query each define a valid default location, Bricks skips those defaults and shows a warning in the builder preview. Invalid or incomplete coordinates are also skipped.

Recognized filter URL parameters take precedence over defaults. **Reset** clears the location; a fresh visit or reload without filter parameters applies it again. Defaults are not reapplied during AJAX updates, pagination, or browser Back/Forward. Coordinates enter the URL only when **Save location in URL** is enabled. See [default filter state](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#default-state).

## Radius and sorting {#radius}

| Setting | Behavior |
| --- | --- |
| **Default radius** | Uses 5 by default. With a radius dropdown, choose a value from **Radius options**; otherwise Bricks uses the first valid option. Without a dropdown, this is the fixed search radius. |
| **Distance unit** | **Kilometres (km)** by default, or **Miles (mi)**. |
| **Radius dropdown** | Off by default. Lets visitors select one configured radius. Default presets are 5, 10, 25, and 50. Each row has a numeric **Radius** and an **Option label**. |
| **Unit label format** | **Abbreviated (km/mi)** by default, **Full text**, or **Disable**. Applies to the radius options and Active Filters label. Disable it when your option labels already contain their units. |
| **Sort results by distance** | On by default. Shows nearest matches first while the filter is active. An active Sort filter takes precedence without removing the radius constraint. |

Radius changes need an origin before they can filter results. Existing taxonomy, custom-field, search, and other query restrictions still apply. Pagination totals reflect the filtered results.

Under **Radius dropdown**, enable **Enhanced radius dropdown** for Choices.js styling. It remains a single-selection control with a valid radius required.

### Let visitors choose the distance order {#distance-sorting}

Add a [Select](https://academy.bricksbuilder.io/builder/elements/filter/filter-select/) or [Radio](https://academy.bricksbuilder.io/builder/elements/filter/filter-radio/) filter targeting the same query and set **Action** to **Sort**. In **Sort options**, set **Source** to **Distance** and choose **Ascending** for nearest first or **Descending** for farthest first. Give each option a label visitors can recognize.

Distance uses the Geolocation search, including a configured default location. It retains the radius when visitors change sort options and works even when this element's **Sort results by distance** is off. A farthest-first 25 km search still excludes results outside 25 km.

On the frontend, Distance options stay visible but disabled without a valid location for the same query. A valid location enables them even when no results match. Choosing a sort option never requests device location; visitors obtain their location through this element's search controls.

See [Distance sorting setup](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#distance-sorting) for the complete configuration.

## When a search applies {#apply-mode}

The Geolocation filter uses **Immediately** and **On submit** labels under **Apply on**.

| Action | Immediately (default) | On submit |
| --- | --- | --- |
| Select an address suggestion or resolve device location | Applies the selected location | Stages the location until a search is submitted |
| Change the radius or pan a map with map search enabled | Applies the change | Stages the change |
| Use the address Search button or press Enter to search | Resolves and applies this location alongside already applied filters | Resolves and applies this location alongside already applied filters |
| Activate a Filter - Submit targeting the same query | Applies all pending filters | Applies all pending filters |

When Enter selects an autocomplete suggestion, that keypress only selects it. Press Enter again to search. In **Immediately** mode, selecting the suggestion can already trigger the update.

In **On submit** mode, device-only setups need a [Filter - Submit](https://academy.bricksbuilder.io/builder/elements/filter/filter-submit/) element targeting the same query. Keep status messages visible so visitors can tell when a location is waiting to be applied.

To apply a pending location and Distance sorting together, set the Select or Radio sort filter's **Apply on** to **Submit** too. A resolved pending location enables its Distance options before submission. Clearing the pending location disables them and clears the pending Distance choice. Use Filter - Submit to apply both changes together.

While a new location is pending, the visible results, distances, active-filter label, and map radius still describe the applied search. They update when the matching results arrive. Failed lookups or requests preserve the previous applied location and results.

## Connect a map {#map}

1. Add a [Map Connector](https://academy.bricksbuilder.io/builder/elements/general/map-connector/) inside the results loop and give it location data for each item. Use coordinates matching the filter's indexed location.
2. Add a [Google Map](https://academy.bricksbuilder.io/builder/elements/general/map/#3-sync-with-query) in JavaScript API render mode, or [Map (Leaflet)](https://academy.bricksbuilder.io/builder/elements/general/map-leaflet/#sync-with-query).
3. Set the map's **Sync with query** to the same results loop targeted by the filter.
4. If exactly one Geolocation filter and one matching map use that query, Bricks connects them automatically. Otherwise, select the intended map under **Map (Optional)** on the filter.

Each Geolocation filter connects to at most one map, and each map to at most one Geolocation filter. Static maps and a map's internal query are not supported filter targets. Leaflet Map Connectors require latitude and longitude.

The map shows the search origin and radius, with markers for the current results. The applied origin and radius stay visible when no results match. Under **Map appearance**, customize the circle's fill and border, origin marker color, or a custom origin marker image.

### Search on map drag

Enable **Search on map drag** on the filter and allow dragging on the connected map. The map center becomes the search origin after the visitor stops panning.

- **Visitor controlled** (default) shows a **Search as I move the map** checkbox. Configure its label, corner position, and **Checked by default** state.
- **Automatic** searches after every qualifying drag without displaying the checkbox.
- **Search delay (ms)** waits after the map settles, using 400 ms by default.

Zooming alone and programmatic map movements do not start a search. **Apply on** still controls whether map changes apply immediately or wait for submission.

## Show the distance in each result {#distance}

Place the following tag in a text element inside the filtered Posts, Terms, or Users loop:

```text
{filter_geo_distance}
```

It shows the current item's distance from the applied origin, using the filter's unit and unit-label format with one decimal place by default. It also works in AJAX-rendered map Info Boxes for those results.

| Argument | Use |
| --- | --- |
| `@to:'km'` or `@to:'mi'` | Convert the displayed distance without changing the search radius. |
| `@decimals:'0'` through `@decimals:'6'` | Set the number of decimal places. |
| `@output:'value'` | Return the rounded numeric value only. |
| `@output:'unit'` | Return the unit label only. |
| `@fallback:'Select a location'` | Show fallback text when no distance is available. |

For example:

```text
{filter_geo_distance @to:'mi' @decimals:'2'}
{filter_geo_distance @fallback:'Select a location'}
```

Without a fallback, the tag returns nothing before a location search is applied or outside a supported filtered loop. API, Array, and provider-specific query loops do not support this tag or Geolocation filtering.

## Active filters and URL state {#state}

An [Active Filters](https://academy.bricksbuilder.io/builder/elements/filter/filter-active-filters/) element shows the location and radius as one removable item. Clear, Reset, and removing that item clear the location search. Applying another independent Geolocation filter to the same query replaces the previous location constraint.

Clearing the location also clears a selected Distance sort and restores the query's normal ordering. Results and URL history update together after the request succeeds. Failed or cancelled requests preserve the last applied results and ordering. Distance options remain configured so they can be enabled for another valid location.

**Save location in URL** is off by default. Enable it if searches should survive a reload or be shareable. It writes the selected coordinates to the page URL and browser history. **URL parameter** changes the parameter name. Browser Back and Forward can restore saved searches.

Geolocation filters support [Global Filters](https://academy.bricksbuilder.io/builder/dynamic-content/global-filters-filter-manager/). Shared behavior includes the coordinate source, search methods, default location, radius, and apply mode. Target query, map connection, and presentation remain local to each linked element.

## Styling and status messages {#styling}

The element has separate control groups for **Layout**, **Label**, **Address**, **Search button**, **Radius dropdown**, **Device location button**, and **Status**. Use these to style the controls at each breakpoint.

Under **Status**, override the pending, loading, success, and error messages. Empty values retain the translated defaults. **Hide status messages** hides them visually while keeping screen reader announcements. It does not hide the separate address-autocomplete fallback notice.

## Troubleshooting {#troubleshooting}

- **No controls appear:** Enable an address or device-location search method. Both are off on a new element.
- **Known locations are missing:** Check the object type, meta keys or provider field, coordinate order and ranges, and filter-index progress. Address-only values cannot be indexed as coordinates.
- **Address search fails:** Check the saved Google key, billing, enabled APIs, and website/API restrictions. Autocomplete needs Places API (New) in addition to the manual-search APIs.
- **Location selected but results have not changed:** Check **Apply on**. Use Search, Enter, or a Filter Submit in **On submit** mode.
- **Map does not connect:** Target the results loop, set the map's **Sync with query** to it, and select the map explicitly if the layout contains multiple filters or maps.
- **Dragging does not search:** Enable map dragging and **Search on map drag**, then check the visitor checkbox and apply mode.

---

# Filter radio

Source: https://academy.bricksbuilder.io/builder/elements/filter/filter-radio/

*Use radio buttons for single-selection query filters, sorting, or results per page, with optional child-term counts for taxonomy filters.*

Creates a radio button filter interface for single-selection filtering. Users can select one option at a time to filter query results. Supports taxonomy terms, WordPress fields, custom fields, and can also function as a sorting or results-per-page control.

Use radio buttons when visitors should select only one option. Set **Action** to **Sort** or **Results per page** when the control should change ordering or page size.

## Settings

- **Target query** (query-list) - Select the post, term, or user query this filter should target. Available sources depend on the query type.
- **URL parameter** (text) - Define a unique, more readable URL parameter name for this filter.
- **Apply on** (select) - Choose when to apply the filter. Options: Input (immediate), Submit (requires button click). Default: Input.
- **Action** (select) - Filter behavior. Options: Filter (traditional filtering), Sort (sorting control), Results per page (pagination control).
- **Source** (select) - Data source for filter options. Options: Taxonomy, WordPress field, Custom field.
- **Field type** (select) - Type of field when using WordPress field or custom field source. Options: Post, Term, User.
- **Field** (select) - Specific field to filter/sort by (varies based on field type and action).
- **Taxonomy** (select) - Taxonomy to use for filtering when source is taxonomy.
- **Order by** (select) - How to order taxonomy terms. Options: Name, Slug, Term ID, Description, Parent, Count, Include, Menu Order, Meta Value, Meta Value Num.
- **Order meta key** (text) - Meta key for ordering when using meta value ordering.
- **Order** (select) - Sort direction. Options: ASC, DESC. Default: ASC.
- **Terms: Include** (select) - Specific taxonomy terms to include in filter options.
- **Terms: Exclude** (select) - Specific taxonomy terms to exclude from filter options.
- **Top level terms only** (checkbox) - Display only top-level terms (parent = 0) when source is taxonomy.
- **Hide count** (checkbox) - Hide the result count for each option.
- **Count: Include children** (checkbox, Bricks 2.5) - Include descendant-term posts in parent taxonomy counts. Off by default. Available with Action set to Filter, a target query, and a selected taxonomy.
- **Hide empty** (checkbox) - Hide options with zero results.
- **Hide count bracket** (checkbox) - Remove brackets around count values. Style count via .brx-option-count.
- **Hierarchical** (checkbox) - Display taxonomy terms in hierarchical structure.
- **Indent: Prefix** (text) - Prefix text for hierarchical indentation. Default: —.
- **Indent: Gap** (number) - Gap spacing for hierarchical indentation.
- **Provider** (select) - Custom field provider for integration (ACF, Meta Box, etc.).
- **Meta key** (text) - Custom field key for filtering.
- **Compare** (select) - Comparison operator for filtering. Default: Equal.
- **Mode** (select) - Display mode for radio buttons. Options: Default (traditional radio buttons), Button (modern button style).
- **Sort options** (repeater) - Configure sorting options when Action is set to Sort.
  - **Source** (select) - Sort field, including **Distance** in Bricks 2.5.
  - **Label** (text) - Display label for the sort option.
  - **Order** (select) - Ascending or Descending. For Distance, nearest first or farthest first.
  - **Meta key** (text) - Meta key for meta-based sorting.
- **Results per page options** (text) - Comma-separated list of results per page options when Action is set to Results per page. Default: 10, 20, 50, 100.
- **Active filter** - Settings for active filter display.
  - **Prefix** (text) - Text to display before filter value.
  - **Suffix** (text) - Text to display after filter value.
  - **Title** (text) - Custom title attribute for filter links.

## Parent-Term Counts {#parent-term-counts}

Enable **Count: Include children** when a parent option should count posts assigned to its child terms and deeper descendants. Posts assigned to both a parent and a descendant count once for the parent. The setting works independently of **Hierarchical** display and is shared when the element uses a global filter. See [taxonomy child counts](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#taxonomy-child-counts) for setup, indexing, and an example.

## Default selection {#default-selection}

Starting with **Bricks 2.5**, this filter can apply a selection before the first query runs. Use **Default value** for one exact option value. For the Sort action, enter a configured sort value such as `title_ASC` or `distance_ASC`; for Results per page, enter a configured page size such as `20`. Dynamic data is supported.

A Distance default such as `distance_ASC` also requires a valid location from a Geolocation filter targeting the same query. Without one, Bricks clears the Distance selection and uses the query's normal order.

The default applies even with **Apply on** set to **Submit**. Filter URL selections take precedence, and **Reset** clears the selection instead of restoring the default. A fresh visit or reload without filter parameters applies it again. See [default filter values](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#default-values) for shared defaults, validation, and URL behavior.

## Distance sorting {#distance-sorting}

Starting with **Bricks 2.5**, set **Action** to **Sort** and add **Distance** as a sort option's **Source**. Set **Order** to **Ascending** for nearest first or **Descending** for farthest first, and give the option a descriptive **Label**.

A [Geolocation filter](https://academy.bricksbuilder.io/builder/elements/filter/filter-geolocation/) must target the same query and provide a valid location, including a default location. Sorting keeps its radius constraint.

Distance options remain visible but disabled without a valid location. A valid location enables them even when no results match. Clearing the location also clears a selected Distance sort and restores the query's normal order. Choosing a sort option never requests device location.

With this filter set to **Submit** and Geolocation set to **On submit**, a resolved pending location enables Distance before submission so visitors can apply both together. See [Distance sorting setup](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#distance-sorting) for apply modes, URL behavior, and failed requests.

> **Developer reference**
>
> See the [Filter - Radio Schema](https://academy.bricksbuilder.io/developer/schema/elements/filter-radio/) for the full JSON schema of this element's settings and controls.

---

# Filter search

Source: https://academy.bricksbuilder.io/builder/elements/filter/filter-search/

*Search query results without a page reload, configure initial search text, and choose AJAX or redirect behavior for Enter.*

Provides a live AJAX search input for real-time content filtering. Searches through post content, titles, and custom fields without page refresh. Features debouncing, minimum character requirements, and optional clear functionality.

**Tip:** Perfect for creating instant search experiences. Use the debounce setting to control API call frequency, and minimum characters to improve performance.

## Settings

- **Target query** (query-list) - Select the Posts, Terms, or Users query this filter should target.
- **URL parameter** (text) - Define a unique, more readable URL parameter name for this filter.
- **Apply on** (select) - Choose when to apply the filter. Options: Input (immediate), Submit (button click or Enter). Default: Input.
- **Debounce (ms)** (number) - Delay before triggering search after typing stops. Default: 500ms.
- **Min. characters** (number) - Minimum characters required to trigger search. Default: 3.
- **Enter action** (select, Bricks 2.4) - Choose **AJAX search** (default) or **Redirect to URL**. Requires a target query.
- **Trigger Filter Submit interactions** (checkbox, Bricks 2.4) - Run the target query's Filter Submit start/end interactions when Enter triggers an AJAX search. Disabled by default and available when Enter action is AJAX search.
- **Redirect to** (text, Bricks 2.4) - Destination URL when Enter action is Redirect to URL. Active filters for the same query are appended as URL parameters.
- **Open in new tab** (checkbox, Bricks 2.4) - Open the Enter-key redirect in a new tab. Available when a redirect URL is set.
- **Input** - Settings for the search input field.
  - **Placeholder** (text) - Placeholder text for the search input. Default: Search.
  - **Placeholder typography** (typography) - Typography for placeholder text.
  - **Label** (text) - Optional label text above the input field.
  - **Label typography** (typography) - Typography for the label text.
- **Icon (Clear)** - Settings for the clear/reset icon.
  - **Icon** (icon) - Icon to display for clearing the search.
  - **Icon color** (color) - Color of the clear icon.
  - **Icon size** (number) - Size of the clear icon.
- **Active filter** - Settings for active filter display.
  - **Prefix** (text) - Text to display before filter value.
  - **Suffix** (text) - Text to display after filter value.
  - **Title** (text) - Custom title attribute for filter links.

## Search with Enter

Pressing Enter runs the configured action immediately, including when **Apply on** is set to **Submit**. Enter bypasses the typing debounce and minimum character threshold.

For a search field that takes visitors to another results page, select a **Target query**, set **Enter action** to **Redirect to URL**, and enter the destination under **Redirect to**. Configure the destination's filters to recognize the same URL parameter names. Leave **Open in new tab** off to navigate in the current tab. An empty redirect URL falls back to an AJAX search.

For an AJAX search that should close an Offcanvas after submission, enable **Trigger Filter Submit interactions** and use the [Filter Submit interaction triggers](https://academy.bricksbuilder.io/builder/features/interactions/#filter-submit-triggers). Ordinary typing does not trigger these submit interactions. The redirect action does not run them.

## Default selection {#default-selection}

Starting with **Bricks 2.5**, this filter can apply a selection before the first query runs. Use **Default value** to set initial search text. The field supports dynamic data and treats commas as part of the search text.

The default applies even with **Apply on** set to **Submit**. Filter URL selections take precedence, and **Reset** clears the selection instead of restoring the default. A fresh visit or reload without filter parameters applies it again. See [default filter values](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#default-values) for shared defaults, validation, and URL behavior.

> **Developer reference**
>
> See the [Filter - Search Schema](https://academy.bricksbuilder.io/developer/schema/elements/filter-search/) for the schema snapshot and Bricks 2.4 settings reference.

---

# Filter range

Source: https://academy.bricksbuilder.io/builder/elements/filter/filter-range/

*Filter query results by numeric ranges using sliders or input fields, with optional default minimum and maximum values.*

Creates a range slider or input interface for filtering content by numeric ranges. Perfect for price filtering, numeric custom fields, or any data that has minimum and maximum values. Supports both slider and input field display modes.

**Tip:** Essential for e-commerce price filtering or any scenario where users need to filter by numeric ranges.

## Settings

- **Target query** (query-list) - Select the Posts, Terms, or Users query this filter should target.
- **URL parameter** (text) - Define a unique, more readable URL parameter name for this filter.
- **Apply on** (select) - Choose when to apply the filter. Options: Input (immediate), Submit (requires button click). Default: Input.
- **Source** (select) - Data source for filter options. Currently limited to Custom field.
- **Field type** (select) - Type of field when using custom field source. Options: Post, Term, User.
- **Provider** (select) - Custom field provider for integration (ACF, Meta Box, etc.).
- **Meta key** (text) - Custom field key containing numeric values for range filtering.
- **Disable auto min/max value** (checkbox) - Manually set min/max values instead of auto-detecting from query results.
- **Mode** (select) - Display mode for the range filter. Options: Slider (visual slider), Input (text inputs).
- **Step** (number) - Increment step for range values. Default: 1.
- **Decimal places** (number) - Number of decimal places to display. Default: 0.
- **Thousand separator** (checkbox) - Add thousand separators to displayed values.
- **Separator** (text) - Thousand separator character. Default: ,.
- **Label** - Settings for range value labels.
  - **Min** (text) - Label for minimum value.
  - **Max** (text) - Label for maximum value.
  - **Direction** (direction) - Layout direction for min/max labels (row/column).
  - **Gap** (number) - Spacing between min/max labels.
- **Input** - Settings for input field mode.
  - **Placeholder** (text) - Placeholder text for input fields.
  - **Typography** (typography) - Typography for input field text.
- **Slider** - Settings for slider mode.
  - **Track color** (color) - Color of the slider track.
  - **Range color** (color) - Color of the selected range on the slider.
  - **Handle color** (color) - Color of the slider handles.
  - **Handle size** (number) - Size of the slider handles.
  - **Track height** (number) - Height of the slider track.
- **Active filter** - Settings for active filter display.
  - **Prefix** (text) - Text to display before filter value.
  - **Suffix** (text) - Text to display after filter value.
  - **Title** (text) - Custom title attribute for filter links.

## Default selection {#default-selection}

Starting with **Bricks 2.5**, this filter can apply a selection before the first query runs. Under **Default value**, enter numeric **Minimum** and **Maximum** values. Leave one endpoint empty to use the original range boundary. Defaults are limited to the original available range and support dynamic data.

The default applies even with **Apply on** set to **Submit**. Filter URL selections take precedence, and **Reset** clears the selection instead of restoring the default. A fresh visit or reload without filter parameters applies it again. See [default filter values](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#default-values) for shared defaults, validation, and URL behavior.

> **Developer reference**
>
> See the [Filter - Range Schema](https://academy.bricksbuilder.io/developer/schema/elements/filter-range/) for the full JSON schema of this element's settings and controls.
