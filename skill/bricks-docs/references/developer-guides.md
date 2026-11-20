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

  // Leaflet map (Bricks 2.5): runtime and Leaflet stylesheet
  wp_enqueue_script( 'bricks-map-leaflet' );
  wp_enqueue_style( 'bricks-leaflet' );

  // Only needed if the Leaflet map uses marker clustering
  // wp_enqueue_script( 'bricks-leaflet-markercluster' );

  // Code prettifier
  wp_enqueue_script( 'bricks-prettify' );
  wp_enqueue_style( 'bricks-prettify' );

  // Choices.js
  wp_enqueue_script( 'bricks-choices-lib' );
  wp_enqueue_script( 'bricks-choices-js' );
  wp_enqueue_style( 'bricks-choices' );
}, 13 );
```

The example uses hook priority `13` so it runs after the Leaflet runtime is registered at priority `12`.

Starting with **Bricks 2.5**, `bricks-map-leaflet` provides the [Map (Leaflet)](https://academy.bricksbuilder.io/builder/elements/general/map-leaflet/) runtime. Its dependencies load `bricks-scripts` and the `bricks-leaflet` library. Enqueuing only the library does not load the element runtime. The element enqueues its assets automatically, including `bricks-leaflet-markercluster` when **Cluster: Markers** is enabled.

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

## Drafts and site versions

Since Bricks 2.5, the `wp bricks drafts` commands inspect, publish, and discard saved [page drafts](https://academy.bricksbuilder.io/builder/interface/drafts/), [site versions](https://academy.bricksbuilder.io/builder/interface/site-versions/), and publish undo points.

Run commands from the WordPress installation directory. Replace `site-admin` with an existing WordPress user login and draft IDs with values from your site.

### List and review

```sh
wp bricks drafts list
wp bricks drafts list --status=all --format=json
wp bricks drafts review DRAFT_ID
```

`list` defaults to `--status=active`. Supported status values are `active`, `published`, `discarded`, and `all`. Output formats are `table` (default), `json`, and `csv`. The `kind` column distinguishes page drafts (`page`), site versions (`site`), and publish undo points (`backup`).

`review` shows a table of saved pending changes:

| Status | Meaning |
| --- | --- |
| `ready` | Bricks can apply the change without an unresolved conflict. |
| `same` | The live value already matches the draft. |
| `conflict` | The change needs a choice between live and draft values. |

The CLI reads saved changes; it does not save unsaved edits from an open Builder tab. Use the Builder's publish dialog when you need a visual comparison before choosing between conflicting values.

### Publish or undo a publish

After reviewing, publish as a user who can edit the draft and publish each included change:

```sh
wp bricks drafts publish DRAFT_ID --user=site-admin
```

This runs immediately, without a confirmation prompt. Bricks checks the current changes again and stops if conflicts remain unresolved. It also stops for missing or closed drafts, insufficient permissions, or another save or publish holding the required lock.

For conflicts, use `--keep-live` or `--keep-draft` with comma-separated `resource:itemId` keys from the reported conflicts. Only include keys you have reviewed:

```sh
wp bricks drafts publish DRAFT_ID --keep-live="globalClasses:abc123" --user=site-admin
```

These flags resolve conflicts; they do not limit publication to the listed items. Other ready changes are published too.

When publication replaces live values, the success message includes an undo version ID. Review that ID with `wp bricks drafts review`, then publish it with the same `publish` command to restore those replaced values. Later edits can cause conflicts during undo.

### Discard saved changes

```sh
wp bricks drafts discard DRAFT_ID --user=site-admin
```

This immediately discards the pending changes, without a confirmation prompt. It requires permission to edit the draft and leaves live data in place, including new shared items that had already been saved live. The CLI does not offer the Builder's option to delete newly created, unused shared items during discard.

## Regenerates CSS Files

Requires the Bricks "CSS loading method" to be set to "external files".

`wp bricks regenerate_assets`

## Global data revisions

Since Bricks 2.5, the `wp bricks history` commands inspect and recover recorded [global data revisions](https://academy.bricksbuilder.io/builder/interface/global-data-history/).

Run commands from the WordPress installation directory. Replace `site-admin` with an existing WordPress user login and item and entry IDs with values from your site.

### Inspect items and entries

Start by listing items with recorded history, then list one item's entries and inspect the entry you want to restore:

```sh
wp bricks history list globalClasses
wp bricks history list globalClasses abc123
wp bricks history show 42
```

`globalClasses` is a resource key. Other examples include `globalVariables`, `components`, `colorPalettes`, and `themeStyles`. An unknown resource key returns an error listing the supported keys.

`list` accepts `--format=table`, `--format=json`, or `--format=csv`; the default is `table`. It lists up to 200 items, or up to 100 entries when you provide an item ID. `show` prints one entry as JSON, including its stored value.

### Restore one item

After inspecting the entry, restore it as a WordPress user with permission to change that resource:

```sh
wp bricks history restore 42 --user=site-admin
```

This restores that item's stored value immediately, preserving other items. The restore uses Bricks' save permissions and conflict checks. Restoring executable code also requires code execution permission. Missing entries and entries without a restorable value return an error.

### Rebuild a resource

Use `rebuild` to replace an entire resource with its recorded values, for example when recovering a damaged class collection. Inspect the relevant history and take a site backup before replacing a whole collection.

```sh
wp bricks history rebuild globalClasses --user=site-admin
```

The default is to rebuild from the latest recorded values. Use `--at` to select an earlier UTC date and time:

```sh
wp bricks history rebuild globalClasses --at="2026-11-01 12:00:00" --user=site-admin
```

Rebuilding requires the WordPress `manage_options` capability. History containing executable code also requires code execution permission. Bricks refuses a rebuild if the retained history cannot establish the complete collection order; restore individual items instead.

### Clear recorded history

```sh
wp bricks history clear
```

This deletes all global data history for the site, leaving the current global data in place. Deleted history is no longer available for recovery.

Both `rebuild` and `clear` ask for confirmation. Their optional `--yes` flag skips that prompt.

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

# Custom JavaScript events in Bricks

Source: https://academy.bricksbuilder.io/developer/guides/custom-javascript-events-in-bricks/

*Work with Bricks custom JavaScript events so scripts can respond to builder and frontend interactions more reliably.*

Bricks dispatches custom JavaScript events for several frontend actions. Use these events when your own scripts need to respond to Bricks forms, popups, query filters, AJAX updates, tabs, accordions, or other interactive elements.

## Form element events

- [bricks/form/submit](https://academy.bricksbuilder.io/builder/features/interactions/#trigger-form-submit) Emitted before an AJAX call for form submission is made.
- [bricks/form/success](https://academy.bricksbuilder.io/builder/features/interactions/#trigger-form-success) Emitted after a successful form submission AJAX call is returned.
- [bricks/form/error](https://academy.bricksbuilder.io/builder/features/interactions/#trigger-form-error) Emitted after an error in the form submission AJAX call is returned.

## Clipboard events {#clipboard-events}

Since Bricks 2.5, the [Copy to clipboard interaction](https://academy.bricksbuilder.io/builder/features/interactions/#copy-to-clipboard) dispatches these events on the element that owns the interaction:

- `bricks/clipboard/success`: The browser confirmed that the text was copied.
- `bricks/clipboard/fail`: Clipboard writing failed or the source element could not be found.

`event.detail.text` contains the copied or attempted text. It is `null` if the source text could not be read. These events do not bubble, so attach listeners directly to the element that owns the copy interaction.

```js
const copyButton = document.querySelector('#copy-coupon')

copyButton?.addEventListener('bricks/clipboard/success', (event) => {
  console.log('Copied:', event.detail.text)
})

copyButton?.addEventListener('bricks/clipboard/fail', (event) => {
  console.log('Could not copy:', event.detail.text)
})
```

Replace `#copy-coupon` with your copy element's selector and run this code after that element exists in the DOM. To configure feedback in the builder, use the [Copy successful and Copy failed triggers](https://academy.bricksbuilder.io/builder/features/interactions/#copy-result-triggers).

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
- [bricks/ajax/pagination/history](#bricks-ajax-pagination-history-code): Emitted after standalone AJAX pagination finishes restoring browser history in Bricks 2.5.
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
> In Bricks 2.5, `bricks/ajax/pagination/completed` also fires after a successful Pagination click updates a query that uses Query Filters. It follows the Query Filter event sequence below, after `bricks/ajax/query_result/displayed`. Changing a filter value alone does not emit this pagination event.

### AJAX query filter event sequence

1. bricks/ajax/start
2. bricks/ajax/end
3. bricks/ajax/query_result/completed
4. bricks/ajax/nodes_added
5. bricks/ajax/query_result/displayed

### Browser history restoration

For standalone AJAX pagination, `bricks/ajax/pagination/completed` includes `isPopState: true` during Back/Forward restoration. Check `queryUpdated` before acting on replaced results: a standalone completion event can also follow a failed request.

After all standalone query restoration requests for the current history navigation finish successfully, Bricks emits `bricks/ajax/pagination/history`. Its `queryIds` array identifies the standalone queries requested for restoration; it can be empty when no standalone query needs refreshing. This event does not wait for queries handled by Query Filters and does not indicate that accumulated Load more or Infinite scroll results were restored. A failed standalone history request falls back to loading the target document.

Use this event for site-specific work after the asynchronous restoration, rather than assuming a `popstate` listener runs after results have loaded. Bricks does not disable native browser scroll restoration.

<span id="bricks-ajax-pagination-history-code"></span>

```js
document.addEventListener('bricks/ajax/pagination/history', (event) => {
  const { queryIds } = event.detail;

  if (!queryIds.includes('your-query-id')) return;

  // The requested standalone query results have finished restoring.
});
```

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
  const { queryId, queryUpdated, isPopState = false } = event.detail;
  if (!queryUpdated) return;

  // isPopState identifies standalone Back/Forward restoration.
  // Add your query-specific logic here.
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
