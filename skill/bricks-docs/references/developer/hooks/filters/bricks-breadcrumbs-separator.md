# Filter: bricks/breadcrumbs/separator

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-breadcrumbs-separator/

*Filters the separator HTML displayed between items in the Breadcrumbs element.*

Filters the separator HTML displayed between items in the Breadcrumbs element.

## Parameters

- `$separator` (*string*): The HTML string for the breadcrumb separator (e.g., a span containing text or an icon).

## Example usage

```php
add_filter( 'bricks/breadcrumbs/separator', function( $separator ) {
    // Change separator to a custom character
    return '<span class="bricks-breadcrumbs-separator"> &raquo; </span>';
} );
```
