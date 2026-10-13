# Action: bricks_before_header

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-before_header/

*Runs before Bricks renders the header template.*

Runs before Bricks renders the header template. Use it to output markup or run logic immediately before header rendering.

## Example usage

```php
add_action( 'bricks_before_header', function() {
    echo '<div class="top-strip">Free shipping this week</div>';
} );
```
