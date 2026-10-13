# Asset Loading Optimization

Source: https://academy.bricksbuilder.io/developer/guides/asset-loading/

*Optimize asset loading in Bricks extensions so scripts and styles are only loaded where they are actually needed.*

"Performance" being one of Bricks' three pillars, Bricks only loads many frontend assets when they are needed on the current page.

https://www.youtube.com/watch?v=O_B19LBtnwM&t=45s

Bricks always enqueues the main frontend stylesheet through the `bricks-frontend` handle and the main frontend script through the `bricks-scripts` handle. Additional libraries such as sliders, lightboxes, maps, animations, icon fonts, and date pickers are registered and loaded only when needed.

By default, Bricks uses the cascade-layer frontend stylesheet (`frontend-layer.min.css`). If cascade layers are disabled, Bricks falls back to `frontend.min.css`. When the CSS loading method is set to "External Files", Bricks uses the lighter frontend stylesheet (`frontend-light-layer.min.css`, or `frontend-light.min.css` when cascade layers are disabled) and loads the generated CSS files for the current page.

## How To Reduce Asset Loading Even Further through "External Files" {#external-files}

By default, generated styles such as page settings, template settings, element styles, global custom CSS, theme styles, color palettes, global class CSS, and other Bricks data are output inline.

To further optimize & minimize the loaded styles you can set the "CSS Loading Method" under "Bricks - Settings - Performance" to "**External Files**".

To regenerate all CSS files in one go, click **Regenerate CSS files** under **Bricks > Settings > Performance > CSS loading method**. This action is available after setting CSS loading method to **External Files**.

**Please click the "Regenerate CSS files" button once you've changed the CSS loading method to "External Files", so Bricks can create the required directory and CSS files.**

This generates minified CSS files for your Bricks data within the `wp-content/uploads/bricks/css` directory (or whatever you've set as your WordPress "uploads" directory) and serves them as needed according to the requested page.

> **Note**
>
> If the "External Files" CSS loading method does conflict for some reason with your server or plugin caching solution or outputs incorrect or missing styles, please revert to the default "**Inline Styles**" CSS loading method, and report the issue to us via [email](https://bricksbuilder.io/contact/), so we can address it. Thank you!

![](https://academy.bricksbuilder.io/assets/bricks-builder-css-loading-method-external-files-1024x835.png)

<figcaption>

CSS Loading Method: "External Files"

</figcaption>

## How To Enqueue Individual Styles & Scripts {#enqueue}

If you are working with a third-party Bricks plugin or if for some reason a certain style/script is not being loaded as needed, you can always load/enqueue those individually to your own needs by following the instructions below.

What follows is a list of Bricks style & script names which you can enqueue on any of your pages as needed through your child theme's functions.php by hooking into the `wp_enqueue_scripts` WordPress action or inside the `enqueue_scripts` function in case your [custom Bricks element](https://academy.bricksbuilder.io/developer/elements/create-your-own-elements/) depends on any of those styles and/or scripts.

```php
add_action( 'wp_enqueue_scripts', function() {
  // isotopeJS (e.g. metro & masonry layouts)
  wp_enqueue_script( 'bricks-isotope' );
  wp_enqueue_style( 'bricks-isotope' );

  // Icon font files
  wp_enqueue_style( 'bricks-font-awesome-6' );
  wp_enqueue_style( 'bricks-font-awesome-6-brands' );
  wp_enqueue_style( 'bricks-ionicons' );
  wp_enqueue_style( 'bricks-themify-icons' );

  // Animations
  wp_enqueue_style( 'bricks-animate' );

  // Tooltips
  wp_enqueue_style( 'bricks-tooltips' );

  // Datepicker
  wp_enqueue_script( 'bricks-flatpickr' );
  wp_enqueue_style( 'bricks-flatpickr' );

  // swiperJS (e.g. slider, carousel)
  wp_enqueue_script( 'bricks-swiper' );
  wp_enqueue_style( 'bricks-swiper' );

  // splideJS (e.g. nestable slider, carousel)
  wp_enqueue_script( 'bricks-splide' );
  wp_enqueue_style( 'bricks-splide' );

  // Lightbox
  wp_enqueue_script( 'bricks-photoswipe' );
  wp_enqueue_script( 'bricks-photoswipe-lightbox' );
  wp_enqueue_script( 'bricks-photoswipe-caption' );
  wp_enqueue_style( 'bricks-photoswipe' );

  // Leaflet map
  wp_enqueue_script( 'bricks-leaflet' );
  wp_enqueue_style( 'bricks-leaflet' );

  // Code prettifier
  wp_enqueue_script( 'bricks-prettify' );
  wp_enqueue_style( 'bricks-prettify' );

  // Choices.js
  wp_enqueue_script( 'bricks-choices-lib' );
  wp_enqueue_script( 'bricks-choices-js' );
  wp_enqueue_style( 'bricks-choices' );
}, 11 );
```

---

# Best Practices

Source: https://academy.bricksbuilder.io/developer/guides/best-practices/

*Follow Bricks development best practices for permalinks, image handling, child-theme usage, and safer long-term customization.*

Please keep the points below in mind when working with Bricks:

| **Permalink Settings** | We recommend **Post name** permalinks for cleaner URLs. Go to **Settings > Permalinks**, select **Post name**, and click **Save Changes**. Bricks builds builder URLs from the page permalink, so other WordPress permalink structures can work as long as WordPress resolves them correctly. |
| --- | --- |
| **Min. Image Dimensions** | Upload images with a minimum width of 600 pixels. Ideally 1600 pixels in width or more.<br /><br />If you already have images in your media library and start working with Bricks make sure to [Regenerate Thumbnails](https://wordpress.org/plugins/regenerate-thumbnails/) so all Bricks-specific image sizes are generated properly. |
| **Never Edit Theme Code Directly** | **Do not edit any of the Bricks theme core files directly!**<br /><br />As all your changes will be lost/overwritten when updating the theme. Use the [Bricks child theme](https://academy.bricksbuilder.io/developer/guides/child-theme/) or a code snippet plugin to extend Bricks with your custom code. |

---

# Bricks CLI

Source: https://academy.bricksbuilder.io/developer/guides/bricks-cli/

*Use Bricks CLI commands through WP-CLI to run builder-related maintenance tasks from the command line.*

Bricks 1.8.1+ integrates with the [WP-CLI](https://wp-cli.org/) (WordPress Command Line Interface). Allowing you to perform specific tasks from your server's command line interface instead of the GUI (Graphical User Interface).

### Regenerates CSS Files

Requires the Bricks "CSS loading method" to be set to "external files".

`wp bricks regenerate_assets`

---

# Child Theme

Source: https://academy.bricksbuilder.io/developer/guides/child-theme/

*Set up a Bricks child theme for custom PHP, assets, templates, and safer update-friendly development.*

> **Note**
>
> Please do not edit any of the Bricks theme core files directly, as updating the theme will cause all your changes to be lost.

Instead, use the Bricks child theme to make modifications and overwrite files. You can download the Bricks child theme directly from your [Bricks account](https://my.bricksbuilder.io/).

Upload this child theme ZIP file (bricks-child.zip) like any other WordPress theme. Go to **Appearance → Themes** and activate **Bricks Child Theme**. You can add your own styles to **style.css**.

## How To Enqueue Scripts (JS) & Styles (CSS)

In order to load your files only on the front end & the canvas and not in the builder panel (as your custom CSS might affect the builder), you have to check against `bricks_is_builder_main()` like this:

```php
add_action( 'wp_enqueue_scripts', function() {
  // Code & check below enqueues your files on the canvas & frontend, not the builder panel. Otherwise custom CSS might affect builder)
  if ( ! bricks_is_builder_main() ) {
    wp_enqueue_style( 'bricks-child', get_stylesheet_uri(), ['bricks-frontend'], filemtime( get_stylesheet_directory() . '/style.css' ) );
  }
} );
```

You can learn more about how a Child Theme works by visiting the official WordPress Codex: [https://developer.wordpress.org/themes/advanced-topics/child-themes/](https://developer.wordpress.org/themes/advanced-topics/child-themes/)

The `functions.php` file of a child theme, unlike `style.css`, does not override the `functions.php` file of the parent theme. Instead, it is loaded in addition to the parent theme's `functions.php`, right before the parent file.

---

# Converter

Source: https://academy.bricksbuilder.io/developer/guides/converter/

*Use the Bricks converter workflow to transform source markup or data into Bricks-compatible structures more safely.*

Bricks offers multiple so-called "Converter" options for legacy data migrations.

The Converter is a built-in tool that scans your database for outdated Bricks data and automatically updates it to the latest valid syntax of the installed version.

> **Note**
>
> The converter performs changes to the Bricks data in your database. So please perform a full-site backup before running the converter.

In current Bricks versions, the database Converter row is hidden from the normal Settings screen. Treat it as a legacy/support workflow, not a routine maintenance step.

When the legacy Converter is run, the process can take a minute or two depending on your server and the size of your Bricks data. Please do not close or refresh the page until you see the green "THE END" success message:

![](https://academy.bricksbuilder.io/assets/bricks-1.4-converter-results-1024x324.png)

<figcaption>

Converter results: Updated Page Settings & Global Custom CSS

</figcaption>

## What is being converted?

With the improved DOM structure and element ID & class names, Bricks replaced the old `bricks-element-` element ID and class prefix with `brxe-`. Structural wrapper IDs such as `#bricks-header`, `#bricks-content`, and `#bricks-footer` are converted to `#brx-header`, `#brx-content`, and `#brx-footer`.

Depending on the selected conversion action, the Converter can update these areas of Bricks data:

- Bricks global settings
- Bricks theme styles
- Bricks global classes
- Bricks page settings
- Bricks page data
- Global elements, including conversion to components
- Bricks templates
- Legacy Container structures
- Entry animations
- Element positioning data

The Converter is not limited to custom CSS/JS. Only run the specific conversion requested for the legacy data you need to migrate.

---

# Bricks CSS: Compatibility guidelines

Source: https://academy.bricksbuilder.io/developer/guides/bricks-css-compatibility-guidelines/

*Follow Bricks CSS compatibility guidelines so custom CSS keeps working across builder output, theme updates, and integrations.*

Bricks aims to use CSS features that are broadly supported in modern browsers and avoid fallbacks that add weight for uncommon older browsers. We use [Baseline](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility) as a practical reference when evaluating CSS support in Bricks output.

## What is Baseline?

Baseline is a compatibility model that tracks when web platform features become widely interoperable across all major browsers. It defines two key stages:

- **Newly Available**: Feature works across all major browsers (desktop and mobile).
- **Widely Available**: Reached ~30 months after “Newly Available”; safe to use in production for most users globally (~95% support).

Baseline considers support in the following browsers:

- Apple Safari (iOS)
- Apple Safari (macOS)
- Google Chrome (Android)
- Google Chrome (desktop)
- Microsoft Edge (desktop)
- Mozilla Firefox (Android)
- Mozilla Firefox (desktop)

## Which CSS features does Bricks use?

Bricks output already includes modern CSS such as the [`:where` pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/:where) and [@layer CSS at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/@layer). Both are listed by MDN as **Widely Available**, which is the kind of broad support we look for before relying on a CSS feature in Bricks output.

![](https://academy.bricksbuilder.io/assets/mdn-baseline.png)

## What happens on much older or less common browsers?

We aim to strike the right balance: adopting modern standards when they’re stable and broadly supported, while avoiding unnecessary technical debt or regressions for the majority of users. Adding fallbacks for edge-case devices below the Baseline threshold would compromise code quality and performance for everyone else.

## Does this affect user-added CSS?

No. This only applies to the CSS generated by Bricks.

You can continue writing your own CSS however you like, including fallbacks or feature checks for legacy devices. Bricks just won't include those fallbacks automatically in its own output.

---

# Custom JavaScript events in Bricks

Source: https://academy.bricksbuilder.io/developer/guides/custom-javascript-events-in-bricks/

*Work with Bricks custom JavaScript events so scripts can respond to builder and frontend interactions more reliably.*

Bricks dispatches custom JavaScript events for several frontend actions. Use these events when your own scripts need to respond to Bricks forms, popups, query filters, AJAX updates, tabs, accordions, or other interactive elements.

## Form element events

- [bricks/form/submit](https://academy.bricksbuilder.io/builder/features/interactions/#trigger-form-submit) Emitted before an AJAX call for form submission is made.
- [bricks/form/success](https://academy.bricksbuilder.io/builder/features/interactions/#trigger-form-success) Emitted after a successful form submission AJAX call is returned.
- [bricks/form/error](https://academy.bricksbuilder.io/builder/features/interactions/#trigger-form-error) Emitted after an error in the form submission AJAX call is returned.

## Tabs / Tabs (Nestable) element events

- [bricks/tabs/changed](#bricks-tabs-changed-code): Emitted after click on a tab title (`@since 1.9.8`)

<span id="bricks-tabs-changed-code"></span>

```php
// Listen for the 'bricks/tabs/changed' event
document.addEventListener('bricks/tabs/changed', (event) => {
  // Extract information from the event detail
  const { elementId, activeIndex, activeTitle, activePane } = event.detail;

  // Only target elementID lwxvfh
  if( elementId !== 'lwxvfh' ) {
    return;
  }

  // Example: Log the details to the console
  console.log(`Tabs Changed - Element ID: ${elementId}, Active Index: ${activeIndex}, Active Title: ${activeTitle}, Active Pane: ${activePane}`);

  // Your custom logic here
  // For example, update the UI based on the tab change
});
```

## Accordion / Accordion (Nestable) element events

- [bricks/accordion/open](#bricks-accordion-open-code): Emitted after an accordion item is opened/expanded via click action (`@since 1.9.8`)
- [bricks/accordion/close](#bricks-accordion-close-code): Emitted after an accordion item is closed/collapsed via click action (`@since 1.9.8`)

<span id="bricks-accordion-open-code"></span>

```php
// Listen for the 'bricks/accordion/open' event
document.addEventListener('bricks/accordion/open', (event) => {
  // Extract information from the event detail
  const { elementId, openItem } = event.detail;

  // Only target elementID qwe3th
  if( elementId !== 'qwe3th' ) {
    return;
  }

  // Example: Log the details to the console
  console.log(`Accordion Opened - Element ID: ${elementId}, Open Item ID: ${openItem}`);

  // Your custom logic here
  // For example, update the UI based on the accordion item being opened
});

```

<span id="bricks-accordion-close-code"></span>

```php
// Listen for the 'bricks/accordion/close' event
document.addEventListener('bricks/accordion/close', (event) => {
  // Extract information from the event detail
  const { elementId, closeItem } = event.detail;

  // Only target elementID qwe3th
  if( elementId !== 'qwe3th' ) {
    return;
  }

  // Example: Log the details to the console
  console.log(`Accordion Closed - Element ID: ${elementId}, Closed Item ID: ${closeItem}`);

  // Your custom logic here
  // For example, update the UI based on the accordion item being closed
});
```

## Animation events

- [bricks/animation/end/\{animationId\}](https://academy.bricksbuilder.io/builder/features/interactions/#bricks-animation-end-code): Emitted when a specified animation (identified by `{animationId}`) completes its playback.

## Popup events

- [bricks/popup/open](https://academy.bricksbuilder.io/builder/features/popup-builder/#bricks-popup-open-close-code) Emitted after popup opened.
- [bricks/popup/close](https://academy.bricksbuilder.io/builder/features/popup-builder/#bricks-popup-open-close-code) Emitted after popup closed.
- [bricks/ajax/popup/start](https://academy.bricksbuilder.io/builder/features/popup-builder/#ajax-events) Emitted before making an AJAX popup call.
- [bricks/ajax/popup/end](https://academy.bricksbuilder.io/builder/features/popup-builder/#ajax-events) Emitted after completing an AJAX popup call.
- [bricks/ajax/popup/loaded](https://academy.bricksbuilder.io/builder/features/popup-builder/#ajax-events) Emitted after adding AJAX popup content to the DOM.

### AJAX popup open event sequence

1. bricks/ajax/popup/start
2. bricks/ajax/popup/end
3. bricks/ajax/popup/loaded
4. bricks/popup/open

## Bricks AJAX events

> **Note**
>
> Bricks AJAX = Infinite Scroll, Load More, AJAX Pagination, or Query Filter.

- [bricks/ajax/start](#bricks-ajax-start-code): Emitted before a Bricks AJAX call is made.
- [bricks/ajax/end](#bricks-ajax-end-code): Emitted after completing a Bricks AJAX call.
- [bricks/ajax/pagination/completed](#bricks-ajax-pagination-completed-code): Emitted after an AJAX pagination call is completed.
- [bricks/ajax/load_page/completed](#bricks-ajax-load_page-completed-code): Emitted after an Infinite scroll AJAX call is completed.
- [bricks/ajax/query_result/completed](#bricks-ajax-query_result-completed-code): Emitted after a Query filter AJAX call is completed.
- [bricks/ajax/nodes_added](#bricks-ajax-nodes_added-code): Emitted after Bricks adds new AJAX result nodes to the DOM. The event detail contains the `queryId`. (`@since 1.11.1`)
- [bricks/ajax/query_result/displayed](#bricks-ajax-query_result-displayed-code): Emitted after adding all filtered results to the DOM.
- [bricks/filter/submit/start](#bricks-filter-submit-start-code): Emitted when a Filter - Submit element starts an AJAX filter submission. The event detail contains the `queryId` and `filterId`. (`@since 2.4`)
- [bricks/filter/submit/end](#bricks-filter-submit-end-code): Emitted when a Filter - Submit AJAX filter submission finishes. The event detail contains the `queryId` and `filterId`. (`@since 2.4`)

### Infinite scroll event sequence

1. bricks/ajax/start
2. bricks/ajax/nodes_added
3. bricks/ajax/end
4. bricks/ajax/load_page/completed

### AJAX pagination event sequence

1. bricks/ajax/start
2. bricks/ajax/nodes_added
3. bricks/ajax/end
4. bricks/ajax/pagination/completed

> **Note**
>
> The `bricks/ajax/pagination/completed` event is only emitted for standalone AJAX pagination. If the Pagination element targets a query that uses Bricks Query Filters, this event is not emitted. In this case, listen for the Query Filter events instead.

### AJAX query filter event sequence

1. bricks/ajax/start
2. bricks/ajax/end
3. bricks/ajax/query_result/completed
4. bricks/ajax/nodes_added
5. bricks/ajax/query_result/displayed

### Filter submit event sequence

The `bricks/filter/submit/start` and `bricks/filter/submit/end` events are specific to the Filter - Submit element. They run only for AJAX filter submissions that refresh the current page results. They are not emitted when the Submit element redirects to another URL.

1. bricks/filter/submit/start
2. bricks/ajax/start
3. bricks/ajax/end
4. bricks/ajax/query_result/completed
5. bricks/ajax/nodes_added
6. bricks/ajax/query_result/displayed
7. bricks/filter/submit/end

Use these events when your script should react only to a deliberate submit action, not to every query filter AJAX request.

<span id="bricks-ajax-start-code"></span>

```php
document.addEventListener('bricks/ajax/start', (event) => {
  // Get the queryId from the event
  const queryId = event.detail.queryId || false;

  if (!queryId) {
    return;
  }

  // Your custom logic here
  // For example, initiate a loader or update UI to indicate AJAX request start
});
```

<span id="bricks-ajax-end-code"></span>

```php
document.addEventListener('bricks/ajax/end', (event) => {
  // Get the queryId from the event
  const queryId = event.detail.queryId || false;

  if (!queryId) {
    return;
  }

  // Your custom logic here
  // For example, initiate a loader or update UI to indicate AJAX request end
});
```

<span id="bricks-ajax-pagination-completed-code"></span>

```php
document.addEventListener('bricks/ajax/pagination/completed', (event) => {
  // Extract queryId from the event detail
  const queryId = event.detail.queryId;

  // Your custom logic here
  // For example, handle the completed pagination for the specific queryId
});
```

<span id="bricks-ajax-load_page-completed-code"></span>

```php
document.addEventListener('bricks/ajax/load_page/completed', (event) => {
  // Extract information from the event detail
  const { queryTrailElement, queryId } = event.detail;

  // Your custom logic here
  // For example, handle the completed AJAX page load for the specific queryId and queryTrailElement
});
```

<span id="bricks-ajax-query_result-completed-code"></span>

```php
document.addEventListener('bricks/ajax/query_result/completed', (event) => {
  // Extract information from the event detail
  const queryId = event.detail.queryId;

  // Your custom logic here
});
```

<span id="bricks-ajax-nodes_added-code"></span>

```php
document.addEventListener('bricks/ajax/nodes_added', (event) => {
  // Extract queryId from the event detail
  const queryId = event.detail.queryId;

  // Your custom logic here
  // For example, initialize scripts that need the new AJAX result nodes to exist first
});
```

<span id="bricks-ajax-query_result-displayed-code"></span>

```php
document.addEventListener('bricks/ajax/query_result/displayed', (event) => {
  // Extract information from the event detail
  const queryId = event.detail.queryId;

  // Your custom logic here
});
```

<span id="bricks-filter-submit-start-code"></span>

```php
document.addEventListener('bricks/filter/submit/start', (event) => {
  const { queryId, filterId } = event.detail;

  // Only react to the Filter - Submit element with Bricks ID xnueeh
  if (filterId !== 'xnueeh') {
    return;
  }

  // Your custom logic here
});
```

<span id="bricks-filter-submit-end-code"></span>

```php
document.addEventListener('bricks/filter/submit/end', (event) => {
  const { queryId, filterId } = event.detail;

  // Only react to the target query with Bricks ID kpmnav
  if (queryId !== 'kpmnav') {
    return;
  }

  // Your custom logic here
});
```

## Mega menu events

- [bricks/megamenu/repositioned](#bricks-megamenu-repositioned-code): Emitted after a mega menu submenu is repositioned on the frontend. The event detail contains the `menuItem` and `submenu`. (`@since 2.0`)

<span id="bricks-megamenu-repositioned-code"></span>

```php
document.addEventListener('bricks/megamenu/repositioned', (event) => {
  const { menuItem, submenu } = event.detail;

  // Your custom logic here
  // For example, update third-party scripts inside the repositioned submenu
});
```
