# Bricks Builder Documentation: Integrations

<!-- content-sha256: af81ea60feaca5efb7054baaaa5f5089c555fd12235b4d4e00f2009c03b8fc84 -->
<!-- content last changed: 2026-10-28 06:58 UTC -->

Unofficial Markdown export of the Bricks Builder Academy (https://academy.bricksbuilder.io/), refreshed daily. Content © Bricks. 28 pages.

## Table of contents

  - [Gutenberg](#integrations-gutenberg)
  - [How to set up your Google Maps API key](#integrations-how-to-set-up-your-google-maps-api-key)
  - [How to use WPML with Bricks](#integrations-how-to-use-wpml-with-bricks)
- [Integrations](#integrations)
  - [How to get your Instagram Access Token](#integrations-instagram-access-token)
  - [Map (Leaflet)](#integrations-map-leaflet)
  - [How to use Polylang with Bricks](#integrations-polylang)
  - [Unsplash Integration](#integrations-unsplash)
    - [Bricks components as blocks](#integrations-gutenberg-components-as-blocks)
    - [WooCommerce advanced modular elements](#integrations-woocommerce-advanced-modular-elements)
    - [Cart (WooCommerce)](#integrations-woocommerce-cart)
    - [Checkout (WooCommerce)](#integrations-woocommerce-checkout)
    - [Create a custom mini cart with Dynamic fragment](#integrations-woocommerce-create-custom-mini-cart-dynamic-fragment)
    - [Creating dynamic WooCommerce archive pages](#integrations-woocommerce-creating-dynamic-woocommerce-archive-pages)
    - [Element: Checkout Coupon](#integrations-woocommerce-element-checkout-coupon)
    - [Element: Checkout Login](#integrations-woocommerce-element-checkout-login)
    - [How to Create Product Quick View with Bricks](#integrations-woocommerce-how-to-create-product-quick-view-with-bricks)
  - [WooCommerce](#integrations-woocommerce)
    - [Checkout v2 multistep checkout](#integrations-woocommerce-multistep-checkout-v2)
    - [Product Archive (WooCommerce)](#integrations-woocommerce-product-archive-woocommerce)
    - [Product Variation Swatches (WooCommerce)](#integrations-woocommerce-product-variation-swatches)
    - [Single Product (WooCommerce)](#integrations-woocommerce-single-product)
    - [Woo Setup Wizard](#integrations-woocommerce-woo-setup-wizard)
    - [WooCommerce Account Builder](#integrations-woocommerce-woocommerce-account-builder)
    - [WooCommerce Template Hooks](#integrations-woocommerce-woocommerce-template-hooks)
    - [WooCommerce Builder](#integrations-woocommerce-woocommerce-builder)
    - [WooCommerce v2 query loops and dynamic tags](#integrations-woocommerce-woocommerce-v2-query-loops-dynamic-tags)
    - [WooCommerce Notices](#integrations-woocommerce-woocommerce-notices)

---

<a id="integrations-gutenberg"></a>

# Gutenberg

Source: https://academy.bricksbuilder.io/integrations/gutenberg/

*Understand how Bricks integrates with Gutenberg, including what each editor is responsible for and where the workflows can overlap.*

If you've created your pages with Gutenberg you can continue editing them with Bricks without having to start all over again. Bricks will convert your Gutenberg blocks into Bricks elements.

You can also save and convert your Bricks generated data to Gutenberg data to continue editing a page with Gutenberg.

This way you'll not suffer any lock-in effect when start using Bricks or if you should ever decide to move away from Bricks.

> **Note**
>
> The block conversion works only with standard WordPress Gutenberg blocks, NOT custom-third party blocks

## How to load Gutenberg data into Bricks

Bricks allows you to convert your existing Gutenberg data into Bricks data. So you can continue editing any page created with Gutenberg in Bricks.

This only works for pages without any existing Bricks data. To delete the Bricks data of any page, first enable **Enable "Delete Bricks data" button** under **Bricks > Settings > General > Miscellaneous**. Then click the "Delete Bricks data" button in the WordPress top menu when editing a page in WordPress.

To enable this functionality go to **Bricks > Settings > General > Block editor** and make sure **Load Block editor data into Bricks** is selected.

## How to save Bricks data for Gutenberg

By default, your WordPress-generated data won’t change when editing with Bricks. If you want to save your Bricks generated data as Block editor data as well go to **Bricks > Settings > General > Block editor** and select **Save Bricks data as Block editor data**.

From now on whenever you edit and save in Bricks, your content will be saved as WordPress content, too. So your WordPress and Bricks data are in sync.

## Render content with Bricks or WordPress {#render-with-wordpress}

You decide which pages you want to create with Gutenberg, the Classic Editor, or Bricks. The post status next to the page title tells you which content is used for rendering on the frontend:

![](https://academy.bricksbuilder.io/assets/wp-admin-pages-post-status-1024x576.png)

To change the data being used to render a page edit the page in WordPress and hover over the **Render with WordPress/Bricks** button in the top menu, and select the source you want to use:

![](https://academy.bricksbuilder.io/assets/wp-admin-edit-page-render-with-wordpress-bricks-1024x576.png)

<figcaption>

Render with Bricks / Render with WordPress

</figcaption>

---

<a id="integrations-how-to-set-up-your-google-maps-api-key"></a>

# How to set up your Google Maps API key

Source: https://academy.bricksbuilder.io/integrations/how-to-set-up-your-google-maps-api-key/

*Set up a Google Maps API key for Bricks and enable the services required for map elements and location features.*

Thanks to the `Map` element, adding a Google Map to Bricks is easy. The biggest hurdle is creating the Google Maps API key. This article will show you how to create an API key and how to prevent unauthorized use by setting API and application restrictions.

> **Note**
>
> Since [Bricks 1.10.2](https://bricksbuilder.io/release/bricks-1-10-2/), Google Maps can be used without an API key through the Embed API, which is very limited by Google. It only allows for one address, zoom level, and map type. For more options, you have to use an API key.

## Prerequisites

Before you start using the Maps JavaScript API, Google Cloud requires a project with a **billing account**, plus the **Maps JavaScript API** and **Geocoding API** enabled. Check out the [Google documentation](https://developers.google.com/maps/documentation/javascript/cloud-setup) for the current setup requirements.

As soon as you have completed the setup, you will find your API key under **Keys and Credentials » API Keys**.

![](https://academy.bricksbuilder.io/assets/Keys-and-credentials-%E2%80%93-Google-Maps-Platform-%E2%80%93-Bricks-%E2%80%93-Google-Clo.png)

Copy and paste the key into **Bricks » Settings » API keys » Google Maps: API key** and hit save.

![](https://academy.bricksbuilder.io/assets/Settings-%E2%80%B9-bricksRecent-%E2%80%94-WordPress.jpg)

Now, you can use the "Map" element on any page. If your map doesn’t show properly, inspect the developer console for more information.

## API and application restrictions

Google Cloud lets you restrict where and for which APIs the API key can be used to prevent unauthorized use.

![](https://academy.bricksbuilder.io/assets/Edit-API-key-%E2%80%93-APIs-and-services-%E2%80%93-Bricks-%E2%80%93-Google-Cloud-console-1024x617.jpg)

### Application restrictions

Since you're running a website, configure the key's application restriction for websites. Select "Websites" and add your URL by clicking the "Add" button. Here are some examples of URLs that Google Cloud can allow:

- Any URL in a single domain with no subdomains: https://example.com
- Any URL in a single subdomain: https://sub.example.com
- Any subdomain in a single domain, using a wildcard asterisk (*): https://*.example.com
- A domain and all its subdomains, using a wildcard asterisk (*):
https://example.com
https://*.example.com

### API Restrictions

**Restrict key** » Select APIs and allow the **Maps JavaScript API** and **Geocoding API**.

Save your API key settings.

## Common problems

If the map is not showing, open the developer console. You will receive further information and how to solve your specific issue there. In most cases, no billing account is assigned, the necessary APIs are not activated, or the restrictions are incorrect.

![](https://academy.bricksbuilder.io/assets/Screenshot-2023-12-05-13.33.02.jpg)

---

<a id="integrations-how-to-use-wpml-with-bricks"></a>

# How to use WPML with Bricks

Source: https://academy.bricksbuilder.io/integrations/how-to-use-wpml-with-bricks/

*Use WPML with Bricks to translate pages, templates, components, and other builder content on multilingual WordPress sites.*

WPML is a WordPress plugin known for its role in facilitating the creation of multilingual websites.

Coupling it with Bricks allows not only for the manual translation of posts, pages, and various content types into numerous languages but also offers automatic translation features, significantly broadening your website's reach and accessibility. Bricks' WPML integration has been available since 1.7, with component translation support added later.

Once you've established a page in your primary language with Bricks, WPML enables you to easily translate the content into any language you wish to add to your website, be it manually or automatically.

This documentation will guide you through the process of translating your Bricks website using WPML.

## Setting up the environment

Before translating, set up your environment with the necessary plugins:

1. **Bricks setup**:
  - This guide will illustrate the translation process using a simple Bricks website. This website has main pages like Home and Blog, and templates including a header and an "All Archives" template, which has a [template condition](https://academy.bricksbuilder.io/builder/features/template-settings/#template-conditions) to apply to all archives and the blog page.

1. **WPML plugin installation**:
  - You can use the [OTGS installer](https://wpml.org/version/otgs-installer-3-0-0/) to install the required **WPML Multilingual CMS **and** WPML String Translation** plugins.

![](https://academy.bricksbuilder.io/assets/bricks-wpml-3-1024x520.png)

1. **Language Configuration**:
  - You can configure your website's languages and other settings through [the WPML setup wizard](https://wpml.org/documentation/getting-started-guide/). During this process, WPML will also ask you for context about your website, such as what it’s about and whose it for.

![](https://academy.bricksbuilder.io/assets/Bricks-Translation-Context-1024x748.png)

Using the context that you provide, WPML’s AI translator – [PTC (Private Translation Cloud)](https://ptc.wpml.org/about/) will create translations that fit your target audience and industry.

## Translation options with WPML & Bricks

WPML offers different ways to translate your Bricks content:

1. **[Advanced Translation Editor](https://wpml.org/documentation/translating-your-contents/advanced-translation-editor/)**:
  - Automatic (AI) Translation: Instantly translate your content using WPML’s AI-based engine, then optionally review it before publishing.
  - Manual Translation: A method where each page & string is translated individually.
2. **[String Translation](https://wpml.org/documentation/getting-started-guide/string-translation/)**:
  - Translate theme/plugin strings, widget texts, and other interface strings found under WPML → String Translation.
3. **Edit with Bricks**:
  - If needed, post-translation modifications to design or layout can be done in the Bricks builder for each language.

For more in-depth information on each method, refer to the official [WPML documentation](https://wpml.org/documentation/).

## Translating website content

Translate your website content using WPML and Bricks through the following steps:

### Bulk translation via translation dashboard {#translation-dashboard}

WPML can translate any content you build with Bricks, including pages, posts, templates, and components.

To translate any Bricks content, start by going to **WPML **→ **Translation Dashboard**. From here, expand the section with the content you want to translate and select your items.

For example, to translate a page, expand the **Pages** section and select the page. This will include all Bricks element data and any component instance property values used on that page. To translate Bricks components themselves, expand the **Bricks components** section and select the components you want to translate.

![](https://academy.bricksbuilder.io/assets/Bricks-TD.png)

Next, select **Translate automatically** for the languages you want to translate into, and click the **Translate **button to begin. If you look under the table, WPML also shows you how much translating your content costs.

![](https://academy.bricksbuilder.io/assets/Bricks-TD-Step-2.png)

In most cases, your translations will be good to go, but you can always review and make changes using WPML’s **Advanced Translation Editor**.

![](https://academy.bricksbuilder.io/assets/Editing-translations-in-the-Advanced-Translation-Editor.png)

Just visit the translated page you want to edit on the front-end, and click **Edit translation **in the top admin bar. This will open the editor, where you can make any changes necessary.

Once you’re done reviewing, you can instantly publish your translations and display them on your website. Remember that you need to switch languages to view your translations.

### Translating individual pages and posts

While **Translation Management** is perfect for translating multiple pages and templates in one go, you may sometimes want to focus on a single page or post—either for fine-tuning the translation or making additional adjustments. In those cases, you can use the **WPML Advanced Translation Editor** directly from the page/post edit screen.
For comprehensive guidance on the various methods to translate pages and posts created by page builders like Bricks, refer to [WPML's official documentation](https://wpml.org/documentation/translating-your-contents/page-builders/) about this topic.

![](https://academy.bricksbuilder.io/assets/bricks-wpml-4-1024x518.png)

![](https://academy.bricksbuilder.io/assets/bricks-wpml-8-1024x516.png)

### Template translation: {#template-translation}

Translating templates follows the same process as translating WordPress pages & posts. Your template settings & type will be automatically duplicated to the translated post.

> **Note**
>
> If the translation of templates is not automatically enabled when you activate WPML, please [refer to the WPML documentation](https://wpml.org/documentation/support/language-configuration-files/#custom-types) on how to enable translation for custom post types, and ensure that it is enabled for “bricks_template”.

![](https://academy.bricksbuilder.io/assets/bricks-wpml-15-1024x296.png)

![](https://academy.bricksbuilder.io/assets/bricks-wpml-14.png)

### Example: Translating an archive template:

We have set up a simple archive template, which is applied to both the "Blog" page and its translated version, "Blogue".

![](https://academy.bricksbuilder.io/assets/bricks-wpml-17-1024x428.png)

![](https://academy.bricksbuilder.io/assets/bricks-wpml-19-564x1024.png)

Each blog page will only display blog posts of that particular language (using only one template):

![](https://academy.bricksbuilder.io/assets/bricks-wpml-18-1024x545.png)

![](https://academy.bricksbuilder.io/assets/bricks-wpml-25-1024x563.png)

## Language switcher & menu translation

### Language switcher

Bricks provides a “Language switcher” element for WPML, which you can add anywhere on your site.

By default, the language switcher comes with a basic preset design. However, you can always customize the switcher to match your website style:

1. Go to **WPML **→ **Languages**.
2. Scroll down to **Custom language switchers** and check the **Enable **box. This will reveal a **Customize **button.
3. Click the button to set your custom preferences and save.

Your changes will immediately take effect on your website.

![](https://academy.bricksbuilder.io/assets/bricks-wpml-7-1024x515.png)

![](https://academy.bricksbuilder.io/assets/Adding-language-swicther-in-Bricks.png)

![](https://academy.bricksbuilder.io/assets/Viewing-language-switcher-on-front-end.png)

### WPML menu translation:

Consult WPML documentation for guidance on [translating WordPress menus](https://wpml.org/documentation/getting-started-guide/translating-menus/).

## Sync Bricks data across translated pages {#sync-bricks-data}

After translating a page, you might want to modify the original page. Those changes you perform with Bricks in your original page are not applied to the secondary language pages.

But Bricks and WPML make it seamless to sync your design changes across translated pages without affecting the translated text. Here’s how you can do it:

### Step 1: Edit your original page with Bricks

Open the page in the primary language in the builder. Make the necessary design changes (edit layout, change styles, etc.)

### Step 2: Save your changes

Once done, save your changes.

### Step 3: Edit with WordPress

Close the builder by clicking "Edit with WordPress" to edit the page in WordPress.

![](https://academy.bricksbuilder.io/assets/bricks-wpml-26-1024x568.png)

### Step 4: Update translation in the "Languages" panel

In the WordPress editor, navigate to the "Languages" panel. Typically found in the right sidebar or the document settings panel.

Here, you will find an option to edit or update the translation. Click the icon to open the "Advanced Translations Editor" as shown in this screenshot:

![](https://academy.bricksbuilder.io/assets/bricks-wpml-27-532x1024.png)

Translate any untranslated strings inside the Advanced Translation Editor, then click the "Complete" button at the bottom of the screen. Your new design changes are now synced with this translated page without affecting the translated text.

## Creating different designs per language {#different-designs}

You can also access and edit the translated content directly with Bricks for specific language design or content modifications. For instance, instead of simply translating the text of your homepage, you can create a completely different layout that appeals to a specific target audience.

To create a different design per language:

1. Use the admin language switcher to change to the language you want to edit.
2. Find the page or template you want to make changes to and open it in Bricks.

![](https://academy.bricksbuilder.io/assets/Switching-to-translations-in-WordPress-admin-1024x692.png)

1. Make your design changes and save. Your pages will now have different designs when switching languages.

![](https://academy.bricksbuilder.io/assets/Translations-with-design-A-1024x661.png)

![](https://academy.bricksbuilder.io/assets/Translations-with-design-B-1024x661.png)

## Additional resources

Consult the following official WPML documentation for further guidance:

1. [**Getting Started with WPML**.](https://wpml.org/documentation/getting-started-guide/)
2. [**WPML FAQ**.](https://wpml.org/faq/)
3. [**Translating Content Created with Page Builders**.](https://wpml.org/documentation/translating-your-contents/page-builders/)
4. [**Translating External Links**.](https://wpml.org/announcements/2020/02/translating-links-with-advanced-translation-editor/)

## Fancy trying out WPML?

If you found this post insightful and you're considering giving WPML a try, we encourage you to use [our affiliate link](https://wpml.org/?aid=482001&affiliate_key=S35UDkP4zjiP).

*Note: The link we've provided is an affiliate link. This means we may earn a small commission if you decide to make a purchase through it. This comes at no extra cost to you, and it assists us in further innovating and refining our offerings.*

---

<a id="integrations"></a>

# Integrations

Source: https://academy.bricksbuilder.io/integrations/

*Learn how Bricks works with WooCommerce, Gutenberg, WPML, Polylang, Google Maps, Unsplash, and other supported integrations.*

The Integrations section brings together Bricks guides for third-party platforms, plugins, and external services that commonly shape real production projects.

## Browse integrations

- [WooCommerce](https://academy.bricksbuilder.io/integrations/woocommerce/) for shop, product, cart, checkout, account, and notice workflows
- [Gutenberg](https://academy.bricksbuilder.io/integrations/gutenberg/) for mixed editor and block-based workflows
- [WPML](https://academy.bricksbuilder.io/integrations/how-to-use-wpml-with-bricks/) for multilingual projects with translated content and templates
- [Polylang](https://academy.bricksbuilder.io/integrations/polylang/) for multilingual content and templates with Polylang
- [Google Maps](https://academy.bricksbuilder.io/integrations/how-to-set-up-your-google-maps-api-key/) for map element setup
- [Unsplash](https://academy.bricksbuilder.io/integrations/unsplash/) for external image sourcing

---

<a id="integrations-instagram-access-token"></a>

# How to get your Instagram Access Token

Source: https://academy.bricksbuilder.io/integrations/instagram-access-token/

*Generate an Instagram access token for Bricks so Instagram-based elements can retrieve and display feed content.*

To use the Instagram Feed element (@since 1.9.1), you need an access token. This token allows secure retrieval of your Instagram account data. This guide explains how to get the token using the Instagram API with Instagram Login.

> **Note**
>
> Before you can publish your app and generate an access token, you must connect your app to a **Business that has completed Business Verification**. Follow Meta’s [Business Verification guide](https://developers.facebook.com/docs/development/release/business-verification/) for instructions.

## Step 1: Ensure you have an Instagram Creator or Business account

Before proceeding, make sure your Instagram account is either a **Creator** or **Business** account.

1. Log in to your Instagram account.
2. Convert your account by following these instructions:
  - [Set up a Creator Account](https://help.instagram.com/2358103564437429?helpref=faq_content).
  - [Convert to a Business Account](https://help.instagram.com/502981923235522).

## Step 2: Set up an application

You first have to set up an application on the Meta for Developers platform by following these steps:

1. Access your [Meta for Developers platform](https://developers.facebook.com/apps). You can use an existing account or [create a new one](https://developers.facebook.com/docs/development/register/).
2. Provide an **App Name** and **Contact Email**.
3. Click **Create App**, then:
  - Under **Add use cases**, select **Manage messaging & content on Instagram** (from the **Content management category**), then click **Next**.
  - When prompted, you may connect a Business account now or skip and do it later.
4. Click **Next** and then **Go to dashboard** to complete the setup.

You will be redirected to the app dashboard for your new app with products you can add to your app.

## Step 3: Add the Instagram product to your app

1. On the app dashboard, scroll down to **Products** and locate **Instagram**.
2. Click **Set Up** next to Instagram.
3. Select **API Setup with Instagram Login** (NOT API Setup with Facebook Login).

## Step 4: Generate your Instagram access token

To retrieve an access token:

1. Assign an Instagram account for token generation:
  - In the App Dashboard, go to **Instagram > API Setup with Instagram Login**.
  - Click **Add an Instagram Account**.
  - Log in with your Instagram Creator or Business account credentials.

![](https://academy.bricksbuilder.io/assets/bricks-instagram-generate-access-token-1024x684.png)

1. Confirm the account connection:
  - Your Instagram account must be public.
  - If you manage multiple accounts, ensure the correct one is selected.
2. Copy the generated access token tied to the assigned Instagram account.

## Step 5: Add the access token to Bricks

To finalize the setup, navigate to `Bricks settings > API keys` from your WordPress dashboard and paste the access token into the `Instagram Access Token` input field, and save your changes.

![](https://academy.bricksbuilder.io/assets/bricks-instagram-access-token-20-1024x101.png)

For more information, refer to Meta’s official documentation: [Create a Meta App for Instagram Platform](https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login/create-a-meta-app-with-instagram).

**Note:** Once you retrieve and add the access token, Bricks will automatically refresh it every **20 days** using the `bricks_refresh_instagram_access_token` CRON job. No manual updates are required.

---

<a id="integrations-map-leaflet"></a>

# Map (Leaflet)

Source: https://academy.bricksbuilder.io/integrations/map-leaflet/

*Use the Leaflet-based map element in Bricks to build interactive maps with layers, markers, and configurable map behavior.*

Starting with **Bricks 2.1**, you can use the new **Map (Leaflet)** element to display fully interactive maps powered by [Leaflet.js](https://leafletjs.com/).

This element allows you to combine multiple map layers, add custom markers, and fine-tune map behaviour directly inside Bricks.

## Overview {#overview}

The Map (Leaflet) element is divided into three main groups of settings:

1. **Layers** – define map sources (OpenStreetMap, OpenTopoMap, etc.)
2. **Markers** – add custom points with icons and popups
3. **Map** – configure global map settings (center, zoom, etc.)

Let’s explore each group in detail.

## Layers {#layers}

Layers control which map tiles are displayed.

Each layer is defined through a **Repeater**. Meaning you can add multiple layers (map styles) and let visitors switch between them.

For each layer, you'll configure:

- **Name** – label shown in the layer switcher (e.g. “Street Map”, “Topographic”).
- **URL** – the provider URL (e.g. `https://tile.openstreetmap.org/{z}/{x}/{y}.png`). Bricks passes this URL to Leaflet, which replaces the placeholders supported by your tile provider. You can view list of *some* providers [here](https://leaflet-extras.github.io/leaflet-providers/preview/index.html).
  - Most tile providers require `{z}`, `{x}`, and `{y}`:
    - `{z}` → zoom level
    - `{x}` / `{y}` → tile coordinates
  - Some providers also use `{s}` for subdomains (a, b, c, …). Add it only when your provider URL requires it.
- **Min/Max Zoom** – zoom levels the layer supports.
- **Error Tile URL** – fallback image if tiles fail to load.
- **Attribution** – copyright or usage text (required by most providers).

👉 Example:

- **Street Map** → OpenStreetMap tiles
- **Topo Map** → OpenTopoMap tiles
- **Satellite** → Esri or other provider

Your users can then toggle between these layers on the frontend.

## Markers {#markers}

Markers let you highlight specific points of interest on your map.

You can set:

- **Default Marker Icon** – used if no custom icon is defined.
- **Marker Repeater** – add multiple markers, each with:
  - **Coordinates (Lat, Lng)**
  - **Label** (for identification)
  - **Custom Icon** (optional, overrides default icon)
  - **Popup Text** (text that shows when the marker is clicked)

## Map

The **Map** group controls the basic setup of your map. The most important settings are the **map height**, which is set to 300 px by default but can be adjusted to match your layout, along with the **map center** (latitude and longitude) and the **initial zoom level**. These define how the map looks and where it is focused when first loaded.

Beyond that, you’ll also find controls grouped around **zoom behaviour**, **map interactions** (like dragging and clicking), and **display options** (such as attribution and resizing). All of these settings are based on Leaflet.js, and you can find full descriptions in the [Leaflet documentation](https://leafletjs.com/reference.html#map).

---

<a id="integrations-polylang"></a>

# How to use Polylang with Bricks

Source: https://academy.bricksbuilder.io/integrations/polylang/

*Use Polylang with Bricks to translate pages, templates, and other builder content across multiple languages.*

Polylang is a WordPress plugin designed to simplify the creation of multilingual websites.

With Polylang, you can write posts, custom post types, pages, create categories, and post tags in multiple languages.

In combination, Bricks and Polylang facilitate the design and management of multilingual websites.

After creating a page in your default language with Bricks, you can use Polylang to translate the page into any other language your website supports.

## Setting up Polylang with Bricks

Assuming you have Bricks installed and activated on your WordPress site, the next step is to set up Polylang. This guide applies to both the free version of Polylang and Polylang Pro.

To set up Polylang with Bricks, follow the steps below:

1. In your WordPress dashboard, go to `Plugins > Add New`.
2. Type "Polylang" into the search bar and press Enter.
3. You'll see the Polylang plugin in the search results. Click on `Install Now`.
4. After the installation is complete, click `Activate`.
5. Once activated, a new `Languages` menu item appears on your WordPress dashboard. Visit it, and add the languages you want to support on your website.

> **Note**
>
> Remember to set the default language and add other languages as needed.

> **Note**
>
> After adding languages and assigning any current posts/pages to their appropriate language, you can start translating your pages and posts with Polylang.

For Polylang Pro users, the installation process is slightly different as the plugin needs to be downloaded from the Polylang website and uploaded to your WordPress site. You can refer to the official Polylang documentation for detailed instructions on installing Polylang Pro.

For detailed instructions on configuring Polylang's settings, please refer to the [official Polylang documentation](https://polylang.pro/doc-category/getting-started/).

## Translating posts & pages

Translating your pages and posts using Polylang and Bricks is a straightforward process. Here are the steps:

1. In your WordPress dashboard, navigate to the page or post you want to translate.
2. On the right-hand side, you'll see a "Languages" meta box (added by Polylang). This box displays your default language and other languages you've added.
3. Under each language, you'll see a "+" button. Click this button to create a new translation for the selected language.

![](https://academy.bricksbuilder.io/assets/polylang-translate-post.png)

1. This action will create a new page or post draft. You can now use Bricks to design your page or write your post in the new language.
2. Once you're done, click "Publish". The translated page or post will automatically be linked to the original one.

> **Note**
>
> **Note:** Polylang Pro users have the advantage of the "Clone" feature, which allows you to copy the entire content and settings of a page or post into a new translation. This can significantly speed up the translation process, especially for complex layouts.

For users of the free version of Polylang, the [Yoast Duplicate Post](https://wordpress.org/plugins/duplicate-post/) plugin can be a good alternative. It allows you to duplicate a post or page, which you can then edit with the translation.

Make sure to enable the duplicator for the "My templates" post type under `Settings > Duplicate post > Permissions`. **Assign the duplicate page to the correct language and link it back to the page you’ve cloned it from.**

Please ensure you check the [official Polylang documentation](https://polylang.pro/doc/translating-pages-posts-categories-and-tags/)for detailed instructions.

## Translating components {#translating-components}

Since Bricks 2.2-beta, you can now translate components with Polylang. All component strings are registered automatically, and you can translate them directly from the WordPress dashboard.

To translate component strings:

1. Go to **Languages > Translations**.
2. Search for the component string you want to translate.
3. Add translations for each language your site supports and save.

> **Note**
>
> Make sure the admin language selector in the top admin bar is set to **Show all languages**.

1.

## Translating templates {#translating-templates}

Translating templates in Bricks using Polylang is a similar process to translating standard pages or posts.

1. From your WordPress dashboard, navigate to `Bricks > Templates` in your WordPress dashboard.
2. Choose the template you want to translate and assign a language to it in the "Languages" meta box.

![](https://academy.bricksbuilder.io/assets/polylang-bricks-template-assign-language.png)

1. Once the language is set, you can initiate the translation process as you would do with a standard post or page by clicking the "+" button for the desired language in the Languages meta box.

![](https://academy.bricksbuilder.io/assets/polylang-bricks-translate-template.png)

1. The newly translated template will be created in draft mode. At this point, you can modify the content and adapt it to the new language using Bricks.

![](https://academy.bricksbuilder.io/assets/polylang-bricks-template-translated.png)

> **Note**
>
> **Note:** Setting a language for your current templates, if not already assigned, is a prerequisite before you can translate them.

> **Note**
>
> **Important:** Duplicating the template for each language you wish to translate it into is essential. If a Bricks page uses a template that has not been translated into the page's language, that template will not be visible on the page in that language. Hence, ensure that all the templates used on your pages are translated for each supported language.

## Using templates conditions {#template-conditions}

Bricks templates have [template conditions](https://academy.bricksbuilder.io/builder/features/template-settings/) that define where a particular template is rendered on your website. While these conditions offer flexibility, using them with Polylang introduces complexities due to how Polylang handles languages as WordPress taxonomy terms.

Although you can select language terms in Bricks conditions, it's generally not recommended because of potential unexpected bugs. This is due to Polylang creating distinct posts or pages for each language, which are separate entities linked by the plugin.

Due to backward compatibility, these language terms are available in the conditionals but may not behave as expected.

> **Note**
>
> Instead, it's advisable to directly translate the templates as covered in the [Translating templates](#translating-templates) section. This involves duplicating each template for every language you want to support and translating the content within those templates. This method ensures consistent results when showing the correct template per language and avoids potential confusion and inconsistencies.

## Managing multilingual menus {#managing-multilingual-menus}

Polylang's method for handling menu translations involves creating a separate menu for each language. To do so, you should follow these steps:

1. Go to `Appearance > Menus` in your WordPress dashboard.
2. Click `Create a new menu`.
3. Give your menu a name, ideally including the language for easy identification.
4. Choose the display location for this menu, then click `Create Menu`.
5. *(Optional)* Use the admin language option in the admin bar at the top of the screen to match the menu language. This ensures the pages listed are in the selected language, helping you add the correct content.
6. Start adding the pages, posts, categories, or custom links this menu will contain.
7. Repeat these steps for each language your website supports.

> **Note**
>
> Keep in mind that Polylang changes the language of the content on your site, not individual menu items, so you’ll need to create separate menus for each language. Additionally, when translating a page or template (e.g., a header template with a Nav element), be sure to edit the navigation element in the translated template to select the correct menu for that language. This ensures that each language version of the header template displays the appropriate menu.

For more details, please refer to the Polylang documentation: [https://polylang.pro/doc/create-menus/](https://polylang.pro/doc/create-menus/).

## The language switcher

Bricks provides a dedicated "Language switcher" element for Polylang, which you can add anywhere on your site and customize without leaving the builder.

![](https://academy.bricksbuilder.io/assets/bricks-polylang-language-switcher.png)

> **Note**
>
> To replace default Polylang flags with custom ones, please refer to the Polylang documentation on this topic [here](https://polylang.pro/doc/can-i-use-my-own-flags-for-the-language-switcher/).

You can also add the language switcher to your WordPress menu by adding the "Language switcher" under Appearance > Menus like this:

![](https://academy.bricksbuilder.io/assets/bricks-polylang-language-switcher-wp-nav-menu.png)

## Troubleshooting common Polylang issues

When integrating Polylang with Bricks, you might encounter some common issues. Here are a few possible problems and suggested solutions:

### 1. Templates don't show after Polylang activation

If you have Bricks templates that don't appear after activating Polylang, this might be due to language settings. Ensure each of your templates is assigned a language. This setting is found on the right side of the WordPress editor page under "Languages". Remember to update your template after assigning a language.

### 2. Untranslated templates do not appear

When an untranslated Bricks template doesn't appear, it might be due to a language discrepancy between the page and the template. If a Bricks page uses a template that isn't translated into that page's language, the template won't show. To fix this, translate your templates into all languages your pages use.

### 3. Incorrect language in menus

If a menu appears in the wrong language, double-check that you've assigned the correct language to each of your menus, as per the [Managing multilingual menus](#managing-multilingual-menus) section above. Remember, Polylang requires a separate menu for each language on your site.

### 4. Incorrect language query results in Archive or Search template

Please ensure all archive or search templates have enabled **Is main query** on the main query loop.

## Additional resources

To learn more about Polylang and its various features, you can refer to the following resources from Polylang's official documentation:

1. [Getting Started with Polylang](https://polylang.pro/doc-category/getting-started/): This guide covers the basics of setting up and using Polylang on your WordPress site.
2. [Polylang FAQ](https://polylang.pro/doc-category/faq/): Here you'll find answers to commonly asked questions about using Polylang.
3. [Polylang advanced](https://polylang.pro/doc-category/polylang-advanced/): This section provides more advanced Polylang guides.

These resources can provide additional insights and answers to more specific or complex issues you might encounter when using Polylang.

---

<a id="integrations-unsplash"></a>

# Unsplash Integration

Source: https://academy.bricksbuilder.io/integrations/unsplash/

*Connect Unsplash to Bricks so you can browse, download, and optionally rename royalty-free images directly from the builder.*

Finding affordable, high-quality, commercially useable photography for your website (that doesn't scream stock photography) is really hard. Bricks is putting an end to it.

[Unsplash.com](https://unsplash.com?ref=bricksbuilder), the world's largest and most generous community of photographers, allows you to use their photography royalty free (commercial use included). No linking back or attribution required. Unsplash operates under a so-called "do whatever you want" [license](https://unsplash.com/license).

Browse and download any Unsplash photo inside the builder by clicking the **Browse Unsplash** button below eligible image and image gallery controls after entering your Unsplash API key. The button appears only on controls that support Unsplash and have not disabled it.

https://youtu.be/yLgi-L2doIM

## Rename & Download

Hover over any photo and click the** Download** button to download a photo from Unsplash directly into your WordPress media library. All resizing is done automatically in the background for you.

File renaming is disabled by default. If you want to enter a custom filename before downloading a photo, enable the "Rename images" checkbox in the top right corner of the Unsplash popup.

## How To Generate Your Unsplash API Key

To receive access to Unsplash's photo library you need to generate an API key. It's 100% free and only takes two minutes.

1. Create an Unsplash developer account if you don't already have one:
[https://unsplash.com/developers](https://unsplash.com/developers)
2. Log in and visit [https://unsplash.com/oauth/applications](https://unsplash.com/oauth/applications)
3. Click **New Application**, check all boxes and click **Accept terms**.
4. Fill out the application name and description and click **Create application**.
5. Scroll down to **Keys** and copy the **Access key**.
6. Return to your WordPress dashboard. Go to **Bricks > Settings > API Keys** and paste your Unsplash API key under **Unsplash API Key**. Click Save.

If you click on **Browse Unsplash** below an eligible image or image gallery control in the builder, the latest Unsplash photos should now appear, ready for you to download.

---

<a id="integrations-gutenberg-components-as-blocks"></a>

# Bricks components as blocks

Source: https://academy.bricksbuilder.io/integrations/gutenberg/components-as-blocks/

*Expose Bricks components as Gutenberg blocks so editors can insert styled, property-driven Bricks content directly inside the block editor.*

https://youtu.be/tgpjMcZaLNc

Most sites built with Bricks follow a simple pattern: you create your pages and templates in Bricks, and write your posts or other content in the block editor (Gutenberg).

That works well for standard content, but as soon as you need something more custom inside the block editor, like a styled testimonial or a reusable promo block, you quickly run out of options.

We are introducing a new experimental feature called **components as blocks** to bridge this gap. It lets you design blocks in Bricks and make them available directly inside the block editor.

You get the same builder features you already use for pages and templates, while deciding exactly what editors can override through component properties.

This makes it possible to:

- Build custom, styled blocks entirely in Bricks
- Keep design consistent across your site by updating the component once in Bricks
- Give editors freedom to customize content inside the block editor while staying within your design system

## Enable components as blocks

This new feature is currently experimental and disabled by default. You can enable it from the WordPress dashboard under `Bricks → Settings → General → Block editor → Bricks components in the block editor`.

Three options are available:

- **Disabled** (default)
- **Enable individual components manually**
  - Components must be enabled individually to appear in the block editor.
  - In the builder:
    - Open the **Components panel**, hover over a component, click **Use in block editor**, then confirm.
    - Or edit a component and toggle **Use in block editor → Enabled** from the component settings header.
  - A filter in the Components panel lets you view only components enabled for the block editor.
- **Enable all components automatically**
  - All Bricks components are instantly available in the block editor.

When a component is enabled for block editor use, additional block-specific settings appear in the component settings header under "Use in block editor":

- **Block category**: Choose which block category the component should appear under inside the block editor.
- **Block icon**: Select the icon shown in the block picker.
- **Block preview image**: Set an optional preview image that appears in the block inserter.

## Insert a component in the block editor

1. Open or create a post/page in the block editor.
2. Click **Add block (+)** and search for your component by name.
3. Select the component. It renders directly inside the editor.

The component behaves like any other block. You can add text above or below, reorder it, or combine it with other block editor blocks.

### Wide and full-width blocks

The block editor's **Wide width** and **Full width** options apply to the outer WordPress block wrapper. The elements inside the component still use their Bricks layout settings.

A Bricks Container has a default maximum width of 1100px. A component with a Container at its root, or a Container nested inside a full-width root element, can therefore remain constrained even when the Gutenberg block is set to **Full width**.

For a full-width component block, use a Section, Block, or Div with 100% width as the outer element. Set the width or maximum width of any inner Container intentionally, then select the required alignment for the block in Gutenberg.

If the editor preview still differs from the frontend, check both the selected Gutenberg alignment and every Bricks layout element that can set a width or maximum width.

## Customize component properties

When you select a Bricks component block in the block editor, its editable properties appear in the **Block settings sidebar** in the same way as editing an instance in Bricks.

All property types are supported:

- Text
- Rich text
- Icon
- Select
- Toggle
- Global classes
- Image
- Image gallery
- Link
- Query loop *(Query editor (PHP), External APIs, and Query manager are not supported at this time)*

Each block instance can have unique property values, while the component design remains consistent.

[Component slots](https://academy.bricksbuilder.io/builder/features/components/#slots) are not supported in component blocks. The block editor offers no way to add elements to a slot, so a slot stays empty in the editor and on the frontend.

## Centralized design updates

All block instances remain linked to the main component in Bricks. Any design change you make in Bricks (such as adjusting layout, typography, or spacing) applies site-wide to every instance, including those inside the block editor.

## Use cases

- **Reusable design elements**: Insert testimonials, event cards, promo blocks, or signup forms into posts.
- **Design consistency**: Global updates in Bricks apply throughout your entire site.
- **Content flexibility**: Editors can update text, images, and toggles per instance without leaving the block editor.
- **Workflow separation**: Designers build components in Bricks, editors use them in the block editor.

As this feature is experimental, we would love your feedback on components as blocks specifically, as well as ideas for how Bricks could integrate even smoother with the block editor to support your workflow. Share your thoughts in the [Bricks forum](https://forum.bricksbuilder.io/) or get in touch with us directly via email.

---

<a id="integrations-woocommerce-advanced-modular-elements"></a>

# WooCommerce advanced modular elements

Source: https://academy.bricksbuilder.io/integrations/woocommerce/advanced-modular-elements/

*Set up and customize WooCommerce cart, checkout, account, and cart-dependent content with the Bricks 2.4 advanced modular workflow.*

Starting in Bricks 2.4, the WooCommerce integration includes an advanced modular workflow for the store areas that usually require the most setup: Cart, Checkout, and My Account.

WooCommerce v2 lets you build these system pages from editable Bricks elements, protected state containers, predefined structures, dynamic data, query loops, conditions, and interactions.

In the classic setup, screens such as empty cart, checkout payment, order received, account orders, account downloads, and password reset are handled through separate Bricks templates or WooCommerce endpoints. In the v2 setup, those screens live as states on the assigned WooCommerce page, so you can switch between them in the builder and edit them in one place.

![](https://academy.bricksbuilder.io/assets/woo-v2-state-filled-cart.png)

![](https://academy.bricksbuilder.io/assets/woo-v2-state-empty-cart.png)

> **Note**
>
> Advanced modular elements are experimental. Enable them under **Bricks > Settings > WooCommerce > Enable advanced modular elements**.
>
> ![](https://academy.bricksbuilder.io/assets/woo-advanced-modular-setting.png)

## What changes in v2

The v2 workflow is useful when you want more control over WooCommerce system pages without recreating WooCommerce logic from scratch.

- Build Cart, Checkout, and My Account pages with editable Bricks elements.
- Edit template or endpoint-style views as page states directly on the assigned WooCommerce page.
- Preview states such as filled/empty cart, checkout/pay/thank-you, and account orders/downloads while editing.
- Insert predefined complete blocks and smaller section blocks.
- Keep generated checkout and account address fields aligned with WooCommerce field definitions.
- Refresh cart-dependent content with the [Dynamic fragment element](https://academy.bricksbuilder.io/builder/elements/woocommerce/dynamic-fragment/).
- Use new WooCommerce v2 [query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/).
- Build [multistep checkout flows](https://academy.bricksbuilder.io/integrations/woocommerce/multistep-checkout-v2/) with checkout step elements and interactions.

## When to use this workflow

Use the advanced modular workflow when you want a more guided setup and a single editing place for each WooCommerce page.

| Workflow | Best for |
| --- | --- |
| **Standard (v1)** | Existing sites that already use WooCommerce shortcode pages and Bricks WooCommerce templates, or stores that prefer separate templates for each WooCommerce screen. |
| **Advanced (v2)** | New or redesigned Cart, Checkout, and My Account pages where you want editable page states, generated structures, and v2 dynamic data directly on the assigned page. |

The classic template workflow remains supported. You can keep using the existing Cart, Empty Cart, Checkout, Thank You, Pay, Order Receipt, and Account template types.

For guided setup checks and presets, use the [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/). The wizard can set up classic WooCommerce layouts without advanced modular elements enabled. V2 setup types are disabled until advanced modular elements are enabled.

## Predefined structures

Cart, Checkout, and Account Page v2 states can generate complete starter layouts or smaller WooCommerce sections through **Insert a structure**.

![](https://academy.bricksbuilder.io/assets/woo-v2-insert-structure-cart.png)

Generated structures are site-aware where needed. For checkout, checkout account credentials, and account address forms, Bricks reads the WooCommerce field definitions that exist at generation time and turns them into editable Bricks form field elements. After generation, you can style, move, reorder, and place those fields like regular Bricks elements.

> **Note**
>
> Some WooCommerce v2 support elements are generated-only or context-specific. If you do not see a v2 support element in the regular Elements panel, create it through **Insert a structure** or the [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/). After generation, the element appears in the Structure panel and can be edited inside its v2 state.

> **Note**
>
> Checkout fields can change after a layout is generated. For example, a plugin may add a VAT field, remove a company field, change labels and placeholders, or add an account field. Use field sync after installing, removing, or reconfiguring plugins that modify WooCommerce checkout or account address fields.

Field sync can report valid, missing, invalid, and duplicate generated fields. It can generate missing fields, remove invalid or duplicate generated fields, and update labels and placeholders from the current WooCommerce field data.

Checkout v2 and several Account v2 form states also include a **Floating label style** option for supported generated fields. Review third-party fields manually because plugin-generated fields can use different markup.

## V2 element groups

The main parent elements are:

- [Cart v2](https://academy.bricksbuilder.io/builder/elements/woocommerce/cart-v2/)
- [Checkout v2](https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-v2/)
- [Account Page v2](https://academy.bricksbuilder.io/builder/elements/woocommerce/account-page-v2/)

V2 layouts can also include support elements that only make sense inside their matching WooCommerce state or generated structure.

Bricks 2.4 registers these advanced modular support elements:

| Area | Registered support elements |
| --- | --- |
| Cart v2 | Cart form, Cart quantity |
| Checkout v2 | Checkout steps navigation, Checkout step nav item, Checkout step, Shipping options, Payment options, WooCommerce form field, WooCommerce form submit, Checkout account fields, Checkout billing address, Checkout shipping address, Checkout order summary, Checkout place order |
| Account Page v2 | WooCommerce login form, Account register form, Account lost password form, Account reset password form, Account orders pagination, Account edit address form, Account edit account form, Account order withdrawal form (when Order Withdrawal is enabled) |
| Cart-dependent content | Dynamic fragment |

Some support elements are generated-only. Create them through **Insert a structure** or the [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/), then edit them from the Structure panel.

## Cart v2

The [Cart v2 element](https://academy.bricksbuilder.io/builder/elements/woocommerce/cart-v2/) is added to the assigned Cart page. It contains two states:

- **Filled cart** for carts that contain products.
- **Empty cart** for carts with no products.

Use the **State** control while editing to switch the builder preview between these states. Each state can contain custom layouts and generated structures, such as the complete cart block or complete empty cart block.

## Checkout v2

The [Checkout v2 element](https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-v2/) is added to the assigned Checkout page. It contains these states:

- Checkout
- Login required
- Pay
- Thank you
- Order receipt

Use the **State** control to design each checkout screen from one page. The checkout state can generate complete checkout structures or smaller sections such as billing fields, shipping fields, payment options, additional fields, order summary, and place order.

Checkout v2 also includes checkout field maintenance actions to help compare generated fields with the site's current WooCommerce checkout fields.

Generated billing and complete checkout structures include a **Checkout account fields** wrapper. It follows WooCommerce's guest checkout, account creation, username generation, and password setup settings. See [Checkout v2 account creation](https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-v2/#account-creation-during-checkout) for the settings matrix and field sync behavior.

The **Login required** state is used when WooCommerce requires a customer to log in before viewing order-related checkout screens, such as pay, receipt, or thank you flows for a registered customer order.

For multistep layouts, see [Checkout v2 multistep checkout](https://academy.bricksbuilder.io/integrations/woocommerce/multistep-checkout-v2/).

## Account Page v2

The [Account Page v2 element](https://academy.bricksbuilder.io/builder/elements/woocommerce/account-page-v2/) is added to the assigned My Account page. It keeps the account navigation and endpoint content together.

It includes states for the common My Account endpoints:

- Dashboard
- Orders
- View order
- Downloads
- Addresses
- Edit address
- Edit account
- Payment methods
- Add payment method
- Login
- Lost password
- Lost password confirmation
- Reset password
- Order withdrawal (WooCommerce 11.1 or later, with Order Withdrawal enabled)

Use the **State** control to switch between endpoint previews while editing. Each state can contain generated starter content that you can customize in the builder.

## Dynamic Fragment

The [Dynamic fragment element](https://academy.bricksbuilder.io/builder/elements/woocommerce/dynamic-fragment/) re-renders itself and its children after WooCommerce cart changes.

![](https://academy.bricksbuilder.io/assets/dynamic-fragment-mini-cart-structure-example.png)

Use it for cart-dependent content outside the main Cart page, such as:

- Custom mini cart content
- Free shipping progress
- Cart totals or subtotal displays

The element includes generated structures for **Mini cart** and **Free shipping progress**. For custom mini carts, wrap the mini cart in Dynamic fragment, add a child loop using the `wooCart` query type, and use cart tags such as `{woo_cart_product_name}`, `{woo_cart_quantity:value}`, `{woo_cart_subtotal}`, and `{woo_cart_remove_link:url}` inside the loop.

Keep the Dynamic fragment wrapper outside other query loops. The cart loop should be a child of the fragment.

Dynamic fragment is frontend-only. It can refresh when it is rendered from the header, content, or footer area, but it does not refresh inside query loop instances or component instances.

## Query loops, dynamic tags, conditions, and interactions

WooCommerce v2 adds query loops for applied coupons, fees, taxes, order items, order totals, order downloads, order customer notes, account orders, account order actions, account downloads, and account addresses.

It also adds dynamic tags for cart totals, free shipping progress, WooCommerce URLs, account addresses, order data, order items, order totals, order actions, downloads, and customer notes.

See [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/) for the complete reference.

Bricks 2.4 also adds WooCommerce conditions for shipping/order visibility and interactions for Dynamic fragment refreshes and checkout step changes.

## Existing WooCommerce templates

Bricks 2.4 also improves WooCommerce order-related template handling. Logged-out customers can still get Bricks layouts for Thank You, Order Receipt, and Order Pay flows when WooCommerce requires login for a non-guest order.

Classic templates and v2 page states can coexist on the same site, but each WooCommerce area should use one setup approach at a time to avoid confusion.

## Caveats

- Advanced modular elements must be enabled before you can add or edit v2 elements.
- V2 page rendering still follows WooCommerce page routing. Cart v2 and Checkout v2 render through the assigned WooCommerce cart and checkout pages.
- WooCommerce block content on assigned WooCommerce pages is not compatible with the v2 setup. The [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) can replace the page content with the matching v2 structure.
- Protected state elements are required children of their v2 parent elements. Do not remove them manually.
- Predefined structures are authored with the default Bricks breakpoint keys. Review responsive styling on sites with custom breakpoints.
- Third-party checkout fields may need manual review after generation or field sync.

---

<a id="integrations-woocommerce-cart"></a>

# Cart (WooCommerce)

Source: https://academy.bricksbuilder.io/integrations/woocommerce/cart/

*Build and customize the WooCommerce cart in Bricks, including the classic shortcode/template workflow and the Cart v2 advanced modular workflow.*

## Overview

The Cart page is a special WooCommerce page, created by default during WooCommerce installation and assigned under **WooCommerce > Settings > Advanced**.

Starting in Bricks 2.4, you can choose between two Cart building workflows:

- **Cart v2 workflow**: Build the assigned Cart page directly with [WooCommerce advanced modular elements](https://academy.bricksbuilder.io/integrations/woocommerce/advanced-modular-elements/) and the [Cart v2 element](https://academy.bricksbuilder.io/builder/elements/woocommerce/cart-v2/).
- **Cart v1 workflow**: Keep the classic WooCommerce cart shortcode on the assigned Cart page and customize the output with separate Bricks Cart and Empty Cart templates.

Use Cart v2 for new builds or redesigns where you want to edit the filled and empty cart states in one place. Use Cart v1 for existing sites that already rely on the classic shortcode/template setup.

The [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) can check or create either workflow. The same v2 data tools can also be used with [Dynamic fragment](https://academy.bricksbuilder.io/builder/elements/woocommerce/dynamic-fragment/) to build cart-dependent header content such as a custom mini cart.

## Cart v2 workflow

With advanced modular elements enabled, Cart v2 keeps the filled cart and empty cart screens as editable states on the assigned Cart page.

Use the [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) and choose **Advanced (v2)** to replace the assigned Cart page content with the [Cart v2 element](https://academy.bricksbuilder.io/builder/elements/woocommerce/cart-v2/) and generated state structure.

Cart v2 includes two states:

- **Filled cart** for carts that contain products.
- **Empty cart** for carts with no products.

Each state can generate starter content through **Insert a structure**. Use **Complete cart block** for the Filled cart state and **Complete empty cart block** for the Empty cart state. Generated structures are appended to the current state content, so you can insert a starter block and then move, style, or remove the generated elements.

Cart v2 is the recommended workflow when you want to design the Cart page directly, switch between filled and empty previews in one place, and use the v2 cart dynamic tags. The classic shortcode/template workflow below is still useful for existing sites that already use separate **WooCommerce - Cart** and **WooCommerce - Empty Cart** templates.

> **Note**
>
> Some Cart v2 support elements, such as the cart form wrapper and cart quantity controls, are generated-only or context-specific. If you cannot find a support element in the regular Elements panel, create it through **Insert a structure** or the [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/), then edit it from the Structure panel.

Cart v2 layouts can use the **Cart contents** query loop and cart total tags such as `{woo_cart_items_count}`, `{woo_cart_order_subtotal}`, `{woo_cart_order_total}`, `{woo_cart_shipping_method}`, `{woo_free_shipping_remaining}`, and `{woo_free_shipping_progress}`.

For the complete element reference, see [Cart v2](https://academy.bricksbuilder.io/builder/elements/woocommerce/cart-v2/). For all new WooCommerce v2 query loops and dynamic tags, see [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/#cart-tags).

## Cart v1 workflow

The classic Cart workflow renders the WooCommerce `[woocommerce_cart]` shortcode on the assigned Cart page, then uses Bricks WooCommerce template types to customize the filled and empty cart screens.

> **Note**
>
> Remove the Gutenberg Cart block if it is located within your Cart Page. Instead, replace it with `[woocommerce_cart]` or use a Shortcode element if you edit the Cart page with Bricks.

![](https://academy.bricksbuilder.io/assets/remove-gutenberg-cart-blocks.png)

For the Cart v1 workflow, place the `[woocommerce_cart]` shortcode directly on the Cart page, or edit the Cart page with Bricks and use a Shortcode element with `[woocommerce_cart]` as its content. Bricks offers two template types to customize the cart:

- **WooCommerce - Cart**: Rendered when the cart contains products.
- **WooCommerce** - **Empty** **Cart**: Rendered when the cart is empty.

![](https://academy.bricksbuilder.io/assets/bricks-woocommerce-templates-cart.png)

> **Note**
>
> The "Cart" and "Empty Cart" template types are only visible if you have the WooCommerce plugin installed and active. These templates are used inside the WooCommerce Cart shortcode logic and **they do not support template conditions (they are automatically rendered on the correct page)**.

By default, the cart in the Bricks theme will be shown as in the image below. You'll notice there are typically two different zones: the cart items table & the cart totals:

![](https://academy.bricksbuilder.io/assets/bricks-woo-cart-blocks.png)

If you want to customize this screen, you'll need to create a **WooCommerce - Cart** template type.

> **Note**
>
> Please remember to add [template hooks](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-template-hooks/#cart-template-hooks) if you are using third-party plugins.

## Cart template {#cart-template}

You would set the **WooCommerce - Cart** template type to customize the Cart page (used when the cart contains products).

When opening this template with Bricks you'll see three new elements (specific for this template type):

![](https://academy.bricksbuilder.io/assets/bricks-woo-cart-elements.png)

<figcaption>

The specific Bricks elements to be used inside the "WooCommerce - Cart" template type

</figcaption>

### Cart items

Render the cart contents table. With this element, you'll be able to hide different parts of the table, style the table elements and the buttons, and hide the coupon input (so you could set it separately using the **Cart Coupon** element). For custom layout, check the section down below [Cart contents loop](#loop).

### Cart totals

Renders the cart totals zone. With this element, you could hide the cart cross-sells, style the totals table, and style the button.

### Cart Coupon

Render the coupon input. Use this element if you don't want to have the coupon input attached to the cart items table. With this element, you could style the input and the apply coupon button

## Empty cart template {#empty-cart-template}

You would set the **WooCommerce - Empty Cart** template type to customize how the cart page renders when the cart is empty.

By default, the empty cart shows a message and a button to return to the shop page.

![](https://academy.bricksbuilder.io/assets/bricks-woocommerce-empty-cart-screen.png)

To customize this screen you need to create a **WooCommerce - Empty Cart** template type where you could place the required elements and configure as needed.

## Cart contents loop {#loop}

Bricks 1.4 introduced the **Cart Contents** query loop. This query loops through all visible products in the cart, enabling [Dynamic Data tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-builder/#dynamic-data) for cart item data such as the product name (post title), product image (featured image), price, description, SKU, and more. This query loop is intended for cart-content layouts and is not restricted to the Cart page.

This allows you to build your own cart items widget. In Bricks 2.4, the same `wooCart` query loop is also useful inside a [Dynamic fragment](https://academy.bricksbuilder.io/builder/elements/woocommerce/dynamic-fragment/) for custom mini cart layouts that refresh after cart changes. Bricks 2.4 also adds separate title, item data, unit price, and savings output for custom cart rows.

### Build your own cart items element inside the cart page {#custom-cart-contents-loop}

By default, the list of products inside the cart appears displayed on a table layout. This happens in the default WooCommerce cart template or when using the Bricks Cart Items element.

To create a different layout for the cart products list, you'll need to add a container with a query loop, and set it to **Cart Contents**. Inside this container you may use the following dynamic data tags. The cart-specific tags were introduced in Bricks 1.5.3; product SKU and GTIN support inside this loop was added in Bricks 2.4.

> **Note**
>
> In order to make your custom cart loop work, you must add `woocommerce-cart-form__cart-item cart_item` CSS class on the loop itself and add `woocommerce-cart-form__contents` CSS class on the parent of looping div.

![](https://academy.bricksbuilder.io/assets/bricks-woo-cart-loop-css-class.png)

<figcaption>

CSS classes needed for WooCommerce JS works in cart page

</figcaption>

![](https://academy.bricksbuilder.io/assets/cart-contents-query-loop.png)

<figcaption>

Cart Contents query loop

</figcaption>

- `{woo_cart_product_name}` - Renders the linked product name together with cart item metadata and other legacy WooCommerce output.
- `{woo_cart_product_title}` - Renders the product title without cart item metadata. Use `:plain` to remove the link.
- **Cart item data** element - Renders variation attributes and compatible extension-provided item data separately from the product title.
- `{woo_cart_remove_link}` - Renders the anchor tag with the link to remove the product from the cart. By default, uses an "x" in the anchor content. Remember to add `product-remove` CSS class on the element that holding this dynamic tag. Do **NOT** use on Rich text element or additional `` tag will cause the AJAX not working.
- `{woo_product_price}` - This tag shows the product price. But when used inside of the Cart Contents loop it doesn't show the sale price.
- `{woo_cart_item_price}` - Renders the current unit price and includes WooCommerce sale-price markup when discounted. Use `:value` for the unformatted current unit price.
- `{woo_cart_item_save}` - Renders the product savings for the full cart item quantity. Use `:value` for the unformatted savings amount or `:percentage` for the numeric discount percentage.
- `{woo_product_sku}` - Returns the product SKU for the current cart item. (@since 2.4)
- `{woo_product_gtin}` - Returns the product GTIN for the current cart item. (@since 2.4)
- `{woo_cart_quantity}` - Renders the input field to add/remove the product quantity inside of the cart.
- `{woo_cart_quantity:value}` - Outputs the cart item quantity as text.
- `{woo_cart_subtotal}` - Renders the product price subtotal (price x quantity)
- `{woo_cart_update}` - Renders the update cart button and nonce. Use this outside the cart item loop but inside the cart form.

Bricks 2.4 also adds cart total and checkout tags such as `{woo_cart_items_count}`, `{woo_cart_order_subtotal}`, `{woo_cart_order_total}`, `{woo_cart_shipping_method}`, `{woo_free_shipping_remaining}`, and `{woo_free_shipping_progress}`. See [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/#cart-totals-and-checkout-tags) for the complete list.

For a custom mini cart, wrap the mini cart in the [Dynamic fragment element](https://academy.bricksbuilder.io/builder/elements/woocommerce/dynamic-fragment/), add a child element with the **Cart contents** query loop, and place cart item tags inside that loop. Put total tags outside the loop but still inside the Dynamic fragment wrapper.

To complete this component, you have to wrap the products loop inside a `form` tag in order to use the product quantity input fields. To do that, wrap the container loop inside of another container (or div, or block) and set the HTML tag to `custom` and then insert `form` in the Custom tag input field.

![](https://academy.bricksbuilder.io/assets/bricks-container-form-cart-items.png)

<figcaption>

Wrap the products loop with a form container

</figcaption>

> **Note**
>
> **IMPORTANT**: Using Bricks 1.10.2+ you have explicitly allow the `form` HTML tag programmatically. Please follow the instructions at [/developer/hooks/filters/filter-bricks-allowed_html_tags/](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-allowed_html_tags/)

This form container, in order to work properly with the WooCommerce scripts needs the following configurations:

- Add the custom class `woocommerce-cart-form` (Style > CSS > CSS classes)
- Add custom attributes: method = `post` and action = `{post_url}`

![](https://academy.bricksbuilder.io/assets/example-form-container.png)

<figcaption>

Example Form container

</figcaption>

![](https://academy.bricksbuilder.io/assets/bricks-cart-form-attributes-2.png)

![](https://academy.bricksbuilder.io/assets/bricks-cart-form-attributes.png)

To add the update cart button, there's also another dynamic data tag `{woo_cart_update}` that you'll need to add inside of the form container (but outside of the loop). This will generate a button with the proper settings to update the cart.

---

<a id="integrations-woocommerce-checkout"></a>

# Checkout (WooCommerce)

Source: https://academy.bricksbuilder.io/integrations/woocommerce/checkout/

*Build and customize the WooCommerce checkout in Bricks, including the classic template workflow and the Checkout v2 advanced modular workflow.*

## Overview

The Checkout page is a special WooCommerce page, created by default during WooCommerce installation and assigned under **WooCommerce > Settings > Advanced**.

Starting in Bricks 2.4, you can choose between two Checkout building workflows:

- **Checkout v2 workflow**: Build the assigned Checkout page directly with [WooCommerce advanced modular elements](https://academy.bricksbuilder.io/integrations/woocommerce/advanced-modular-elements/) and the [Checkout v2 element](https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-v2/).
- **Checkout v1 workflow**: Keep the classic WooCommerce checkout shortcode on the assigned Checkout page and customize the output with separate Bricks Checkout, Thank You, Pay, and Order Receipt templates.

Use Checkout v2 for new builds or redesigns where you want to edit checkout, payment, thank-you, receipt, and login-required states in one place. Use Checkout v1 for existing sites that already rely on the classic shortcode/template setup.

The [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) can check or create either workflow.

## Checkout v2 workflow

With advanced modular elements enabled, Checkout v2 keeps the checkout, pay, thank-you, order receipt, and login-required screens as editable states on the assigned Checkout page.

Use the [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) and choose:

- **Advanced (v2)** for a complete one-page checkout structure.
- **Advanced multistep (v2)** for a ready-made [multistep checkout structure](https://academy.bricksbuilder.io/integrations/woocommerce/multistep-checkout-v2/).

Checkout v2 can generate complete checkout blocks or smaller sections such as billing fields, shipping fields, payment options, order summary, and place order. Generated checkout fields are editable Bricks elements, so you can move, style, and reorder them after generation.

For existing Checkout v2 layouts, check that the payment section wrapper has the `brx-woo-payment-section` class. Add it manually if it is missing so the payment heading and methods hide together for free orders. Keep terms and Place order controls outside that wrapper. See [Checkout v2 payment section for free orders](https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-v2/#payment-section-for-free-orders) for the steps.

Use Checkout v2 field sync after installing or reconfiguring plugins that change WooCommerce checkout fields. Field sync can find missing, invalid, and duplicate generated fields, generate missing fields, remove invalid or duplicate fields, and update labels or placeholders from WooCommerce.

Checkout v2 also adds query loops and dynamic tags for applied coupons, fees, taxes, order items, order totals, order downloads, and customer notes. See [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/) for the complete reference.

The **Login required** state is used when WooCommerce requires a customer to log in before viewing order-related checkout screens. Bricks 2.4 also improves logged-out Thank you, Order receipt, and Order pay handling for non-guest orders.

## Checkout v1 workflow

The classic Checkout workflow renders the WooCommerce `[woocommerce_checkout]` shortcode on the assigned Checkout page, then uses Bricks WooCommerce template types to customize the checkout-related screens.

> **Note**
>
> Remove the Gutenberg Checkout block if it is located within your Checkout Page. Instead, replace it with `[woocommerce_checkout]` or use a Shortcode element if you edit the Checkout page with Bricks.

![](https://academy.bricksbuilder.io/assets/remove-gutenberg-checkout-block.png)

For the Checkout v1 workflow, place the `[woocommerce_checkout]` shortcode directly on the Checkout page, or edit the Checkout page with Bricks and use a Shortcode element with `[woocommerce_checkout]` as its content. Bricks offers four template types to customize the checkout workflow:

- WooCommerce - Checkout
- WooCommerce - Thank you
- WooCommerce - Pay
- WooCommerce - Order receipt

![](https://academy.bricksbuilder.io/assets/bricks-woocommerce-checkout-templates.png)

> **Note**
>
> The "WooCommerce - Checkout", "WooCommerce - Pay", "WooCommerce - Thank you", and "WooCommerce - Order receipt" template types are only visible if you have the WooCommerce plugin installed and active. These templates are used inside the WooCommerce checkout shortcode logic and **they do not support template conditions (they are automatically rendered on the correct page)**.

## Checkout template {#checkout-template}

The default checkout page consists of a two-columns layout: one column with the billing and shipping details form and another one with the order summary + a button to proceed with the order.

![](https://academy.bricksbuilder.io/assets/bricks-woocommerce-checkout-screen.png)

<figcaption>

Bricks default WooCommerce default checkout screen

</figcaption>

Use the **WooCommerce - Checkout** template type to change the appearance of this first checkout screen.

When editing this template with Bricks you’ll see two new elements (specific to this template type):

![](https://academy.bricksbuilder.io/assets/bricks-woocommerce-checkout-elements.png)

### Checkout customer details

The checkout customer details element renders the billing and shipping details form.

You'll be able to remove/hide some of the non-required fields (e.g. Company name) and style the form fields.

### Checkout order review

The checkout order review element renders the order summary, the available payment methods, and the button to place the order. Using this element, you'll be able to style its different parts.

### Remove the checkout coupon form {#remove-coupon-form}

If you have enabled the use of coupons in the WooCommerce general settings you'll notice a blue coupon form on the top of the checkout form page. If you want to remove this form from the checkout page you may hide it using custom CSS or adding the following code to your child theme:

```php
remove_action( 'woocommerce_before_checkout_form', 'woocommerce_checkout_coupon_form', 10 );
```

### Checkout Coupon & Checkout Login elements {#checkout-coupon-login}

Starting at version 1.11.1 you have greater control over the location and design of the checkout coupon & login by enabling and using the following two checkout elements:

- [Checkout Coupon element](https://academy.bricksbuilder.io/integrations/woocommerce/element-checkout-coupon/)
- [Checkout Login element](https://academy.bricksbuilder.io/integrations/woocommerce/element-checkout-login/)

## Thank you template {#thank-you-template}

After placing an order, and depending on the payment workflow, you'll get to the "Thank you" screen.

![](https://academy.bricksbuilder.io/assets/bricks-woocommerce-checkout-thank-you.png)

<figcaption>

The Bricks default **Thank You** screen

</figcaption>

To style this screen, you'd create a Bricks template of type **WooCommerce - Thank you**. And insert the **Checkout Thank You** element to customize the thank you message, and modify the styles of the different components of the order details.

### Failed-order messages

The classic Checkout Thank You element supports WooCommerce's `woocommerce_thankyou_order_failed_text` filter. Checkout v2 uses `{woo_order_failed_text}` for the failed-order message in newly generated Thank you blocks.

To use the filtered message in an existing Checkout v2 layout:

1. Open the assigned Checkout page in Bricks and select its **Thank you** state.
2. Find the message element inside the **Order failed** block.
3. Replace its text with `{woo_order_failed_text}` and save.

Keep the block's conditions, payment retry link, styling, and hooks. See [Failed-order text](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/#failed-order-text) for filter and preview behavior.

## Pay template {#pay-template}

For the situation where the visitor gets a link to pay for an unpaid order, there's a special checkout screen that contains the order summary, the available payment gateways, and the button to pay for the order.

![](https://academy.bricksbuilder.io/assets/bricks-woocommerce-form-pay-default-471x1024.png)

<figcaption>

Default pay form screen with the representation of the Bricks elements

</figcaption>

If you would like to customize this screen you'd need to add a **WooCommerce - Pay** template type where you'll have access to two new elements: the **Checkout order table** and the **Checkout order payment** both with style controls to customize the look and feel.

## Order receipt {#order-receipt-template}

For the situation where the visitor gets a link to the unpaid order receipt, the checkout workflow triggers the `checkout/order-receipt.php` template, which by default will look like this:

![](https://academy.bricksbuilder.io/assets/bricks-woocommerce-order-receipt-default.png)

If you would like to customize this template you could add the Bricks **WooCommerce - Order receipt **template type and inside the builder, you'll have access to the order-specific Dynamic Data tags such as:

![](https://academy.bricksbuilder.io/assets/bricks-woocommerce-order-dynamic-data-tags.png)

`{woo_order_id}` - Returns the order id

`{woo_order_number}` - Returns the order number

`{woo_order_date}` - Returns the order date

`{woo_order_total}` - Returns the order total

`{woo_order_payment_title}` - Returns the order payment method name

`{woo_order_email}` - Returns the email address registered with the order

> **Note**
>
> **NOTE:** These Dynamic Data tags will also work inside the **WooCommerce - Thank you** template type.

Bricks 2.4 adds additional order tags and order-aware query loops for v2 layouts, including order items, totals, downloads, actions, and customer notes. See [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/#order-tags).

---

<a id="integrations-woocommerce-create-custom-mini-cart-dynamic-fragment"></a>

# Create a custom mini cart with Dynamic fragment

Source: https://academy.bricksbuilder.io/integrations/woocommerce/create-custom-mini-cart-dynamic-fragment/

*Build a WooCommerce mini cart that refreshes after cart changes using Dynamic fragment, the Cart contents query loop, and cart dynamic tags.*

Use the Dynamic fragment element when you need cart-dependent content outside the main Cart page, such as a custom mini cart in a header Offcanvas, dropdown, or popup.

Dynamic fragment re-renders itself and its children after WooCommerce cart changes. For a mini cart, place the cart item loop and cart totals inside the fragment so product rows, quantities, subtotal, and buttons stay current after add-to-cart, remove, and quantity changes.

> **Note**
>
> Dynamic fragment requires **Bricks > Settings > WooCommerce > Enable advanced modular elements**.

## Common setup

Mini carts are usually added to a header template and shown in an Offcanvas:

- The header contains the cart icon and cart count.
- The cart icon toggles the Offcanvas.
- The Offcanvas contains the generated mini cart structure.

Place the generated mini cart in a dropdown or popup for smaller layouts. Use an Offcanvas when you want more room for product rows, quantity controls, totals, and checkout actions.

## Create the Offcanvas mini cart

1. Open the header template or page where the mini cart should appear.
2. Add an **Offcanvas** element.
3. Inside the Offcanvas content area, add a **Dynamic fragment** element.
4. In the Dynamic fragment controls, go to **Insert a structure**.
5. Select **Mini cart**.
6. Click **Generate**.

![](https://academy.bricksbuilder.io/assets/dynamic-fragment-offcanvas-mini-cart.png)

Bricks appends the generated structure inside the Dynamic fragment. It does not replace existing child elements.

## What Bricks generates

The generated Mini cart structure already includes the cart item layout, totals, and buttons. You do not need to add these manually unless you want to change the design or content.

Inside the Dynamic fragment, Bricks creates:

- A **Details wrapper** that contains the mini cart content.
- A **Cart loop** using the **Cart contents** query type.
- A cart row inside the loop with product image, product title, product price, product excerpt, item data, quantity control, remove icon, and line subtotal.
- An empty-cart message from the Cart contents query loop.
- A separate block after the Cart loop for the subtotal and action buttons.
- A condition on that subtotal/actions block so it only shows when the Cart loop has more than `0` results.
- **View Cart** and **Checkout** buttons using WooCommerce URL dynamic data.

![](https://academy.bricksbuilder.io/assets/dynamic-fragment-mini-cart-structure-example.png)

## What the generated structure uses

The generated cart row uses WooCommerce cart tags inside the **Cart contents** loop.

Common row tags:

| Tag or element | Use |
| --- | --- |
| `{featured_image}` | Product image. |
| `{woo_cart_product_title:plain}` | Product title as plain text, without variation metadata. |
| **Cart item data** | Variation attributes and compatible extension-provided item data. |
| `{woo_cart_quantity}` | Quantity input. |
| `{woo_cart_quantity:value}` | Quantity number as text. |
| `{woo_cart_subtotal}` | Line subtotal. |
| `{woo_cart_remove_link:url}` | Remove URL for a link or icon. |

For a custom row, use `{woo_cart_item_price}` when you need the formatted unit price with sale-price markup. `{woo_cart_item_save}` returns the quantity-aware product savings and can be used in a condition through `{woo_cart_item_save:value}`.

The subtotal and buttons are outside the Cart contents loop, but still inside the Dynamic fragment. The generated structure uses:

| Element              | Dynamic data                |
| -------------------- | --------------------------- |
| Subtotal amount      | `{woo_cart_order_subtotal}` |
| View Cart button URL | `{woo_url:cart}`            |
| Checkout button URL  | `{woo_url:checkout}`        |

The generated remove icon uses `{woo_cart_remove_link:url}` as its link URL. Keep the `product-remove` CSS class on the remove element so WooCommerce cart behavior can target it.

![](https://academy.bricksbuilder.io/assets/dynamic-fragment-offcanvas-mini-cart-subtotal-condition.png)

## Add a header cart icon

In the header template, add a second Dynamic fragment near the navigation for the cart icon and count. This fragment only needs to contain the small cart trigger, not the full mini cart.

Inside that header Dynamic fragment:

1. Add an Icon element and choose a cart icon.
2. Add a Text Basic element for the cart count.
3. Set the count text to `{woo_cart_items_count}`.
4. Position the count as a small badge on the cart icon.
5. Add an element condition to the count so it only shows when `{woo_cart_items_count}` is greater than `0`.
6. Add an interaction to the cart icon:
   - **Trigger**: Click
   - **Action**: Toggle offcanvas
   - **Offcanvas: CSS selector**: the target Offcanvas element ID, such as `#brxe-evudao`

Because the icon and count are inside Dynamic fragment, the count updates after cart changes. Keep the rest of the header outside the Dynamic fragment unless it also depends on cart data.

![](https://academy.bricksbuilder.io/assets/dynamic-fragment-header-mini-cart-trigger.png)

![](https://academy.bricksbuilder.io/assets/dynamic-fragment-header-mini-cart-trigger-interaction.png)

## Open the Offcanvas after add to cart

You can open the mini cart Offcanvas when a product is added through AJAX.

On the Offcanvas element, add an interaction:

- **Trigger**: Added to cart
- **Action**: Toggle offcanvas
- **Offcanvas: CSS selector**: the Offcanvas element ID

Add a condition to the Offcanvas if you do not want this behavior on checkout. For example, show the Offcanvas only when the current URL does not contain `{woo_url:checkout}`.

![](https://academy.bricksbuilder.io/assets/dynamic-fragment-offcanvas-mini-cart-interaction.png)

Keep **Added to cart** for this interaction if the Offcanvas should toggle only after an addition. The [Bricks cart contents changed](https://academy.bricksbuilder.io/builder/features/interactions/#cart-contents-changed) trigger, available since Bricks 2.4, also runs after successful AJAX quantity changes and removals. Using it with **Toggle offcanvas** would toggle the mini cart during those updates too.

## Preview the refresh behavior

Dynamic fragment refreshes on the frontend after WooCommerce cart events such as add to cart, remove from cart, cart emptied, cart totals updated, checkout updated, and coupon apply/remove events.

The **Bricks dynamic fragments refreshed** interaction signals that fragment content has been replaced. It can run during initial synchronization or checkout recalculation without a cart item change. To show a custom “Cart updated” confirmation, use **Bricks cart contents changed**, which waits for a confirmed item change and the related UI updates to finish.

To test the mini cart:

1. Open the frontend page that contains the mini cart.
2. Add a product to the cart.
3. Confirm the mini cart updates without reloading the page.
4. Confirm the header cart count updates.
5. Click the cart icon and confirm the Offcanvas opens.
6. Remove the item or change quantity if your layout includes quantity controls.
7. Confirm the row count, subtotal, and buttons still render correctly.

![](https://academy.bricksbuilder.io/assets/dynamic-fragment-offcanvas-mini-cart-frontend-added-to-cart.png)

## Limits

- Dynamic fragment is frontend-only.
- Keep the Dynamic fragment wrapper outside other query loops. The Cart contents loop can be inside the fragment.
- Component instances are not supported.
- The fragment must render from the header, content, or footer area.
- Keep the fragment focused on cart-dependent content. Static header, menu, or layout elements do not need to be inside it.

## Related

- [Dynamic fragment element](https://academy.bricksbuilder.io/builder/elements/woocommerce/dynamic-fragment/)
- [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/)
- [WooCommerce advanced modular elements](https://academy.bricksbuilder.io/integrations/woocommerce/advanced-modular-elements/)

---

<a id="integrations-woocommerce-creating-dynamic-woocommerce-archive-pages"></a>

# Creating dynamic WooCommerce archive pages

Source: https://academy.bricksbuilder.io/integrations/woocommerce/creating-dynamic-woocommerce-archive-pages/

*Create dynamic WooCommerce archive pages in Bricks with product queries, archive templates, and WooCommerce-specific dynamic data.*

By following this tutorial, you will be able to create a custom WooCommerce archive template that can show product categories and products.

At the same time you can also use the **Shop page display** option and **Category page display** option to control when to show categories or products.

![](https://academy.bricksbuilder.io/assets/woocommerce-product-catalog-options.png)

<figcaption>

Appearance > Customize > WooCommerce > Product Catalog

</figcaption>

![](https://academy.bricksbuilder.io/assets/dynamic-woo-archive-result.gif)

<figcaption>

Example result

</figcaption>

## Step 1: Products & Product Categories Preparation

Ensure your product categories created included subcategories as well. Add some products and assigned them to different product categories. Best if you can add some images for each category, we will output them in the template too.

![](https://academy.bricksbuilder.io/assets/woocommerce-data-prepared-1024x643.png)

## Step 2: Create WooCommerce Archive

Remember to select the correct template type (**WooCommerce - Product archive**)
If you are not familiar with the Bricks product archive, you can learn more about them [here](https://academy.bricksbuilder.io/integrations/woocommerce/product-archive-woocommerce/).

![](https://academy.bricksbuilder.io/assets/woo-archive-template.png)

Set the conditions for the template in Settings > Template Settings > Conditions so it will be applied when browsing the WooCommerce shop page and product categories & tags archive pages.

![](https://academy.bricksbuilder.io/assets/woo-archive-template-conditions.png)

You have to create 2 different query loops and we will use condition to dynamically render them in actual frontend. In below example, 2 sections were created. 1 for the product categories loop, and another 1 for the products loop.

![](https://academy.bricksbuilder.io/assets/2-sections-for-2-loops.png)

## Step 3: Product Categories Section

> **Note**
>
> Important: You must enable code execution when using echo dynamic tag. Please also ensure the function names added in the `bricks/code/echo_function_names` hook. Reference: [Code Review](https://academy.bricksbuilder.io/builder/features/code-review/)

To show product categories dynamically, you will need to use `get_queried_object_id()` PHP function on Parent field. Simply use Bricks echo dynamic tag and set `{echo:get_queried_object_id}` on Parent field like below.

![](https://academy.bricksbuilder.io/assets/product-categories-loop-settings.png)

Additionally, we will also use `woocommerce_get_loop_display_mode()` PHP function from WooCommerce to conditionally display this section.

`woocommerce_get_loop_display_mode()` will return either **products**, **subcategories**, or **both** (in string) based on your settings.

![](https://academy.bricksbuilder.io/assets/woocommerce_get_loop_display_mode.png)

Let's set the condition on the categories section like this:

Use `{echo:woocommerce_get_loop_display_mode}` != products

![](https://academy.bricksbuilder.io/assets/product-categories-section-condition-settings.png)

<figcaption>

This section will show if you are not selecting Show products

</figcaption>

Here are the settings for the looping images and text of my example.`{woo_product_cat_image}` to output the category image. `{term_name:link}` to output the category text with link

![](https://academy.bricksbuilder.io/assets/looping-term-settings.png)

## Step 4: Products Section

Query settings for products are pretty straightforward, just control how many posts per page will do.

![](https://academy.bricksbuilder.io/assets/products-loop-settings.png)

Let's set the condition on the products section like this:

Use `{echo:woocommerce_get_loop_display_mode}` != subcategories

![](https://academy.bricksbuilder.io/assets/products-condition-settings-01.png)

<figcaption>

Products section will shows if you are not selecting Show subcategories / Show categories

</figcaption>

Here are the settings for the looping product for your reference. (Only focus on the dynamic tag I used instead of the style)

![](https://academy.bricksbuilder.io/assets/looping-product-settings.png)

![](https://academy.bricksbuilder.io/assets/product-structure.png)

In case your product has multiple product categories checked, but you wish to output the first checked category only so the green box wouldn't be too long, you can use this simple custom function. Just replace the `{post_terms_product_cat}` with `{echo:product_first_category_name}`

```php
// Place in your child theme functions.php
// Returns the first category name of a product
function product_first_category_name() {
	global $product;
	if( $product && is_a( $product, 'WC_Product' ) ) {
		// Get the product categories
		$terms = get_the_terms( $product->get_id(), 'product_cat' );

		$cats = [];

		// Loop through the categories, and add them to the $cats array
		foreach( $terms as $term ) {
			$cats[] = $term->name;
		}

		// Return the first category
		if( ! empty($cats) ) {
			ob_start();
			echo $cats[0];
			return ob_get_clean();
		}
	}
}

```

## Check Result

Now, your shop page and product category pages should be able to work as expected. You can always control when to display the product categories section and products section via the settings in the WordPress dashboard under **Appearance > Customize > WooCommerce > Product Catalog**

![](https://academy.bricksbuilder.io/assets/dynamic-woo-archive-final-result.gif)

<figcaption>

Custom WooCommerce Archive Template

</figcaption>

---

<a id="integrations-woocommerce-element-checkout-coupon"></a>

# Element: Checkout Coupon

Source: https://academy.bricksbuilder.io/integrations/woocommerce/element-checkout-coupon/

*Use the Bricks Checkout Coupon element inside WooCommerce checkout templates to render and style the coupon form.*

This Checkout coupon element, available @since 1.11.1, allows you to display the coupon field in various locations on the checkout page, making it easy for customers to apply discount codes during their purchase.

In previous versions, you couldn’t control the location of the checkout coupon. Additionally, styling options were limited, and adjustments required custom CSS. With this new, dedicated checkout coupon element you now have greater control over placement and design.

To use this element, first enable it under **`Bricks > Settings > WooCommerce`** by turning on **`Enable Bricks WooCommerce "Checkout coupon" element`**.

![](https://academy.bricksbuilder.io/assets/woocommerce-checkout-coupon-setting.png)

> **Note**
>
> WooCommerce **`Enable the use of coupon codes`** must also be active under **WooCommerce > Settings > General**. When the Bricks Checkout Coupon element is enabled, the native WooCommerce checkout coupon form is removed, so add this element where you want the coupon form to appear.

> **Note**
>
> **Note:** This element is specifically designed for the Checkout page and will only work when placed on the **Checkout template** or the Checkout page itself, depending on your design requirements.

**Key Controls**

**Location:**

- By default, the **Checkout Coupon** element will appear where it’s placed in the layout. However, you can choose alternative positions, such as: Before Order Review Heading, After Order Review Heading, Before Payment
- Custom location settings only apply on the actual frontend (Checkout page). To ensure correct placement, add this element at the top of your Checkout template.

![](https://academy.bricksbuilder.io/assets/woocommerce-checkout-coupon-element-controls.png)

![](https://academy.bricksbuilder.io/assets/element-location-example.png)

You can set the form to be toggle-able, hiding it by default and revealing it only when the toggle is clicked, for a cleaner layout.

---

<a id="integrations-woocommerce-element-checkout-login"></a>

# Element: Checkout Login

Source: https://academy.bricksbuilder.io/integrations/woocommerce/element-checkout-login/

*Use the Bricks Checkout Login element inside WooCommerce checkout templates to render and style the returning-customer login prompt.*

The Checkout Login element allows for a convenient login option directly on the checkout page, enabling returning customers to sign in before completing their purchase.

This feature becomes available once you've enabled **`Enable log-in during checkout`** under **`WooCommerce > Settings > Accounts & Privacy`**.

In previous versions, the placement of the checkout login form was fixed, and styling options were limited, requiring custom CSS for adjustments. Now, you can control both placement and appearance.

![](https://academy.bricksbuilder.io/assets/woocommerce-enable-login-during-checkout.png)

To use this element, activate it under **`Bricks > Settings > WooCommerce`** by toggling on **`Enable Bricks WooCommerce "Checkout login" element`**.

![](https://academy.bricksbuilder.io/assets/woocommerce-checkout-login-setting.png)

> **Note**
>
> When the Bricks Checkout Login element is enabled, the native WooCommerce checkout login form is removed. Add this element where you want the returning-customer login prompt to appear. The WooCommerce **`Enable log-in during checkout`** setting must stay enabled; on the frontend, the element does not render for users who are already logged in.

> **Note**
>
> **Note:** This element is specifically intended for the Checkout page. Place it within the **Checkout template** or directly on the Checkout page, depending on your design needs.

**Key Controls**

**Location:**

- By default, the **Checkout Login** element will appear where it’s placed in the layout. However, you can choose alternative positions, such as: Before Order Review Heading, After Order Review Heading, Before Payment.
- Custom location settings only apply on the frontend. To ensure the login form appears in the desired location, add this element at the beginning of your Checkout template.

![](https://academy.bricksbuilder.io/assets/woocommerce-checkout-login-element-controls.png)

![](https://academy.bricksbuilder.io/assets/element-location-example.png)

You can set the form to be toggle-able, hiding it by default and revealing it only when the toggle is clicked, for a cleaner layout.

---

<a id="integrations-woocommerce-how-to-create-product-quick-view-with-bricks"></a>

# How to Create Product Quick View with Bricks

Source: https://academy.bricksbuilder.io/integrations/woocommerce/how-to-create-product-quick-view-with-bricks/

*Create a WooCommerce product quick view in Bricks so shoppers can preview products without leaving the current listing page.*

## Step 1: Design a Popup Template for Quick View

Begin by designing the popup template that will be used for the Quick View functionality. Incorporate essential elements such as the Product Gallery, Product Rating, Product Price, and Add to Cart button.

Additionally, consider including a WooCommerce Notice element within the popup to display any notifications or confirmations directly to the user after an add-to-cart action.

It's crucial to implement the appropriate template hooks, similar to those used in a standard single product page. If you're unfamiliar with template hooks, we recommend reviewing [this article](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-template-hooks/#single-product-template-hooks) for further guidance.

Below is an example of a WooCommerce Quick View Popup design:

![](https://academy.bricksbuilder.io/assets/woo-quick-view-design-example.png)

## Step 2: Configure Popup settings

To proceed, ensure that you have enabled the **"WooCommerce Quick View"** (@since 1.10.2) and **"Fetch content via AJAX"** options in **Settings > Template Settings > Popup**.

Enabling the **AJAX loader** will enhance the user experience by providing a smoother interaction with the Quick View Popup.

> **Note**
>
> Do not set any template condition for the popup template as we will embed it in the Products loop.

![](https://academy.bricksbuilder.io/assets/woo-quick-view-popup-control.png)

## Step 3: Create a Product Query Loop

Proceed by creating a Product query loop on a new page or within your Shop page template. Insert the necessary elements according to your specific requirements.

Include the appropriate [template hooks](https://academy.bricksbuilder.io/integrations/woocommerce/product-archive-woocommerce/) within the loop to ensure that any WooCommerce third-party plugins can effectively apply their logic within your Product query loop.

![](https://academy.bricksbuilder.io/assets/woo-quick-view-query-loop-example.png)

## Step 4: Insert Popup template and Configure Interaction to Trigger Quick View Popup

Within the product query loop, insert a Template element and select the popup template you created in Step 1.

For a cleaner HTML structure, you may choose to enable the "Render without wrapper" option.

![](https://academy.bricksbuilder.io/assets/woo-quick-view-template-element-location.png)

![](https://academy.bricksbuilder.io/assets/woo-quick-view-popup-template-element.png)

Instead of using the Add to Cart element within the loop, utilize a Button element.

To ensure this button triggers the Quick View popup, configure the interaction as shown in the following screenshot:

![](https://academy.bricksbuilder.io/assets/woo-quick-view-button-interaction.png)

## Summary

By following these steps, you've successfully implemented a Quick View Popup feature using Bricks.

This enhancement not only improves the user experience by allowing visitors to quickly access product details without navigating away from the current page, but it also provides a seamless integration with WooCommerce.

Remember, fine-tuning the design and interaction settings can further optimize the effectiveness of the Quick View feature, ensuring it meets your specific needs and enhances your overall site performance.

---

<a id="integrations-woocommerce"></a>

# WooCommerce

Source: https://academy.bricksbuilder.io/integrations/woocommerce/

*Build WooCommerce shop, product, cart, checkout, account, and notice experiences with Bricks templates, elements, and integration guides.*

Bricks includes dedicated WooCommerce elements and template workflows so you can build the full storefront experience visually while still working with WooCommerce data and hooks.

## WooCommerce guides

- [WooCommerce Builder](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-builder/) for the main workflow
- [WooCommerce advanced modular elements](https://academy.bricksbuilder.io/integrations/woocommerce/advanced-modular-elements/) for the Bricks 2.4 Cart, Checkout, and My Account v2 workflow
- [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) for guided WooCommerce setup checks and presets
- [Checkout v2 multistep checkout](https://academy.bricksbuilder.io/integrations/woocommerce/multistep-checkout-v2/) for the multistep checkout workflow
- [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/) for the v2 data reference
- [Product Archive](https://academy.bricksbuilder.io/integrations/woocommerce/product-archive-woocommerce/) for shop and archive layouts
- [Single Product](https://academy.bricksbuilder.io/integrations/woocommerce/single-product/) for product detail pages
- [Product Quick View](https://academy.bricksbuilder.io/integrations/woocommerce/how-to-create-product-quick-view-with-bricks/) for quick-view popup workflows
- [Product Variation Swatches](https://academy.bricksbuilder.io/integrations/woocommerce/product-variation-swatches/) for color, image, and label swatches
- [Cart](https://academy.bricksbuilder.io/integrations/woocommerce/cart/) for cart layouts
- [Checkout](https://academy.bricksbuilder.io/integrations/woocommerce/checkout/) for checkout flows
- [WooCommerce Account Builder](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-account-builder/) for account templates
- [WooCommerce Template Hooks](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-template-hooks/) for hook-aware template work
- [WooCommerce Notices](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-notices/) for notice styling and output

---

<a id="integrations-woocommerce-multistep-checkout-v2"></a>

# Checkout v2 multistep checkout

Source: https://academy.bricksbuilder.io/integrations/woocommerce/multistep-checkout-v2/

*Create and customize a multistep WooCommerce checkout with Checkout v2, checkout step elements, navigation, validation, and interactions.*

Checkout v2 can split the WooCommerce checkout form into multiple editable steps while keeping the native WooCommerce checkout form and submission flow in place.

Use this workflow when you want a guided checkout experience with separate sections for account login, customer details, shipping, extras, order review, and payment.

![](https://academy.bricksbuilder.io/assets/checkout-v2-multistep-frontend.png)

> **Note**
>
> Checkout v2 multistep checkout requires **Bricks > Settings > WooCommerce > Enable advanced modular elements**.

## Create a multistep checkout

You can create a multistep Checkout v2 layout in either of these ways:

- Go to [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/), choose the Checkout area, then select **Advanced multistep (v2)**.
- Edit the assigned Checkout page with Bricks, select the Checkout v2 **Checkout** state, choose **Complete checkout** under **Insert a structure**, enable **Generate as multistep**, then click **Generate**.

![](https://academy.bricksbuilder.io/assets/checkout-v2-multistep.png)

The generated structure adds the checkout form sections, checkout step wrappers, step navigation, and next/back interactions for a complete starter flow.

## Generated structure

A multistep checkout uses these generated support elements:

- **Checkout steps navigation**: Displays the step navigation list.
- **Checkout step nav item**: One navigation item inside the steps navigation.
- **Checkout step**: Wraps the content for one checkout step.
- **Checkout account fields**, **Checkout billing address**, **Checkout shipping address**, **Payment options**, **Place order**, and other generated checkout support elements.

Some of these support elements are generated-only or context-specific. If you do not see them in the regular Elements panel, create them through **Insert a structure** instead. After generation, you can select, style, move, and edit them in the Structure panel like other Bricks elements.

![](https://academy.bricksbuilder.io/assets/checkout-v2-multistep-structure-example.png)

## Step order and navigation

Checkout step order follows the order of the **Checkout step** elements in the Structure panel. The first step is the initial step.

Navigation items mirror the checkout steps by order. If a checkout step is conditional, add the same condition to the matching navigation item so the visible navigation and visible steps stay aligned.

For the Shipping step, use **Checkout : Needs shipping** with a value of **Yes** on both the step and its navigation item. Use **Checkout : Needs shipping address** only on the **Ship to another address** control and shipping-address fields. A cart can still require shipping methods when WooCommerce is set to use the billing address for shipping.

Newly generated complete checkout structures include these conditions. If the layout was generated earlier or customized, review the Shipping step, navigation item, and address-field conditions manually because preset changes do not rewrite existing page content.

Each Checkout step has these controls:

- **Step ID**: Used by navigation, interactions, and direct step jumps.
- **Step label**: Used as the step label.
- **Allow direct entry**: Lets the customer jump to this step even if previous steps have not been reached.
- **Validate before leave**: Requires the current step to pass checkout field validation before moving forward.
- **Auto focus first field**: Focuses the first available field when the step becomes active.

Use stable, readable step IDs such as `customer-info`, `shipping`, `order-review`, or `payment` when you plan to target a step with interactions.

## Account Login step visibility

The generated complete multistep structure adds **Checkout : Login step needed** conditions to the Account Login navigation item, the Account Login step, and the Customer info Back button.

- Logged-out customer and **Enable log-in during checkout** enabled: Account Login is the first step, and Customer info includes a Back button.
- Logged-out customer and **Enable log-in during checkout** disabled: Account Login is not rendered. Customer info becomes the first step and has no Back button.
- Logged-in customer: Account Login and the Customer info Back button are not rendered.

If you build a custom multistep structure, apply the same **Checkout : Login step needed** condition to all three elements. Keeping the navigation item, step, and Back button under the same condition prevents an empty first step or a Back button with no previous step.

Account creation fields follow the WooCommerce checkout settings separately from the Account Login step. See [Checkout v2 account creation](https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-v2/#account-creation-during-checkout).

## Step buttons and interactions

Generated multistep layouts use regular Bricks buttons with the **Checkout step** interaction action.

The action can:

- Move to the next step.
- Move to the previous step.
- Go to a specific step by Step ID.
- Go to a specific checkout field by field key or field ID, such as `billing_postcode`.
- Scroll the target step or field into view.

![](https://academy.bricksbuilder.io/assets/interaction-checkout-step-action.png)

Use the **Bricks checkout step changed** interaction trigger when you need to run another action after the active checkout step changes.

## Step numbers

For the navigation element, enable **Show step number** on **Checkout steps navigation** to render step numbers with CSS.

Inside custom headings or labels, use `{woo_checkout_current_step_number}` to output the current step number dynamically.

## Validation

Enable **Validate before leave** on a Checkout step when the customer must complete required fields before moving forward.

Backward navigation is always allowed. Forward navigation checks the current step only when **Validate before leave** is enabled.

Free orders do not require a payment method selection. Required terms still apply, and orders that require payment must have a selected payment method.

WooCommerce notices can still link to invalid fields. The checkout step script can route the customer to the step that contains the field and focus it.

## Payment section for free orders

The generated **Payment Options** wrapper uses `brx-woo-payment-section` to hide the payment heading and methods when the cart does not require payment. If this class is missing from an existing or custom layout, add it manually under **Style > CSS > CSS classes** on that wrapper, without a leading dot.

Keep the terms checkbox, step buttons, and **Place order** controls outside the wrapper. Apply the class to the payment section inside the Checkout step, rather than the entire step. See [Checkout v2 payment section for free orders](https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-v2/#payment-section-for-free-orders) for the full steps.

## Recommended review

After generating the multistep layout:

- Test the checkout as a guest and as a logged-in customer.
- Test with **Enable log-in during checkout** both enabled and disabled.
- Test optional and required account creation with WooCommerce username and password generation enabled and disabled.
- Test products that require shipping and products that do not require shipping.
- Review conditional steps, such as account login and shipping.
- Confirm the final payment step contains the payment options, terms, and place order button.
- Test a zero-total order, then change shipping or remove a coupon so payment is required. Confirm the payment section reappears and the terms and Place order controls stay available in both cases.
- Test required field validation and WooCommerce notices.
- Review mobile spacing for the step navigation and buttons.

## Related docs

- [Checkout v2 element](https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-v2/)
- [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/)
- [WooCommerce advanced modular elements](https://academy.bricksbuilder.io/integrations/woocommerce/advanced-modular-elements/)
- [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/)

---

<a id="integrations-woocommerce-product-archive-woocommerce"></a>

# Product Archive (WooCommerce)

Source: https://academy.bricksbuilder.io/integrations/woocommerce/product-archive-woocommerce/

*Build WooCommerce product archive templates in Bricks for shop, category, tag, and other archive views.*

> **Note**
>
> The template type "WooCommerce – Product Archive" is only visible if WooCommerce is installed & active.

Create a template of type "WooCommerce – Product Archive" in Bricks to design your product archive pages (product categories, tags, attributes, etc.).

To create this template, go to the Bricks templates screen and add a new template. Then select the template type **"WooCommerce – Product Archive"** from the top-right dropdown:

![](https://academy.bricksbuilder.io/assets/woocommerce-template-type-product-archive.png)

Click "Publish" or "Save Draft". Then "Edit with Bricks" to open the builder.

It is also possible to create/edit this and other templates in the Bricks editor interface by clicking on the Folders icon or pressing CMD / CTRL + SHIFT + L.

> **Note**
>
> Please remember to add [template hooks](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-template-hooks/#product-archive-template-hooks) if you are using third-party plugins.

## Product Archive Elements {#elements}

![](https://academy.bricksbuilder.io/assets/woocommerc-product-archive-elements-580x1024.png)

### Archive title

There is no specific element to add a heading to the product archive.

To add a heading to this template you could use the Post Title element or add a Heading element with the `{archive_title}` tag.

### Breadcrumbs

Use the breadcrumbs element to output the navigation links from "Home", and higher level categories until the content displayed in the page.

This element uses the WooCommerce breadcrumbs default engine to generate each part of the breadcrumbs path.

### Products archive description

The products archive description will render the product category (or any other product taxonomy term) description.

If used in a template that renders the **Shop** page, it will output the page content (from the Gutenberg/blocks editor).

### Products

This is the main element to list products in a grid. You have controls to customize the style and layout, tweak the query, and select which content (fields) you want to show for each product.

This element interconnects with the **Products Filter**, **Products Pagination**, **Products Orderby** and the **Products Total Results** elements.

This means that the query results will be conditioned by the filters and the orderby conditions and it will also impact the pagination and the total results elements output.

The query used inside the products element to generate the grid of products will merge the query arguments from the element with the default WooCommerce query in the case the page rendered is the product archive or the product taxonomy archive (product category or product tag). This means that if you are seeing a certain product category archive page you only get a list of products from that category.

### Products filter

The products filter element allows you to add query filters to the page so the visitor could search/narrow down the list of products presented.

This element contains three filter types:

- **Taxonomy**: filter the list by one or multiple taxonomy terms.
- **Product attributes**: filter the list by product attributes like size, color or any other custom attribute used.
- **Others**: Special set of filters like a product **price dual-range slider**, a** stars rating** filter, a status **stock** filter or a simple **search** input. In this set, you will also find a **Reset filters** option which you would set to add a reset product filters button.

When using the taxonomy or product attributes filters, you may select different filter inputs, like a dropdown, a set of checkboxes, a radio list, a text list, or a box list.

### Products pagination

List of page links that allow the visitor to navigate through the different products' list pages.

### Products orderby

Adds a dropdown to the layout where the visitor could change the order of the products in the presented list. The default sort options are by popularity, by average rating, by latest, and by price (low to high and high to low). This list uses the WooCommerce default list and it can be extended using the WooCommerce hooks or third-party plugins.

### Products total results

Use this element to output the number of results returned by the current products query.

---

<a id="integrations-woocommerce-product-variation-swatches"></a>

# Product Variation Swatches (WooCommerce)

Source: https://academy.bricksbuilder.io/integrations/woocommerce/product-variation-swatches/

*Integrate WooCommerce product variation swatches with Bricks and understand how they behave inside builder templates.*

Bricks 2.0 introduces **Product variation swatches**, giving you more control over how product attribute options (i.e. color, size, pattern) appear on the frontend.

Instead of dropdowns, you can now display your product variations as **color swatches, image buttons, or custom labels**, creating a more visual and intuitive shopping experience.

This feature integrates directly into the **Add to cart** element, letting you style variation swatches exactly how you want, without the need for extra plugins.

![](https://academy.bricksbuilder.io/assets/bricks-woo-variation-swatches-before-1024x637.png)

<figcaption>

Before Product Variation Swatches

</figcaption>

![](https://academy.bricksbuilder.io/assets/bricks-woo-variation-swatches-after-1024x637.png)

<figcaption>

After Product Variation Swatches

</figcaption>

## Enable product variation swatches

To get started, go to **Bricks > Settings > WooCommerce > Enable product variation swatches**.

![](https://academy.bricksbuilder.io/assets/bricks-woo-variation-swatches-enable.png)

Once enabled, you’ll be able to customize variation swatches directly from your product attribute settings.

## Assign a swatch type to product attributes

Go to **Products > Attributes**, and click "Edit" on an existing attribute (or create a new one).

![](https://academy.bricksbuilder.io/assets/bricks-woo-variation-swatches-edit-attribute.png)

You’ll see a new **Swatch type** setting with the following options:

- **None (default)**: Standard WooCommerce behavior (dropdowns)
- **Color**: Displays swatches using color values
- **Label**: Displays custom text labels for each term
- **Image**: Displays swatches using images from your media library

![](https://academy.bricksbuilder.io/assets/bricks-woo-variation-swatches-attribute-settings.png)

**Example:** Use the "Color" swatch type to show red and blue color boxes, or choose "Label" for size options like S, M, L.

### Set a fallback value (optional)

While editing the attribute, you can also set a **Fallback value**. This fallback will be used if a specific term doesn't have its own swatch value.

For **Image** swatches, Bricks checks images in this order:

1. The image assigned to the individual term.
2. The matching product variation image, if **Use product variation image** is enabled for the attribute.
3. The attribute fallback image.

## Assign swatch values to individual terms

Next, click **Configure terms** for the attribute you just edited.

![](https://academy.bricksbuilder.io/assets/bricks-woo-variation-swatches-configure-terms.png)

Then, click **Edit** on a specific term (like “Red” or “Large”).

![](https://academy.bricksbuilder.io/assets/bricks-woo-variation-swatches-edit-term.png)

For each term, you’ll see a new input that matches the swatch type:

- **Color** → Choose a color
- **Image** → Select or upload an image
- **Label** → Add custom text

![](https://academy.bricksbuilder.io/assets/bricks-woo-variation-swatches-term-settings.png)

These values are what will be shown on the frontend in the Add to cart element.

## Style swatches in the Add to cart element

Variation swatches are rendered inside the **Add to cart** element, as long as your product uses attributes with a swatch type.

To style them:

1. Select the **Add to cart** element (e.g in your single product template)
2. Open the new **Variation swatches** group in the element settings

![](https://academy.bricksbuilder.io/assets/bricks-woo-variation-swatches-add-to-cart.png)

From there, you can adjust the size, spacing, borders, active states, tooltips, and more.

## Unavailable variation options

Bricks follows the availability state of the hidden WooCommerce variation dropdown. When WooCommerce disables an option for the current attribute combination, Bricks adds the `disabled` class and `aria-disabled="true"` to the matching swatch.

You can style unavailable swatches with custom CSS:

```css
.bricks-variation-swatches li.disabled,
.bricks-variation-swatches li[aria-disabled="true"] {
  opacity: 0.45;
  text-decoration: line-through;
}
```

There is no separate Bricks setting that forces every out-of-stock option to be hidden or disabled. If a swatch does not receive the disabled state, check the product's stock settings and the exact variation combination in WooCommerce first.

That's it. With variation swatches, you can now turn standard variation dropdowns into polished, interactive product selectors, designed your way, directly in the Bricks builder.

---

<a id="integrations-woocommerce-single-product"></a>

# Single Product (WooCommerce)

Source: https://academy.bricksbuilder.io/integrations/woocommerce/single-product/

*Build WooCommerce single product templates in Bricks and customize the main product layout, data, and related elements.*

> **Note**
>
> The template type "WooCommerce - Single Product" is only visible if WooCommerce is installed & active.

Create a template of type "WooCommerce - Single product" in Bricks to design an individual layout for the single products page.

To create this template, go to the Bricks templates screen and add a new template. Then select the template type **"WooCommerce - Single Product"** from the top-right dropdown:

![](https://academy.bricksbuilder.io/assets/WooCommerce-Template-Type-Single-Product.png)

Click "Publish" or "Save Draft". Then "Edit with Bricks" to open the builder.

It is also possible to create/edit this and other templates in the Bricks editor interface by clicking on the Folders icon or pressing CMD / CTRL + SHIFT + L.

> **Note**
>
> Please remember to add [template hooks](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-template-hooks/#single-product-template-hooks) if you are using third-party plugins.

## Single Product Elements {#elements}

When editing a "Single Product" template you'll find the "Products" elements at the very top of the elements panel:

![](https://academy.bricksbuilder.io/assets/woocommerc-single-product-elements-379x1024.png)

### Product title

The product title renders the title of the product.

### Product gallery

The product gallery element displays the product images defined in the product image and in the product gallery meta boxes.

*To disable the image zoom or lightbox, go to "Bricks > Settings > WooCommerce > Single Product".*

### Product short description

Renders the content of the Product short description editor.

### Product price

Renders the product price. If the product is on sale, you could hide the regular price.

### Product stock

Displays the number of products in stock. You can replace the number of products in stock with a custom message for "in", "low", or "out of stock".

### Product meta

Use the product meta element to display product data like the SKU, the product categories or tags, or any other WooCommerce metadata. Use [Dynamic Data](https://academy.bricksbuilder.io/builder/dynamic-content/dynamic-data/) to pull the values.

### Product rating

Shows the product's rating on a scale of 1 to 5 stars.

### Product content

Renders the product's main content as written in the WordPress editor.

### Add to cart

This element adds an "Add to cart" button to trigger the addition of this element to the cart. With this element, you may style the product variations inputs, the product stock, the quantity input, and the look & feel of the button itself.

### Related products

Shows a list of products that have the same product categories and tags of the main product displayed in the page.

### Product reviews

Renders the product reviews and review form as a standalone element. Do not use the Product reviews element together with the Product tabs element on the same page, as Product tabs can also output reviews.

### Product additional information

Renders the list of product attributes. This information will also be part of the product tabs element.

### Product tabs

Renders a section with the default tabs: Description, Additional Information, and Reviews. Other tabs might be added by third-party plugins.

### Product up/cross-sells

The product up/cross-sells element renders linked product recommendations. You can set it to show **Up-sells**, **Cross-sells**, or **Cart Cross-sells** (by default, it lists up-sell products).

![](https://academy.bricksbuilder.io/assets/woocommerce-product-upsells.png)

<figcaption>

WooCommerce product editor screen - Linked Products

</figcaption>

---

<a id="integrations-woocommerce-woo-setup-wizard"></a>

# Woo Setup Wizard

Source: https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/

*Create or repair Bricks WooCommerce shop, product, cart, checkout, and account layouts with guided setup checks and presets.*

The Woo Setup Wizard helps you check, create, and repair the main WooCommerce layouts used by Bricks.

Go to **Bricks > Woo Setup Wizard** to review the current setup status for the store. The wizard checks the Shop, Single product, Cart, Checkout, and My Account areas, then shows the available setup actions for each area.

![](https://academy.bricksbuilder.io/assets/woo-setup-wizard.png)

The wizard is not dependent on **Enable advanced modular elements**. It can set up the classic WooCommerce builder workflow without that setting. Advanced v2 setup types may appear in the wizard, but they stay disabled until advanced modular elements are enabled under **Bricks > Settings > WooCommerce > Enable advanced modular elements**.

## When to use it

Use the wizard when you want Bricks to review the WooCommerce setup and create the expected page or template structure for you.

- Set up WooCommerce pages after installing Bricks on a new store.
- Repair a Cart, Checkout, or My Account page that is missing the expected Bricks content.
- Replace WooCommerce block content with Bricks page content.
- Create the classic Bricks WooCommerce templates for shop, product, cart, checkout, or account areas.
- Create Cart v2, Checkout v2, or Account Page v2 structures for the assigned WooCommerce pages.
- Review whether existing published WooCommerce templates may conflict with a selected setup.

> **Caution**
>
> The wizard can replace Bricks page content, clear WooCommerce block markup from the assigned page, switch the page editor mode to Bricks, create Bricks templates, or draft existing published WooCommerce templates for the same area. Review the setup summary before running an action on an existing store.

## Areas checked

The wizard checks these WooCommerce areas:

- **Shop**: shop page and product archive template setup.
- **Single product**: single product template setup.
- **Cart**: assigned Cart page, classic cart templates, and Cart v2 page structure.
- **Checkout**: assigned Checkout page, classic checkout templates, and Checkout v2 page structure.
- **My Account**: assigned My Account page, classic account templates, and Account Page v2 page structure.

## Setup types

Each area can offer one or more setup types, depending on the selected WooCommerce area and whether advanced modular elements are enabled.

| Area | Setup types |
| --- | --- |
| Shop | Standard (v1) |
| Single product | Standard (v1) |
| Cart | Standard (v1), Advanced (v2) |
| Checkout | Standard (v1), Advanced (v2), Advanced multistep (v2) |
| My Account | Standard (v1), Advanced (v2) |

![](https://academy.bricksbuilder.io/assets/woo-setup-wizard-advanced-off.png)

**Standard (v1)** creates or repairs the classic Bricks WooCommerce workflow. This setup uses the assigned WooCommerce page together with the traditional Bricks WooCommerce template types or shortcode-based page content.

**Advanced (v2)** replaces the assigned WooCommerce page content with the matching v2 parent element and generated state structure. Use it for Cart, Checkout, and My Account pages when you want to edit related WooCommerce screens as states on one page.

**Advanced multistep (v2)** is available for Checkout. It creates a Checkout v2 page with a ready-made [multistep checkout structure](https://academy.bricksbuilder.io/integrations/woocommerce/multistep-checkout-v2/).

## Status checks

The wizard reports missing, incomplete, or incompatible setup details before you run an action.

Common checks include:

- Required WooCommerce page is not assigned.
- Assigned WooCommerce page was deleted.
- Assigned page is still edited with the WordPress editor instead of Bricks.
- Assigned page contains WooCommerce block content.
- Required v2 parent element is missing from the assigned page.
- Required v2 states are missing. My Account v2 includes Order withdrawal only when the WooCommerce feature is enabled.
- Required v2 state elements are empty.
- Existing published WooCommerce templates may conflict with the selected setup.
- Classic setup is missing expected WooCommerce shortcodes or template types.

![](https://academy.bricksbuilder.io/assets/woo-setup-wizard-errors.png)

The wizard does not create or assign missing WooCommerce pages. If a page is not assigned, assign it first in the WooCommerce settings, then return to **Bricks > Woo Setup Wizard**.

## What setup can change

Depending on the selected area and setup type, the wizard can:

- Write Bricks page content to the assigned WooCommerce page.
- Clear WordPress `post_content` when it contains WooCommerce block markup.
- Set the assigned page editor mode to Bricks.
- Create Bricks WooCommerce templates from presets.
- Draft existing published WooCommerce templates for the same template type when they would conflict.
- Generate external CSS files when file-based CSS generation is enabled.
- Ask for overwrite confirmation when the target page already contains Bricks data.

![](https://academy.bricksbuilder.io/assets/woo-setup-wizard-confirmation.png)

## Before running setup

Review the setup summary before confirming any action.

- Confirm the correct WooCommerce pages are assigned in the WooCommerce settings.
- Duplicate or export important pages and templates on existing stores.
- Check whether the selected setup edits pages, templates, or both.
- Review whether existing WooCommerce templates will be drafted.
- If the site uses custom breakpoints, review responsive styles after setup. Presets are authored with the default Bricks breakpoint keys, such as `mobile_landscape` and `mobile_portrait`.

## After setup

Open the generated page or template in Bricks and review the result.

- For classic layouts, confirm the expected WooCommerce template types and shortcodes are in place.
- For Cart v2, review the Filled cart and Empty cart states.
- For Checkout v2, review Checkout, Login required, Pay, Thank you, and Order receipt states.
- For Advanced multistep Checkout v2, test the checkout step navigation and interactions.
- For Account Page v2, review the account navigation, login, password, address, order, download, and edit account states. Include Order withdrawal when enabled.
- Test the live Cart, Checkout, and My Account flows with WooCommerce products and customer sessions.

## Related docs

- [WooCommerce Builder](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-builder/)
- [WooCommerce advanced modular elements](https://academy.bricksbuilder.io/integrations/woocommerce/advanced-modular-elements/)
- [Cart](https://academy.bricksbuilder.io/integrations/woocommerce/cart/)
- [Checkout](https://academy.bricksbuilder.io/integrations/woocommerce/checkout/)
- [WooCommerce Account Builder](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-account-builder/)

---

<a id="integrations-woocommerce-woocommerce-account-builder"></a>

# WooCommerce Account Builder

Source: https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-account-builder/

*Customize WooCommerce account-area screens in Bricks with the classic Account builder templates or the Account Page v2 advanced modular workflow.*

Bricks 1.9 introduces the My Account builder, which lets you customize the account area of your WooCommerce site.

This includes the My Account page (logged-in), the account login/register/lost & reset password pages (shown when not logged-in), and all My Account endpoints (e.g., Orders, Downloads, etc.).

> **Note**
>
> Starting in Bricks 2.4, you can also build the My Account page directly with [WooCommerce advanced modular elements](https://academy.bricksbuilder.io/integrations/woocommerce/advanced-modular-elements/) and the [Account Page v2 element](https://academy.bricksbuilder.io/builder/elements/woocommerce/account-page-v2/). The classic account template workflow below is still supported.

> **Note**
>
> **IMPORTANT:** In order to ensure that all your customizations to the WooCommerce My Account templates are properly applied, it is imperative that you complete the "[My Account Page (logged in)](#my-account-page)" step.

## Account Page v2 workflow

With advanced modular elements enabled, Account Page v2 keeps the account wrapper, navigation, login state, password states, and account endpoint states together on the assigned My Account page.

Use the [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) and choose **Advanced (v2)** to replace the assigned My Account page content with the Account Page v2 element and generated state structure.

Account Page v2 includes states for:

- Dashboard
- Orders
- View order
- Downloads
- Addresses
- Edit address
- Edit account
- Payment methods
- Add payment method
- Login
- Lost password
- Lost password confirmation
- Reset password
- Order withdrawal (WooCommerce 11.1 or later, with Order Withdrawal enabled)

Each state can generate a complete starter block through **Insert a structure**. Address and account forms use editable Bricks form field elements, so you can style and reorder them after generation.

The Account edit-address state has its own field sync because WooCommerce account address editing and checkout use different field contexts. Use it after plugins or WooCommerce settings change address fields.

Account Page v2 also adds query loops and dynamic tags for account orders, order actions, account downloads, account addresses, order data, downloads, and customer notes. See [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/#account-tags).

### Endpoints added by plugins

Account Page v2 provides editable states for the built-in WooCommerce account routes listed above. An endpoint registered by another plugin does not appear automatically as an additional editable state in the builder.

WooCommerce account endpoints are routes on the assigned My Account page, not separate WordPress pages. A plugin that registers an endpoint and its output callback correctly can still render its content through WooCommerce on that page, but Bricks does not provide a dedicated Account Page v2 state for designing that endpoint.

If a plugin endpoint is blank on the frontend, temporarily test the My Account page with WooCommerce's default account output or without the Account Page v2 element. If it remains blank, check the plugin's endpoint registration. If it works only without Account Page v2, include the plugin name and endpoint slug when contacting Bricks support.

## My Account Page (logged in) {#my-account-page}

To design your My Account page (navigation + content wrapper), **please edit your "My Account" page directly**. You'll find a dedicated "Account Page" element that you can add and adjust its settings to your liking.

![](https://academy.bricksbuilder.io/assets/bricks-woocommerce-my-account-page-1.png)

<figcaption>

Custom My Account page using the "Account - Page" element

</figcaption>

> **Note**
>
> **IMPORTANT:** If you have the *"Enable Bricks WooCommerce "Notice" element"* Bricks setting enabled, please make sure that you have added the "Notice" element to your account page or to all account templates individually. So the notifications when submitting the account forms (e.g., address, reset password, etc.) are displayed.

Starting in Bricks 2.4, the classic **Account - Page** element supports WooCommerce's native Order Withdrawal flow for guests and logged-in customers when the WooCommerce feature is enabled; use the [Account Page v2 Order withdrawal state](https://academy.bricksbuilder.io/builder/elements/woocommerce/account-page-v2/#order-withdrawal) to customize its layout.

## Account - Login / Register {#my-account-login-register}

The login form is displayed when a not-logged-in visitor views the My Account page. And the registration form, if you have the *"Allow customers to create an account on the "My account" page"* WooCommerce setting enabled.

You can design your account login/registration layout by creating a new template type "WooCommerce - Account - Login".

When editing this template, you'll find dedicated elements for the **"Account - Login form"** & **"Account - Register form"** as shown in the screenshot below:

You should also check the **Account creation** settings located at *WooCommerce > Settings > Accounts & Privacy* section to control what form to be displayed via **Account - Register form** element.

![](https://academy.bricksbuilder.io/assets/woocommerce-account-creation-settings.png)

![](https://academy.bricksbuilder.io/assets/bricks-woocommerce-account-login-register.png)

<figcaption>

Custom account login/register template

</figcaption>

> **Note**
>
> **IMPORTANT:** Ensure you have inserted a Basic Text element with `{do_action:woocommerce_before_customer_login_form}` before your Login and Register form. And another Basic Text element with `{do_action:woocommerce_after_customer_login_form}` after the forms.

![](https://academy.bricksbuilder.io/assets/woocommerce-do-action-account-login.png)

<figcaption>

Example do_action location. Before and after the login/register forms.

</figcaption>

## Account - Lost / reset password {#my-account-lost-reset-password}

The WooCommerce account builder in Bricks also provides the following dedicated templates and elements for the lost & reset password pages:

| **Account page** | **Template type** | **Elements** |
| --- | --- | --- |
| Lost password | WooCommerce - Account - Lost password | Account - Lost password |
| Lost password confirmation | WooCommerce - Account - Lost password (Confirmation) | Displayed after submitting the lost password form. No special elements.<br /><br />Example:<br />*A password reset email has been sent to the email address on file for your account, but may take several minutes to show up in your inbox. Please wait at least 10 minutes before attempting another reset.* |
| Reset password | WooCommerce - Account - Reset password | Account - Reset password |

## Templates for specific account endpoints {#my-account-endpoints}

Designing the account content area for individual account endpoints (Orders, Downloads, etc.) is possible by creating templates of the corresponding template type.

In the example below, we created a "WooCommerce - Account - Orders" template, to which we then added the "Account - Orders" that we styled a bit.

![](https://academy.bricksbuilder.io/assets/bricks-woocommerce-account-orders-1024x384.png)

> **Note**
>
> When editing the template for an account endpoint (Orders, Downloads, etc.), the drag & drop area is located inside the account content area. Offering a better preview in the builder than just rendering an empty canvas without the account navigation.

The process of creating those account endpoint templates is the same for all other WooCommerce account template types.

## Account template types & elements

| **Template type** | **Endpoint** | **Element** |
| --- | --- | --- |
| WooCommerce - Account - Dashboard | `/` | - |
| WooCommerce - Account - Orders | `orders/` | Account - Orders |
| WooCommerce - Account - View order | `view-order/{order_id}/` | Account - View order |
| WooCommerce - Account - Downloads | `downloads/` | Account - Downloads |
| WooCommerce - Account - Payment methods | `payment-methods/` | Account - Payment methods |
| WooCommerce - Account - Add payment method | `add-payment-method/` | Account - Add payment method |
| WooCommerce - Account - Addresses | `edit-address/` | Account - Addresses |
| WooCommerce - Account - Edit address | `edit-address/billing/`<br />`edit-address/shipping/` | Account - Edit address |
| WooCommerce - Account - Edit account | `edit-account/` | Account - Edit account |

---

<a id="integrations-woocommerce-woocommerce-template-hooks"></a>

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

<a id="integrations-woocommerce-woocommerce-builder"></a>

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

<a id="integrations-woocommerce-woocommerce-v2-query-loops-dynamic-tags"></a>

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

---

<a id="integrations-woocommerce-woocommerce-notices"></a>

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
