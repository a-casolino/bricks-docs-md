# WooCommerce Builder

Source: https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-builder/

*Understand how Bricks works with WooCommerce templates, advanced modular elements, and dynamic product data across shop flows.*

WooCommerce is a free plugin to manage the e-commerce functionality of your WordPress site. It is the world's most popular open-source solution to create and manage a shop on the Internet, and therefore Bricks proudly integrates with it.

Bricks introduces the new in-theme WooCommerce Builder, which allows you to build your entire store with it. Including the main shop page, single product page, products archives, cart, checkout, and account pages.

To design these layouts, Bricks offers WooCommerce-specific elements and template types.

Starting in Bricks 2.4, Cart, Checkout, and My Account can also use the [advanced modular workflow](https://academy.bricksbuilder.io/integrations/woocommerce/advanced-modular-elements/). This workflow lets you edit multiple WooCommerce page states directly on the assigned WooCommerce page with Cart v2, Checkout v2, and Account Page v2.

Use the [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) to review the current WooCommerce setup and create or repair classic and v2 WooCommerce layouts from guided presets.

Certain elements only show when editing a specific template type.

The `Checkout customer details` element, for example, is only available when editing the `WooCommerce Checkout` template.

## Getting Started {#start}

To access the WooCommerce Builder in Bricks, install and activate the free WooCommerce plugin available in the official [WordPress repository](https://wordpress.org/plugins/woocommerce/) or through your WordPress dashboard under `Plugins → Add New`.

After activation, you might want to set up the store using the in-site configuration wizard or do it manually through the WooCommerce settings menus.

Please note that during the configuration wizard, you won't need to pick up a new theme because Bricks is already a theme and fully supports WooCommerce.

With the configuration done and after adding some products, you can start visually building your WooCommerce layouts with Bricks.

## WooCommerce Templates {#templates}

With WooCommerce activated, you can visually create and style the following WooCommerce templates in Bricks:

> **Note**
>
> These template types are the classic WooCommerce Builder workflow. If advanced modular elements are enabled, Cart, Checkout, and My Account can instead be set up with v2 elements directly on their assigned WooCommerce pages.

Use the [WooCommerce advanced modular elements](https://academy.bricksbuilder.io/integrations/woocommerce/advanced-modular-elements/) workflow when you want Cart, Checkout, and My Account states in one editable page instead of separate templates. The classic template workflow remains supported for existing stores and for projects that prefer separate template parts.

| **Template Type** | **Description** |
| --- | --- |
| **Single product** | Individual product page. |
| **Product archive** | Archive pages like product categories, tags, attributes, etc. Set visibility via Template Conditions. |
| **Cart** | The cart (when it contains products). |
| **Empty cart** | The empty cart (when it doesn't contain any products). |
| **Checkout** | Checkout screen where the customer enters billing & shipping details and selects the payment method. |
| **Pay** | Checkout screen where the customer enters the payment details. |
| **Thank you** | Displayed after successful checkout completion. |
| **Order receipt** | Displayed when viewing the order receipt. |
| **Account login** | Displayed when viewing the My Account page not logged in. |
| **Account lost password** | Displayed when viewing the lost password My Account page. |
| **Account lost password (confirmation)** | Displayed after submitting the lost password form. |
| **Account reset password** | Displayed after clicking the link in the password reset email. |
| **Account dashboard** | Displayed when viewing the My account page logged in. |
| **Account orders** | Displayed when viewing the "Orders" tab of the My Account page. |
| **Account view order** | Displayed when viewing an individual order. |
| **Account downloads** | Displayed when viewing the "Downloads" tab of the My Account page. |
| **Account payment methods** | Displayed when viewing saved payment methods. |
| **Account add payment method** | Displayed when adding a new payment method. |
| **Account addresses** | Displayed when viewing the "Addresses" tab of the My Account page. |
| **Account edit address** | Displayed when editing the billing or shipping address on the My Account page. |
| **Account edit account** | Displayed when editing the account details on the My Account page. |

## My Account builder

Starting at Bricks 1.9, you can also visually design your Account page. Including the login/registration, lost & reset password pages.

For account-specific template behavior, see [WooCommerce Account Builder](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-account-builder/).

## Shop page {#shop-page}

The shop page is a special WooCommerce page which is defined as the archive page for your products.

To design a unique Shop page layout, you can directly edit the Shop page with Bricks.

Or you could add a template condition in your `WooCommerce - Product Archive` template so this template is used for the Shop page as well. Since shop page is the archive for the product post type, just set it like this.

![](https://academy.bricksbuilder.io/assets/shop-page-woocommerce-product-archive-condition.png)

## WooCommerce elements {#elements}

Bricks aims to provide the most flexible approach to the visual design of the WooCommerce templates without losing the functionality & hooks WooCommerce already provides that many third-party WooCommerce plugins/extensions rely upon.

Among the general WooCommerce elements and Products element, Bricks has special elements for specific WooCommerce template types like the cart or the checkout.

More than 30 WooCommerce-specific elements in total are available to design your WooCommerce templates & pages with Bricks.

![](https://academy.bricksbuilder.io/assets/bricks-woocommerce-elements.gif)

These are some of the WooCommerce-specific elements:

- Add to cart
- Product title
- Product gallery
- Product price
- Product stock
- Product meta
- Product rating
- Product reviews
- Product content
- Product short description
- Product additional information
- Product tabs
- Product up/cross-sells
- Related products

## Dynamic Data {#dynamic-data}

The WooCommerce integration adds new [dynamic data tags](https://academy.bricksbuilder.io/builder/dynamic-content/dynamic-data/#:~:text=Bricks%201.4%20introduces,support%20double%20quotes) to target product and [order properties](https://academy.bricksbuilder.io/integrations/woocommerce/checkout/#order-receipt-template).

Bricks 2.4 also adds v2 WooCommerce tags for cart totals, checkout steps, WooCommerce URLs, account addresses, order data, downloads, and customer notes. See the full [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/) reference.

`{woo_product_price}` - Returns the full product price with currency and HTML

`{woo_product_regular_price}` - Returns the product regular price with currency and HTML

`{woo_product_sale_price}` - Returns the product sale price with currency and HTML. If no sale price set, empty string will be returned.

`{woo_product_regular_price:plain}` - Returns product regular price with currency without HTML

`{woo_product_regular_price:value}` - Returns product regular price as simple string (e.g: 65.3, 2.5, 5)

`{woo_product_cat_image}` - Renders the product category image

`{woo_product_images}` - Renders the product featured image and product gallery images. Can use on Carousel and Image gallery element. You can also use `:value` filter to output the gallery images IDs in comma separated format. (@since 1.11)

`{woo_product_gallery_images}` - Renders the product gallery images (excluded the product featured image). Can use on Carousel and Image gallery element. You can also use `:value` filter to output the gallery images IDs in comma separated format. (@since 1.11)

`{woo_add_to_cart}` - Renders the add to cart button

`{woo_product_on_sale}` - Renders the on-sale badge if the product is on sale

`{woo_product_rating}` - Renders the product rating

`{woo_product_rating:plain}` - Outputs the product rating in text form. Ex: Rated 5.00 out of 5

`{woo_product_rating:format}` - Outputs the product rating even if no rating has been submitted yet

`{woo_product_sku}` - Returns the product SKU. Can be used on single product pages and inside a custom Cart Contents loop. Cart Contents loop support was added in Bricks 2.4.

`{woo_product_gtin}` - Returns the product GTIN (Global Trade Item Number) from the WooCommerce global unique ID field. Can be used on single product pages and inside a custom Cart Contents loop. By default, the value is wrapped in a `span.gtin`; append the `:value` filter to output the plain text value. (@since 2.4)

> **Note**
>
> GTIN is not shown in the Product meta element. Use the `{woo_product_gtin}` dynamic tag directly where you want to output it.

`{woo_product_gtin}` - Returns the product GTIN when supported by the installed WooCommerce version

`{woo_product_excerpt}` - Renders the product short description

`{woo_product_stock}` - Renders the product stock (append `value` filter outputs number of products in stock)

`{woo_product_stock_status}` - Outputs `instock`, `outofstock`, or `onbackorder` (Useful for element conditions)

`{woo_product_badge_new}` - Renders "New" span with classes `.badge.new` if condition met. (@since 1.11.1) (Bricks Settings > WooCommerce > Products.)

`{woo_product_badge_new:plain}` - Renders "New" text only if condition met. (@since 1.11.1) (Bricks Settings > WooCommerce > Products.)

`{woo_product_type}` - Returns the WooCommerce product type.

Inside a [Cart Contents query loop](https://academy.bricksbuilder.io/integrations/woocommerce/cart/#loop), you can also use cart-specific tags:

`{woo_cart_product_name}` - Renders the linked cart product name with its legacy combined metadata output.

`{woo_cart_product_title}` - Renders the product title without cart item metadata. Use it with the **Cart item data** element when the title and variation details need separate styling. (@since 2.4)

`{woo_cart_item_price}` - Renders the formatted unit price, including regular and current sale-price markup when discounted. Append `:value` for the unformatted current unit price. (@since 2.4)

`{woo_cart_item_save}` - Renders the formatted product savings for the full cart item quantity. Append `:value` for the unformatted amount or `:percentage` for the numeric discount percentage. (@since 2.4)

`{woo_cart_remove_link}` - Renders the cart item remove link.

`{woo_cart_quantity}` - Renders the cart quantity input.

`{woo_cart_subtotal}` - Renders the cart item subtotal.

`{woo_cart_update}` - Renders the update cart button.

On checkout thank you and order receipt templates, Bricks also supports order tags:

`{woo_order_id}` - Returns the order ID.

`{woo_order_number}` - Returns the order number.

`{woo_order_date}` - Returns the order date.

`{woo_order_total}` - Returns the order total.

`{woo_order_payment_title}` - Returns the order payment method.

`{woo_order_email}` - Returns the order email.

`{woo_order_failed_text}` - Returns the failed-order message. Requires advanced modular elements. See [Failed-order text](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/#failed-order-text).

You can use the basic dynamic tags as well.

`{post_id}` - Outputs the product ID

`{post_title:link}` - Renders the product title with link

`{post_terms_product_cat}` - Renders the product categories with links

`{post_terms_product_cat:plain}` - Renders the product categories without links)

### WooCommerce v2 dynamic data

When advanced modular elements are enabled, Bricks adds WooCommerce dynamic tags for:

- Cart totals, applied coupons, applied fees, taxes, shipping totals, and free shipping progress.
- Checkout step data and WooCommerce page/endpoint URLs.
- Account addresses and account edit-address state data.
- Order details, order items, order totals, order actions, downloads, and customer notes.

Most of these tags depend on a v2 page state or query loop context. For example, `{woo_order_item_title}` belongs inside a `wooOrderItems` loop, while `{woo_cart_applied_coupon}` belongs inside a `wooCartCoupons` loop.

## Bricks Settings: WooCommerce

You'll find a dedicated tab for the WooCommerce integration in your WordPress dashboard under "Bricks > Settings > WooCommerce".

![](https://academy.bricksbuilder.io/assets/woo-settings-1.11.png)

- **Disable WooCommerce Builder** - This toggle disables the Bricks' WooCommerce integration.
- **Enable Bricks WooCommerce "Notice" element** - Removes native WooCommerce notice output so you can place the Notice element manually.
- **Enable Bricks WooCommerce "Checkout coupon" element** - Removes the native checkout coupon form and lets you place the Checkout Coupon element manually. WooCommerce **Enable the use of coupon codes** must be active under **WooCommerce > Settings > General**.
- **Enable Bricks WooCommerce "Checkout login" element** - Removes the native checkout login form and lets you place the Checkout Login element manually. WooCommerce **Enable log-in during checkout** must be active under **WooCommerce > Settings > Accounts & Privacy**.
- **Show quantity input field in product loop** - Shows quantity inputs for purchasable simple products that are in stock.
- **Enable product variation swatches** - Converts variation dropdowns to color, image, or label swatches on the Add to cart element.
- **Product Badge "Sale"** - Choose between not showing the on-sale badge, showing the "Sale" badge, or the discount percentage.
- **Product Badge "New"** - Show a "New" badge if the product was published in less than the .. days configured.
- **Disable Product Gallery Zoom/Lightbox** - Disable the product gallery zoom or lightbox scripts.

![](https://academy.bricksbuilder.io/assets/ajax-add-to-cart-error-action-setting.png)

- **Enable AJAX add to cart** - Enables Bricks' AJAX add to cart behavior for purchasable, in-stock simple products and product variations in product loops when they support `ajax_add_to_cart`.
- **AJAX add to cart texts and notices** - Customize the adding/added button text, reset delay, "View cart" button visibility, notice output, and scroll-to-notice behavior.
- **AJAX add to cart Error action** - Select either "Redirect to product page" or "Show notice" when an error occurs during the AJAX add to cart process. You can also scroll to the notice when "Show notice" is selected. (@since 1.11)

## Theme Styles {#theme-styles}

When WooCommerce is active, you'll find the following control groups in the Theme Styles panel:

- WooCommerce - Button
- WooCommerce - Notice

## WooCommerce Products Query Loop {#query}

![](https://academy.bricksbuilder.io/assets/new-woocommerce-product-queries.png)

You can use these checkboxes under WooCommerce section to easily retrieve WooCommerce products. Please select the "Products" post type; otherwise, the WooCommerce section will be hidden. (`@since 1.10`)

Check [this article](https://academy.bricksbuilder.io/builder/dynamic-content/query-loop/#woocommerce) for more examples.

Bricks 2.4 adds v2 WooCommerce query loops for cart coupons, fees, taxes, orders, order items, downloads, customer notes, account orders, account order actions, account downloads, and account addresses. See [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/#query-loops) for the complete list.

---

# WooCommerce Notices

Source: https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-notices/

*Style WooCommerce notices in Bricks and control how success, error, and info messages appear across storefront flows.*

New theme style settings under "WooCommerce - Notice" and a new "WooCommerce Notice" element were introduced in Bricks `1.8.1`. Allowing you to elevate the appearance of WooCommerce (WC) notices across your website.

With this new theme style, you can effortlessly customize the design of WC notices, ensuring they blend seamlessly with your website's overall look and feel.

This article explains how to enable the Bricks WooCommerce Notice element, where to place it, and how it replaces native WooCommerce notice output.

## Theme Style: WooCommerce - Notice {#woocommerce-notice-theme-style}

You can find the "WooCommerce - Notice" settings in the builder under Settings > [Theme Styles](https://academy.bricksbuilder.io/builder/styling/theme-styles/).

There are three different types of notice: Error, Success, and default Notice.

![](https://academy.bricksbuilder.io/assets/wc-notice-theme-style.png)

With the WC notice theme style, you can effortlessly align your notice styles with your brand guidelines, and achieve a uniform and professional appearance for your notices.

## Element: WooCommerce Notice {#woocommerce-notice-element}

One of the primary objectives of this new feature is to offer you greater control over the placement of WC notices within their website's design.

Native WC notices often pose challenges, as they may appear outside of the desired design or wrapper, impacting the aesthetics and user experience.

To start using the Bricks WooCommerce notice element you first have to enable it under `Bricks > Settings > WooCommerce > Enable Bricks WooCommerce "Notice" element`.

![](https://academy.bricksbuilder.io/assets/bricks-wc-notice-element.png)

> **Note**
>
> Once enabled all native WC notices are automatically removed from your website. So you can & have to manually place the notice element in your desired template & location.

![](https://academy.bricksbuilder.io/assets/bricks-wc-notice-preview.png)

<figcaption>

WC notice element. Not only theme style but can also style individual elements as well.

</figcaption>

**The following Bricks templates should be equipped with the Notice element:**

- WooCommerce Product Archive
- WooCommerce Single Product
- WooCommerce Cart
- WooCommerce Empty Cart
- WooCommerce Checkout
- WooCommerce Pay
- WooCommerce My account login
- WooCommerce My account lost password
- WooCommerce My account reset password

In addition to the Bricks templates mentioned above, several pages within your WooCommerce website require the Notice element **if they are edited and rendered using Bricks**. These pages include:

- My Account page (if the WC notice is not placed in the My account login template)
- Checkout page (if the WC notice is not placed in the Checkout template)
- Pay / order-pay page (if the WC notice element is not placed in the Pay template)
- Cart page (if the WC notice element is not placed in the Cart template)
- Shop page (if the WC notice element is not placed in the Product Archive template)

**Only one Notice element is needed per page.**

If you happen to add multiple WC notice elements, only the first one will output the actual notices, following the native WooCommerce behavior. WooCommerce clears notices after the 1st output. Check WooCommerce `wc_print_notices()` for more information.

---

# WooCommerce Template Hooks

Source: https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-template-hooks/

*Use WooCommerce template hooks in Bricks to preserve third-party plugin output and place additional content in key storefront locations.*

Bricks 1.7 introduces a new [`do_action`](https://academy.bricksbuilder.io/builder/dynamic-content/dynamic-data/#do_action) dynamic tag, which is designed to address the majority of compatibility issues between Bricks and third-party WooCommerce plugins. This new dynamic tag not only solves these compatibility issues but also enhances the flexibility of design by allowing users to place hooks anywhere they desire.

This article will guide you through the templates that need to be updated with the new `do_action` dynamic tag, though this step is optional if your Bricks-built WooCommerce website is already functioning properly.

Please note that when using the `do_action` dynamic tag with the specified hooks, Bricks will automatically remove certain native WooCommerce actions to prevent duplicate content.

As an example, consider using `{do_action:woocommerce_after_shop_loop_item_title}` dynamic tag in Bricks. This tag will automatically remove the `woocommerce_template_loop_rating` and `woocommerce_template_loop_price` actions. The reason for this is because the Product price and Product rating elements will be used to output the information in the desired location. At the same time, other plugins or codes will still be able to successfully hook onto the dynamic tag.

#### WooCommerce actions list removed by Bricks when using the do_action tag {#woo-special-actions-list}

| Hook | Actions removed by Bricks, Priority |
| --- | --- |
| woocommerce_before_shop_loop_item | woocommerce_template_loop_product_link_open, 10 |
| woocommerce_before_shop_loop_item_title | woocommerce_show_product_loop_sale_flash, 10<br />woocommerce_template_loop_product_thumbnail, 10 |
| woocommerce_shop_loop_item_title | woocommerce_template_loop_product_title,10 |
| woocommerce_after_shop_loop_item_title | woocommerce_template_loop_rating, 5<br />woocommerce_template_loop_price, 10 |
| woocommerce_after_shop_loop_item | woocommerce_template_loop_product_link_close, 5<br />woocommerce_template_loop_add_to_cart, 10 |
| woocommerce_before_single_product_summary | woocommerce_show_product_sale_flash, 10<br />woocommerce_show_product_images, 20 |
| woocommerce_single_product_summary | woocommerce_template_single_title, 5<br />woocommerce_template_single_rating, 10<br />woocommerce_template_single_price, 10<br />woocommerce_template_single_excerpt, 20<br />woocommerce_template_single_add_to_cart, 30<br />woocommerce_template_single_meta, 40<br />woocommerce_template_single_sharing, 50 |
| woocommerce_after_single_product_summary | woocommerce_output_product_data_tabs, 10<br />woocommerce_upsell_display, 15<br />woocommerce_output_related_products, 20 |
| woocommerce_before_main_content | woocommerce_output_content_wrapper,10<br />woocommerce_breadcrumb, 20 |
| woocommerce_archive_description | woocommerce_taxonomy_archive_description, 10<br />woocommerce_product_archive_description, 10 |
| woocommerce_before_shop_loop | woocommerce_result_count, 20<br />woocommerce_catalog_ordering, 30 |
| woocommerce_after_shop_loop | woocommerce_pagination, 10 |
| woocommerce_after_main_content | woocommerce_output_content_wrapper_end, 10 |
| woocommerce_cart_is_empty | wc_empty_cart_message, 10 |

> **Note**
>
> Simply use a Basic Text element when applying the `{do_action:xxx}` dynamic tag within your template.

## WooCommerce Single Product Template Hooks {#single-product-template-hooks}

For the WooCommerce Single Product template, the following hooks are recommended to be used with the `do_action` dynamic tag:

- `{do_action:woocommerce_before_single_product}` - Important (WooCommerce notice)
- `{do_action:woocommerce_before_single_product_summary}`
- `{do_action:woocommerce_single_product_summary}` - Important (Many third-party plugins using this hook to inject their code)
- `{do_action:woocommerce_after_single_product_summary}`
- `{do_action:woocommerce_after_single_product}`

Best to place all of these in your single product template if you are not sure which hook will be using by the third-party plugins.

![](https://academy.bricksbuilder.io/assets/bricks-standard-woocommerce-single-product-template-hooks.png)

<figcaption>

Single product template hooks location

</figcaption>

## WooCommerce Product Archive Template Hooks {#product-archive-template-hooks}

For the WooCommerce Product Archive template, the following hooks are recommended to be used with the `do_action` dynamic tag:

- `{do_action:woocommerce_archive_description}`
- `{do_action:woocommerce_before_shop_loop}` - Important (WooCommerce notice)
- `{do_action:woocommerce_before_shop_loop_item}`
- `{do_action:woocommerce_before_shop_loop_item_title}`
- `{do_action:woocommerce_shop_loop_item_title}`
- `{do_action:woocommerce_after_shop_loop_item_title}`
- `{do_action:woocommerce_after_shop_loop_item}`
- `{do_action:woocommerce_after_shop_loop}`

![](https://academy.bricksbuilder.io/assets/bricks-standard-woocommerce-product-archive-template-hooks.png)

<figcaption>

Product archive template hooks location (Custom Query Loop)

</figcaption>

In Bricks 1.7, the dynamic tag `do_action` hooks will be automatically included in the fields of the Products element (for newly inserted Products elements only).

![](https://academy.bricksbuilder.io/assets/Products-element-with-do_action-included-since-1_6_3.png)

<figcaption>

Default Products element with do_action hooks (Bricks 1.7+)

</figcaption>

## WooCommerce Empty Cart Template Hooks {#empty-cart-template-hooks}

For the WooCommerce Empty Cart template, the following hook is recommended to be used with the `do_action` dynamic tag:

- `{do_action:woocommerce_cart_is_empty}` - Important (WooCommerce notice)

![](https://academy.bricksbuilder.io/assets/bricks-standard-woocommerce-empty-cart-template-hooks.png)

<figcaption>

Empty cart template hook location

</figcaption>

## WooCommerce Cart Template Hooks {#cart-template-hooks}

For the WooCommerce Cart template, the following hooks are recommended to be used with the `do_action` dynamic tag:

- `{do_action:woocommerce_before_cart}` - Important (WooCommerce notice)
- `{do_action:woocommerce_before_cart_collaterals}`
- `{do_action:woocommerce_after_cart}`

![](https://academy.bricksbuilder.io/assets/bricks-standard-woocommerce-cart-template-hooks.png)

<figcaption>

Cart template hooks location

</figcaption>

## WooCommerce Pay Template {#pay-template-hooks}

For the WooCommerce Pay template, the following hooks are recommended to be used with the `do_action` dynamic tag:

- `{do_action:woocommerce_pay_order_before_payment}`

![](https://academy.bricksbuilder.io/assets/woo-pay-template.png)

<figcaption>

Pay template hooks location

</figcaption>

By following this guide, you can ensure that the templates created in Bricks are fully compatible with WooCommerce and that all necessary actions and details are displayed as intended.

---

# WooCommerce v2 query loops and dynamic tags

Source: https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/

*Use the WooCommerce v2 query loops, dynamic data tags, conditions, and interactions added for advanced modular WooCommerce layouts in Bricks 2.4.*

Bricks 2.4 adds WooCommerce-specific query loops and dynamic tags for advanced modular Cart, Checkout, and My Account layouts.

Use them when you build with [WooCommerce advanced modular elements](https://academy.bricksbuilder.io/integrations/woocommerce/advanced-modular-elements/), or when you need a custom cart-dependent layout such as a mini cart inside the [Dynamic fragment element](https://academy.bricksbuilder.io/builder/elements/woocommerce/dynamic-fragment/).

> **Note**
>
> Advanced v2 query loops and dynamic tags require **Bricks > Settings > WooCommerce > Enable advanced modular elements**. The existing **Cart contents** query loop remains available for the classic cart workflow.

## Query loops

Use these query loop types from the **Query type** control. `wooCart` is the existing Cart contents loop. The other query types are added for advanced modular layouts and only appear when advanced modular elements are enabled.

![](https://academy.bricksbuilder.io/assets/woo-v2-query-loop-types.png)

| Query type               | Builder label              | Use it for                                                                 |
| ------------------------ | -------------------------- | -------------------------------------------------------------------------- |
| `wooCart`                | Cart contents              | Visible cart line items. Use for cart rows and custom mini cart item rows. |
| `wooCartCoupons`         | Checkout : Applied coupons | Applied cart coupons.                                                      |
| `wooCartFees`            | Checkout : Applied fees    | Cart fees.                                                                 |
| `wooCartTaxes`           | Checkout : Applied taxes   | Cart tax rows.                                                             |
| `wooOrderItems`          | Order : Order items        | Line items from the current order context.                                 |
| `wooOrderTotals`         | Order : Order totals       | Order total rows from the current order context.                           |
| `wooOrderDownloads`      | Order : Order downloads    | Downloadable items from the current order context.                         |
| `wooOrderCustomerNotes`  | Order : Customer notes     | Customer notes from the current order context.                             |
| `wooAccountOrders`       | Account : Orders           | Customer orders in the Account orders state.                               |
| `wooAccountOrderActions` | Account : Order actions    | Available actions for the current order inside a `wooAccountOrders` loop.  |
| `wooAccountDownloads`    | Account : Downloads        | Downloads available to the current account.                                |
| `wooAccountAddresses`    | Account : Addresses        | Billing and shipping address rows in the Account addresses state.          |

Order loops use the current order context. That context exists in Checkout v2 pay, thank-you, and order receipt states, in Account v2 view-order states, and inside order-aware account loops.

> **Note**
>
> Order-related query loops are compatible with WooCommerce HPOS because they use WooCommerce order APIs and `WC_Order` objects. If you add custom code around these loops, use WooCommerce CRUD functions such as `wc_get_orders()` and `wc_get_order()` instead of direct `shop_order` post or postmeta queries.

## Cart tags

Use these tags inside the `wooCart` query loop:

- `{woo_cart_product_name}` - Cart item product name, including WooCommerce cart item metadata.
- `{woo_cart_product_title}` - Product title without variation attributes or other cart item metadata. Add `:plain` to remove the product link.
- `{woo_cart_item_price}` - Formatted unit price. A discounted item includes the regular price and current price using WooCommerce sale-price markup. Add `:value` for the unformatted current unit price.
- `{woo_cart_item_save}` - Formatted product savings for the full line item quantity. Add `:value` for the unformatted savings amount or `:percentage` for the numeric discount percentage without a percent symbol.
- `{woo_cart_remove_link}` - Remove link markup. Use `{woo_cart_remove_link:url}` when you only need the remove URL.
- `{woo_cart_quantity}` - Quantity input. Use `{woo_cart_quantity:value}` for the numeric quantity.
- `{woo_cart_subtotal}` - Cart line subtotal.

You can also use product tags inside the `wooCart` loop, such as `{featured_image}`, `{woo_product_price}`, `{woo_product_sku}`, and `{woo_product_gtin}`.

Use `{woo_cart_product_title}` when the product title and item details need separate elements or styling. The existing `{woo_cart_product_name}` remains available for layouts that rely on its combined output, including item metadata, backorder notices, and WooCommerce cart item hooks.

`{woo_cart_item_price}` uses the current cart item product or variation and follows the store's cart tax display setting. `{woo_cart_item_save}` compares that unit price with the regular price, then multiplies the monetary savings by the cart item quantity.

> **Note**
>
> Cart item savings only cover a product's regular-price reduction. Coupon discounts, fees, shipping, and other cart or order-level adjustments are not included. The savings tags return no value when the product has no regular price or the current price is not lower.

## Cart item data element

Add the **Cart item data** element inside a **Cart contents** query loop to render variation attributes and item data separately from the product title.

The element includes variation attributes even when their values appear in the variation name. It also includes compatible data added through WooCommerce's `woocommerce_get_item_data` filter and preserves safe formatted display values supplied by extensions.

Use these controls to design the output:

- **Show labels** and **Label suffix**. The default suffix is `:`.
- **Show separators** and **Separator**. The default separator is `/`.
- **Layout** controls for direction, wrapping, alignment, justification, and row and column gaps.
- **Item** controls for direction, alignment, gap, padding, background, border, and box shadow.
- **Label** and **Value** controls for width, flex grow and shrink, spacing, background, border, box shadow, and typography.
- **Separator** typography and margin.

The element renders nothing on the frontend when used outside a Cart contents loop or when the current item has no item data.

## Cart totals and checkout tags

These tags can be used in cart, checkout, and cart-dependent fragments without being inside the `wooCart` loop:

- `{woo_cart_items_count}`
- `{woo_cart_order_subtotal}`
- `{woo_cart_order_total}`
- `{woo_cart_applied_coupon_total_amount}`
- `{woo_cart_applied_fee_total_amount}`
- `{woo_cart_shipping_method}`
- `{woo_cart_shipping_total_amount}`
- `{woo_free_shipping_min_amount}`
- `{woo_free_shipping_remaining}`
- `{woo_free_shipping_progress}`
- `{woo_checkout_current_step_number}`
- `{woo_url}`

Some tags support `:value` to return a plain number instead of formatted WooCommerce HTML, such as `{woo_cart_shipping_total_amount:value}` and `{woo_free_shipping_progress:value}`.

## Coupon, fee, and tax tags

| Query loop       | Tags                                                            |
| ---------------- | --------------------------------------------------------------- |
| `wooCartCoupons` | `{woo_cart_applied_coupon}`, `{woo_cart_applied_coupon_amount}` |
| `wooCartFees`    | `{woo_cart_applied_fee}`, `{woo_cart_applied_fee_amount}`       |
| `wooCartTaxes`   | `{woo_cart_applied_tax_label}`, `{woo_cart_applied_tax_amount}` |

Use the total tags outside the loop when you only need a combined value:

- `{woo_cart_applied_coupon_total_amount}`
- `{woo_cart_applied_fee_total_amount}`

## WooCommerce URL tag

Use `{woo_url}` to output common WooCommerce page and endpoint URLs. Without a key, it returns the shop URL.

| Tag                                               | Returns                                    |
| ------------------------------------------------- | ------------------------------------------ |
| `{woo_url}` or `{woo_url:shop}`                   | Shop page URL                              |
| `{woo_url:cart}`                                  | Cart page URL                              |
| `{woo_url:checkout}`                              | Checkout page URL                          |
| `{woo_url:account}` or `{woo_url:myaccount}`      | My Account page URL                        |
| `{woo_url:dashboard}`                             | My Account dashboard endpoint URL          |
| `{woo_url:orders}`                                | My Account orders endpoint URL             |
| `{woo_url:downloads}`                             | My Account downloads endpoint URL          |
| `{woo_url:addresses}` or `{woo_url:edit-address}` | My Account edit-address endpoint URL       |
| `{woo_url:edit-account}`                          | My Account edit-account endpoint URL       |
| `{woo_url:payment-methods}`                       | My Account payment methods endpoint URL    |
| `{woo_url:add-payment-method}`                    | My Account add payment method endpoint URL |
| `{woo_url:lost-password}`                         | My Account lost password endpoint URL      |
| `{woo_url:order-withdrawal}`                       | Order Withdrawal endpoint URL, when enabled |
| `{woo_url:customer-logout}`                       | My Account logout endpoint URL             |
| `{woo_url:terms}`                                 | WooCommerce terms and conditions page URL  |
| `{woo_url:privacy}`                               | WooCommerce privacy policy page URL        |

Registered WooCommerce account endpoint query vars can also be resolved by key. This only returns a URL; it does not add custom Account v2 states.

## Account tags

Use these tags in Account v2 states.

| Context                          | Tags                                                                                                                                                                                              |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account addresses state          | `{woo_account_addresses_description}`                                                                                                                                                             |
| `wooAccountAddresses` query loop | `{woo_account_address_type}`, `{woo_account_address_title}`, `{woo_account_address}`, `{woo_account_address_has_address}`, `{woo_account_address_edit_url}`, `{woo_account_address_action_label}` |
| Account edit-address state       | `{woo_account_edit_address_title}`, `{woo_account_edit_address_type}`, `{woo_account_edit_address_type_label}`                                                                                    |

### Order withdrawal tags

These Bricks 2.4 tags require advanced modular elements and WooCommerce 11.1 or later with **Order Withdrawal** enabled. Use them inside the [Account Page v2 Order withdrawal state](https://academy.bricksbuilder.io/builder/elements/woocommerce/account-page-v2/#order-withdrawal).

| Tag | Output |
| --- | --- |
| `{woo_order_withdrawal_screen}` | Current screen: `form`, `review`, or `confirmation`. Empty in the builder. |
| `{woo_order_withdrawal_value:first_name}` | Submitted first name. |
| `{woo_order_withdrawal_value:last_name}` | Submitted last name. |
| `{woo_order_withdrawal_value:email}` | Submitted email address. |
| `{woo_order_withdrawal_value:email_confirmation}` | Submitted email confirmation. |
| `{woo_order_withdrawal_value:order_number}` | Submitted order number. |
| `{woo_order_withdrawal_value:withdrawal_type}` | Submitted withdrawal type key, such as `full_order` or `specific_items_only`. |
| `{woo_order_withdrawal_value:withdrawal_type_label}` | Withdrawal type label, such as **Entire order** or **Specific items only**. |
| `{woo_order_withdrawal_value:additional_details}` | Submitted additional details, with line breaks preserved in text output. Displays **None provided** when empty. |

The value tags display sample data in the builder and submitted form values on the frontend. They do not retrieve data from a matching WooCommerce order or create an order context for order tags and query loops. Outside the withdrawal state's frontend rendering, these tags return no value.

## Order tags

Use these tags in Checkout v2 order states, Account v2 order states, or order-aware query loops.

![](https://academy.bricksbuilder.io/assets/woo-v2-order-awareness-tags.png)

General order tags:

- `{woo_order_id}`
- `{woo_order_number}`
- `{woo_order_date}`
- `{woo_order_status}`
- `{woo_order_failed_text}` - Failed-order message. See [Failed-order text](#failed-order-text) for filtering and preview behavior.
- `{woo_order_total}`
- `{woo_order_payment_title}`
- `{woo_order_email}`
- `{woo_order_checkout_payment_url}`
- `{woo_order_again_url}`
- `{woo_order_user_id}`
- `{woo_order_billing_address}`
- `{woo_order_billing_phone}`
- `{woo_order_shipping_address}`
- `{woo_order_shipping_phone}`
- `{woo_order_view_url}`
- `{woo_order_view_aria_label}`
- `{woo_order_item_count}`
- `{woo_order_total_with_item_count}`

Use these inside `wooOrderItems`:

- `{woo_order_item_name}`
- `{woo_order_item_title}` - Product title without variation metadata. Add `:plain` to remove the product link.
- `{woo_order_item_quantity}`
- `{woo_order_item_price}`
- `{woo_order_item_line_subtotal}`
- `{woo_order_item_meta}`

Use `{woo_order_item_title}` with the **Order item data** element when the title and persisted order metadata need separate styling. If the original product has been deleted, the title tag falls back to the item name stored with the order.

Add the **Order item data** element inside an **Order : Order items** query loop. It renders persisted variation and other formatted order item metadata in Checkout v2 Pay, Thank you, and Order receipt states, the Account v2 View order state, and an Order items loop nested inside **Account : Orders**.

The Cart item data and Order item data elements have the same controls, but they use different data sources. Cart item data comes from the active cart. Order item data comes from the saved order item and runs WooCommerce's formatted metadata filters.

> **Note**
>
> Use `{woo_order_item_meta}` when an extension depends on WooCommerce's complete order-item metadata output or its start, end, and display hooks. The structured **Order item data** element does not run arbitrary complete-output hooks because their markup cannot be split reliably across the element's Label and Value controls.

For custom CSS, the elements use separate class prefixes:

| Output    | Cart item data                   | Order item data                   |
| --------- | -------------------------------- | --------------------------------- |
| Root      | `.brx-cart-item-data`            | `.brx-order-item-data`            |
| Item      | `.brx-cart-item-data__item`      | `.brx-order-item-data__item`      |
| Label     | `.brx-cart-item-data__label`     | `.brx-order-item-data__label`     |
| Value     | `.brx-cart-item-data__value`     | `.brx-order-item-data__value`     |
| Separator | `.brx-cart-item-data__separator` | `.brx-order-item-data__separator` |

Each item also receives a metadata-key modifier class, such as `.brx-cart-item-data__item--color`, and a matching `data-key` attribute.

Use these inside `wooOrderTotals`:

- `{woo_order_total_label}`
- `{woo_order_total_value}`

Use these inside `wooAccountOrderActions`, usually inside a `wooAccountOrders` loop:

- `{woo_order_action_url}`
- `{woo_order_action_name}`
- `{woo_order_action_aria_label}`

Use these inside `wooOrderDownloads` or `wooAccountDownloads`:

- `{woo_order_download_product}`
- `{woo_order_download_name}`
- `{woo_order_download_url}`
- `{woo_order_downloads_remaining}`
- `{woo_order_download_access_expires}`

Use these inside `wooOrderCustomerNotes`:

- `{woo_order_customer_note_date}`
- `{woo_order_customer_note_comment}`

### Failed-order text

Use `{woo_order_failed_text}` for the payment failure message in a Checkout v2 **Thank you** state. On the frontend, it returns a message only for a current order with the **Failed** status. It returns no value for other statuses or when no order is available.

The message uses WooCommerce's `woocommerce_thankyou_order_failed_text` filter, which receives the message and current `WC_Order`. Bricks sanitizes HTML with `wp_kses_post()` and restores the default localized message for non-string filter results.

In the builder, a failed preview order shows the filtered message. Without a failed preview order, Bricks shows the default message without calling the filter.

See [Failed-order messages](https://academy.bricksbuilder.io/integrations/woocommerce/checkout/#failed-order-messages) to update a saved Checkout v2 layout.

## Conditions

Bricks 2.4 adds WooCommerce conditions for checkout and order-aware layouts:

- **Checkout : Login step needed**
- **Checkout : Needs shipping**
- **Checkout : Needs shipping address**
- **Checkout : Order has status**
- **Order : Needs shipping address**
- **Order : Has downloads**

Use them to show or hide content inside checkout steps, thank-you/order receipt layouts, view-order screens, and other checkout or order-aware sections.

**Checkout : Login step needed** returns **Yes** only for logged-out customers when **Enable log-in during checkout** is enabled in WooCommerce. The generated [Checkout v2 multistep checkout](https://academy.bricksbuilder.io/integrations/woocommerce/multistep-checkout-v2/#account-login-step-visibility) uses this condition to hide its Account Login step and related navigation when that step is not available.

Use **Checkout : Needs shipping** for shipping methods and for a complete Shipping step. It returns **Yes** when the non-empty cart contains products that require shipping. In a multistep checkout, apply it to both the Shipping step and the matching navigation item.

Use **Checkout : Needs shipping address** for the **Ship to another address** control and the shipping-address fields. When WooCommerce is set to force shipping to the billing address, this condition returns **No** even if the cart still needs shipping.

See [Element Conditions](https://academy.bricksbuilder.io/builder/features/element-conditions/#woocommerce) for condition setup and comparison behavior.

Use **Order withdrawal screen** with **Your details**, **Review**, or **Confirmation** to show the matching section inside the Account Page v2 withdrawal state. It requires advanced modular elements and WooCommerce Order Withdrawal to be enabled. All three sections remain visible in the builder.

## Interactions

Bricks 2.4 adds these WooCommerce interaction triggers:

- **Bricks cart contents changed** - Runs after a confirmed AJAX item addition, removal, or quantity change and the related UI updates finish. It does not run for initial synchronization, unchanged quantities, failed updates, or coupon, address, shipping, and totals-only recalculations.
- **Bricks dynamic fragments refreshed** - Runs after Dynamic fragment content has been refreshed.
- **Bricks checkout step changed** - Runs after a Checkout v2 step changes.

**Bricks cart contents changed** is available whenever WooCommerce is active, including pages without Dynamic fragments. The other two triggers require advanced modular elements. For a custom cart confirmation popup, use [Bricks cart contents changed](https://academy.bricksbuilder.io/builder/features/interactions/#cart-contents-changed). A fragment refresh alone does not confirm that cart items changed.

The **Checkout step** interaction action can move a multistep checkout to the next step, previous step, a specific step, or a specific checkout field. It can also scroll the target step or field into view.

See [Checkout v2 multistep checkout](https://academy.bricksbuilder.io/integrations/woocommerce/multistep-checkout-v2/) for the full multistep workflow.

## JavaScript events

Developers can listen for the same frontend events:

```js
document.body.addEventListener(
  "bricks/woocommerce/cart-contents-changed",
  (event) => {
    console.log(event.detail.requestId, event.detail.sourceEvent);
  },
);

document.body.addEventListener(
  "bricks/woocommerce/fragments/refreshed",
  (event) => {
    console.log(event.detail.fragments);
  },
);

document.body.addEventListener(
  "bricks/woocommerce/checkout-step-changed",
  (event) => {
    console.log(event.detail.stepId);
  },
);
```

For `bricks/woocommerce/cart-contents-changed`, `requestId` identifies the confirmed request. `sourceEvent` contains the AJAX endpoint name, such as `bricks_update_cart_item_quantity`, or `update_cart` for a cart-page request. The event does not include cart item data.

### Coupon failure events

Bricks' custom coupon handlers emit these WooCommerce events when the response contains an error notice. Listen with `jQuery(document.body).on()`:

| Event | Bricks handler | Additional arguments |
| --- | --- | --- |
| `errored_coupon` | Cart Coupon with **Update cart via AJAX** enabled | Coupon code, raw returned notice HTML |
| `errored_coupon_in_checkout` | Checkout Coupon | Coupon code, raw returned notice HTML |

The existing `applied_coupon` and `applied_coupon_in_checkout` events also fire for error responses. They do not confirm that a coupon was accepted.
