# Action: bricks/load_elements/after

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-load_elements-after/

*Runs after Bricks loads element classes.*

Runs after Bricks loads element classes. Use it to restore integration state after element labels, controls, or classes are initialized.

## Example usage

```php
add_action( 'bricks/load_elements/after', function() {
    // Restore state after Bricks loads element classes.
} );
```
