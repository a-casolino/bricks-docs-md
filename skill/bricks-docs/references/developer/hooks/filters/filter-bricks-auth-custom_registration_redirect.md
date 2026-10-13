# Filter: bricks/auth/custom_registration_redirect

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-auth-custom_registration_redirect/

*This filter allows for the customization of the redirect page ID for the registration page.*

This filter allows for the customization of the redirect page ID for the registration page.

## Example Usage:

```php
add_filter( 'bricks/auth/custom_registration_redirect', function( $selected_registration_page_id ) {
    return /* New registration page ID */;
});
```

**Parameters:**

- `$selected_registration_page_id` (int|false): The ID of the custom registration page if set; otherwise, `false`.

**Return:**

- (int|false): The custom page ID for registration redirection, or `false` if no custom page is set.
