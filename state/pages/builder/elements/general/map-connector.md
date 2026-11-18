*Connect query-loop items to Google or Leaflet map markers using coordinates, per-item marker settings, and Info Box templates.*

The **Map Connector** works with the Google [Map](https://academy.bricksbuilder.io/builder/elements/general/map/) element and, starting with **Bricks 2.5**, [Map (Leaflet)](https://academy.bricksbuilder.io/builder/elements/general/map-leaflet/) when **Sync with query** is enabled. Place **one Map Connector inside each item** of the query loop that should produce a marker.

It renders an invisible **`<template>`** node that stores latitude, longitude, and/or address plus optional **Info Box** popup template data and **per-item marker overrides**. The Map reads these nodes to build markers when the query updates (pagination, filters, load more, etc.).

See [Google Map: Sync with query](https://academy.bricksbuilder.io/builder/elements/general/map/#3-sync-with-query) or [Leaflet: Sync with query](https://academy.bricksbuilder.io/builder/elements/general/map-leaflet/#sync-with-query) for setup. External controls target the results loop containing the connectors, rather than the map itself.

Leaflet requires both **Latitude** and **Longitude**. It ignores address-only connectors. Google Maps can geocode an **Address** when coordinates are not supplied.

For [Geolocation filtering](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#filter-geolocation-element), the filter's data source must contain saved coordinates. Geocoding a connector's Address for a Google marker does not create coordinates in the filter index. Use the same location fields for the filter and connector so the radius search and markers agree.

Both map types preview the connected loop's markers in the builder. Test filters and pagination on the frontend.

## Active Marker State {#active-marker-state}

Starting with **Bricks 2.5**, a connector synced to a **Google Map** or **Map (Leaflet)** receives `map-marker-active` when its marker is selected by a click or an **Open address (Map)** interaction. This works without an Info Box. The class is removed when another marker is selected or the marker state is reset.

The connector itself is invisible. To highlight a card, assign a class such as `property-card` to the repeated item and use `.property-card:has(.map-marker-active)` in your CSS. See the [active connected item example](https://academy.bricksbuilder.io/builder/elements/general/map/#active-connected-item).

Both Google Map and Map (Leaflet) support **Scroll active item into view** in Sync mode. Bricks finds the loop item and scroll container automatically. See the [Google Map scroll settings](https://academy.bricksbuilder.io/builder/elements/general/map/#scroll-active-item) or [Leaflet scroll settings](https://academy.bricksbuilder.io/builder/elements/general/map-leaflet/#scroll-active-item).

The `infobox-opened` class on interaction elements follows the Info Box's open/close state. Use `map-marker-active` on the connector to style the selected result independently of whether it has an Info Box.

## Settings

- **Latitude** (text) - Use dynamic data from the looped post (placeholder shows Berlin-area example).

- **Longitude** (text).

- **Address** (text) - Google Maps only: alternative to coordinates, resolved through geocoding. Leaflet requires latitude and longitude.

An error notice appears when all three fields are empty. For Leaflet, fill in both coordinate fields even if an Address is already set.

### Info Box (Popup)

- **Info Box: Template (Popup)** (select) - Popup template with **Template Settings > Popup > Info Box (Map)** enabled.

- **Info** - Reminds you to enable the Info Box option on the popup template.

### Markers

An **info** control notes that **Marker: Type** (text vs image) is configured on the connected map element, while fields here **override** that map’s defaults for **this** loop item.

Use the connector to set values for each loop item. Set global marker typography and image dimensions on the connected map element.

- **Label** (text) - Screen reader label (`aria-label`) for the marker.

- **Marker: Text** - Text for the default text marker.

- **Marker: Text (Active)** - Text for the active text marker.

- **Marker: Image** - Image for the default image marker.

- **Marker: Image (Active)** - Image for the active image marker.

> **Developer reference**
>
> See the [Map Connector Schema](https://academy.bricksbuilder.io/developer/schema/elements/map-connector/) for the full JSON schema of this element's settings and controls.