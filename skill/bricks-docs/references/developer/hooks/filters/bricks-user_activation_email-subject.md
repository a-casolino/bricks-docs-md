# Filter: bricks/user_activation_email/subject

Source: https://academy.bricksbuilder.io/developer/hooks/filters/bricks-user_activation_email-subject/

*Filters the subject for Bricks user activation emails.*

Filters the subject for Bricks user activation emails.

## Parameters

- `$subject` (string): The email subject.
- `$user_id` (int): The user ID receiving the activation email.

## Example usage

```php
add_filter( 'bricks/user_activation_email/subject', function( $subject, $user_id ) {
    return '[Site access] Activate your account';
}, 10, 2 );
```
