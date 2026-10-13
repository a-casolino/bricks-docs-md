# Filter: bricks/user_activation_email/from_name

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-user_activation_email-from_name/

*Filters the sender name for Bricks user activation emails.*

Filters the sender name for Bricks user activation emails.

## Parameters

- `$from_name` (string): The email sender name.
- `$user_id` (int): The user ID receiving the activation email.

## Example usage

```php
add_filter( 'bricks/user_activation_email/from_name', function( $from_name, $user_id ) {
    return get_bloginfo( 'name' );
}, 10, 2 );
```
