# Taxonomy

Source: https://academy.bricksbuilder.io/builder/elements/single/taxonomy/

*Displays taxonomy terms for the current post.*

Displays taxonomy terms for the current post.

## Settings

- **Taxonomy** (select) - Taxonomy to display terms from. Default: post_tag.
- **Disable link** (checkbox) - Remove links from taxonomy terms.
- **Separator** (text) - Text to display between terms.
- **Order by** (select) - Sort terms by criteria. Default: Name.
- **Order** (select) - Sort direction. Default: Ascending.
- **Size** (select) - Button size for terms.
- **Style** (select) - Button style for terms. Default: dark.
- **Spacing** (number) - Gap between terms. Default: 10px.
- **Icon** (icon) - Icon to display with each term.

> **Developer reference**
>
> See the [Taxonomy Schema](https://academy.bricksbuilder.io/developer/schema/elements/post-taxonomy/) for the full JSON schema of this element's settings and controls.

---

# Pagination

Source: https://academy.bricksbuilder.io/builder/elements/wordpress/pagination/

*The Pagination element displays page navigation for query results with customizable styling.*

The Pagination element displays page navigation for query results with customizable styling.

## Settings

- **Query** (query-list) - Select which query this pagination controls.

- **Alignment** (justify-content) - Horizontal alignment of pagination links.

- **Height** (number with units) - Height of pagination buttons.

- **Width** (number with units) - Width of pagination buttons.

- **Spacing** (number with units) - Gap between pagination buttons. Default: 20px.

- **Background** (color) - Background color of pagination buttons.

- **Border** (border) - Border styling for pagination buttons.

- **Typography** (typography) - Font settings for pagination buttons.

### Current

- **Background** (color) - Background color of the current page button.

- **Border** (border) - Border styling for the current page button.

- **Typography** (typography) - Font settings for the current page button.

### Icons

- **Previous Icon** (icon) - Icon for the previous page button.

- **Next Icon** (icon) - Icon for the next page button.

### Miscellaneous

- **End Size** (number) - Number of page numbers shown at the start and end. Default: 1.

- **Mid Size** (number) - Number of page numbers shown on each side of current page. Default: 2.

> **Developer reference**
>
> See the [Pagination Schema](https://academy.bricksbuilder.io/developer/schema/elements/pagination/) for the full JSON schema of this element's settings and controls.

---

# Nav menu

Source: https://academy.bricksbuilder.io/builder/elements/wordpress/nav-menu/

*The Nav Menu element displays WordPress navigation menus with customizable styling and behavior. It supports mega menus, multilevel navigation, mobile.*

The Nav Menu element displays WordPress navigation menus with customizable styling and behavior. It supports mega menus, multilevel navigation, mobile responsiveness, and various animation effects.

## Settings

### Menu Selection

- **Menu (WordPress)** (select) - Select a WordPress navigation menu to display. Options are populated from available WordPress menus. Includes a link to manage menus in WordPress admin.

- **Alignment** (direction) - Layout direction of the menu. Controls `flex-direction` property for `.bricks-nav-menu` selector.

### Top level

- **Justify content** (justify-content) - Horizontal alignment of menu items. Excludes space options. Controls `justify-content` property for `.bricks-nav-menu > li > a` and `.bricks-nav-menu > li > .brx-submenu-toggle` selectors.

- **Gap** (number with units) - Gap between menu items. Controls `gap` property for `.bricks-nav-menu` selector.

- **Margin** (spacing) - Margin around menu items. Controls `margin` property for `.bricks-nav-menu > li` selector.

- **Padding** (spacing) - Padding inside menu items. Controls `padding` property for `.bricks-nav-menu > li > a` and `.bricks-nav-menu > li > .brx-submenu-toggle > *` selectors.

- **Background** (background) - Background styling for menu items. Excludes video. Controls `background` property for `.bricks-nav-menu > li > a` and `.bricks-nav-menu > li > .brx-submenu-toggle` selectors.

- **Border** (border) - Border styling for menu items. Controls `border` property for `.bricks-nav-menu > li > a` and `.bricks-nav-menu > li > .brx-submenu-toggle` selectors.

- **Typography** (typography) - Font settings for top-level menu items. Controls `font` property for `.bricks-nav-menu > li > a` and `.bricks-nav-menu > li > .brx-submenu-toggle > *` selectors.

#### Active State

- **Active** (separator) - Visual separator for active state controls.

- **Active background** (background) - Background styling for active/current page items. Controls `background` property for current menu item selectors including `.bricks-nav-menu > .current-menu-item > a`, `.bricks-nav-menu > .current-menu-item > .brx-submenu-toggle`, and ancestor selectors.

- **Active border** (border) - Border styling for active items. Controls `border` property for current menu item selectors including `.bricks-nav-menu .current-menu-item > a`, `.bricks-nav-menu .current-menu-item > .brx-submenu-toggle`, and ancestor selectors.

- **Active typography** (typography) - Typography settings for active items. Controls `font` property for current menu item selectors including `.bricks-nav-menu .current-menu-item > a`, `.bricks-nav-menu .current-menu-item > .brx-submenu-toggle > *`, and ancestor selectors.

#### Icon

- **Icon** (separator) - Separator for icon controls.

- **Icon (Sub menu)** (icon) - Icon for submenu toggles. Triggers re-render. Controls SVG rendering for `.bricks-nav-menu > li.menu-item > .brx-submenu-toggle svg` selector.

- **Icon transform** (transform) - Transform settings for submenu icons when closed. Controls `transform` property for `.bricks-nav-menu button[aria-expanded="false"] > *` selector.

- **Icon transform (Open)** (transform) - Transform settings for submenu icons when open. Controls `transform` property for `.bricks-nav-menu button[aria-expanded="true"] > *` selector.

- **Icon typography** (typography) - Typography settings for submenu toggle buttons. Excludes font-family, font-weight, font-style, text-align, text-decoration, text-transform, and letter-spacing. Controls `font` property for `.bricks-nav-menu > li.menu-item-has-children > .brx-submenu-toggle button[aria-expanded]` selector.

- **Icon position** (select) - Position of submenu icons. Options from icon position control options. Default placeholder: "Right".

- **Icon margin** (spacing) - Margin around submenu toggle buttons. Controls `margin` property for `.bricks-nav-menu .brx-submenu-toggle button` selector.

- **Icon padding** (spacing) - Padding inside submenu toggle buttons. Controls `padding` property for `.bricks-nav-menu .brx-submenu-toggle button` selector.

### Sub menu

- **Position: Static** (checkbox) - Enable to position submenus in document flow (e.g. inside offcanvas). Description: "Enable to position in document flow (e.g. inside offcanvas)."

- **Background** (background) - Background styling for sub-menus. Excludes video. Controls `background` property for `.bricks-nav-menu .sub-menu` selector.

- **Border** (border) - Border styling for sub-menus. Controls `border` property for `.bricks-nav-menu .sub-menu` selector.

- **Box shadow** (box-shadow) - Shadow effect for sub-menus. Controls `box-shadow` property for `.bricks-nav-menu .sub-menu` selector.

- **Transform** (transform) - Transform settings for sub-menus. Controls `transform` property for `.bricks-nav-menu > li > .sub-menu` and `.bricks-nav-menu > li > .brx-megamenu` selectors.

- **Transform (Open)** (transform) - Transform settings for sub-menus when open. Controls `transform` property for `.bricks-nav-menu > li.open > .sub-menu` and `.bricks-nav-menu > li.open > .brx-megamenu` selectors.

#### Caret

- **Caret** (separator) - Separator for caret controls.

- **Size** (number with units) - Size of the caret (triangle pointer). Triggers re-render. Controls `border-width` property for `.bricks-nav-menu > li > .sub-menu.caret::before` selector.

- **Color** (color) - Color of the caret. Controls `border-bottom-color` property for `.bricks-nav-menu > li > .sub-menu.caret::before` selector. Only available when caret size is set.

- **Transform** (transform) - Transform settings for the caret. Controls `transform` property for `.bricks-nav-menu > li > .sub-menu.caret::before` selector. Only available when caret size is set.

- **Position** (dimensions) - Position settings for the caret. Controls positioning properties for `.bricks-nav-menu > li > .sub-menu.caret::before` selector. Only available when caret size is set.

#### Item

- **Item** (separator) - Separator for submenu item controls.

- **Justify content** (justify-content) - Horizontal alignment of submenu items. Excludes space options. Controls `justify-content` property for `.bricks-nav-menu .sub-menu a` and `.bricks-nav-menu .sub-menu button` selectors.

- **Padding** (spacing) - Padding inside submenu items. Controls `padding` property for `.bricks-nav-menu .sub-menu a` and `.bricks-nav-menu .sub-menu button` selectors.

- **Background** (background) - Background styling for submenu items. Controls `background` property for `.bricks-nav-menu .sub-menu .menu-item` selector.

- **Border** (border) - Border styling for submenu items. Controls `border` property for `.bricks-nav-menu .sub-menu > li` selector.

- **Typography** (typography) - Font settings for submenu items. Controls `font` property for `.bricks-nav-menu .sub-menu > li > a` and `.bricks-nav-menu .sub-menu > li > .brx-submenu-toggle > *` selectors.

#### Active State

- **Active** (separator) - Separator for submenu active state controls.

- **Active background** (background) - Background styling for active submenu items. Controls `background` property for current submenu item selectors including `.bricks-nav-menu .sub-menu > .current-menu-item > a`, `.bricks-nav-menu .sub-menu > .current-menu-item > .brx-submenu-toggle`, and ancestor selectors.

- **Active border** (border) - Border styling for active submenu items. Controls `border` property for current submenu item selectors including `.bricks-nav-menu .sub-menu > .current-menu-item > a`, `.bricks-nav-menu .sub-menu > .current-menu-item > .brx-submenu-toggle`, and ancestor selectors.

- **Active typography** (typography) - Typography settings for active submenu items. Controls `font` property for current submenu item selectors including `.bricks-nav-menu .sub-menu > .current-menu-item > a`, `.bricks-nav-menu .sub-menu > .current-menu-item > .brx-submenu-toggle > *`, and ancestor selectors.

#### Icon

- **Icon** (separator) - Separator for submenu icon controls.

- **Icon** (icon) - Icon for submenu toggles. Triggers re-render. Controls SVG rendering for `.bricks-nav-menu .sub-menu .brx-submenu-toggle svg` selector.

- **Icon size** (number with units) - Size of submenu icons. Controls `height` and `width` properties for `.bricks-nav-menu .sub-menu .brx-submenu-toggle svg` selector, and `font-size` for `.bricks-nav-menu .sub-menu .brx-submenu-toggle i` selector.

- **Icon transform** (transform) - Transform settings for submenu icons. Controls `transform` property for `.bricks-nav-menu .sub-menu button > *` selector.

- **Icon transform (Open)** (transform) - Transform settings for submenu icons when open. Controls `transform` property for `.bricks-nav-menu .sub-menu button[aria-expanded="true"] > *` selector.

- **Icon typography** (typography) - Typography settings for submenu toggle buttons. Excludes font-family, font-weight, font-style, text-align, text-decoration, text-transform, and letter-spacing. Controls `font` property for `.bricks-nav-menu .sub-menu .brx-submenu-toggle > a + button` selector.

- **Icon position** (select) - Position of submenu icons. Options from icon position control options. Default placeholder: "Right".

- **Icon margin** (spacing) - Margin around submenu toggle buttons. Controls `margin` property for `.bricks-nav-menu .sub-menu .brx-submenu-toggle button` selector.

- **Icon padding** (spacing) - Padding inside submenu toggle buttons. Controls `padding` property for `.bricks-nav-menu .sub-menu .brx-submenu-toggle button` selector.

### Mobile menu

- **Mobile menu** (separator) - Separator for mobile menu controls.

- **Hide at breakpoint** / **Show at breakpoint** (select) - Breakpoint at which to show/hide mobile menu. Options include all breakpoints plus "Always" and "Never". Default placeholder: "Mobile landscape". Triggers re-render.

- **Position** (select) - Position of mobile menu. Options: Right, Left. Default placeholder: "Left".

- **Top** (number with units) - Top position of mobile menu. Controls `top` property for `.bricks-mobile-menu-wrapper` selector.

- **Width** (number with units) - Width of mobile menu. Controls `width` property for `.bricks-mobile-menu-wrapper` selector. Default placeholder: "300px".

- **Height** (number with units) - Height of mobile menu. Controls `height` property for `.bricks-mobile-menu-wrapper` selector.

- **Fade in** (checkbox) - Enable fade-in animation for mobile menu.

- **Vertical** (justify-content) - Vertical alignment of mobile menu content. Controls `justify-content` property for `.bricks-mobile-menu-wrapper` selector. Default placeholder: "Top".

- **Horizontal** (align-items) - Horizontal alignment of mobile menu content. Excludes stretch option. Controls `align-items` and `justify-content` properties for `.bricks-mobile-menu-wrapper` selector, and sets `width` to `auto` for `.bricks-mobile-menu-wrapper a`. Default placeholder: "Top".

- **Text align** (text-align) - Text alignment in mobile menu. Controls `text-align` property for `.bricks-mobile-menu-wrapper` selector.

- **Background** (background) - Background styling for mobile menu wrapper. Controls `background` property for `.bricks-mobile-menu-wrapper:before` selector.

- **Background filters** (filters) - Background filters for mobile menu. Controls `filter` property for `.bricks-mobile-menu-wrapper:before` selector.

- **Box shadow** (box-shadow) - Shadow effect for mobile menu. Controls `box-shadow` property for `.bricks-mobile-menu-wrapper:before` selector.

- **Overlay** (background) - Background styling for mobile menu overlay. Excludes video. Controls `background` property for `.bricks-mobile-menu-overlay` selector.

#### Top level

- **Top level** (separator) - Separator for mobile menu top-level controls.

- **Padding** (spacing) - Padding for top-level mobile menu items. Controls `padding` property for `.bricks-mobile-menu > li > a` and `.bricks-mobile-menu > li > .brx-submenu-toggle > *` selectors. Default placeholder: top 0, right 30, bottom 0, left 30.

- **Background** (color) - Background color for mobile menu items. Controls `background-color` property for `.bricks-mobile-menu > li > a` and `.bricks-mobile-menu > li > .brx-submenu-toggle` selectors.

- **Background (Active)** (color) - Background color for active mobile menu items. Controls `background-color` property for `[aria-current="page"]` and `.bricks-mobile-menu > .current-menu-item > .brx-submenu-toggle` selectors.

- **Border** (border) - Border styling for mobile menu items. Controls `border` property for `.bricks-mobile-menu > li > a` and `.bricks-mobile-menu > li > .brx-submenu-toggle` selectors.

- **Border (Active)** (border) - Border styling for active mobile menu items. Controls `border` property for current menu item selectors.

- **Typography** (typography) - Font settings for mobile menu items. Excludes text-align. Controls `font` property for `.bricks-mobile-menu > li > a` and `.bricks-mobile-menu > li > .brx-submenu-toggle > *` selectors.

- **Typography (Active)** (typography) - Typography settings for active mobile menu items. Excludes text-align. Controls `font` property for various current menu item selectors.

#### Icon

- **Icon (Sub menu)** (icon) - Icon for mobile submenu toggles. Triggers re-render. Controls SVG rendering for `.bricks-mobile-menu-wrapper .brx-submenu-toggle svg` selector.

- **Close icon (Sub menu)** (icon) - Close icon for mobile submenu toggles. Triggers re-render. Only available when main icon is set. Controls SVG rendering for `.bricks-mobile-menu-wrapper .brx-submenu-toggle svg.close` selector.

- **Icon typography** (typography) - Typography settings for mobile submenu toggle buttons. Excludes font-family, font-weight, font-style, text-align, text-decoration, text-transform, and letter-spacing. Controls `font` property for `.bricks-mobile-menu > .menu-item-has-children .brx-submenu-toggle button` selector. Only available when icon is set.

- **Icon position** (select) - Position of mobile submenu icons. Options from icon position control options. Default placeholder: "Right".

- **Icon margin** (spacing) - Margin around mobile submenu toggle buttons. Controls `margin` property for `.bricks-mobile-menu .menu-item-has-children .brx-submenu-toggle button` selector.

#### Sub menu

- **Sub menu** (separator) - Separator for mobile submenu controls. Description: "Keep open while styling".

- **Padding** (spacing) - Padding for mobile submenu items. Controls `padding` property for `.bricks-mobile-menu .sub-menu > .menu-item > a` and `.bricks-mobile-menu .sub-menu > .menu-item > .brx-submenu-toggle > *` selectors.

- **Background** (color) - Background color for mobile submenu items. Controls `background-color` property for `.bricks-mobile-menu .sub-menu > .menu-item > a` and `.bricks-mobile-menu .sub-menu > .menu-item > .brx-submenu-toggle` selectors.

- **Background (Active)** (color) - Background color for active mobile submenu items. Controls `background-color` property for current submenu item selectors.

- **Border** (border) - Border styling for mobile submenu items. Controls `border` property for `.bricks-mobile-menu .sub-menu > .menu-item` selector.

- **Border (Active)** (border) - Border styling for active mobile submenu items. Controls `border` property for current submenu item selectors.

- **Typography** (typography) - Font settings for mobile submenu items. Controls `font` property for `.bricks-mobile-menu .sub-menu > li > a` and `.bricks-mobile-menu .sub-menu > li > .brx-submenu-toggle > *` selectors.

- **Active typography** (typography) - Typography settings for active mobile submenu items. Controls `font` property for current submenu item selectors.

#### Hamburger toggle

- **Hamburger toggle** (separator) - Separator for hamburger toggle controls.

- **aria-label** (text) - Accessibility label for hamburger toggle button. Default placeholder: "Open mobile menu".

- **Toggle width** (number with units) - Width of hamburger toggle bars. Controls `width` property for `.bricks-mobile-menu-toggle`, `.bricks-mobile-menu-toggle .bar-top`, `.bricks-mobile-menu-toggle .bar-center`, and `.bricks-mobile-menu-toggle .bar-bottom` selectors with `!important`.

- **Color** (color) - Color of hamburger toggle bars. Controls `color` property for `.bricks-mobile-menu-toggle` selector.

- **Hide close** (checkbox) - Hide hamburger toggle when mobile menu is open. Controls `display` property for `&.show-mobile-menu .bricks-mobile-menu-toggle` selector (sets to `none` with `!important`).

- **Color close** (color) - Color of hamburger toggle when mobile menu is open. Controls `color` property for `&.show-mobile-menu .bricks-mobile-menu-toggle` selector with `!important`.

- **Close position** (dimensions) - Position of hamburger toggle when mobile menu is open. Controls positioning properties for `&.show-mobile-menu .bricks-mobile-menu-toggle` selector.

### Mega menu

- **Enable** (checkbox) - Enable mega menu functionality.

- **CSS selector** (text) - CSS selector for mega menu positioning. Uses width & horizontal position of target node. Only available when mega menu is enabled.

- **Toggle on** (select) - How mega menus are triggered. Options: Click, Hover, Click or hover. Default placeholder: "Hover". Only available when mega menu is enabled.

- **Transition** (text) - Transition settings for mega menus. Supports dynamic data. Controls `transition` property for `.brx-megamenu` selector. Only available when mega menu is enabled.

- **Transform** (transform) - Transform settings for mega menus. Controls `transform` property for `.bricks-nav-menu > .brx-has-megamenu > .brx-megamenu` selector. Only available when mega menu is enabled.

- **Transform (Open)** (transform) - Transform settings for mega menus when open. Controls `transform` property for `.bricks-nav-menu > .brx-has-megamenu.open > .brx-megamenu` selector. Only available when mega menu is enabled.

### Multilevel

- **Enable** (checkbox) - Enable multilevel navigation functionality.

- **Back: Text** (text) - Text for back button in multilevel navigation. Only available when multilevel is enabled.

- **Back: Typography** (typography) - Typography settings for back button. Controls `font` property for `.brx-multilevel-back` selector. Only available when multilevel is enabled.

- **Back: Background** (color) - Background color for back button. Controls `background-color` property for `.brx-multilevel-back` selector. Only available when multilevel is enabled.

> **Developer reference**
>
> See the [Nav Menu Schema](https://academy.bricksbuilder.io/developer/schema/elements/nav-menu/) for the full JSON schema of this element's settings and controls.

---

# Posts

Source: https://academy.bricksbuilder.io/builder/elements/wordpress/posts/

*The Posts element displays a list or grid of posts with customizable query, layout, and styling options.*

The Posts element displays a list or grid of posts with customizable query, layout, and styling options.

## Settings

- **Query** (query) - Configure which posts to display with filters for post type, categories, tags, etc.

- **Link entire post** (checkbox) - Make the entire post card clickable.

### Layout

- **Layout** (select) - Display style. Options: `list`, `grid`, `masonry`, `metro`.

- **Columns** (number) - Number of columns in grid layout.

- **Spacing** (number with units) - Gap between posts.

- **Image height** (number with units) - Fixed height for images.

- **Image ratio** (text) - Aspect ratio for images.

### Image

- **Image size** (select) - Size of post images.

- **Image position** (select) - Position of images in post cards.

- **Image width** (number with units) - Custom image width.

- **Image height** (number with units) - Custom image height.

### Fields

- **Post title** (checkbox) - Display post titles.

- **Post title tag** (select) - HTML tag for titles.

- **Meta data** (checkbox) - Display post meta (date, author, etc.).

- **Meta data** (repeater) - Configure which meta fields to show.

- **Excerpt** (checkbox) - Display post excerpts.

- **Excerpt length** (number) - Number of words in excerpt.

- **Read more text** (text) - Custom read more link text.

### Content

- Typography and styling controls for post content.

### Overlay

- Overlay settings for post images.

### Filter

- **Filter** (checkbox) - Enable category/tag filtering.

- **Filter taxonomy** (select) - Which taxonomy to filter by.

- **Filter position** (select) - Where to display filters.

### Pagination

- **Pagination** (select) - Pagination type. Options: `none`, `numbers`, `load more`, `infinite scroll`.

- **Load more text** (text) - Text for load more button.

- **Loading text** (text) - Text shown while loading.

- **No more posts text** (text) - Text when no more posts available.

> **Developer reference**
>
> See the [Posts Schema](https://academy.bricksbuilder.io/developer/schema/elements/posts/) for the full JSON schema of this element's settings and controls.

---

# Search

Source: https://academy.bricksbuilder.io/builder/elements/wordpress/search/

*Displays a search form with input field and submit button, or an icon that opens an overlay search.*

Displays a search form with input field and submit button, or an icon that opens an overlay search.

## Settings

- **Type** (select) - Choose between Input or Icon & Overlay. Default: Input.
- **aria-label** (text) - Accessibility label for overlay type. Required for overlay.
- **Action URL** (text) - URL where search form submits. Default: home URL.
- **Additional parameters** (repeater) - Hidden input fields added to search form.

### Input
- **Height** (number) - Input field height.
- **Width** (number) - Input field width.
- **Placeholder** (text) - Placeholder text. Default: "Search ...".
- **Placeholder color** (color) - Color of placeholder text.
- **Background color** (color) - Input background color.
- **Border** (border) - Input border settings.
- **Box shadow** (box-shadow) - Input box shadow.
- **Typography** (typography) - Input text typography.
- **Show label** (checkbox) - Display label above input. Default: false.
- **Label text** (text) - Text for input label.
- **Label typography** (typography) - Typography for input label.

### Button / Icon
- **aria-label** (text) - Accessibility label for button.
- **Text** (text) - Button text.
- **Icon** (icon) - Button icon.
- **Padding** (spacing) - Button padding.
- **Height** (number) - Button height.
- **Width** (number) - Button width.
- **Background color** (color) - Button background color.
- **Border** (border) - Button border settings.
- **Box shadow** (box-shadow) - Button box shadow.
- **Typography** (typography) - Button text typography.

### Overlay
- **Direction (Form)** (direction) - Flex direction of overlay form.
- **Gap** (number) - Gap between form elements.
- **Title** (text) - Overlay title. Default: "Search site".
- **Title tag** (text) - HTML tag for title. Default: h4.
- **Title typography** (typography) - Typography for overlay title.
- **Background** (background) - Overlay background.
- **Background: Overlay** (color) - Overlay background overlay color.
- **Button: Width** (number) - Overlay button width.
- **Button: Padding** (spacing) - Overlay button padding.
- **Button: Background color** (color) - Overlay button background color.
- **Button: Border** (border) - Overlay button border.
- **Button: Typography** (typography) - Overlay button typography.

> **Developer reference**
>
> See the [Search Schema](https://academy.bricksbuilder.io/developer/schema/elements/search/) for the full JSON schema of this element's settings and controls.

---

# Shortcode

Source: https://academy.bricksbuilder.io/builder/elements/wordpress/shortcode/

*The Shortcode element executes WordPress shortcodes within your Bricks pages.*

The Shortcode element executes WordPress shortcodes within your Bricks pages.

## Settings

- **Shortcode** (textarea) - Enter the shortcode to execute, including the square brackets (e.g., `[gallery ids="72,73,74,75" columns="3"]`). Supports dynamic data.

- **Don't render in builder** (checkbox) - Show a placeholder instead of rendering the shortcode in the builder. Useful for shortcodes that slow down the builder or cause conflicts.

- **Placeholder: Width** (number with units) - Width of the placeholder when "Don't render in builder" is enabled.

- **Placeholder: Height** (number with units) - Height of the placeholder when "Don't render in builder" is enabled.

> **Developer reference**
>
> See the [Shortcode Schema](https://academy.bricksbuilder.io/developer/schema/elements/shortcode/) for the full JSON schema of this element's settings and controls.

---

# Sidebar

Source: https://academy.bricksbuilder.io/builder/elements/wordpress/sidebar/

*Displays a WordPress sidebar with its widgets.*

Displays a WordPress sidebar with its widgets.

## Settings

- **Sidebar** (select) - Select which sidebar to display. Default: none.
- **Widget margin** (spacing) - Set the margin for widgets. Default: 0 0 40px 0.
- **Title typography** (typography) - Typography settings for widget titles.
- **Content typography** (typography) - Typography settings for widget content.
- **Search background color** (color) - Background color for search inputs in widgets.
- **Search border** (border) - Border settings for search inputs in widgets.

> **Developer reference**
>
> See the [Sidebar Schema](https://academy.bricksbuilder.io/developer/schema/elements/sidebar/) for the full JSON schema of this element's settings and controls.

---

# WordPress

Source: https://academy.bricksbuilder.io/builder/elements/wordpress/wordpress/

*The WordPress element displays various WordPress widgets with customizable styling.*

The WordPress element displays various WordPress widgets with customizable styling.

## Settings

- **Widget** (select) - Type of WordPress widget to display. Options: `archives`, `calendar`, `categories`, `pages`, `recent comments`, `recent posts`, `tag cloud`, `taxonomy`. Default: `posts`.

- **Icon** (icon) - Optional icon for the widget. Available for most widget types.

- **Icon typography** (typography) - Font settings for the icon.

### Widget-specific settings

- **Show count** (checkbox) - Display item counts. Available for archives, categories, tag cloud, taxonomy.

- **Sort by** (select) - Sort order for pages. Options: `page title`, `page date`, `page modified`, `page order`, `page ID`. Available for pages.

- **Include** (select) - Specific pages to include. Available for pages.

- **Exclude** (select) - Specific pages to exclude. Available for pages.

- **Number of comments** (number) - How many recent comments to show. Available for recent comments.

- **Number of posts** (number) - How many recent posts to show. Available for recent posts.

- **Direction** (direction) - Layout direction for posts. Available for recent posts.

- **Show date** (checkbox) - Display post dates. Available for recent posts.

- **Show featured image** (checkbox) - Display post thumbnails. Available for recent posts.

- **Featured image sizes** (select) - Size of featured images. Available for recent posts.

- **Featured image width** (text) - Custom width for images. Available for recent posts.

- **Featured image height** (text) - Custom height for images. Available for recent posts.

- **Post title typography** (typography) - Font settings for post titles. Available for recent posts.

- **Post meta typography** (typography) - Font settings for post meta. Available for recent posts.

- **Taxonomy** (select) - Which taxonomy to display. Available for tag cloud and taxonomy.

### Title

- **Title** (text) - Custom title for the widget.

- **HTML tag** (select) - HTML tag for the title. Options: `p`, `h1`-`h6`. Default: `h3`.

- **Border** (border) - Border styling for the title.

- **Typography** (typography) - Font settings for the title.

> **Developer reference**
>
> See the [WordPress Schema](https://academy.bricksbuilder.io/developer/schema/elements/wordpress/) for the full JSON schema of this element's settings and controls.

---

# Account - Add payment method

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-add-payment-method/

*Displays the Add payment method endpoint content inside My Account templates.*

Displays the Add payment method endpoint content inside My Account templates.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Wrapper** (separator)
- **Payment Methods List** (separator)
- **Payment Method Item** (separator)
- **Label** (separator)
- **Custom Radio (Checked)** (separator)
- **Color** (color)
- **Payment Box** (separator)
- **Add Payment Method Button** (separator)
- **Margin** (spacing)
- **Padding** (spacing)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - Addresses

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-addresses/

*Displays the customer addresses section inside My Account.*

Displays the customer addresses section inside My Account.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Direction** (direction)
- **Gap** (number)
- **Title** (separator)
- **Address** (separator)
- **Margin** (spacing)
- **Padding** (spacing)
- **Background color** (color)
- **Border** (border)
- **Box shadow** (box-shadow)
- **Typography** (typography)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - Downloads

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-downloads/

*Displays customer downloadable products inside My Account.*

Displays customer downloadable products inside My Account.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Table** (separator)
- **Head** (separator)
- **Body** (separator)
- **Links** (separator)
- **Button** (separator)
- **Background color** (color)
- **Border** (border)
- **Box shadow** (box-shadow)
- **Typography** (typography)
- **Padding** (spacing)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - Edit account

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-form-edit-account/

*Displays the Edit account form inside My Account.*

Displays the Edit account form inside My Account.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Label typography** (typography)
- **Margin** (spacing)
- **Padding** (spacing)
- **Background color** (color)
- **Border** (border)
- **Box shadow** (box-shadow)
- **Typography** (typography)
- **Width** (number)
- **Gap** (number)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - Login form

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-form-login/

*Displays the WooCommerce My Account login form.*

Displays the WooCommerce My Account login form.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Disable** (checkbox)
- **Typography** (typography)
- **Align items** (align-items)
- **Width** (number)
- **Gap** (number)
- **Label typography** (typography)
- **Field** (separator)
- **Margin** (spacing)
- **Padding** (spacing)
- **Background color** (color)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - Edit address

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-form-edit-address/

*Displays the Edit address form inside My Account.*

Displays the Edit address form inside My Account.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Hide** (checkbox)
- **Margin** (spacing)
- **Padding** (spacing)
- **Background color** (color)
- **Border** (border)
- **Box shadow** (box-shadow)
- **Typography** (typography)
- **Label typography** (typography)
- **Placeholder typography** (typography)
- **Field** (separator)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - Lost password

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-form-lost-password/

*Displays the Lost password request form used in My Account flows.*

Displays the Lost password request form used in My Account flows.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Disable** (checkbox)
- **Typography** (typography)
- **Align items** (align-items)
- **Width** (number)
- **Gap** (number)
- **Label typography** (typography)
- **Field** (separator)
- **Margin** (spacing)
- **Padding** (spacing)
- **Background color** (color)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - Register form

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-form-register/

*Displays the WooCommerce account registration form.*

Displays the WooCommerce account registration form.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Generate password** (separator)
- **Typography** (typography)
- **Privacy policy** (separator)
- **Link** (typography)
- **Align items** (align-items)
- **Width** (number)
- **Gap** (number)
- **Label typography** (typography)
- **Field** (separator)
- **Margin** (spacing)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - Reset password

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-form-reset-password/

*Displays the Reset password form used after password reset link validation.*

Displays the Reset password form used after password reset link validation.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Disable** (checkbox)
- **Typography** (typography)
- **Align items** (align-items)
- **Width** (number)
- **Gap** (number)
- **Label typography** (typography)
- **Field** (separator)
- **Margin** (spacing)
- **Padding** (spacing)
- **Background color** (color)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - Orders

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-orders/

*Displays the customer orders table inside My Account.*

Displays the customer orders table inside My Account.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Head** (separator)
- **Body** (separator)
- **Body - Heading** (separator)
- **Links** (separator)
- **Button** (separator)
- **Background color** (color)
- **Border** (border)
- **Box shadow** (box-shadow)
- **Typography** (typography)
- **Padding** (spacing)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - Page v2

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-page-v2/

*Displays the WooCommerce My Account page as editable endpoint states with shared account navigation.*

Displays the WooCommerce My Account page as editable endpoint states with shared account navigation.

https://youtu.be/M1ZZLgnZOjM

> **Note**
>
> This element requires **Bricks > Settings > WooCommerce > Enable advanced modular elements**. The generated states also use the Bricks WooCommerce Notice element, so enable **Enable Bricks WooCommerce "Notice" element** on the same tab.

## Set up the account page

1. Go to **Bricks > Settings > WooCommerce**, enable **Enable advanced modular elements** and **Enable Bricks WooCommerce "Notice" element**, and save.
2. Open **Bricks > Woo Setup Wizard** and choose **My account**. **Advanced (v2)** is selected by default.
3. Click **Setup** and confirm that the existing page content will be replaced.

The wizard adds **Account - Page v2** to the assigned My Account page with a generated structure for every state. See [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) for the other options.

## Where this element works

My Account page.

## Key settings

- **State** (radio) - Switches the builder preview between My Account endpoint states.
- **Direction** (direction)
- **Gap** (number)
- **Disable navigation** (checkbox)
- **Navigation** - Direction, Align items, Justify content, Gap, Border, and Box shadow for the menu; Background, Item padding, Border, Box shadow, and Typography for each item; Active background, Border, Box shadow, and Typography for the current item.
- **Content** - Padding, Background, Border, Box shadow, and Typography for the content area.

Navigation and Content styles apply to every logged-in state at once. Set **Direction** to row to place the menu beside the content, then set the navigation **Direction** to column for a sidebar menu.

The navigation is not shown on the **Login**, **Lost password**, **Lost password (Confirmation)**, **Reset password**, and **Order withdrawal** states.

## Navigation items

The menu items come from the WooCommerce account endpoints. To remove an item, for example **Downloads** in a store without downloadable products, go to **WooCommerce > Settings > Advanced**, clear the endpoint's slug under **Account endpoints**, and save.

## Builder preview

- **Orders** and **View order** use the orders of the account you are logged in with. If that account has no orders, the canvas shows the generated dynamic tags and the empty orders message. Customers see their own orders on the frontend.
- Sample WooCommerce notices (error, success, and info) appear above the states in the builder so you can style them. They are not shown to customers.

## States

- **Dashboard**
- **Orders**
- **View order**
- **Downloads**
- **Addresses**
- **Edit address**
- **Edit account**
- **Payment methods**
- **Add payment method**
- **Login**
- **Lost password**
- **Lost password (Confirmation)**
- **Reset password**
- **Order withdrawal** (requires WooCommerce 11.1 or later with Order Withdrawal enabled)

<div className="screenshot screenshot--control-panel">

![Account Page v2 State controls, including Order withdrawal and the Add missing states button.](https://academy.bricksbuilder.io/assets/account-page-v2-states-with-missing-state.webp)

</div>

## Generated structures

Each state can generate a complete starter block for that endpoint from **Insert a structure**.

Generated structures are appended to the current state content and do not overwrite existing content.

> **Note**
>
> Account Page v2 uses support elements for generated account forms and account orders pagination. Account orders, downloads, addresses, and order actions use v2 query loops and dynamic tags inside the matching account state. If you cannot find a support element in the regular Elements panel, use **Insert a structure** and then edit the generated element in the Structure panel.

![](https://academy.bricksbuilder.io/assets/account-v2-view-orders-structure-example.png)

## Add missing states

If an expected state element is missing, select **Account - Page v2** and click **Add missing states**. Bricks checks all currently available account states and appends any missing state elements without replacing existing states or their content. This can restore an unexpectedly missing state or add a state introduced after the page was built.

The button appears only when states are missing and your builder permissions allow adding elements. States that depend on a disabled WooCommerce feature are excluded. For an Account Page v2 inside a component, edit the component definition to repair its states.

Added states start empty. Select each added state and use **Insert a structure** to generate its starter content. This tool does not restore deleted custom layouts or refill existing empty states; generate content inside an empty state separately.

## Order withdrawal

This public state requires WooCommerce 11.1 or later with **Order Withdrawal** enabled under **WooCommerce > Settings > Advanced > Features**. It lets guests and logged-in customers enter, review, and confirm a withdrawal request.

Select **Order withdrawal (State)** and generate **Complete order withdrawal block** under **Insert a structure**. If the state is missing, use **Add missing states** first. The generated block includes **Your details**, **Review**, and **Confirmation** sections. All three appear together with sample data in the builder; their **Order withdrawal screen** conditions select the matching section on the frontend.

Keep the generated **Account order withdrawal form** wrappers, submit buttons, and screen conditions when customizing the layout. WooCommerce handles validation and submission. Use the [withdrawal dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/#order-withdrawal-tags) to display submitted details. A missing or empty withdrawal state falls back to WooCommerce's native form.

Add a visible link using `{woo_url:order-withdrawal}` so customers can find the endpoint; WooCommerce does not add one automatically. A withdrawal request does not cancel an order or issue a refund.

## Field maintenance

The Edit address state can audit and sync generated account address fields against the current WooCommerce account address field registry.

Use the field maintenance actions after plugins or WooCommerce settings change account address fields:

- **Check address fields**
- **Generate missing fields**
- **Remove invalid fields**
- **Remove duplicate fields**

The Edit address state uses one set of address fields for billing and shipping, so the elements are named without a prefix, for example **Address: Company name**. **Check address fields** compares them with the billing and shipping address fields WooCommerce currently uses. The other buttons appear once the check has found something to fix.

**Generate missing fields** adds the new elements at the top of the Edit address state, outside the edit address form. Drag each one into the **Address field wrapper**, for example below **Address: Last name**, so it renders inside the form.

In Bricks 2.4.3, a field removed with **Remove invalid fields** can stay in the builder canvas until you reload the builder. For the Phone field, the canvas keeps showing "Field not available for the current address." The Structure panel is already correct, and the field is gone from the page once you save.

See [Checkout v2 field maintenance](https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-v2/#field-maintenance) for the same workflow on the checkout.

![](https://academy.bricksbuilder.io/assets/account-v2-sync-address-fields.png)

## Query loops and dynamic data

Account Page v2 supports WooCommerce v2 query loops for account orders, order actions, account downloads, and account addresses.

Use account and order tags such as `{woo_account_address_title}`, `{woo_account_address}`, `{woo_order_number}`, `{woo_order_view_url}`, `{woo_order_download_name}`, and `{woo_order_action_url}` in the matching state or query loop.

See [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/#account-tags) for the complete reference.

## Usage tips

- Use [WooCommerce advanced modular elements](https://academy.bricksbuilder.io/integrations/woocommerce/advanced-modular-elements/) or the [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) to create the recommended Account Page v2 structure.
- Review each state after setup so logged-in, logged-out, password reset, payment method, and order views all match your store design.
- Floating labels are available for the account forms in the Edit address, Edit account, Login, Lost password, Reset password, and Order withdrawal states. The Edit account and Edit address forms generated by the Woo Setup Wizard have them turned on.
- WooCommerce form buttons, such as **Save changes**, **Log in**, and **Register**, do not pick up your theme's button styles. Style them in the element settings or with a global class.
- Use the classic [WooCommerce Account Builder](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-account-builder/) workflow if you prefer separate endpoint templates.

---

# Account - Page

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-page/

*Displays the full My Account layout including navigation and endpoint content.*

Displays the full My Account layout including navigation and endpoint content.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Direction** (direction)
- **Gap** (number)
- **Disable navigation** (checkbox)
- **Align items** (align-items)
- **Justify content** (justify-content)
- **Background** (color)
- **Border** (border)
- **Box shadow** (box-shadow)
- **Item** (separator)
- **Padding** (spacing)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - View order

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-view-order/

*Displays order details for a selected order in My Account.*

Displays order details for a selected order in My Account.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Preview order ID** (number)
- **Hide** (checkbox)
- **Typography** (typography)
- **Mark** (separator)
- **Padding** (spacing)
- **Background color** (color)
- **Title** (separator)
- **Meta** (separator)
- **Description** (separator)
- **Table** (separator)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# WooCommerce Breadcrumbs

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/breadcrumbs/

*Display WooCommerce breadcrumb navigation in Bricks and customize the home link, prefixes, suffixes, separators, and spacing.*

Displays WooCommerce breadcrumb navigation.

## Settings

- **Before** (text) - Text to display before breadcrumbs.

- **Home: URL** (text) - Custom URL for home link. Default: home URL.

- **Home: Label** (text) - Label for home link. Default: "Home".

- **Home: Icon** (icon) - Icon for home link.

- **Home: Gap** (number with units) - Gap between home icon and label.

- **Home: Icon Size** (number) - Size of home icon.

- **Hide label** (checkbox) - Hide home label when icon is present. Only available when Home: Icon is set.

- **Prefix** (text) - Text to display before each breadcrumb item.

- **Suffix** (text) - Text to display after each breadcrumb item.

### Separator

- **Type** (select) - Separator type. Options: Text, Icon. Default: Text.

- **Separator** (text) - Separator text. Default: "/". Only available when Type is not Icon.

- **Icon** (icon) - Separator icon. Only available when Type is Icon.

- **Icon typography** (typography) - Typography for separator icon. Only available when Icon is set. Excludes: font-family, font-weight, font-style, text-align, text-decoration, text-transform, line-height, letter-spacing.

- **Gap** (number with units) - Gap between breadcrumb items.

- **Margin** (spacing) - Margin around separators.

---

# Account - Payment methods

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-payment-methods/

*Displays saved payment methods inside My Account.*

Displays saved payment methods inside My Account.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Head** (separator)
- **Body** (separator)
- **Delete button** (separator)
- **Make default button** (separator)
- **Add payment method** (separator)
- **Background color** (color)
- **Border** (border)
- **Box shadow** (box-shadow)
- **Typography** (typography)
- **Padding** (spacing)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Cart totals

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/cart-collaterals/

*Displays cart totals and related collateral content from the Cart page.*

Displays cart totals and related collateral content from the Cart page.

## Where this element works

Cart page templates.

## Key settings

- **Disable cross sells** (checkbox)
- **Hide title** (checkbox)
- **Title** (typography)
- **Subtotal** (typography)
- **Total** (typography)
- **Table** (separator)
- **Margin** (spacing)
- **Padding** (spacing)
- **Border** (border)
- **Button** (separator)

## Usage tips

- Place cart elements in a dedicated Cart template to avoid empty output on non-cart pages.
- Keep spacing and table styling consistent across cart rows, totals, and coupon sections for better usability.

---

# Cart coupon

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/cart-coupon/

*Displays the coupon input section for the Cart page.*

Displays the coupon input section for the Cart page.

## Where this element works

Cart page templates.

## Key settings

- **General** (separator)
- **Update cart via AJAX** (checkbox)
- **Direction** (direction)
- **Input** (separator)
- **Placeholder** (text)
- **Width** (number)
- **Background color** (color)
- **Border** (border)
- **Placeholder typography** (typography)
- **Button** (text)

## Usage tips

- Place cart elements in a dedicated Cart template to avoid empty output on non-cart pages.
- Keep spacing and table styling consistent across cart rows, totals, and coupon sections for better usability.

---

# Cart items

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/cart-items/

*Displays the cart items table with product rows and quantity controls.*

Displays the cart items table with product rows and quantity controls.

## Where this element works

Cart page templates.

## Key settings

- **Disable link** (checkbox)
- **Header** (separator)
- **Hide** (checkbox)
- **Background** (color)
- **Border** (border)
- **Typography** (typography)
- **Body** (separator)
- **Image** (separator)
- **Disable** (checkbox)
- **Width** (number)

## Usage tips

- Place cart elements in a dedicated Cart template to avoid empty output on non-cart pages.
- Keep spacing and table styling consistent across cart rows, totals, and coupon sections for better usability.

---

# Cart v2

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/cart-v2/

*Displays the WooCommerce cart page as editable Filled cart and Empty cart states.*

Displays the WooCommerce cart page as editable Filled cart and Empty cart states.

> **Note**
>
> This element requires **Bricks > Settings > WooCommerce > Enable advanced modular elements**.

## Where this element works

Cart page. The element only appears in the Elements panel while you edit the page that WooCommerce uses as its cart page.

## Key settings

- **State** (radio) - Switches the builder preview between Filled cart and Empty cart.

## States

- **Filled cart** - Used when the cart contains products.
- **Empty cart** - Used when the cart has no products.

The generated Cart v2 structure keeps both states as internal child elements, so you can edit each state from the Structure panel. The top of the Structure panel shows the state you are editing. Click **Switch** there to change the previewed state.

![](https://academy.bricksbuilder.io/assets/cart-v2-states.png)

## Generated structures

Each state can generate starter content from **Insert a structure**:

- **Complete cart block**
- **Complete empty cart block**

Generated structures are appended to the current state content and do not overwrite existing content.

For a step-by-step setup, see [Cart v2 workflow](https://academy.bricksbuilder.io/integrations/woocommerce/cart/#cart-v2-workflow).

The complete cart block contains a cart loop with one row per product (image, title, price, excerpt, item data, Cart quantity and a remove icon), a cross-sells section, a free shipping progress bar, summary rows for subtotal, coupons, fees, taxes, shipping and total, a checkout button and the Cart coupon element.

> **Note**
>
> In Bricks 2.4.3 the complete cart block includes a WooCommerce Notice element, but generating it from **Insert a structure** does not enable that element. Enable **Bricks > Settings > WooCommerce > Enable Bricks WooCommerce "Notice" element** first, or the canvas shows that the element doesn't exist. The [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) enables it for you.

![](https://academy.bricksbuilder.io/assets/cart-v2-state-insert-structure.png)

> **Note**
>
> Cart v2 uses the Cart form and Cart quantity support elements inside the Filled cart state. If you cannot find a support element in the regular Elements panel, use **Insert a structure** and then edit the generated element in the Structure panel.

![](https://academy.bricksbuilder.io/assets/cart-v2-filled-cart-structure-example.png)

## Builder preview and frontend behavior

While you edit the Filled cart state, the builder previews a sample cart with sample notices. Loops without data, such as coupons or fees, show their dynamic tags on the canvas. Check the real values on the frontend.

On the frontend, the Cart quantity element updates the cart via AJAX (a quantity of zero removes the product), the Cart coupon element applies coupons via AJAX, and each applied coupon gets its own summary row with a remove icon.

The **Coupon total row** below the applied coupons shows the total of all coupons. If your store only allows one coupon at a time, it repeats the coupon amount, so you can delete it.

> **Note**
>
> In Bricks 2.4.3, lazy-loaded images in the Empty cart state stay blank when the last product is removed on the frontend, until the page is reloaded. If your empty state contains images, such as a Products element, disable lazy loading under **Bricks > Settings > Performance**.

## Query loops and dynamic data

Use the **Cart contents** query loop for custom cart item rows. Cart v2 layouts can also use cart total tags such as `{woo_cart_items_count}`, `{woo_cart_order_subtotal}`, `{woo_cart_order_total}`, `{woo_cart_shipping_method}`, `{woo_free_shipping_remaining}`, and `{woo_free_shipping_progress}`.

See [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/) for the complete reference.

## Usage tips

- Use [WooCommerce advanced modular elements](https://academy.bricksbuilder.io/integrations/woocommerce/advanced-modular-elements/) or the [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) to create the recommended Cart v2 structure.
- Design both states so the cart page is complete whether the customer has products in the cart or not.
- Use the classic [Cart template workflow](https://academy.bricksbuilder.io/integrations/woocommerce/cart/) if you prefer separate Cart and Empty Cart templates.

---

# Checkout customer details

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-customer-details/

*Displays billing and shipping customer detail fields on Checkout.*

Displays billing and shipping customer detail fields on Checkout.

## Where this element works

Checkout templates (and order-received context for thank-you flows).

## Key settings

- **Remove billing fields** (select)
- **Remove shipping fields** (select)
- **Title** (separator)
- **Hide** (checkbox)
- **Typography** (typography)
- **Labels** (separator)
- **Margin** (spacing)
- **Fields** (separator)
- **Placeholder typography** (typography)
- **Hide additional information** (checkbox)

## Usage tips

- Use checkout elements only in Checkout templates so forms and order data render correctly.
- Test logged-in and guest checkout flows after styling changes to ensure all states remain usable.

---

# Checkout coupon

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-coupon/

*Displays the coupon prompt and form on the Checkout page.*

Displays the coupon prompt and form on the Checkout page.

## Where this element works

Checkout templates (and order-received context for thank-you flows).

## Key settings

- **Location** (select)
- **Toggleable form** (checkbox)
- **Text** (text)
- **Justify content** (justify-content)
- **Gap** (number)
- **Button** (separator)
- **Disable text** (checkbox)
- **Icon** (icon)
- **Icon typography** (typography)
- **Disable coupon message** (checkbox)

## Usage tips

- Use checkout elements only in Checkout templates so forms and order data render correctly.
- Test logged-in and guest checkout flows after styling changes to ensure all states remain usable.

---

# Checkout login

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-login/

*Displays the returning customer login prompt on Checkout.*

Displays the returning customer login prompt on Checkout.

## Where this element works

Checkout templates (and order-received context for thank-you flows).

## Key settings

- **Location** (select)
- **Toggleable form** (checkbox)
- **Text** (text)
- **Justify content** (justify-content)
- **Gap** (number)
- **Button** (separator)
- **Disable text** (checkbox)
- **Icon** (icon)
- **Icon typography** (typography)
- **Disable login message** (checkbox)

## Usage tips

- Use checkout elements only in Checkout templates so forms and order data render correctly.
- Test logged-in and guest checkout flows after styling changes to ensure all states remain usable.

---

# Checkout order payment

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-order-payment/

*Displays available payment methods and payment actions on Checkout.*

Displays available payment methods and payment actions on Checkout.

## Where this element works

Checkout templates (and order-received context for thank-you flows).

## Key settings

- **Preview order ID** (number)
- **Margin** (spacing)
- **Padding** (spacing)
- **Background** (color)
- **Border** (border)
- **Label typography** (typography)
- **Description** (separator)
- **Typography** (typography)
- **Privacy** (separator)
- **Button** (separator)

## Usage tips

- Use checkout elements only in Checkout templates so forms and order data render correctly.
- Test logged-in and guest checkout flows after styling changes to ensure all states remain usable.

---

# Checkout order review

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-order-review/

*Displays the order review section on Checkout.*

Displays the order review section on Checkout.

## Where this element works

Checkout templates (and order-received context for thank-you flows).

## Key settings

- **Hide title** (checkbox)
- **Title** (text)
- **Title typography** (typography)
- **Subtitles typography** (typography)
- **Items** (separator)
- **Typography** (typography)
- **Padding** (spacing)
- **Border** (border)
- **Margin** (spacing)
- **Background** (color)

## Usage tips

- Use checkout elements only in Checkout templates so forms and order data render correctly.
- Test logged-in and guest checkout flows after styling changes to ensure all states remain usable.

---

# Checkout order table

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-order-table/

*Displays the checkout order table with line items, totals, and taxes.*

Displays the checkout order table with line items, totals, and taxes.

## Where this element works

Checkout templates (and order-received context for thank-you flows).

## Key settings

- **Preview order ID** (number)
- **Padding** (spacing)
- **Background** (color)
- **Border** (border)
- **Typography** (typography)

## Usage tips

- Use checkout elements only in Checkout templates so forms and order data render correctly.
- Test logged-in and guest checkout flows after styling changes to ensure all states remain usable.

---

# Checkout v2

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-v2/

*Displays the WooCommerce checkout page as editable Checkout, Login required, Pay, Thank you, and Order receipt states.*

Displays the WooCommerce checkout page as editable Checkout, Login required, Pay, Thank you, and Order receipt states.

> **Note**
>
> This element requires **Bricks > Settings > WooCommerce > Enable advanced modular elements**.

## Where this element works

Checkout page.

## Key settings

- **State** (radio) - Switches the builder preview between checkout states.

## States

- **Checkout** - Customer details, order summary, payment options, and place order layout.
- **Login required** - Login screen shown when WooCommerce requires login before an order-related checkout screen.
- **Pay** - Payment screen for unpaid orders.
- **Thank you** - Order confirmation screen after checkout.
- **Order receipt** - Receipt screen for unpaid order links that no longer need payment.

![](https://academy.bricksbuilder.io/assets/checkout-v2-states.png)

## Generated structures

The Checkout state can generate these structures:

- **Complete checkout**
- **Billing fields**
- **Shipping fields**
- **Payment options**
- **Additional fields**
- **Order summary**
- **Place order**

When **Complete checkout** is selected, **Generate as multistep** creates a ready-made multistep checkout layout.

The **Billing fields** and **Complete checkout** structures also generate the account credential fields currently required by WooCommerce. Bricks places these fields inside a **Checkout account fields** wrapper so WooCommerce's account-creation settings control their frontend visibility.

The Login required, Pay, Thank you, and Order receipt states each provide a complete block for that state.

> **Note**
>
> Some Checkout v2 support elements, including generated form fields, checkout steps, step navigation items, payment options, and place order sections, rely on the correct Checkout v2 state context. If you cannot find a support element in the regular Elements panel, use **Insert a structure** and then edit the generated element in the Structure panel.

![](https://academy.bricksbuilder.io/assets/checkout-v2-structure-example.png)

## Customize the Checkout state

https://youtu.be/xD0ihyBFErQ

Everything inside the Checkout state is a regular Bricks element. Each form field is its own **WooCommerce form field** element with **Label**, **Hide label**, and **Placeholder** settings, so you can move, group, and lay out fields like any other elements.

The layout from the Woo Setup Wizard also uses the Bricks **Notice**, **Checkout coupon**, and **Checkout login** elements. Enable them under **Bricks > Settings > WooCommerce**, next to **Enable advanced modular elements**.

Common changes after generating the checkout:

- **Collapse the login form:** Select **Checkout login** and enable **Toggleable form**. Returning customers then see a single "Returning customer? Click here to login" line that opens the form.
- **Remove a field:** Select the **Checkout** state and choose the field under **Remove unwanted fields** > **Billing** or **Shipping**. This removes it from WooCommerce's checkout fields. Delete the field's element in the Structure panel as well. In Bricks 2.4.3, the element otherwise still renders as an optional field, and WooCommerce ignores anything customers type into it.
- **Reorder fields:** Drag field elements in the Structure panel. The generated layout places **Billing: Apartment** after the email field, so you may want to move it below **Billing: Street address**.
- **Style all fields at once:** Use the **Style** groups on the **Checkout** state, such as **Input / Textarea / Select** for borders and corners, instead of styling each field. The searchable Country and State dropdowns have their own **Select2** groups, so give them the same border.
- **Style the button:** Select **Checkout place order** to set the button's background, text color, and border radius.
- **Show the order number:** Click **Switch**, choose the **Thank you** state, and add `{woo_order_number}` to its heading, for example `Thank you! Order #{woo_order_number} is confirmed`. The builder previews a sample order, so the number only appears on real orders.

The builder preview of the Checkout state uses a sample cart and shows sample notices and hook placeholders such as `{do_action:woocommerce_...}`. They do not appear on the frontend. Test the result on the frontend with a real cart.

### Floating labels

The **Floating label** style (Checkout state > **Style**) places field labels inside the fields and moves them up when a field has a value. The Woo Setup Wizard enables it for the Checkout and Login required states. Keep the field labels visible for it to work.

In Bricks 2.4.3, when the store sells to a single country, the Country field renders as a plain select and its floating label overlaps the selected country. Until this is fixed, add this rule under **Bricks > Settings > Custom code > Custom CSS**:

```css
.bricks-floating-label .brxe-woocommerce-form-field:has(> .woocommerce-input-wrapper > select:not(.select2-hidden-accessible)) > label {
  top: 10px;
  transform: scale(.75);
  transform-origin: left top;
}
```

## Shipping option labels

> **Note**
>
> The customized shipping-label behavior and Bricks filters described below are available since Bricks 2.4.5.

The **Shipping options** element displays the available shipping methods for each package. An ordinary rate shows the method name as its primary label and the formatted price or **Free** as its secondary label.

When a plugin or custom callback changes `woocommerce_cart_shipping_method_full_label` and supplies usable label content, Bricks displays that complete label once as the primary label. Safe HTML is preserved. For example, a customized label containing **Pickup points: $19.90** appears once, without an additional **Pickup points** name or separate price. If the customization contains no text or meaningful image alternative text, Bricks keeps the method name as the primary label.

Select **Shipping options** in the Structure panel to style its labels:

- **Label** controls style the primary label, including a customized full label.
- **Secondary label** controls style the separate price or other secondary content, when present.

Review existing checkout layouts that styled a plugin's full label through **Secondary label**. The customized full label now uses **Label** styles.

Developers can customize each label independently with [`bricks/woocommerce/shipping_options/primary_label`](https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-shipping_options-primary_label/) and [`bricks/woocommerce/shipping_options/secondary_label`](https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-shipping_options-secondary_label/). Both receive the label HTML, the calculated `WC_Shipping_Rate`, and the Shipping options element instance. These filters change the displayed labels without changing the calculated shipping charge or selected rate.

The secondary filter receives an empty string when a customized full label supplies the primary label. Return separate secondary content if needed, or an empty string to omit it. Bricks only adds the input's `aria-describedby` link when a secondary label is rendered.

## Payment section for free orders

In the **Checkout** state, payment methods are hidden when the cart does not require payment, such as after a coupon reduces the total to zero. They reappear when a shipping or coupon change makes payment necessary again.

The `brx-woo-payment-section` class lets the surrounding payment section, including its heading, hide and reappear with the payment methods. Newly generated **Payment options** and **Complete checkout** structures include this class on the **Payment Options** wrapper, including the multistep layout.

Existing checkout layouts are not updated automatically. If the class is missing, add it manually:

1. Edit the assigned Checkout page with Bricks and select the **Checkout** state.
2. In the Structure panel, select the wrapper containing the payment heading and **Payment options** element. In generated layouts, this is the **Payment Options** Block.
3. Open **Style > CSS > CSS classes** and add `brx-woo-payment-section` without a leading dot. Keep any existing classes, separated by spaces.
4. Keep the terms checkbox and **Place order** controls outside this wrapper so customers can still submit free orders. In a multistep layout, add the class to the payment section wrapper inside the step, rather than the entire Checkout step.
5. Save and test the checkout on the frontend with both a zero total and a total that requires payment.

Without this wrapper class, the payment methods still hide for free orders, but the surrounding heading and section can remain visible.

## Account creation during checkout

Checkout v2 follows the guest checkout and account creation settings under **WooCommerce > Settings > Accounts & Privacy**.

| Guest checkout | Account creation during checkout | Checkout behavior |
| --- | --- | --- |
| Enabled | Disabled | Guests can check out without account fields. |
| Enabled | Enabled | Guests can select **Create an account?** to reveal the required account fields. |
| Disabled | Enabled | Account creation is required. The account fields remain visible without the optional **Create an account?** checkbox. |
| Disabled | Disabled | Logged-out customers see the Checkout v2 **Login required** state. |

WooCommerce decides which credential fields are required:

| Generate account login | Send password setup link | Credential fields |
| --- | --- | --- |
| Enabled | Enabled | None |
| Disabled | Enabled | Username |
| Enabled | Disabled | Password |
| Disabled | Disabled | Username and password |

Generated username and password fields are required. Bricks reads these fields from WooCommerce's current checkout field registry, including fields added by third-party plugins, instead of assuming a fixed set.

The **Allow customers to create an account on the My Account page** setting applies to Account Page v2 registration and does not change account creation during Checkout v2.

## Multistep checkout

Use [Checkout v2 multistep checkout](https://academy.bricksbuilder.io/integrations/woocommerce/multistep-checkout-v2/) when you want the Checkout state split into multiple steps.

You can create the multistep layout with the [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) by choosing **Advanced multistep (v2)**, or generate it from the Checkout state by selecting **Complete checkout** and enabling **Generate as multistep**.

![](https://academy.bricksbuilder.io/assets/checkout-v2-multistep.png)

The generated layout includes Checkout steps navigation, checkout step nav items, checkout step wrappers, and next/back interactions.

![](https://academy.bricksbuilder.io/assets/checkout-v2-multistep-structure-example.png)

![](https://academy.bricksbuilder.io/assets/checkout-v2-multistep-frontend.png)

## Field maintenance

When order notes are disabled in WooCommerce, a saved Order notes field can remain visible in the builder while being hidden on the frontend. Remove unused notes elements or empty headings from **Additional fields**, keeping any fields used by checkout extensions.

Checkout v2 includes a **Sync checkout fields** control group with actions to compare generated fields with the site's current WooCommerce checkout fields:

- **Check checkout fields**
- **Generate missing fields**
- **Remove invalid fields**
- **Remove duplicate fields**

Use these after changing WooCommerce checkout fields, for example the **Company name**, **Address line 2**, or **Phone** field in **Appearance > Customize > WooCommerce > Checkout**, or after installing or removing plugins that change checkout fields. The layout does not follow those changes by itself, because every field is its own element.

https://youtu.be/caoSy6gGefE

Select the **Checkout** state and click **Check checkout fields**. Bricks compares the field elements in the state with the checkout fields WooCommerce currently uses and lists them as missing, invalid, or duplicate. Invalid field elements are also marked in red in the Structure panel. The **Generate missing fields**, **Remove invalid fields**, and **Remove duplicate fields** buttons appear once the check has found something to fix.

- **Generate missing fields** adds an element for each missing field. Billing, shipping, and additional fields are added at the top of the Checkout state, not inside their sections. Drag each one into place in the Structure panel, for example below **Billing: Last name**. A shipping field left at the top also shows when the customer does not ship to a different address.
- **Remove invalid fields** deletes field elements that WooCommerce no longer uses, such as Phone after the field is set to **Hidden**.
- **Remove duplicate fields** deletes extra elements for the same field.

New elements copy the field's current label and placeholder from WooCommerce. Field sync does not update the labels or placeholders of existing field elements.

In Bricks 2.4.3, a removed field can stay visible in the builder canvas even though the Structure panel no longer lists it. Save and reload the builder; the canvas then matches the frontend.

The audit includes WooCommerce's `account` field section. Missing account fields are inserted into the **Checkout account fields** wrapper.

Enabling **Generate account login** or **Send password setup link** does not remove the corresponding saved username or password element from an existing Checkout v2 structure. Until you run field sync, an element that WooCommerce no longer registers can still render as an optional field, but WooCommerce does not process its value because it generates that credential. Run **Check checkout fields**, then **Remove invalid fields**.

Checkout structures created with a Bricks 2.4 beta may contain a standalone **Create account** checkbox or may not contain the account wrapper. Regenerate the checkout structure or use the field sync actions after updating. Bricks creates the wrapper when missing account fields are generated and removes an obsolete standalone checkbox after the replacement wrapper and checkbox exist.

![](https://academy.bricksbuilder.io/assets/checkout-v2-sync-checkout-fields.png)

## Query loops, dynamic tags, and interactions

For saved Thank you layouts, see [Failed-order messages](https://academy.bricksbuilder.io/integrations/woocommerce/checkout/#failed-order-messages) to replace a typed payment failure message with `{woo_order_failed_text}`.

Checkout v2 supports WooCommerce v2 query loops for applied coupons, fees, taxes, order items, order totals, order downloads, and customer notes.

It also adds checkout/order tags such as `{woo_checkout_current_step_number}`, `{woo_order_number}`, `{woo_order_total}`, `{woo_order_item_count}`, and `{woo_order_total_with_item_count}`.

For multistep checkout layouts, use the **Checkout step** interaction action to move to the next step, previous step, a specific step, or a specific checkout field.

See [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/) for the complete reference.

## Usage tips

- Use [WooCommerce advanced modular elements](https://academy.bricksbuilder.io/integrations/woocommerce/advanced-modular-elements/) or the [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) to create the recommended Checkout v2 structure.
- Design every checkout state that customers can reach, especially Pay, Thank you, Order receipt, and Login required.
- Use the classic [Checkout template workflow](https://academy.bricksbuilder.io/integrations/woocommerce/checkout/) if you prefer separate checkout templates.

---

# Checkout thank you

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-thankyou/

*Displays the order received / thank you content after checkout.*

Displays the order received / thank you content after checkout.

## Where this element works

Checkout templates (and order-received context for thank-you flows).

## Key settings

- **Preview order ID** (number)
- **Hide message** (checkbox)
- **Margin** (spacing)
- **Padding** (spacing)
- **Background** (color)
- **Border** (border)
- **Typography** (typography)
- **Label typography** (typography)
- **Action buttons** (separator)
- **Gap** (number)

## Usage tips

- Use checkout elements only in Checkout templates so forms and order data render correctly.
- Test logged-in and guest checkout flows after styling changes to ensure all states remain usable.

---

# Dynamic fragment

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/dynamic-fragment/

*Re-renders WooCommerce cart-dependent content after cart changes.*

Re-renders WooCommerce cart-dependent content after cart changes.

https://youtu.be/Q6wYRAvVN0Y

> **Note**
>
> This element requires **Bricks > Settings > WooCommerce > Enable advanced modular elements**.

## Where this element works

WooCommerce-aware Bricks layouts, such as page content, headers, and footers that need to update after cart changes.

## Key settings

- **Insert a structure** (select) - Choose a generated starter structure.
- **Generate** (button) - Adds the selected structure to the element.

## Generated structures

- **Mini cart**
- **Free shipping progress**

Generated structures are appended to the current content and do not overwrite existing content.

![](https://academy.bricksbuilder.io/assets/dynamic-fragment-states.png)

## Usage tips

- Use Dynamic fragment for cart-dependent content outside the main Cart page, such as a [custom mini cart](https://academy.bricksbuilder.io/integrations/woocommerce/create-custom-mini-cart-dynamic-fragment/), free shipping progress, or cart totals.
- Keep the fragment focused on content that needs to refresh after add-to-cart, remove-from-cart, or quantity changes.
- Keep the Dynamic fragment wrapper outside other query loops. A cart loop can be placed inside the fragment.

## Free shipping progress

The **Free shipping progress** structure adds a Progress Bar that shows how much more the cart needs for free shipping. Place the Dynamic fragment where shoppers see it on every page, for example a bar at the top of the header template, so it updates as products are added.

- **Minimum amount:** Bricks reads it from WooCommerce. It is the **Minimum order amount** of the **Free shipping** method in the shipping zone that matches the cart, with **Free shipping requires** set to a minimum order amount (alone or combined with a coupon). Change it in **WooCommerce > Settings > Shipping**, not in Bricks. If several free shipping methods match, Bricks uses the one with the smallest remaining amount.
- **Cart amount:** the cart subtotal minus coupon discounts, unless **Apply minimum order rule before coupon discount** is enabled on the free shipping method.
- **Label:** `Add {woo_free_shipping_remaining} more for free shipping`.
- **Value:** `{woo_free_shipping_progress:value}`, a number from 0 to 100 (the percentage of the minimum the cart has reached).
- **Conditions:** the bar only renders while a minimum exists (`{woo_free_shipping_min_amount:value}` is not 0) and the cart is below it (`{woo_free_shipping_progress:value}` is less than 100).

Once the cart reaches the minimum, the bar is hidden. The structure has no message for that state. To show one, add an element such as Basic Text inside the same Dynamic fragment and give it the condition **Dynamic data** `{woo_free_shipping_progress:value}` `==` `100`.

![Builder showing a Dynamic fragment in the header template with the generated Free shipping progress bar and a Basic Text "Your order ships free" with a condition that shows it when the free shipping progress equals 100.](https://academy.bricksbuilder.io/assets/dynamic-fragment-free-shipping-reached-condition.webp)

The Builder canvas previews a sample cart, so the bar can show "Add $0.00 more" and the conditions are not applied there. Check the real amounts on the frontend with products in the cart.

## Custom mini cart

For a mini cart, add a Dynamic fragment inside an Offcanvas in the header template and generate the **Mini cart** structure. A second Dynamic fragment in the header holds the cart icon and item count, so the count updates too. [Create a custom mini cart with Dynamic fragment](https://academy.bricksbuilder.io/integrations/woocommerce/create-custom-mini-cart-dynamic-fragment/) walks through the full setup, including the interactions that open the panel.

See [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/) for the cart tags you can use inside the fragment.

## Refresh behavior

Dynamic fragment refreshes after WooCommerce cart, coupon, and checkout events such as add to cart, remove from cart, cart emptied, cart totals updated, checkout updated, and coupon apply/remove events.

After a refresh, Bricks reruns frontend functions and dispatches:

```js
document.body.addEventListener('bricks/woocommerce/fragments/refreshed', (event) => {
  console.log(event.detail.fragments)
})
```

This refresh event also covers initial synchronization and checkout recalculations that do not change cart items. For a custom success notice or popup, use the [Bricks cart contents changed](https://academy.bricksbuilder.io/builder/features/interactions/#cart-contents-changed) interaction trigger, available since Bricks 2.4. It runs after a confirmed AJAX addition, removal, or quantity change and the related UI updates finish.

## Limitations

- Dynamic fragment is frontend-only.
- Do not place the Dynamic fragment wrapper inside a query loop.
- Component instances are not supported.
- The source area must be header, content, or footer.

---

# Mini cart

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/mini-cart/

*Displays a mini cart icon with cart count and dropdown cart details.*

Displays a mini cart icon with cart count and dropdown cart details.

## Settings

- **Icon** (icon) - Cart icon. Default: ti-shopping-cart.
- **Icon typography** (typography) - Typography for cart icon. Only available when Icon is set.
- **Open on add to cart (AJAX)** (checkbox) - Open mini cart when products are added via AJAX.

### Cart count

- **Visibility** (select) - Show/hide cart count. Options: Hide (Always), Show (Always). Default: Hide if empty.
- **Background color** (color) - Cart count background color. Only available when Visibility is not Hide (Always).
- **Border** (border) - Cart count border settings. Only available when Visibility is not Hide (Always).
- **Typography** (typography) - Cart count typography. Only available when Visibility is not Hide (Always).
- **Transform** (transform) - Cart count transform. Only available when Visibility is not Hide (Always) and Off-Canvas is not Top or Bottom.
- **Height** (number with units) - Cart count height. Only available when Visibility is not Hide (Always).
- **Width** (number with units) - Cart count width. Only available when Visibility is not Hide (Always).
- **Top** (number with units) - Cart count top position. Only available when Visibility is not Hide (Always).
- **Right** (number with units) - Cart count right position. Only available when Visibility is not Hide (Always).
- **Bottom** (number with units) - Cart count bottom position. Only available when Visibility is not Hide (Always).
- **Left** (number with units) - Cart count left position. Only available when Visibility is not Hide (Always).

### Cart subtotal

- **Position** (select) - Subtotal position. Options: Right, Left.
- **Gap** (number with units) - Gap between icon and subtotal. Only available when Position is set.
- **Typography** (typography) - Subtotal typography. Only available when Position is set.

### Cart details

- **Hide** (checkbox) - Hide cart details dropdown.
- **Don't close on click outside mini cart** (checkbox) - Prevent auto-close on outside clicks. Only available when Hide is not checked.
- **Off-Canvas** (select) - Off-canvas position. Options: Top, Right, Bottom, Left. Only available when Hide is not checked.
- **Height** (number with units) - Cart details height. Only available when Hide is not checked and Off-Canvas is not Top or Bottom.
- **Width** (number with units) - Cart details width. Default: 400px. Only available when Hide is not checked and Off-Canvas is not Top or Bottom.
- **Image width** (number with units) - Product image width. Default: 60px. Only available when Hide is not checked.
- **Padding** (spacing) - Cart details padding. Only available when Hide is not checked.
- **Position** (dimensions) - Cart details position. Only available when Hide is not checked and Off-Canvas is Disabled.
- **Transform** (transform) - Cart details transform. Only available when Hide is not checked and Off-Canvas is not Top or Bottom.
- **Background** (color) - Cart details background color. Only available when Hide is not checked.
- **Border** (border) - Cart details border settings. Only available when Hide is not checked.
- **Box shadow** (box-shadow) - Cart details box shadow. Only available when Hide is not checked.
- **Typography (Title)** (typography) - Title typography. Only available when Hide is not checked.
- **Typography (Quantity)** (typography) - Quantity typography. Only available when Hide is not checked.

#### Buttons

- **Background color** (color) - Button background color. Only available when Hide is not checked.
- **Border** (border) - Button border settings. Only available when Hide is not checked.
- **Typography** (typography) - Button typography. Only available when Hide is not checked.

#### Close

- **Icon** (icon) - Close icon. Only available when Hide is not checked.
- **Typography** (typography) - Close typography. Only available when Hide is not checked and Icon is set. Excludes: font-family, font-weight, font-style, text-align, text-decoration, text-transform, line-height, letter-spacing.
- **Position** (dimensions) - Close position. Only available when Hide is not checked and Icon is set.
- **Padding** (spacing) - Close padding. Only available when Hide is not checked and Icon is set.
- **Background color** (color) - Close background color. Only available when Hide is not checked and Icon is set.
- **Border** (border) - Close border settings. Only available when Hide is not checked and Icon is set.

---

# Products archive description

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/products-archive-description/

*Displays the description for WooCommerce product archives (shop page, categories, tags).*

Displays the description for WooCommerce product archives (shop page, categories, tags).

---

# Products filter

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/products-filter/

*Displays product filters for WooCommerce product listings.*

Displays product filters for WooCommerce product listings.

## Settings

- **Filters** (repeater) - Product filter configurations.
  - **Filter type** (select) - Type of filter. Options: Taxonomy, Product attribute, Other.
  - **Filter by** (select) - Specific filter to apply (depends on type).
  - **Filter input** (select) - Input type. Options: Dropdown, Checkbox, Radio list, Text list, Box list.
  - **Any option text** (text) - Text for "any" option. Default: "Any".
  - **Only parent terms** (checkbox) - Show only parent terms.
  - **Show empty terms** (checkbox) - Include terms with no products.
  - **Filter title** (text) - Title for the filter.
  - **Hide title** (checkbox) - Hide filter title.
  - **Collapse** (checkbox) - Make filter collapsible.
- **Spacing** (number) - Gap between filters. Default: 30px.

### Title
- **Margin** (spacing) - Title margin. Default: 0 0 15px 0.
- **Padding** (spacing) - Title padding.
- **Typography** (typography) - Title typography.
- **Background color** (color) - Title background color.

---

# Notice

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/notice/

*Displays WooCommerce system notices (success, info, and error messages).*

Displays WooCommerce system notices (success, info, and error messages).

## Where this element works

Shop/archive templates and WooCommerce pages where the related data exists.

## Key settings

- **Preview notice type** (select)

## Usage tips

- Keep notice styles highly readable so customers can quickly understand errors and confirmation messages.
- Check all notice types (success, info, error) in real cart and checkout scenarios.

---

# Products orderby

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/products-orderby/

*Displays a dropdown to sort WooCommerce products.*

Displays a dropdown to sort WooCommerce products.

## Settings

- **Order by** (select) - Available sorting options. Multiple selection. Leave empty to use WooCommerce default list.

---

# Products pagination

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/products-pagination/

*Displays pagination for WooCommerce product listings.*

Displays pagination for WooCommerce product listings.

## Settings

- **Alignment** (align-items) - Pagination alignment.
- **Previous Icon** (icon) - Icon for previous page link.
- **Next Icon** (icon) - Icon for next page link.
- **End Size** (number) - How many numbers on either the start and the end list edges. Minimum: 1.
- **Mid Size** (number) - How many numbers to either side of the current page. Minimum: 1.

---

# Products total results

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/products-total-results/

*Displays the total number of products found and current result range.*

Displays the total number of products found and current result range.

---

# Products

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/products/

*Displays WooCommerce products in a grid layout with customizable fields and widgets.*

Displays WooCommerce products in a grid layout with customizable fields and widgets.

## Settings

- **Columns** (number) - Number of columns. Range: 1-6. Default: 4. Supports breakpoints.
- **Gap** (number) - Spacing between products. Default: 30px.

### Query
- Product query controls (via Woocommerce_Helpers::get_product_query_controls).

### Fields
- **Content** (repeater) - Dynamic data fields to display. Default includes WooCommerce hooks and product fields like title, image, price, add to cart.
- **Link entire product** (checkbox) - Make entire product clickable if no field links exist.

### Widgets
- **Show Before Grid** (select) - Widgets to show before products grid. Options: Pagination, Result Count, Order by. Multiple selection.
- **Show After Grid** (select) - Widgets to show after products grid. Options: Pagination, Result Count, Order by. Multiple selection.
- **Sort by options** (select) - Available sorting options. Default: Default sorting. Multiple selection.

---

# WooCommerce Template Hook

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/template-hook/

*Renders output from a selected WooCommerce template hook so you can place WooCommerce hook content in your layout.*

Renders output from a selected WooCommerce template hook so you can place WooCommerce hook content in your layout.

## Where this element works

Any WooCommerce template where the selected hook is executed.

## Key settings

- **Template** (select)
- **Hook** (select)
- **Show tips** (checkbox)

## Usage tips

- Pick hooks intentionally and avoid duplicating WooCommerce default output in the same area.
- If expected content does not appear, confirm the selected hook runs in the current template context.
