*Runs before Bricks loads element classes.*

Runs before Bricks loads element classes. Use it to prepare integration state before element labels, controls, or classes are initialized.

## Example usage

```php
add_action( 'bricks/load_elements/before', function() {
    // Prepare state before Bricks loads element classes.
} );
```