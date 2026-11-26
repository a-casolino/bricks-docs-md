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
