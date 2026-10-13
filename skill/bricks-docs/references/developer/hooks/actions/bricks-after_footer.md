# Action: bricks_after_footer

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-after_footer/

*Runs after Bricks renders the footer and before the site wrapper closes.*

Runs after Bricks renders the footer and before the site wrapper closes. Use it when custom output needs to appear immediately after the footer template.

## Example usage

```php
add_action( 'bricks_after_footer', function() {
    echo '<div class="after-footer-note">Footer add-on output</div>';
} );
```
