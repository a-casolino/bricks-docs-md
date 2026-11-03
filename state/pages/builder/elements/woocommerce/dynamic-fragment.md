*Re-renders WooCommerce cart-dependent content after cart changes.*

Re-renders WooCommerce cart-dependent content after cart changes.

https://youtu.be/Q6wYRAvVN0Y

> **Note**
>
> This element requires **Bricks > Settings > WooCommerce > Enable advanced modular elements**.

## Where this element works

WooCommerce-aware Bricks layouts, such as page content, headers, and footers that need to update after cart changes.

## Key settings

- **Insert a structure** (select) - Choose a generated starter structure.
- **Generate** (button) - Adds the selected structure to the element.

## Generated structures

- **Mini cart**
- **Free shipping progress**

Generated structures are appended to the current content and do not overwrite existing content.

![](https://academy.bricksbuilder.io/assets/dynamic-fragment-states.png)

## Usage tips

- Use Dynamic fragment for cart-dependent content outside the main Cart page, such as a [custom mini cart](https://academy.bricksbuilder.io/integrations/woocommerce/create-custom-mini-cart-dynamic-fragment/), free shipping progress, or cart totals.
- Keep the fragment focused on content that needs to refresh after add-to-cart, remove-from-cart, or quantity changes.
- Keep the Dynamic fragment wrapper outside other query loops. A cart loop can be placed inside the fragment.

## Free shipping progress

The **Free shipping progress** structure adds a Progress Bar that shows how much more the cart needs for free shipping. Place the Dynamic fragment where shoppers see it on every page, for example a bar at the top of the header template, so it updates as products are added.

- **Minimum amount:** Bricks reads it from WooCommerce. It is the **Minimum order amount** of the **Free shipping** method in the shipping zone that matches the cart, with **Free shipping requires** set to a minimum order amount (alone or combined with a coupon). Change it in **WooCommerce > Settings > Shipping**, not in Bricks. If several free shipping methods match, Bricks uses the one with the smallest remaining amount.
- **Cart amount:** the cart subtotal minus coupon discounts, unless **Apply minimum order rule before coupon discount** is enabled on the free shipping method.
- **Label:** `Add {woo_free_shipping_remaining} more for free shipping`.
- **Value:** `{woo_free_shipping_progress:value}`, a number from 0 to 100 (the percentage of the minimum the cart has reached).
- **Conditions:** the bar only renders while a minimum exists (`{woo_free_shipping_min_amount:value}` is not 0) and the cart is below it (`{woo_free_shipping_progress:value}` is less than 100).

Once the cart reaches the minimum, the bar is hidden. The structure has no message for that state. To show one, add an element such as Basic Text inside the same Dynamic fragment and give it the condition **Dynamic data** `{woo_free_shipping_progress:value}` `==` `100`.

![Builder showing a Dynamic fragment in the header template with the generated Free shipping progress bar and a Basic Text "Your order ships free" with a condition that shows it when the free shipping progress equals 100.](https://academy.bricksbuilder.io/assets/dynamic-fragment-free-shipping-reached-condition.webp)

The Builder canvas previews a sample cart, so the bar can show "Add $0.00 more" and the conditions are not applied there. Check the real amounts on the frontend with products in the cart.

## Custom mini cart

For a mini cart, add a Dynamic fragment inside an Offcanvas in the header template and generate the **Mini cart** structure. A second Dynamic fragment in the header holds the cart icon and item count, so the count updates too. [Create a custom mini cart with Dynamic fragment](https://academy.bricksbuilder.io/integrations/woocommerce/create-custom-mini-cart-dynamic-fragment/) walks through the full setup, including the interactions that open the panel.

See [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/) for the cart tags you can use inside the fragment.

## Refresh behavior

Dynamic fragment refreshes after WooCommerce cart, coupon, and checkout events such as add to cart, remove from cart, cart emptied, cart totals updated, checkout updated, and coupon apply/remove events.

After a refresh, Bricks reruns frontend functions and dispatches:

```js
document.body.addEventListener('bricks/woocommerce/fragments/refreshed', (event) => {
  console.log(event.detail.fragments)
})
```

This refresh event also covers initial synchronization and checkout recalculations that do not change cart items. For a custom success notice or popup, use the [Bricks cart contents changed](https://academy.bricksbuilder.io/builder/features/interactions/#cart-contents-changed) interaction trigger, available since Bricks 2.4. It runs after a confirmed AJAX addition, removal, or quantity change and the related UI updates finish.

## Limitations

- Dynamic fragment is frontend-only.
- Do not place the Dynamic fragment wrapper inside a query loop.
- Component instances are not supported.
- The source area must be header, content, or footer.