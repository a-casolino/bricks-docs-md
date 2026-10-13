# Filter: bricks/content/attributes

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-content-attributes/

*Programmatically add HTML attributes to the main tag.*

Programmatically add HTML attributes to the `main` tag.

```php
add_filter( 'bricks/content/attributes', function( $attributes ) {
  // Add 'data-is-content' HTML attribute to main with value 'y'
  $attributes['data-is-content'] = 'y';
  return $attributes;
} );
```

- [/developer/hooks/filters/filter-bricks-header-attributes/](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-header-attributes/)
- [/developer/hooks/filters/filter-bricks-header-attributes/](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-header-attributes/)
