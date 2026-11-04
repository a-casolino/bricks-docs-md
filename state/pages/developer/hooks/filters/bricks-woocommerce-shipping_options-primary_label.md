*Customize the primary label of each rate in the WooCommerce Shipping options element.*

Use `bricks/woocommerce/shipping_options/primary_label` to customize the primary label of each shipping rate rendered by the **Shipping options** element in [Checkout v2](https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-v2/#shipping-option-labels).

> **Note**
>
> Available since Bricks 2.4.5. Shipping options requires **Bricks > Settings > WooCommerce > Enable advanced modular elements**.

## Parameters

- `$label` (string): The resolved primary label HTML. This is the method name for an ordinary rate, or the complete customized label supplied through `woocommerce_cart_shipping_method_full_label` when it contains usable content.
- `$method` (`WC_Shipping_Rate`): The calculated shipping rate being rendered.
- `$element` (`Bricks\Woocommerce_Shipping_Options`): The Shipping options element instance.

## Return value and behavior

Return a string containing the primary label text or HTML. Bricks sanitizes the returned HTML with `wp_kses_post()` and displays it using the element's **Label** styles.

The filter runs after WooCommerce's full-label customization, once per rendered rate. If the returned value is empty, whitespace-only, or contains no usable content after sanitization, Bricks retains the resolved primary label. An image with meaningful `alt` text counts as usable content.

This filter does not change the secondary label, calculated shipping charge, or selected rate. Use [`bricks/woocommerce/shipping_options/secondary_label`](https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-shipping_options-secondary_label/) to customize the secondary label separately.

## Example: Add a pickup instruction

Add this callback to a child theme's `functions.php` or a custom plugin. Replace `local_pickup` with the method ID you want to target.

```php
add_filter( 'bricks/woocommerce/shipping_options/primary_label', function( $label, $method, $element ) {
    if ( $method->get_method_id() !== 'local_pickup' ) {
        return $label;
    }

    return $label . ' <small>' . esc_html__( 'Bring your order confirmation.', 'your-textdomain' ) . '</small>';
}, 10, 3 );
```

Returning the original `$label` for other methods preserves their existing names and any customized full labels.