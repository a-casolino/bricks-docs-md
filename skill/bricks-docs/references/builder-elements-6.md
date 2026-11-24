# Mini cart

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/mini-cart/

*Displays a mini cart icon with cart count and dropdown cart details.*

Displays a mini cart icon with cart count and dropdown cart details.

## Settings

- **Icon** (icon) - Cart icon. Default: ti-shopping-cart.
- **Icon typography** (typography) - Typography for cart icon. Only available when Icon is set.
- **Open on add to cart (AJAX)** (checkbox) - Open mini cart when products are added via AJAX.

### Hide an empty cart (since 2.5)

Enable **Hide if empty** to hide the entire Mini cart element on the frontend when the cart has no products. It remains visible in the Builder so you can edit it. This is separate from **Cart count > Visibility**, which only controls the count badge. The element updates after AJAX cart changes.

### Cart count

- **Visibility** (select) - Show/hide cart count. Options: Hide (Always), Show (Always). Default: Hide if empty.
- **Background color** (color) - Cart count background color. Only available when Visibility is not Hide (Always).
- **Border** (border) - Cart count border settings. Only available when Visibility is not Hide (Always).
- **Typography** (typography) - Cart count typography. Only available when Visibility is not Hide (Always).
- **Transform** (transform) - Cart count transform. Only available when Visibility is not Hide (Always) and Off-Canvas is not Top or Bottom.
- **Height** (number with units) - Cart count height. Only available when Visibility is not Hide (Always).
- **Width** (number with units) - Cart count width. Only available when Visibility is not Hide (Always).
- **Top** (number with units) - Cart count top position. Only available when Visibility is not Hide (Always).
- **Right** (number with units) - Cart count right position. Only available when Visibility is not Hide (Always).
- **Bottom** (number with units) - Cart count bottom position. Only available when Visibility is not Hide (Always).
- **Left** (number with units) - Cart count left position. Only available when Visibility is not Hide (Always).

### Cart subtotal

- **Position** (select) - Subtotal position. Options: Right, Left.
- **Gap** (number with units) - Gap between icon and subtotal. Only available when Position is set.
- **Typography** (typography) - Subtotal typography. Only available when Position is set.

### Custom empty cart template (since 2.5)

To show a custom empty state in the cart details instead:

1. Create and publish a **Section** template containing the empty-cart message or layout.
2. Select the Mini cart and open **Content > Cart details**.
3. Leave **Hide** off and select the Section under **Empty cart template**.
4. Enable **Preview empty state** to inspect the template in the Builder. This preview setting does not change the visitor's cart.
5. Save and test the frontend with an empty cart, then add and remove a product.

Leave **Hide if empty** off if visitors should be able to open this empty state. An unpublished, empty, or non-Section template cannot be used. Avoid placing the Mini cart inside the same Section template selected as its empty state.

<div className="screenshot screenshot--control-panel">

![Mini cart controls with Hide if empty off, an Empty cart template selected, and Preview empty state enabled.](https://academy.bricksbuilder.io/assets/builder/release-2.5/mini-cart-empty-panel.webp)

</div>

The selected Section replaces the default empty-cart message:

![An empty Mini cart displays a custom message and an Explore the collection button.](https://academy.bricksbuilder.io/assets/builder/release-2.5/mini-cart-empty-result.webp)

### Cart details

- **Hide** (checkbox) - Hide cart details dropdown.
- **Don't close on click outside mini cart** (checkbox) - Prevent auto-close on outside clicks. Only available when Hide is not checked.
- **Off-Canvas** (select) - Off-canvas position. Options: Top, Right, Bottom, Left. Only available when Hide is not checked.
- **Height** (number with units) - Cart details height. Only available when Hide is not checked and Off-Canvas is not Top or Bottom.
- **Width** (number with units) - Cart details width. Default: 400px. Only available when Hide is not checked and Off-Canvas is not Top or Bottom.
- **Image width** (number with units) - Product image width. Default: 60px. Only available when Hide is not checked.
- **Padding** (spacing) - Cart details padding. Only available when Hide is not checked.
- **Position** (dimensions) - Cart details position. Only available when Hide is not checked and Off-Canvas is Disabled.
- **Transform** (transform) - Cart details transform. Only available when Hide is not checked and Off-Canvas is not Top or Bottom.
- **Background** (color) - Cart details background color. Only available when Hide is not checked.
- **Border** (border) - Cart details border settings. Only available when Hide is not checked.
- **Box shadow** (box-shadow) - Cart details box shadow. Only available when Hide is not checked.
- **Typography (Title)** (typography) - Title typography. Only available when Hide is not checked.
- **Typography (Quantity)** (typography) - Quantity typography. Only available when Hide is not checked.

#### Buttons

- **Background color** (color) - Button background color. Only available when Hide is not checked.
- **Border** (border) - Button border settings. Only available when Hide is not checked.
- **Typography** (typography) - Button typography. Only available when Hide is not checked.

#### Close

- **Icon** (icon) - Close icon. Only available when Hide is not checked.
- **Typography** (typography) - Close typography. Only available when Hide is not checked and Icon is set. Excludes: font-family, font-weight, font-style, text-align, text-decoration, text-transform, line-height, letter-spacing.
- **Position** (dimensions) - Close position. Only available when Hide is not checked and Icon is set.
- **Padding** (spacing) - Close padding. Only available when Hide is not checked and Icon is set.
- **Background color** (color) - Close background color. Only available when Hide is not checked and Icon is set.
- **Border** (border) - Close border settings. Only available when Hide is not checked and Icon is set.

---

# Notice

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/notice/

*Displays WooCommerce system notices (success, info, and error messages).*

Displays WooCommerce system notices (success, info, and error messages).

## Where this element works

Shop/archive templates and WooCommerce pages where the related data exists.

## Key settings

- **Preview notice type** (select)

## Usage tips

- Keep notice styles highly readable so customers can quickly understand errors and confirmation messages.
- Check all notice types (success, info, error) in real cart and checkout scenarios.

Since Bricks 2.5, use a Notice element in a non-AJAX popup with the [Coupon error interaction](https://academy.bricksbuilder.io/builder/features/interactions/#coupon-error) to show the returned coupon error. Follow the [WooCommerce Notice setup](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-notices/#woocommerce-notice-element) before placing the element.

---

# Products archive description

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/products-archive-description/

*Displays the description for WooCommerce product archives (shop page, categories, tags).*

Displays the description for WooCommerce product archives (shop page, categories, tags).

---

# Products pagination

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/products-pagination/

*Displays pagination for WooCommerce product listings.*

Displays pagination for WooCommerce product listings.

## Settings

- **Alignment** (align-items) - Pagination alignment.
- **Previous Icon** (icon) - Icon for previous page link.
- **Next Icon** (icon) - Icon for next page link.
- **End Size** (number) - How many numbers on either the start and the end list edges. Minimum: 1.
- **Mid Size** (number) - How many numbers to either side of the current page. Minimum: 1.

---

# Products filter

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/products-filter/

*Displays product filters for WooCommerce product listings.*

Displays product filters for WooCommerce product listings.

## Settings

- **Filters** (repeater) - Product filter configurations.
  - **Filter type** (select) - Type of filter. Options: Taxonomy, Product attribute, Other.
  - **Filter by** (select) - Specific filter to apply (depends on type).
  - **Filter input** (select) - Input type. Options: Dropdown, Checkbox, Radio list, Text list, Box list.
  - **Any option text** (text) - Text for "any" option. Default: "Any".
  - **Only parent terms** (checkbox) - Show only parent terms.
  - **Show empty terms** (checkbox) - Include terms with no products.
  - **Filter title** (text) - Title for the filter.
  - **Hide title** (checkbox) - Hide filter title.
  - **Collapse** (checkbox) - Make filter collapsible.
- **Spacing** (number) - Gap between filters. Default: 30px.

### Title
- **Margin** (spacing) - Title margin. Default: 0 0 15px 0.
- **Padding** (spacing) - Title padding.
- **Typography** (typography) - Title typography.
- **Background color** (color) - Title background color.

---

# Products orderby

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/products-orderby/

*Displays a dropdown to sort WooCommerce products.*

Displays a dropdown to sort WooCommerce products.

## Settings

- **Order by** (select) - Available sorting options. Multiple selection. Leave empty to use WooCommerce default list.

---

# Products total results

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/products-total-results/

*Displays the total number of products found and current result range.*

Displays the total number of products found and current result range.

---

# Products

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/products/

*Displays WooCommerce products in a grid layout with customizable fields and widgets.*

Displays WooCommerce products in a grid layout with customizable fields and widgets.

## Settings

- **Columns** (number) - Number of columns. Range: 1-6. Default: 4. Supports breakpoints.
- **Gap** (number) - Spacing between products. Default: 30px.

### Query
- Product query controls (via Woocommerce_Helpers::get_product_query_controls).

### Fields
- **Content** (repeater) - Dynamic data fields to display. Default includes WooCommerce hooks and product fields like title, image, price, add to cart.
- **Link entire product** (checkbox) - Make entire product clickable if no field links exist.

### Widgets
- **Show Before Grid** (select) - Widgets to show before products grid. Options: Pagination, Result Count, Order by. Multiple selection.
- **Show After Grid** (select) - Widgets to show after products grid. Options: Pagination, Result Count, Order by. Multiple selection.
- **Sort by options** (select) - Available sorting options. Default: Default sorting. Multiple selection.

---

# WooCommerce Template Hook

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/template-hook/

*Renders output from a selected WooCommerce template hook so you can place WooCommerce hook content in your layout.*

Renders output from a selected WooCommerce template hook so you can place WooCommerce hook content in your layout.

## Where this element works

Any WooCommerce template where the selected hook is executed.

## Key settings

- **Template** (select)
- **Hook** (select)
- **Show tips** (checkbox)

## Usage tips

- Pick hooks intentionally and avoid duplicating WooCommerce default output in the same area.
- If expected content does not appear, confirm the selected hook runs in the current template context.
