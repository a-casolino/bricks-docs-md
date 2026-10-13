# Action: bricks_before_footer

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-before_footer/

*Runs before Bricks renders the footer template.*

Runs before Bricks renders the footer template. Use it to output markup or run logic immediately before footer rendering.

## Example usage

```php
add_action( 'bricks_before_footer', function() {
    echo '<div class="before-footer-cta">Need help?</div>';
} );
```
