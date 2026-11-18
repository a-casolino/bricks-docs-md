# Map (Leaflet)

Source: https://academy.bricksbuilder.io/integrations/map-leaflet/

*Use the Leaflet-based map element in Bricks to build interactive maps with layers, markers, and configurable map behavior.*

The **Map (Leaflet)** element, available since Bricks 2.1, displays maps powered by [Leaflet.js](https://leafletjs.com/). Choose tile providers, add markers, and configure the map inside Bricks without a Google Maps API key.

Starting with **Bricks 2.5**, it supports query-generated markers, syncing with a separate query loop, clustering, text and image markers with active styles, and custom Info Boxes. See the [Map (Leaflet) element reference](https://academy.bricksbuilder.io/builder/elements/general/map-leaflet/) for setup and settings.

## Overview {#overview}

The Map (Leaflet) element is divided into three main groups of settings:

1. **Layers** – define map sources (OpenStreetMap, OpenTopoMap, etc.)
2. **Markers** – add custom points with icons and popups
3. **Map** – configure global map settings (center, zoom, etc.)

## Layers {#layers}

Layers control which map tiles are displayed.

Each layer is defined through a **Repeater**. Meaning you can add multiple layers (map styles) and let visitors switch between them.

For each layer, you'll configure:

- **Name** – label shown in the layer switcher (e.g. “Street Map”, “Topographic”).
- **URL** – the provider URL (e.g. `https://tile.openstreetmap.org/{z}/{x}/{y}.png`). Bricks passes this URL to Leaflet, which replaces the placeholders supported by your tile provider. You can view list of *some* providers [here](https://leaflet-extras.github.io/leaflet-providers/preview/index.html).
  - Most tile providers require `{z}`, `{x}`, and `{y}`:
    - `{z}` → zoom level
    - `{x}` / `{y}` → tile coordinates
  - Some providers also use `{s}` for subdomains (a, b, c, …). Add it only when your provider URL requires it.
- **Min/Max Zoom** – zoom levels the layer supports.
- **Error Tile URL** – fallback image if tiles fail to load.
- **Attribution** – copyright or usage text (required by most providers).

For example:

- **Street Map** → OpenStreetMap tiles
- **Topo Map** → OpenTopoMap tiles
- **Satellite** → Esri or other provider

Your users can then toggle between these layers on the frontend.

## Markers {#markers}

Markers identify locations using latitude and longitude. Choose one of three sources:

- **Static**: Add rows under **Markers**, with coordinates, optional icons, and popup text.
- **Query loop** (Bricks 2.5): Populate the first marker row with dynamic data and use it as a template for each query result.
- **Sync with query** (Bricks 2.5): Place [Map Connectors](https://academy.bricksbuilder.io/builder/elements/general/map-connector/) inside a separate results loop and select that loop on the map. Markers update with frontend filters, AJAX pagination, and Load More.

Leaflet does not geocode street addresses. Provide latitude and longitude on every connector. Use the separate results loop as the target for filters, pagination, and Load More.

For marker appearance, clustering, custom Info Boxes, and scrolling to a connected result, see the [element reference](https://academy.bricksbuilder.io/builder/elements/general/map-leaflet/#marker-source).

## Geolocation filtering {#geolocation-filtering}

From Bricks 2.5, use [Filter - Geolocation](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#filter-geolocation-element) with a Posts, Terms, or Users listing and **Sync with query** to search within a radius. The filter reads saved coordinates; Leaflet's marker coordinates come from Map Connectors inside the same results loop.

Device location and searching after map drags work without Google APIs. Enabling address search requires Google Maps JavaScript API and Geocoding API; autocomplete additionally requires Places API (New). See [Leaflet geolocation setup](https://academy.bricksbuilder.io/builder/elements/general/map-leaflet/#geolocation-filtering) for the filter and map connection.

## Map

Set **Height** (the placeholder is `300px`), **Map center**, and the initial zoom level in the **Map** group.

From Bricks 2.5, the initial view centers a single marker at the configured zoom or fits multiple markers. Enable **Disable initial fit map** to preserve your configured center and zoom. Existing static maps also adopt this behavior, so enable the setting if you need to retain their previous view.

**Fit map on markers change** separately controls whether frontend updates to the synced query adjust the view. Both settings are off by default. See [Map view and behavior](https://academy.bricksbuilder.io/builder/elements/general/map-leaflet/#map-view) for details.

The Map group also includes zoom interactions, dragging, attribution, and resize tracking. See the [Leaflet documentation](https://leafletjs.com/reference.html#map) for the underlying options.
