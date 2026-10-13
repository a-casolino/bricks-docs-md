# Action: bricks_after_header

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-after_header/

*Runs after Bricks renders the header template.*

Runs after Bricks renders the header template. Use it for output or setup that should happen directly after the site header.

## Example usage

```php
add_action( 'bricks_after_header', function() {
    echo '<div class="after-header-banner">Announcement</div>';
} );
```
