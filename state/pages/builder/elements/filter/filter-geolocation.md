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