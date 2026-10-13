# Filter: bricks/builder/i18n

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-i18n/

*Place and customize the following filter to add translatable string to the builder.*

Place and customize the following filter to add translatable string to the builder.

```php
add_filter( 'bricks/builder/i18n', function( $i18n ) {
  // Example: Provide translatable string for element category 'custom'
  $i18n['custom'] = esc_html__( 'Custom', 'bricks' );

  return $i18n;
} );
```
