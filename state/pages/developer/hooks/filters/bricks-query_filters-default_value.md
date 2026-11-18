*Supply or disable initial query-filter selections using the original page, product, or archive context.*

Available in **Bricks 2.5**, `bricks/query_filters/default_value` filters the initial selection before the target query runs. Use it when a default depends on PHP logic, such as choosing one material from the current product's terms.

For defaults that only need a fixed value or dynamic data tag, use the builder's [Default value controls](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#default-values).

## Parameters

- `$value` (*mixed*): The configured default after dynamic data has resolved, or `null` when no default is configured. Numeric and date ranges receive a two-item endpoint array. Geolocation receives an associative coordinate array when its default-location toggle is enabled.
- `$context` (*array*): The filter identity, resolved settings, and original page context.

| Context key | Value |
| --- | --- |
| `filter_id` | Physical filter element ID. |
| `definition_id` | Linked global filter ID, or an empty string for an independent filter. |
| `query_id` | Rendered target query ID, including an instance suffix where applicable. |
| `filter_type` | Element name, such as `filter-radio` or `filter-geolocation`. |
| `filter_action` | `filter`, `sort`, or `per_page`. |
| `settings` | Effective element settings, including shared global-filter settings. |
| `post_id` | Original page, product, or preview post ID. Zero for archive contexts. |
| `queried_object` | Original WordPress queried object, or the builder preview object. |

## Return values

Return `$value` to keep the configured default or `null` to disable it. The hook can supply a default even when no builder default is configured.

| Filter | Return format |
| --- | --- |
| Radio, single Select, Search, sort, or results per page | A scalar value. Choice values must match a configured option, such as `cotton`, `title_ASC`, or `20`. |
| Checkbox or multiple Select | An array of exact option values, such as `['cotton', 'wool']`. |
| Range | Two numeric endpoints, such as `[20, 100]`. Use `''` for an endpoint that should use the original range boundary. |
| Single Datepicker | A date string in `YYYY-MM-DD` format. |
| Datepicker range | Two dates in `YYYY-MM-DD` format, with both endpoints present. |
| Geolocation | An array with `lat` and `lng`, plus optional `label`, `radius`, and `unit` (`km` or `mi`). Omitted radius and unit use the filter settings. |

Returned values undergo the same validation as builder defaults. Return resolved values rather than dynamic data expressions. Invalid or unavailable choices, invalid coordinates, and invalid range endpoints are ignored and produce builder-preview warnings. Geolocation still requires at least one enabled visitor search method, and its origin is normalized to `default`.

## Example: Select one material from the current product

This example selects the product's material with the lowest term ID. It applies only to a Radio or single Select filter using the `pa_material` taxonomy on a single product page.

```php
add_filter( 'bricks/query_filters/default_value', function( $value, $context ) {
    $settings = $context['settings'];

    if ( ! in_array( $context['filter_type'], [ 'filter-radio', 'filter-select' ], true ) ||
        $context['filter_action'] !== 'filter' ||
        ( $settings['filterSource'] ?? '' ) !== 'taxonomy' ||
        ( $settings['filterTaxonomy'] ?? '' ) !== 'pa_material' ||
        ( ! empty( $settings['choicesJs'] ) && ! empty( $settings['enableMultiple'] ) ) ||
        ! $context['post_id'] ||
        get_post_type( $context['post_id'] ) !== 'product' ) {
        return $value;
    }

    $slugs = wp_get_post_terms( $context['post_id'], 'pa_material', [
        'fields'  => 'slugs',
        'orderby' => 'term_id',
        'order'   => 'ASC',
    ] );

    return is_wp_error( $slugs ) || ! $slugs ? null : $slugs[0];
}, 10, 2 );
```

`post_id` refers to the original product even when the filter lives in a template. For an independent filter, check `filter_id` to limit the callback to one element. For linked desktop and mobile copies, check `definition_id` to address the shared filter.

## Initialization and state

The hook runs once per rendered query/filter group during initialization, including groups without a configured default. Linked elements targeting the same query share one evaluation. Reusing a definition on another query creates a separate evaluation. Resolved defaults are request-local and do not overwrite the saved settings or expressions.

A recognized filter URL restores the complete selection across URL-enabled queries on the page. Omitted filters remain clear, and an explicit empty parameter also suppresses defaults. Queries with URL parameters disabled still apply defaults.

Defaults apply before the first query, including Submit-based filters. Reset clears defaults while respecting exclusions. AJAX updates, pagination, Load more, and history restoration do not reapply them. A fresh visit or reload without filter parameters applies defaults again. See [default state behavior](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#default-state).