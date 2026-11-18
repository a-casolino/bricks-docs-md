*Display tile-based maps, populate markers from a query, or sync them with a filterable listing using Map Connectors.*

**Map (Leaflet)** displays maps using tile layers such as OpenStreetMap. Configure the tile provider under **Layers**, add locations under **Markers**, and set the center, zoom, and interactions under **Map**. It does not require a Google Maps API key. Tile providers may have their own access and attribution requirements.

Starting with **Bricks 2.5**, the element supports query-generated markers, **Sync with query**, clustering, text and image markers with active styles, and custom Info Boxes.

## Layers

Add a row to **Layers** for each tile source visitors should be able to select. Each row has:

- **Name**: Label in the layer switcher.
- **URL**: Tile URL template, such as `https://tile.openstreetmap.org/{z}/{x}/{y}.png`.
- **Min Zoom** and **Max Zoom**: Zoom levels supported by the tile provider.
- **Error Tile URL**: Fallback image for failed tiles.
- **Attribution**: Credits required by the provider.

The default layer uses OpenStreetMap. See the [Leaflet integration guide](https://academy.bricksbuilder.io/integrations/map-leaflet/#layers) for tile URL placeholders and provider examples.

## Choose the marker source {#marker-source}

| Mode | Use it for | Location data comes from |
| --- | --- | --- |
| Static | A fixed set of locations | Rows in the **Markers** repeater |
| Query loop | Markers generated from posts, terms, or other query results | Dynamic data in the first marker row |
| Sync with query | A map beside a listing that changes through filters, AJAX pagination, or Load More | Map Connectors inside a separate query loop |

Leaflet requires latitude and longitude. It does not convert street addresses into coordinates. Address-only Map Connectors are ignored.

### Static markers {#static-markers}

Add a row under **Markers** for each location. Enter **Coordinates** as `latitude, longitude`, for example `52.5164, 13.3776`. Dynamic data is supported. Static and query markers with missing, nonnumeric, or out-of-range coordinates are skipped.

Use **Label** to distinguish rows in the builder. It is separate from the screen reader **Label** in the marker settings. Add **Popup (Text)** for content shown when the marker is clicked. Each row can override the map's text or image marker defaults.

### Query loop {#query-loop}

Use the map's own query when you need markers without a separate visible results listing.

1. Under **Markers**, enable **Query loop**.
2. Open **Query** and choose the content to retrieve.
3. In the first marker row, use dynamic data for **Coordinates** and any marker text, images, or **Popup (Text)** that should change for each result.
4. For a custom popup design, select an **Info Box: Template (Popup)**. See [Info Boxes](#info-boxes).

Bricks uses the first marker row as the template for every query result. The screenshots below use a Publisher terms query with an ACF Google Map field named `map_location`. Its **Coordinates** value is:

```text
{acf_map_location:array_value|lat}, {acf_map_location:array_value|lng}
```

<div className="screenshot screenshot--control-panel">

![The first Leaflet marker row uses dynamic latitude and longitude from an ACF map field.](https://academy.bricksbuilder.io/assets/leaflet-query-marker-coordinates-2x.webp)

</div>

<div className="screenshot screenshot--control-panel">

![Leaflet Query loop enabled with a Terms query targeting the Publishers taxonomy.](https://academy.bricksbuilder.io/assets/leaflet-query-source-settings-2x.webp)

</div>

To update markers through filters, pagination, or Load More, create a separate results loop and use [Sync with query](#sync-with-query).

### Sync with query {#sync-with-query}

Use this mode to keep markers connected to a visible listing, such as property cards beside a map.

1. Create a [Query Loop](https://academy.bricksbuilder.io/builder/dynamic-content/query-loop/) on a layout element, such as a Block or Div.
2. Place one [Map Connector](https://academy.bricksbuilder.io/builder/elements/general/map-connector/) inside the repeated item.
3. Set the connector's **Latitude** and **Longitude** using dynamic data from each result. Add marker overrides or an Info Box template if needed.
4. On Map (Leaflet), leave **Query loop** off. Under **Markers > Sync with query**, select the results loop.
5. Point filters, AJAX Pagination, Load More, and any Query Results Summary at that same results loop.
6. Enable **Map > Fit map on markers change** if the map should adjust its view after the results change.

Markers refresh when the connected loop changes on the frontend. Set **Text: No results** under **Markers** to customize the message when there are no locations. The default is `No locations found`. **No results typography** styles the message, and **No results position** places it at the top, bottom, or center of the map.

![Publisher cards beside Leaflet markers populated from the same Terms query.](https://academy.bricksbuilder.io/assets/leaflet-synced-publisher-list-2x.webp)

The builder previews the connected loop's markers. Test visitor filtering, pagination, and Load More on the frontend.

### Geolocation filtering {#geolocation-filtering}

Starting with **Bricks 2.5**, a [Filter - Geolocation](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#filter-geolocation-element) can limit the connected Posts, Terms, or Users listing to a radius around a location. Set its **Target query** to the results loop containing the Map Connectors, then select that same loop under the map's **Sync with query** control. The map's own query and static markers are not filter targets.

The filter connects automatically when exactly one Geolocation filter and one matching map use the query. For multiple filters or maps, select **Map (Optional)** on the filter. Each filter connects to one map, and each map can be controlled by one filter.

Device-location searches and **Search on map drag** work without Google APIs. Optional address search uses Google Maps JavaScript API and Geocoding API, and autocomplete additionally requires Places API (New). These services are separate from Leaflet's tile provider.

The map shows the applied search origin and radius, including when no locations match. Configure their appearance on the filter. Enable **Search on map drag** on the filter to search around the map center after a visitor finishes panning. Dragging must be enabled on the map. In **Visitor controlled** mode, visitors choose whether to search using a **Search as I move the map** checkbox; **Automatic** mode searches after every qualifying drag. Zooming alone does not trigger a search. **Apply on: On submit** stages the new location until submitted.

### Scroll the active item into view {#scroll-active-item}

In Sync mode, enable **Scroll active item into view** under **Markers** to scroll to a marker's connected result when the marker is clicked or selected through an **Open address (Map)** interaction. This works even when the marker has no Info Box. It is off by default.

- **Scroll behavior**: **Follow site setting** (default), **Smooth**, or **Instant**.
- **Scroll position**: **Nearest** (default), **Start**, or **Center**.

Bricks finds the result's nearest vertically scrollable parent, or scrolls the page when there is none. **Nearest** leaves an already visible item in place. No scroll-container selector is needed.

The selected result's Map Connector also receives `map-marker-active`, including when no Info Box is configured. Use this class to [style the connected card](https://academy.bricksbuilder.io/builder/elements/general/map-connector/#active-marker-state).

<div className="screenshot screenshot--control-panel">

![Leaflet synced to Publishers (Terms), with Scroll active item into view enabled, Smooth behavior, and Center positioning.](https://academy.bricksbuilder.io/assets/leaflet-sync-query-settings-2x.webp)

</div>

## Marker appearance {#marker-appearance}

Under **Markers > Marker**, choose **Type: Image** (default) or **Text**. Settings on individual marker rows or Map Connectors override the map's defaults.

### Text markers

Set the marker text and its active text, then style typography, background, border, box shadow, and padding for each state. **Max. width** limits the text marker's width. Dynamic data can display a property's price or a location's name.

### Image markers

Choose the normal and active marker images. Each state has height, width, border, and box shadow controls. Existing Leaflet **Icon** and **Marker (Default)** settings remain supported for saved maps.

Use the marker's screen reader **Label** to describe its location or purpose.

### Clustering

Enable **Cluster: Markers** to group nearby markers. Set **Cluster: Background color** and **Cluster: Text color** to style the cluster icons. The clustering library loads only when clustering is enabled.

![Publisher-name text markers and purple clusters showing marker counts on a Leaflet map.](https://academy.bricksbuilder.io/assets/leaflet-text-markers-clustering-2x.webp)

## Info Boxes and interactions {#info-boxes}

Static markers use **Popup (Text)**. Query and Sync modes support custom Bricks popup templates:

1. Create a Popup template and enable **Template Settings > Popup > Info Box (Map)**.
2. Design and publish the template. Use dynamic data for the current query result.
3. In Query mode, select it under **Markers > Info Box: Template (Popup)** on the map. In Sync mode, select it on the Map Connector instead.

Info Box templates support **Fetch content via AJAX** and its loader animation. See the [Info Box template guide](https://academy.bricksbuilder.io/builder/elements/general/map/#info-box-popup-template) for template setup.

Use **Open address (Map)** on an element inside the connected result to select its marker and open its Info Box. Use **Close address (Map)** on a button or icon inside the Info Box to close it. These actions are available under [Interactions](https://academy.bricksbuilder.io/builder/features/interactions/#action).

![A custom publisher Info Box showing Hachette Book Group, Saint Joseph, MO, a View publisher link, and a close button.](https://academy.bricksbuilder.io/assets/leaflet-custom-infobox-detail.webp)

## Map view and behavior {#map-view}

| Setting | Behavior |
| --- | --- |
| Height | Map height. The placeholder is `300px`. |
| Map center | Center coordinates as `latitude, longitude`. |
| Disable initial fit map | Keep the configured center and zoom on page load. Off by default. |
| Fit map on markers change | Adjust the view after synced query results change. Off by default. |
| Zoom level (Initial) | Starting zoom. Defaults to `13`. Used when centering a single marker automatically. |
| Zoom level (Min) / (Max) | Constrain how far the map can zoom. |

By default, the initial view centers a single marker at the configured zoom or fits multiple markers.

**Disable initial fit map** and **Fit map on markers change** are independent. Enable the first to preserve the view on page load, and the second if later query updates should fit the current markers.

An active Geolocation search keeps its origin and radius visible instead of fitting the view to the result markers. A successful search with no matching locations retains the search area.

> **Existing Leaflet maps**
>
> Starting with Bricks 2.5, existing static Leaflet maps also use automatic initial fitting. To retain a manually configured center and zoom, enable **Map > Disable initial fit map**, including for maps with one marker.

<div className="screenshot screenshot--control-panel">

![Leaflet Map settings with Disable initial fit map enabled, Fit map on markers change disabled, and the center and zoom controls visible.](https://academy.bricksbuilder.io/assets/leaflet-initial-fit-settings-2x.webp)

</div>

The Map group also includes zoom snapping and increments, double-click and scroll wheel zoom, box zoom, zoom and attribution controls, closing popups on map clicks, dragging, and resize tracking. See [Leaflet's map options](https://leafletjs.com/reference.html#map) for the underlying behavior.

> **Developer reference**
>
> See the [Map (Leaflet) Schema](https://academy.bricksbuilder.io/developer/schema/elements/map-leaflet/) for the element's settings and controls.