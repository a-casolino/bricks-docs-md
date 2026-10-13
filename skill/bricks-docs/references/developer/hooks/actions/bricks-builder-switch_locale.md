# Action: bricks/builder/switch_locale

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-builder-switch_locale/

*Runs when Bricks switches the builder locale.*

Runs when Bricks switches the builder locale. Use it to synchronize integration state when the builder language changes.

## Parameters

- `$locale` (string): The locale Bricks is switching the builder to.

## Example usage

```php
add_action( 'bricks/builder/switch_locale', function( $locale ) {
    // Switch integration language context to match the builder.
}, 10, 1 );
```
