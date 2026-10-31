# Facebook page

Source: https://academy.bricksbuilder.io/builder/elements/general/facebook-page/

*The Facebook Page element embeds a Facebook page plugin with customizable display options.*

The Facebook Page element embeds a Facebook page plugin with customizable display options.

## Settings

- **Facebook page URL** (text) - The URL of the Facebook page to embed. Default: "https://facebook.com/facebook".

- **Height (px)** (number) - Height of the embedded page in pixels. Minimum: 70, Maximum: 500. Default: 500.

- **Width (px)** (number) - Width of the embedded page in pixels. Minimum: 180, Maximum: 500. Default: 340.

- **Tabs** (select) - Tabs to display on the page plugin. Options: `timeline`, `events`, `messages`. Multiple selection allowed.

- **Hide cover** (checkbox) - Hide the page cover photo.

- **Show friends' photos** (checkbox) - Display profile photos of the page's friends.

- **Hide CTA button** (checkbox) - Hide the call-to-action button.

- **Small header** (checkbox) - Use a smaller header size.

> **Developer reference**
>
> See the [Facebook Page Schema](https://academy.bricksbuilder.io/developer/schema/elements/facebook-page/) for the full JSON schema of this element's settings and controls.

---

# Map (Leaflet)

Source: https://academy.bricksbuilder.io/builder/elements/general/map-leaflet/

*Map (Leaflet) (map-leaflet) embeds an interactive map using Leaflet and tile layers (default: OpenStreetMap). Unlike the Google Map element, it does not use the.*

**Map (Leaflet)** (`map-leaflet`) embeds an interactive map using **Leaflet** and **tile layers** (default: **OpenStreetMap**). Unlike the Google [Map](https://academy.bricksbuilder.io/builder/elements/general/map/) element, it does **not** use the Google Maps JavaScript API—use this when you want OSM-style tiles or custom tile URLs without Google.

The element is **not draggable** in the builder (`draggable = false`) to avoid conflicts with map interaction. It enqueues `bricks-leaflet` scripts and styles.

## Layers

**Layers** (repeater) — Each layer:

- **Name** (text) — e.g. `OpenStreetMap`.
- **URL** (text) — Tile URL template with `{z}`, `{x}`, `{y}` placeholders.
- **Min Zoom**, **Max Zoom** (number).
- **Error Tile URL** (text).
- **Attribution** (text).

Default repeater row uses OpenStreetMap’s standard tile URL.

## Markers

**Markers** (repeater):

- **Coordinates** (text) — `latitude, longitude` (comma-separated). Supports dynamic data.
- **Label** (text) — Builder-only helper to tell markers apart.
- **Icon** (image) — Per-marker image; **Height** / **Width** (px) when set.
- **Popup (Text)** (editor) — Popup content for that marker.

### Marker (Default)

Global defaults when a marker has no custom icon:

- **Icon** (image), **Icon: Height (px)**, **Icon: Width (px)**.

## Map

- **Height** (number with units) — Map container height. Default placeholder: `300px`. Triggers reload when changed.

- **Map center** (text) — `latitude, longitude`.

- **Zoom level (Initial)** (number).

- **Zoom level (Min)**, **Zoom level (Max)** (number).

- **Zoom: Snap**, **Zoom: Delta** (number).

- **Zoom: Double-click** (select) — Enabled, Enabled (Center), or Disabled.

- **Zoom: Scroll wheel** (select) — Same options.

- **Box Zoom** (checkbox).

- **Zoom Control** (checkbox).

- **Attribution Control** (checkbox).

- **Close popup on click** (checkbox).

- **Dragging** (checkbox).

- **Track resize** (checkbox) — See [Leaflet map options](https://leafletjs.com/reference.html#map).

> **Developer reference**
>
> See the [Map (Leaflet) Schema](https://academy.bricksbuilder.io/developer/schema/elements/map-leaflet/) for the full JSON schema of this element's settings and controls.

---

# Map Connector

Source: https://academy.bricksbuilder.io/builder/elements/general/map-connector/

*The Map Connector works with the Google Map element when Sync with query is enabled. Place one Map Connector inside each item of the query loop that should.*

The **Map Connector** works with the Google [Map](https://academy.bricksbuilder.io/builder/elements/general/map/) element when **Sync with query** is enabled. Place **one Map Connector inside each item** of the query loop that should produce a marker.

It renders an invisible **`<template>`** node that stores latitude, longitude, and/or address plus optional **Info Box** popup template data and **per-item marker overrides**. The Map reads these nodes to build markers when the query updates (pagination, filters, load more, etc.).

See [Map → Sync with query](https://academy.bricksbuilder.io/builder/elements/general/map/#sync-with-query) for the full workflow.

## Settings

- **Latitude** (text) — Use dynamic data from the looped post (placeholder shows Berlin-area example).

- **Longitude** (text).

- **Address** (text) — Alternative to coordinates; may geocode via Google when coordinates are not set.

An **error** info appears when all three are empty—Bricks expects at least one source of location via dynamic tags.

### Info Box (Popup)

- **Info Box: Template (Popup)** (select) — Popup template with **Template Settings → Popup → Info Box (Map)** enabled.

- **Info** — Reminds you to enable the Info Box option on the popup template.

### Markers

An **info** control notes that **Marker: Type** (text vs image) is configured on the **Map** element, while fields here **override** that map’s defaults for **this** loop item.

On the connector, Bricks only exposes marker fields that are **not** flagged `mainOnly` in the shared map-marker control set—so you set **per-loop values**, not the global marker typography or image dimensions (those stay on the **Map** element):

- **Label** (text) — Screen reader label (`aria-label`) for the marker.

- **Marker: Text** — **Text** field for the default text marker.

- **Marker: Text (Active)** — **Text** field for the active text marker.

- **Marker: Image** — **Icon** (image) for the default image marker.

- **Marker: Image (Active)** — **Icon** (image) for the active image marker.

> **Developer reference**
>
> See the [Map Connector Schema](https://academy.bricksbuilder.io/developer/schema/elements/map-connector/) for the full JSON schema of this element's settings and controls.

---

# Map

Source: https://academy.bricksbuilder.io/builder/elements/general/map/

*The Map element in Bricks allows you to display Google Maps with a range of capabilities, from showing a single location to dynamically rendering multiple.*

The **Map** element in Bricks allows you to display Google Maps with a range of capabilities, from showing a single location to dynamically rendering multiple markers based on queries.

You can get started quickly by adding a Google Maps API key. Follow this guide to set it up: [How to set up your Google Maps API key](https://academy.bricksbuilder.io/integrations/how-to-set-up-your-google-maps-api-key/).

Without an API key, the Map element is still functional but limited to displaying **a single marker** only.

![](https://academy.bricksbuilder.io/assets/map-without-google-maps-api.png)

To ensure a marker is shown, simply enter a pair of coordinates (latitude and longitude, separated by a comma) in the **Address** field.

## Choose how the map renders

With an API key saved, **Render mode** lets you choose **Google Maps JavaScript API** (the default) or **Iframe embed**. Use Iframe embed when the map only needs a single address and you do not need API-only features such as multiple markers, clustering, query syncing, or custom Info Boxes. The iframe mode does not load the Google Maps JavaScript API for that map. Set its **Loading** option to `lazy` (the default) or `eager`.

Without an API key, the map uses the single-address iframe mode automatically. The Render mode selector appears only when an API key is saved.

## Displaying multiple addresses

To unlock advanced features such as multiple locations, clustering, and custom Info Boxes, save a valid **Google Maps API key** and use the **Google Maps JavaScript API** render mode. You will then see more controls on the element.

![](https://academy.bricksbuilder.io/assets/bricks-2.0-map-addresses.png)

Bricks supports three address input modes:

### 1) Static

Manually define multiple locations using the "Addresses" **Repeater** control of the Map element. This mode supports only the default Google Maps Info Box.

### 2) Query loop

Use this mode when map addresses to feed the map with addresses/coordinates from a query.

For example, if you have a **custom post type** like "Properties" where each property contains an address, enabling the Query loop allows you to show markers of all property addresses on the map. `(@since 2.0)`

![](https://academy.bricksbuilder.io/assets/bricks-2.0-map-query-loop.png)

You can also define a [custom Info Box](#info-box-popup-template) using a popup template.

In our example above, we selected the custom post type `property`, where each address is stored in a custom field (ACF). Providing the latitude & longitude coordinates will be more accurate than a physical address.

### 3) Sync with query

Ideal for use cases where the map is shown alongside a dynamic query loop such as a directory, Sync with query allows the map to update live with the query as users interact via **AJAX Pagination**, **Load More**, or **Query Filters**.

This mode requires adding a [Map Connector](#map-connector-element) element inside the target query loop.

It also supports [custom Info Boxes](#info-box-popup-template) using popup templates.

**Example setup:** You want to display a query loop on the same page as your map and connect the two. If this query loop uses **AJAX Pagination**, **Query Filters**, or **Load More**, enabling Sync with query allows the map markers to update dynamically in real-time as users interact with those features.

![](https://academy.bricksbuilder.io/assets/bricks-2.0-map-sync-with-query.png)

**Map markers update according to query results**:

![](https://academy.bricksbuilder.io/assets/bricks-2.0-map-sync-with-query-filters.png)

## Markers

![](https://academy.bricksbuilder.io/assets/markers-control.png)

### Cluster markers

Enable this option to automatically group nearby markers into a cluster. `(@since 2.0)`

![](https://academy.bricksbuilder.io/assets/cluster-markers.png)

## General Settings

### Map ID

![](https://academy.bricksbuilder.io/assets/map_id-control.png)

Enter your **Google Maps ID** (available in your Google Cloud Console) to enable the latest Maps features `(@since 2.0)`  
When set:

- Bricks uses Google's modern `AdvancedMarker` API.
- Map styles are managed via your Google Console (style settings in Bricks are disabled).
- Deprecated browser console warnings are avoided.

### Map Center

![](https://academy.bricksbuilder.io/assets/map-center-control.png)

Set the default center point of the map. Particularly useful when using **Sync with query**—if the synced query returns no results, the map will reset to this center point. `(@since 2.0)`

### Others

![](https://academy.bricksbuilder.io/assets/general-settings.png)

## Map Connector (element)

**The Map Connector element `(@since 2.0)` is required when using Sync with query.**

Place it inside the target query loop that you want to sync with your map. It generates an invisible `<template>` node containing location data, which is then read by the map to dynamically render the markers.

**Note:** It's strongly recommended to provide **latitude and longitude** values whenever available. If you rely solely on addresses and require geocoding every time markers are rendered, you may incur charges from the Google Maps Platform Geocoding API.

![](https://academy.bricksbuilder.io/assets/map-connector.png)

You can also define the Info Box (popup template) that should show when a marker is clicked. Make sure the selected popup template has the **"Info Box (Map)"** option enabled in its settings.

## Info Box (Popup template)

Introduced in version 2.0, the **Info Box (Map)** option is available in Popup template settings.

![](https://academy.bricksbuilder.io/assets/infobox-popup.png)

- Once enabled, the popup will display with a default width of 300px in the builder and remove the backdrop for preview.
- You can customize the design of the Info Box in the builder.
- Supports **Fetch content via AJAX**.
- Supports **AJAX loader** animation when loading dynamically.
- It is recommended to set **Populate Content** to the post or term being looped so dynamic data displays correctly in the builder.

![](https://academy.bricksbuilder.io/assets/infobox-popup-preview.png)

## Map Interactions

Two new map interaction actions are introduced in Bricks 2.0:

- Open address (Map)
- Close address (Map)

![](https://academy.bricksbuilder.io/assets/interaction.png)

Use cases:

- Use a button or element inside the query loop to **open** the Info Box for the corresponding marker.
- Add a close icon inside the Info Box popup to allow users to manually **close** it.

These interactions provide greater control and flexibility over how Info Boxes behave in dynamic mapping scenarios.

When an Info Box opens, Bricks adds the `infobox-opened` class to the interaction elements associated with that marker. The class is removed when the Info Box closes. You can use this class to style the open state or a parent element that contains the interaction element:

```css
.looping-div:has(.infobox-opened) {
  background-color: blue;
}
```

## Resolving Google Maps Script Conflicts with Other Plugins

If you're using a plugin like Fluent Form, which may enqueue the Google Maps script on the same page, this can result in a JavaScript conflict because the script cannot be loaded twice.

To prevent this issue, you can dequeue Bricks' Google Maps script and trigger the `bricksMap()` function manually after a short delay, ensuring the Fluent Forms map script has loaded first:

```php
add_action( 'wp_enqueue_scripts', function() {
  if ( is_page( 1567 ) ) {
    wp_deregister_script( 'bricks-google-maps' );
  }
}, 999 );

add_action( 'wp_footer', function() {
  if ( is_page( 1567 ) ) {
    echo '<script>
      document.addEventListener("DOMContentLoaded", function() {
        setTimeout(function() {
          bricksMap();
        }, 1000); // Adjust delay if needed
      });
    </script>';
  }
}, 999 );
```

Replace `1567` with your actual page ID. Adjust the delay as necessary to ensure the Fluent Forms map script has fully loaded before `bricksMap()` runs.

## Settings

### Addresses

- **Addresses** (repeater) - Add map locations. Each address has:
  - **Latitude** (text) - Latitude coordinate. Placeholder: `52.5164154966524`.
  - **Longitude** (text) - Longitude coordinate. Placeholder: `13.377643715349544`.
  - **Address** (text) - Address for geocoding (alternative to coordinates). Placeholder: `Berlin, Germany`.
  - **Info Box template** (select) - Template for infobox popup.
  - **Title** (text) - Infobox title.
  - **Subtitle** (text) - Infobox subtitle.
  - **Content** (textarea) - Infobox content.
  - **Images** (image-gallery) - Images for infobox.
  - **Width** (number) - Infobox width. Placeholder: `300`.
  - **Label** (text) - Screen reader label for accessibility.
  - **Marker: Text** (text) - Text marker content. Placeholder: `Marker`.
  - **Marker: Text (Active)** (text) - Active text marker content. Placeholder: `Marker`.
  - **Marker: Image** (image) - Image marker.
  - **Marker: Image (Active)** (image) - Active image marker.

### Query loop

- **Has loop** (checkbox) - Enable query loop for dynamic addresses.
- **Query** (query) - Configure which posts to display.
- **Info Box: Template** (select) - Template for infobox popup in query loop.

### Sync with query

- **Sync with query** (query-list) - Connect to existing query loop for dynamic markers.
- **Text: No results** (text) - Message when no locations found. Placeholder: `No locations found`.

### Markers

- **Cluster: Markers** (checkbox) - Enable marker clustering.
- **Cluster: Background color** (color) - Cluster background color.
- **Cluster: Text color** (color) - Cluster text color.

- **Marker** (separator) - Global marker settings.
- **Type** (select) - Marker type. Options: `image`, `text`. Default: `image`.

#### Marker: Text

- **Max. width** (number with units) - Maximum text marker width.
- **Typography** (typography) - Text marker font settings.
- **Background color** (color) - Text marker background.
- **Border** (border) - Text marker border styling.
- **Box shadow** (box-shadow) - Text marker shadow.
- **Padding** (spacing) - Text marker padding.

#### Marker: Text (Active)

- **Typography** (typography) - Active text marker font settings.
- **Background color** (color) - Active text marker background.
- **Border** (border) - Active text marker border styling.
- **Box shadow** (box-shadow) - Active text marker shadow.
- **Padding** (spacing) - Active text marker padding.

#### Marker: Image

- **Marker** (image) - Default marker image.
- **Height** (number) - Marker height in pixels. Placeholder: `40`.
- **Width** (number) - Marker width in pixels. Placeholder: `40`.
- **Border** (border) - Marker border styling.
- **Box shadow** (box-shadow) - Marker shadow.

#### Marker: Image (Active)

- **Marker (Active)** (image) - Active marker image.
- **Height** (number) - Active marker height in pixels. Placeholder: `40`.
- **Width** (number) - Active marker width in pixels. Placeholder: `40`.
- **Border** (border) - Active marker border styling.
- **Box shadow** (box-shadow) - Active marker shadow.

### Map

- **Map ID** (text) - Google Maps ID from Cloud Console for advanced features.
- **Render mode** (select) - With an API key saved, choose Google Maps JavaScript API or Iframe embed. Default: Google Maps JavaScript API.
- **Loading** (select) - For iframe rendering, choose `lazy` or `eager`. Default: `lazy`.

#### Map center

- **Latitude (Center)** (text) - Map center latitude. Placeholder: `52.5164154966524`.
- **Longitude (Center)** (text) - Map center longitude. Placeholder: `13.377643715349544`.
- **Address (Center)** (text) - Map center address. Placeholder: `Berlin, Germany`.

#### General settings

- **Height** (number with units) - Map container height. Placeholder: `300px`.
- **Zoom level** (number) - Initial map zoom level. Range: 0-20. Placeholder: `12`.
- **Map type** (select) - Map style. Options: `roadmap`, `satellite`, `hybrid`, `terrain`. Default: `roadmap`.
- **Map style** (select) - Predefined map styles. Requires roadmap type.
- **Custom map style** (code) - JSON code for custom styling from Snazzy Maps.
- **Apply: Custom map style** (apply) - Apply custom style changes.
- **Fit map on markers change** (checkbox) - Auto-adjust view when markers change.
- **Scroll** (checkbox) - Enable scroll wheel zooming. Default: true.
- **Draggable** (checkbox) - Enable map dragging. Default: true.
- **Fullscreen Control** (checkbox) - Show fullscreen button.
- **Map Type Control** (checkbox) - Show map type selector.
- **Street View Control** (checkbox) - Show street view button. Default: true.
- **Disable Default UI** (checkbox) - Hide all default controls.
- **Disable clickable POI** (checkbox) - Disable clicking on points of interest.
- **Zoom Control** (checkbox) - Show zoom controls. Default: true.
- **Zoom level (Min)** (number) - Minimum zoom level.
- **Zoom level (Max)** (number) - Maximum zoom level.

### No API Key Mode

When no Google Maps API key is configured, the element falls back to Google Maps Embed API with limited functionality:

- **Address** (text) - Single address for embedded map. Placeholder: `Berlin, Germany`.
- **Loading** (select) - Loading behavior. Options: `eager`, `lazy`. Default: `lazy`.

> **Developer reference**
>
> See the [Map (Google) Schema](https://academy.bricksbuilder.io/developer/schema/elements/map/) for the full JSON schema of this element's settings and controls.

---

# Nav (Nestable)

Source: https://academy.bricksbuilder.io/builder/elements/general/nav-nested/

*The Nav (Nestable) element creates hierarchical navigation menus with dropdown functionality, multilevel support, and mobile-responsive behavior. It supports.*

The Nav (Nestable) element creates hierarchical navigation menus with dropdown functionality, multilevel support, and mobile-responsive behavior. It supports nested menu structures and can be used to build complex navigation systems.

## Settings

### HTML Tag & Accessibility

- **HTML tag** (text) - HTML tag for the navigation element. Supports dynamic data. Default placeholder: `nav`. Validates HTML tag format.

- **aria-label** (text) - Accessibility label for the navigation. Supports dynamic data. Default placeholder: "Menu".

### Top Level (Item)

- **Gap** (number with units) - Gap between top-level navigation items. Controls `gap` property for `.brx-nav-nested-items` selector.

- **Justify content** (justify-content) - Horizontal alignment of top-level items. Deprecated since version 1.10. Description suggests using "Align items" under "Mobile menu" instead. Direction: row. Excludes space options.

- **Padding** (spacing) - Padding for top-level navigation items. Controls `padding` property for multiple selectors including `.brx-nav-nested-items > li > a`, text links, icons, SVG elements, and submenu toggles.

- **Background color** (color) - Background color for top-level items. Controls `background-color` property for links, text links, icons, SVG elements, and submenu toggles.

- **Border** (border) - Border styling for top-level items. Controls `border` property for links, text links, icons, SVG elements, and submenu toggles.

- **Typography** (typography) - Typography settings for top-level items. Controls `font` property for links, text links, icons, SVG elements, and submenu toggles.

- **Transform** (transform) - Transform settings for top-level items. Controls `transform` property for links, text links, icons, SVG elements, and submenu toggles.

- **Transition** (text) - Transition settings for top-level items. Supports dynamic data. Controls `transition` property for list items, links, text links, icons, SVG elements, submenu toggles, and submenu toggle children.

#### Active State

- **Active** (separator) - Visual separator for active state controls.

- **Background color** (color) - Background color for active/current page items. Controls `background-color` property for `[aria-current="page"]` and `.brx-submenu-toggle.aria-current` selectors.

- **Border** (border) - Border styling for active items. Controls `border` property for `[aria-current="page"]` and `.brx-submenu-toggle.aria-current` selectors.

- **Typography** (typography) - Typography settings for active items. Controls `font` property for `[aria-current="page"]` and `.brx-submenu-toggle.aria-current > *` selectors.

#### Dropdown (Top Level Only)

- **Dropdown** (separator) - Separator for top-level dropdown controls. Description: "Only applies to top level dropdown elements."

- **Text padding** (spacing) - Padding for dropdown text. Controls `padding` property for `.brx-nav-nested-items > li > .brx-submenu-toggle > span` selector.

- **Icon padding** (spacing) - Padding for dropdown icons. Controls `padding` property for `.brx-nav-nested-items > li > .brx-submenu-toggle button` selector.

- **Gap** (number with units) - Gap between text and icon in dropdown toggles. Controls `gap` property for `.brx-nav-nested-items > li > .brx-submenu-toggle` selector.

### Dropdown

#### Text

- **Text** (separator) - Separator for dropdown text controls. Description: "Control dropdown element text."

- **Text padding** (spacing) - Padding for dropdown text. Controls `padding` property for `.brx-submenu-toggle span` selector (applies to all dropdowns).

#### Icon

- **Icon** (separator) - Separator for dropdown icon controls. Description: "Edit dropdown to set icon individually."

- **Icon padding** (spacing) - Padding for dropdown icons. Controls `padding` property for `.brx-submenu-toggle button` selector.

- **Gap** (number with units) - Gap between text and icon in dropdown toggles. Controls `gap` property for `.brx-submenu-toggle` selector.

- **Icon position** (select) - Position of the dropdown icon. Options from icon position control options. Default placeholder: "Right". Controls `flex-direction` property for `.brx-submenu-toggle` selector (sets to `row-reverse` when left).

- **Icon size** (number with units) - Size of the dropdown icon. Controls `font-size` property for `.brx-submenu-toggle button` selector.

- **Icon color** (color) - Color of the dropdown icon. Controls `color` property for `.brx-submenu-toggle button` selector.

- **Icon transform** (transform) - Transform settings for dropdown icons. Controls `transform` property for `.brx-submenu-toggle button > *` selector (targets icon only).

- **Icon transform (Open)** (transform) - Transform settings for dropdown icons when open. Controls `transform` property for `.brx-submenu-toggle button[aria-expanded="true"] > *` selector (targets icon only).

- **Icon transition** (text) - Transition settings for dropdown icons. Supports dynamic data. Controls `transition` property for `.brx-submenu-toggle button[aria-expanded] > *` selector (targets icon only). Uses `!important` to override other transitions.

#### Content

- **Content** (separator) - Separator for dropdown content controls. Description: "Sub menu, mega menu, or multilevel area."

- **Min. width** (number with units) - Minimum width for dropdown content. Controls `min-width` property for `.brx-dropdown-content` selector. Triggers re-render.

- **Background color** (color) - Background color for dropdown content. Controls `background-color` property for `.brx-dropdown-content` selector.

- **Border** (border) - Border styling for dropdown content. Controls `border` property for `.brx-dropdown-content` selector.

- **Box shadow** (box-shadow) - Box shadow for dropdown content. Controls `box-shadow` property for `.brx-dropdown-content` selector.

- **Typography** (typography) - Typography settings for dropdown content. Controls `font` property for `.brx-dropdown-content` selector.

- **Transform** (transform) - Transform settings for dropdown content. Controls `transform` property for `.brx-nav-nested-items > .brxe-dropdown > .brx-dropdown-content` selector.

- **Transform (Open)** (transform) - Transform settings for dropdown content when open. Controls `transform` property for `.brx-nav-nested-items > .brxe-dropdown.open > .brx-dropdown-content` selector.

- **Transition** (text) - Transition settings for dropdown content. Supports dynamic data. Controls `transition` property for `.brx-dropdown-content` selector.

- **Z-index** (number) - Z-index for dropdown elements. Controls `z-index` property for `.brxe-dropdown` selector. Default placeholder: 1001.

#### Item

- **Item** (separator) - Separator for dropdown item controls.

- **Padding** (spacing) - Padding for dropdown items. Controls `padding` property for `.brx-dropdown-content > li > a` and `.brx-dropdown-content :where(.brx-submenu-toggle > *)` selectors.

- **Background** (color) - Background color for dropdown items. Controls `background-color` property for `.brx-dropdown-content > li` and `.brx-dropdown-content .brx-submenu-toggle` selectors.

- **Border** (border) - Border styling for dropdown items. Controls `border` property for `.brx-dropdown-content > li:not(.brxe-dropdown)` and `.brx-dropdown-content .brx-submenu-toggle` selectors.

- **Typography** (typography) - Typography settings for dropdown items. Controls `font` property for `.brx-dropdown-content > li > a` and `.brx-dropdown-content .brx-submenu-toggle > *` selectors.

- **Transition** (text) - Transition settings for dropdown items. Supports dynamic data. Controls `transition` property for dropdown content items, links, submenu toggles, and megamenu elements.

#### Multilevel

- **Multilevel** (separator) - Separator for multilevel controls. Description: "Show only active dropdown. Toggle on click. Inner dropdowns inherit multilevel."

- **Enable** (checkbox) - Enable multilevel dropdown functionality.

- **Back: Text** (text) - Text for the back button in multilevel navigation. Only available when multilevel is enabled.

- **Back: Typography** (typography) - Typography settings for the back button. Only available when multilevel is enabled. Controls `font` property for `.brx-multilevel-back` selector.

- **Back: Background** (color) - Background color for the back button. Only available when multilevel is enabled. Controls `background-color` property for `.brx-multilevel-back` selector.

### Mobile Menu

- **Mobile menu** (separator) - Separator for mobile menu controls. Description: "Insert "Toggle" element after "Nav items" to show/hide your mobile menu."

- **Keep open while styling** (checkbox) - Keep mobile menu open during styling in the builder. Adds `brx-open` class. Not saved as setting.

- **Hide at breakpoint** / **Show at breakpoint** (select) - Breakpoint at which to show/hide mobile menu. Options include all breakpoints plus "Always" and "Never". Default placeholder: "Mobile landscape". Triggers re-render.

- **Width** (number with units) - Width of the mobile menu. Controls `width` property for `&.brx-open .brx-nav-nested-items` selector.

- **Height** (number with units) - Height of the mobile menu. Controls `height` property for `&.brx-open .brx-nav-nested-items` selector.

- **Padding (Dropdown)** (spacing) - Padding for dropdown content in mobile view. Controls padding for `&.brx-open .brx-dropdown-content > *` selector. Description: "Used to create visual hierarchy between nested dropdowns."

- **Align items** (align-items) - Vertical alignment of mobile menu items. Controls `align-items` property for `&.brx-open .brx-nav-nested-items` selector.

- **Justify content** (justify-content) - Horizontal alignment of mobile menu items. Controls `justify-content` property for `&.brx-open .brx-nav-nested-items` selector.

- **Position** (dimensions) - Position settings for the mobile menu. Controls multiple position properties.

- **Background color** (color) - Background color for the mobile menu. Controls `background-color` property for mobile menu selectors.

#### Item

- **Item** (separator) - Separator for mobile menu item controls.

- **Align items** (align-items) - Vertical alignment of mobile menu items. Excludes `stretch` option. Controls `align-items` property for various mobile menu item selectors.

> **Developer reference**
>
> See the [Nav (Nestable) Schema](https://academy.bricksbuilder.io/developer/schema/elements/nav-nested/) for the full JSON schema of this element's settings and controls.

---

# Offcanvas

Source: https://academy.bricksbuilder.io/builder/elements/general/offcanvas/

*The Offcanvas element is a nestable panel that slides (or offsets) in from a chosen edge of the viewport. Typical use: mobile navigation. Bricks suggests adding.*

The **Offcanvas** element is a **nestable** panel that slides (or offsets) in from a chosen edge of the viewport. Typical use: mobile navigation. Bricks suggests adding a [Toggle](https://academy.bricksbuilder.io/builder/elements/general/toggle/) elsewhere on the page that targets this Offcanvas (see the in-element info link to the menu builder article).

The default structure includes an inner **Block** (`.brx-offcanvas-inner`) for your content—often with starter **Text** and a **Toggle** labeled for closing—and a second **Block** acting as the **Backdrop** (`.brx-offcanvas-backdrop`), which you can remove if you do not want a backdrop.

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

*The Nestable Tabs element allows creating tabbed content with drag-and-drop nesting in the builder.*

The Nestable Tabs element allows creating tabbed content with drag-and-drop nesting in the builder.

## Settings

- **Direction** (direction) - Layout direction of the tabs. Controls the `flex-direction` CSS property. Set "ID" on tab menu "Div" to open a tab via anchor link (no spaces, no pound sign).

- **Open tab on** (select) - Trigger for opening tabs. Options: `click`, `hover`. Default: `click`.

- **Open tab index** (text) - Index of the tab to expand on page load, starting at 0. Default: 0.

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

# Product price

Source: https://academy.bricksbuilder.io/builder/elements/product/product-price/

*Displays the WooCommerce product price, including regular price, sale price, and price range for variable products.*

Displays the WooCommerce product price, including regular price, sale price, and price range for variable products.

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

> **Developer reference**
>
> See the [Post Content Schema](https://academy.bricksbuilder.io/developer/schema/elements/post-content/) for the full JSON schema of this element's settings and controls.

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

- **Share via** (repeater) - Social media services to include. Default includes: Facebook, X, LinkedIn, WhatsApp, Pinterest, Telegram, VKontakte, Bluesky, Email.
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

---

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
