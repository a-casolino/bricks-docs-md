# Filter: bricks/elements/nav_menu/menus

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-elements-nav_menu-menus/

*Filters the nav menus shown in the Nav Menu element while in the builder.*

Filters the nav menus shown in the Nav Menu element while in the builder. Return an array of menu objects to override the menus Bricks loads from WordPress.

## Parameters

- `$menus` (array|null): Menus to use in the builder. Return null to let Bricks fall back to wp_get_nav_menus().

## Example usage

```php
add_filter( 'bricks/elements/nav_menu/menus', function( $menus ) {
    return wp_get_nav_menus();
} );
```
