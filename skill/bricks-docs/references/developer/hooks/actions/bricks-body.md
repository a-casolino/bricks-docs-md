# Action: bricks_body

Source: https://academy.bricksbuilder.io/developer/hooks/actions/bricks-body/

*Runs after the document head closes. Bricks uses it to print the opening body tag and body-start output.*

Runs in `header.php` after the document head closes and before the site-wrapper and header hooks.

Bricks attaches its opening `<body>` tag callback to this hook at priority `1`. Default-priority callbacks run after the opening body tag and after Bricks has printed body-start scripts and skip links.

## Example usage

```php
add_action( 'bricks_body', function() {
    echo '<div id="body-integration-root"></div>';
} );
```
