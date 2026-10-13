*Runs in header.php before the header render action. Bricks uses it to open the builder wrapper.*

Runs in `header.php` after `bricks_body` and before `bricks_before_header`.

In the builder, Bricks uses this hook to open the `.brx-body` wrapper around the builder frame. On the frontend, it is a general position before the header render flow.

## Example usage

```php
add_action( 'bricks_before_site_wrapper', function() {
    echo '<div class="before-site-wrapper">';
} );
```