# Filter: bricks/dynamic_data/post_terms_separator

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-dynamic_data-post_terms_separator/

*Programmatically set the post term separator like so:*

Programmatically set the post term separator like so:

```php
add_filter( 'bricks/dynamic_data/post_terms_separator', function( $sep, $post, $taxonomy ) {
  return ' : ';
}, 10, 3 );
```
