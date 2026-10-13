# Filter: bricks/comments/author_tag

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-comments-author_tag/

*Filters the HTML tag used to wrap the comment author's name in the comments list.*

Filters the HTML tag used to wrap the comment author's name in the comments list.

## Parameters

- `$tag` (*string*): The HTML tag name. Defaults to `h5`.

## Example usage

```php
add_filter( 'bricks/comments/author_tag', function( $tag ) {
    // Change author name tag to 'span'
    return 'span';
} );
```
