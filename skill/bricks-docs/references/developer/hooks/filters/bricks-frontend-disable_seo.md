# Filter: bricks/frontend/disable_seo

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-frontend-disable_seo/

*Determines whether Bricks should generate and output SEO meta tags (e.g., description, keywords, robots) and modify the document title. Use this to disable.*

Determines whether Bricks should generate and output SEO meta tags (e.g., description, keywords, robots) and modify the document title. Use this to disable Bricks' built-in SEO features if you are using a dedicated SEO plugin.

## Parameters

- `$disable` (*bool*): Whether to disable SEO tags.

## Example usage

```php
add_filter( 'bricks/frontend/disable_seo', function( $disable ) {
    // Example: Always disable Bricks SEO features
    return true;
} );
```
