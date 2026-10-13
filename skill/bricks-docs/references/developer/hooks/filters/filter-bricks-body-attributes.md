# Filter: bricks/body/attributes

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-body-attributes/

*Filter the HTML attributes Bricks adds to the body tag on the frontend.*

Filter to add HTML attributes to the `body` tag (@since 1.5).

```php
add_filter( 'bricks/body/attributes', function( $attributes ) {
  // Add 'data-is-body' HTML attribute to footer with value 'y'
  $attributes['data-is-body'] = 'y';

  return $attributes;
} );
```
