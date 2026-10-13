*Filters the content for Bricks user activation emails.*

Filters the content for Bricks user activation emails.

## Parameters

- `$content` (string): The email content.
- `$user_id` (int): The user ID receiving the activation email.

## Example usage

```php
add_filter( 'bricks/user_activation_email/content', function( $content, $user_id ) {
    return $content;
}, 10, 2 );
```