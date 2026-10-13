# Filter: bricks/breadcrumbs/home_label

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-breadcrumbs-home_label/

*Filters the label text used for the \"Home\" link in the Breadcrumbs element.*

Filters the label text used for the "Home" link in the Breadcrumbs element.

## Parameters

- `$home_label` (*string*): The home label text (may include HTML if an icon is used).

## Example usage

```php
add_filter( 'bricks/breadcrumbs/home_label', function( $home_label ) {
    return 'Start';
} );
```
