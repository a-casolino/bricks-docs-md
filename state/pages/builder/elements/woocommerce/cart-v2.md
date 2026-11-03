*Displays the WooCommerce cart page as editable Filled cart and Empty cart states.*

Displays the WooCommerce cart page as editable Filled cart and Empty cart states.

> **Note**
>
> This element requires **Bricks > Settings > WooCommerce > Enable advanced modular elements**.

## Where this element works

Cart page. The element only appears in the Elements panel while you edit the page that WooCommerce uses as its cart page.

## Key settings

- **State** (radio) - Switches the builder preview between Filled cart and Empty cart.

## States

- **Filled cart** - Used when the cart contains products.
- **Empty cart** - Used when the cart has no products.

The generated Cart v2 structure keeps both states as internal child elements, so you can edit each state from the Structure panel. The top of the Structure panel shows the state you are editing. Click **Switch** there to change the previewed state.

![](https://academy.bricksbuilder.io/assets/cart-v2-states.png)

## Generated structures

Each state can generate starter content from **Insert a structure**:

- **Complete cart block**
- **Complete empty cart block**

Generated structures are appended to the current state content and do not overwrite existing content.

For a step-by-step setup, see [Cart v2 workflow](https://academy.bricksbuilder.io/integrations/woocommerce/cart/#cart-v2-workflow).

The complete cart block contains a cart loop with one row per product (image, title, price, excerpt, item data, Cart quantity and a remove icon), a cross-sells section, a free shipping progress bar, summary rows for subtotal, coupons, fees, taxes, shipping and total, a checkout button and the Cart coupon element.

> **Note**
>
> In Bricks 2.4.3 the complete cart block includes a WooCommerce Notice element, but generating it from **Insert a structure** does not enable that element. Enable **Bricks > Settings > WooCommerce > Enable Bricks WooCommerce "Notice" element** first, or the canvas shows that the element doesn't exist. The [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) enables it for you.

![](https://academy.bricksbuilder.io/assets/cart-v2-state-insert-structure.png)

> **Note**
>
> Cart v2 uses the Cart form and Cart quantity support elements inside the Filled cart state. If you cannot find a support element in the regular Elements panel, use **Insert a structure** and then edit the generated element in the Structure panel.

![](https://academy.bricksbuilder.io/assets/cart-v2-filled-cart-structure-example.png)

## Builder preview and frontend behavior

While you edit the Filled cart state, the builder previews a sample cart with sample notices. Loops without data, such as coupons or fees, show their dynamic tags on the canvas. Check the real values on the frontend.

On the frontend, the Cart quantity element updates the cart via AJAX (a quantity of zero removes the product), the Cart coupon element applies coupons via AJAX, and each applied coupon gets its own summary row with a remove icon.

The **Coupon total row** below the applied coupons shows the total of all coupons. If your store only allows one coupon at a time, it repeats the coupon amount, so you can delete it.

> **Note**
>
> In Bricks 2.4.3, lazy-loaded images in the Empty cart state stay blank when the last product is removed on the frontend, until the page is reloaded. If your empty state contains images, such as a Products element, disable lazy loading under **Bricks > Settings > Performance**.

## Query loops and dynamic data

Use the **Cart contents** query loop for custom cart item rows. Cart v2 layouts can also use cart total tags such as `{woo_cart_items_count}`, `{woo_cart_order_subtotal}`, `{woo_cart_order_total}`, `{woo_cart_shipping_method}`, `{woo_free_shipping_remaining}`, and `{woo_free_shipping_progress}`.

See [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/) for the complete reference.

## Usage tips

- Use [WooCommerce advanced modular elements](https://academy.bricksbuilder.io/integrations/woocommerce/advanced-modular-elements/) or the [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) to create the recommended Cart v2 structure.
- Design both states so the cart page is complete whether the customer has products in the cart or not.
- Use the classic [Cart template workflow](https://academy.bricksbuilder.io/integrations/woocommerce/cart/) if you prefer separate Cart and Empty Cart templates.