*Customize or remove the secondary label of each rate in the WooCommerce Shipping options element.*

Use `bricks/woocommerce/shipping_options/secondary_label` to customize the secondary label of each shipping rate rendered by the **Shipping options** element in [Checkout v2](https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-v2/#shipping-option-labels).

> **Note**
>
> Available since Bricks 2.4.5. Shipping options requires **Bricks > Settings > WooCommerce > Enable advanced modular elements**.

## Parameters

- `$label` (string): The resolved secondary label HTML. For an ordinary rate, this is the formatted price, including any applicable tax indication, or **Free**. It is an empty string when a customized WooCommerce full label supplies the primary label.
- `$method` (`WC_Shipping_Rate`): The calculated shipping rate being rendered.
- `$element` (`Bricks\Woocommerce_Shipping_Options`): The Shipping options element instance.

## Return value and behavior

Return a string containing the secondary label text or HTML. Bricks sanitizes the returned HTML with `wp_kses_post()` and displays it using the element's **Secondary label** styles.

The filter runs once per rendered rate, after the primary label filter. It can add secondary content even when the incoming `$label` is empty. Return `''` to omit the secondary label and its `aria-describedby` link from the shipping input.

This filter changes presentation only. It does not change the calculated shipping charge, selected rate, or primary label. Use [`bricks/woocommerce/shipping_options/primary_label`](https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-shipping_options-primary_label/) to customize the primary label separately.

## Example: Add a collection instruction

Add this callback to a child theme's `functions.php` or a custom plugin. It adds an instruction to local pickup while retaining any existing price or **Free** label.

```php
add_filter( 'bricks/woocommerce/shipping_options/secondary_label', function( $label, $method, $element ) {
    if ( $method->get_method_id() !== 'local_pickup' ) {
        return $label;
    }

    $instruction = '<small>' . esc_html__( 'Collect during store opening hours.', 'your-textdomain' ) . '</small>';

    return $label !== '' ? $label . ' ' . $instruction : $instruction;
}, 10, 3 );
```

When a plugin provides a customized full label, that label remains in the primary position and the collection instruction appears as the secondary label.