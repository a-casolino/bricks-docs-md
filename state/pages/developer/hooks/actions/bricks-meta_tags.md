*Runs in the document head before wp_head().*

Runs in the document head before `wp_head()`. Use it to output meta tags that should be controlled through the Bricks header template flow.

## Example usage

```php
add_action( 'bricks_meta_tags', function() {
    echo '<meta name="theme-color" content="#111111">';
} );
```