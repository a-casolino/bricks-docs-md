# Filter: bricks/footer/attributes

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-footer-attributes/

*Programmatically add HTML attributes to the footer tag.*

Programmatically add HTML attributes to the `footer` tag.

```php
add_filter( 'bricks/footer/attributes', function( $attributes ) {
  // Add 'data-is-footer' HTML attribute to footer with value 'y'
  $attributes['data-is-footer'] = 'y';

  return $attributes;
} );
```

- [/developer/hooks/filters/filter-bricks-header-attributes/](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-header-attributes/)
- [/developer/hooks/filters/filter-bricks-content-attributes/](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-content-attributes/)
