# Create Your Own Elements

Source: https://academy.bricksbuilder.io/developer/elements/create-your-own-elements/

*Create custom Bricks elements by extending the element API, registering controls, and rendering frontend output.*

The Bricks [child theme](https://academy.bricksbuilder.io/developer/guides/child-theme/), which you can download from your [Bricks account](https://my.bricksbuilder.io/) includes a simple custom element for demonstration purposes. The article below explains in more detail how to create your own elements programmatically.

Creating your own elements with Bricks follows a pattern similar to how you create WordPress widgets. You start by extending the `Bricks\Element` class and populate the required properties and methods for your element.

First, create a new file `element-test.php` in the root folder of your Bricks child theme.

## Blank element class {#builder}

```php
<?php
// element-test.php
if ( ! defined( 'ABSPATH' ) ) exit; // Exit if accessed directly

class Prefix_Element_Test extends \Bricks\Element {
  // Element properties
  public $category     = '';
  public $name         = '';
  public $icon         = '';
  public $css_selector = '';
  public $scripts      = [];
  public $nestable     = false; // true || @since 1.5

  // Methods: Builder-specific
  public function get_label() {}
  public function get_keywords() {}
  public function set_control_groups() {}
  public function set_controls() {}

  // Methods: Frontend-specific
  public function enqueue_scripts() {}
  public function render() {}
}
```

Let's walk through the element builder properties and methods:

| **$category** required | Category name (all lowercase, no spaces). Use any of the predefined element categories (e.g. `general`, `media`, etc.) or assign your own category name.<br /><br />When setting your own category make sure to provide a translatable category string for the builder using the filter: [bricks/builder/i18n](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-i18n/) |
| --- | --- |
| **$name** required | Unique element identifier (all lowercase, no spaces). To avoid any conflicts with other elements please prefix your element name, e.g.: `prefix-element-test`. |
| **$icon** | Icon font CSS class. Bricks includes the following icon fonts. Use any icon font CSS class to represent your element in the builder panel:  [Fontawesome 6](https://fontawesome.com/icons?d=gallery&m=free) (i.e. "fas fa-anchor") [Ionicons 4](https://ionicons.com/v4/cheatsheet.html) (i.e. "ion-md-alarm") [Themify Icons](https://themify.me/themify-icons) (i.e. "ti-bolt-alt") |
| **$css_selector** | By default all CSS control settings are applied to the element wrapper:  `.bricks-element-wrapper`. If you want the default CSS selector to target a child HTML element, set this selector here. |
| **$nestable** | Omit for plain elements. Set to `true` to create a [nestable element](https://academy.bricksbuilder.io/developer/elements/nestable-elements/). |
| **$scripts** | An array of JavaScript scripts that run when an element is rendered on the frontend or updated in the builder. The Counter element, for example, uses a script named "bricksCounter" (defined in *frontend.min.js*).<br /><br />To load this script we use: `public $scripts = ['bricksCounter'];`<br /><br />Please prefix all your scripts. E.g.: `prefixElementTest` |
| **get_label()** required | Return localised element label. |
| **get_keywords()** | Array of strings that when matched during the element search display the element in the search results. |
| **set_control_groups()** | By default, all element controls show ungrouped in the builder panel under the "Content" tab. Define custom control groups for your element controls by setting the following properties for each control group: **title** — Localized control group title. **tab** — Set to either "content" or "style". |
| **set_controls()** required | Define element controls. For an overview of all available controls and their settings visit: [Element Controls](https://academy.bricksbuilder.io/developer/controls/element-controls/) |
| **enqueue_scripts()** | Load element-specific scripts and styles. Those are loaded only on pages where this element is used. Results in better performance. Example: `wp_enqueue_script( 'prefix-element-test', get_template_directory_uri() . '/js/custom.js', ['jquery'], '1.0', true );` |
| **render()** required | Renders element HTML. Define HTML attributes via `$this->set_attribute()` and output them via `$this->render_attribute()` |
| **`set_attribute( $key, $attribute, $value )`** | Helper function to set HTML attributes for any HTML tag. `$key` serves as the unique identifier for this HTML tag. `$attribute` is the HTML attribute name. `$value` is a string or array which holds the attribute value(s). |
| **`render_attributes( $key )`** | Helper function to render HTML attributes defined via `$this->set_attribute()`. `$key` serves as the unique identifier for this HTML tag. |
| **`render_dynamic_data_tag( $tag, $context, $args )`** | Helper function to render dynamic data tags inside the render function using `$this->render_dynamic_data_tag(...)`. An example of a `$tag` is the `{post_title}`. Using this helper function sets the correct post Id depending on the environment where the element is being rendered. |
| **`render_dynamic_data( $content )`** | Helper function to render content (string) that could contain dynamic data tags. Use this helper function inside the render function calling `$this->render_dynamic_data(...)`. Using this helper function sets the correct post Id depending on the environment where the element is being rendered. |

Let's populate our element properties and methods with some data:

```php
<?php
// element-test.php

if ( ! defined( 'ABSPATH' ) ) exit; // Exit if accessed directly

class Prefix_Element_Test extends \Bricks\Element {
  // Element properties
  public $category     = 'general'; // Use predefined element category 'general'
  public $name         = 'prefix-test'; // Make sure to prefix your elements
  public $icon         = 'ti-bolt-alt'; // Themify icon font class
  public $css_selector = '.prefix-test-wrapper'; // Default CSS selector
  public $scripts      = ['prefixElementTest']; // Script(s) run when element is rendered on frontend or updated in builder

  // Return localised element label
  public function get_label() {
    return esc_html__( 'Test element', 'bricks' );
  }

  // Set builder control groups
  public function set_control_groups() {
    $this->control_groups['text'] = [ // Unique group identifier (lowercase, no spaces)
      'title' => esc_html__( 'Text', 'bricks' ), // Localized control group title
      'tab' => 'content', // Set to either "content" or "style"
    ];

    $this->control_groups['settings'] = [
      'title' => esc_html__( 'Settings', 'bricks' ),
      'tab' => 'content',
    ];
  }

  // Set builder controls
  public function set_controls() {
    $this->controls['content'] = [ // Unique control identifier (lowercase, no spaces)
      'tab' => 'content', // Control tab: content/style
      'group' => 'text', // Show under control group
      'label' => esc_html__( 'Content', 'bricks' ), // Control label
      'type' => 'text', // Control type
      'default' => esc_html__( 'Content goes here ..', 'bricks' ), // Default setting
    ];

    $this->controls['type'] = [
      'tab' => 'content',
      'group' => 'settings',
      'label' => esc_html__( 'Type', 'bricks' ),
      'type' => 'select',
      'options' => [
        'info' => esc_html__( 'Info', 'bricks' ),
        'success' => esc_html__( 'Success', 'bricks' ),
        'warning' => esc_html__( 'Warning', 'bricks' ),
        'danger' => esc_html__( 'Danger', 'bricks' ),
        'muted' => esc_html__( 'Muted', 'bricks' ),
      ],
      'inline' => true,
      'clearable' => false,
      'pasteStyles' => false,
      'default' => 'info',
    ];
  }

  // Enqueue element styles and scripts
  public function enqueue_scripts() {
    wp_enqueue_script( 'prefix-test-script' );
  }

  // Render element HTML
  public function render() {
    // Set element attributes
    $root_classes[] = 'prefix-test-wrapper';

    if ( ! empty( $this->settings['type'] ) ) {
      $root_classes[] = "color-{$this->settings['type']}";
    }

    // Add 'class' attribute to element root tag
    $this->set_attribute( '_root', 'class', $root_classes );

    // Render element HTML
    // '_root' attribute is required (contains element ID, class, etc.)
    echo "<div {$this->render_attributes( '_root' )}>"; // Element root attributes
      if ( ! empty( $this->settings['content'] ) ) {
        echo "<div>{$this->settings['content']}</div>";
      }
    echo '</div>';
  }
}
```

You can browse the documented Bricks controls at: [/developer/controls/](https://academy.bricksbuilder.io/developer/controls/)

> **Note**
>
> All element settings are stored in `$this->settings`. To view of element settings you can print them on the screen like so: `var_dump( $this->settings );` in the `render()` function.

## Load and register your element {#register}

After creating your custom element you need to load and register your element. Open up `functions.php` of your Bricks child theme and copy & paste the following code:

```php
/**
 * Register custom elements
 */
add_action( 'init', function() {
  $element_files = [
    __DIR__ . '/element-test.php',
  ];

  foreach ( $element_files as $file ) {
    \Bricks\Elements::register_element( $file );
  }
}, 11 );
```

The `register_element` method accepts 3 arguments:

- `$file` (required): The full path to the custom element PHP file in the server
- `$name` (optional): A string containing the name of the custom element (e.g.: `prefix-element-test`)
- `$element_class` (optional): A string containing the class name of the element (e.g.: `Prefix_Element_Test`) which should derive from the Bricks element class (`\Bricks\Element`)

> **Note**
>
> **Note:** Using the `$name` and `$element_class` arguments will improve the loading performance.

---

# Nestable Elements (API)

Source: https://academy.bricksbuilder.io/developer/elements/nestable-elements/

*Understand the Bricks API for nestable elements, including how parents, children, and allowed structures are defined.*

Bricks 1.5 introduces **Nestable Elements**. Plus an API that allows you to programmatically define your own custom elements that can contain other elements. In exactly the structure you want.

Prior to Bricks 1.5 every element in Bricks was "flat". Meaning even though an element contained a deep HTML structure (like the Slider, etc.) you couldn't click on an inner part of this element to edit it directly (e.g. contents of slide 3), or change the inner structure of it to your liking via Drag & Drop, as you could do inside a layout element.

Making it often impossible to properly customise more complex elements like the Icon Box, Pricing Table, List, etc.

Complex elements such as the Accordion, Slider, and Tabs weren't properly customisable at all.

## Full Access & Control Over Individual Element Structure

Starting at version 1.5, Bricks provides three nestable elements:

- Accordion (Nestable)
- Slider (Nestable)
- Tabs (Nestable)

Those elements were notoriously hard to properly customise due to their complex structure, and the limits of their "flat" element structure.

Now that you can populate every slide with the elements you want, purpose-specific slider-like elements such as the "Carousel" & "Team Members" are not really needed.

![](https://academy.bricksbuilder.io/assets/bricks-1.5-nestable-accordion-1024x398.jpg)

<figcaption>

Accordion - Nestable

</figcaption>

> **Note**
>
> Nestable elements are going to exist alongside their flat origin elements for the foreseeable future until we have collected enough feedback & fixed any major bugs in order to fully make the switch to nestable elements.

> **Note**
>
> Certain interactive nestable elements that are heavily JavaScript-driven (such as the Accordion, Slider, and Tabs) might prevent the Drag & drop from working 100% on the canvas. If you encounter this behavior you can always add & order elements by using the Structure panel too.

> **Note**
>
> **Nestable tabs**: If you need to change the `display` property of the tab "pane", please do so by adding another "Block" element inside the panel and setting the `display` setting there. The pane itself uses `display: none` in order to hide all non-active panes. If you change the display setting there, all tab panes will always be visible.

So you can start playing around with those new nestable elements, and slowly transition away from the old plain elements.

Over time we'll convert more and more `flat` elements into nestable elements, so that you'll be able to properly customize most elements in Bricks once their nestable equivalent becomes available.

## Nestable Elements API {#api}

The rest of this article shows how to programmatically create your own nestable elements.

A good starting point to learn about the new nestable elements syntax is to inspect the Bricks source code of the following nestable element files:

- accordion-nested.php
- slider-nested.php
- tabs-nested.php

### Define Your Custom Element As "nestable"

First make sure to set the [`$nestable`](https://academy.bricksbuilder.io/developer/elements/create-your-own-elements/#builder) property of your custom element class to `true`.

This is required so Bricks knows to render this custom element using the nestable render function in the builder, and to enable drag & drop inside the builder for this custom element.

### Nestable Element Template

You can define the structure of your custom element via the `get_nestable_children` function. It expects to return an array of element definitions.

This is best illustrated by having a look at the Nestable Slider elements' `get_nestable_children` function:

```php
public function get_nestable_children() {
  return [
      [
        'name'     => 'block',
        'label'    => esc_html__( 'Slide', 'bricks' ) . ' {item_index}',
        'settings' => [
          '_hidden' => [
            '_cssClasses' => 'hidden-class', // CSS class not visible in builder UI
          ],
        ],
        'children' => [
            [
              'name'     => 'heading',
              'settings' => [
                'text' => esc_html__( 'Slide', 'bricks' ) . ' {item_index}',
              ],
            ],
            [
              'name'     => 'button',
              'settings' => [
                'text'  => esc_html__( 'I am a button', 'bricks' ),
                'size'  => 'lg',
                'style' => 'primary',
              ],
            ],
          ],
      ],
  ];
}
```

The code above adds a "Slide" block inside the nestable slider, which then contains a "Heading" & "Button" element.

The `children` property, if set, accepts an array of further nested elements. Specify the `settings` array to populate individual elements inside your nestable element as needed.

### Nestable Render Function (PHP) {#php}

The only new function you need to add to your PHP `render()` function is called `render_children` and it requires the element instance `$this` to be passed as the first parameter:

```php
public function render() {
  $output = "<div {$this->render_attributes( '_root' )}>";

  // Render children elements (= individual items)
  $output .= Frontend::render_children( $this );

  $output .= '</div>';

  echo $output;
}
```

### Nestable Render Function (Vue x-template) {#x-template}

To render elements inside your nestable element in your custom x-template, simply add the `` component plus `element` props as shown in the following code snippet:

```php
public function render_builder() {
  <script type="text/x-template" id="tmpl-bricks-element-custom-nestable">
    <component :is="tag">
      <h2>Title before nestable children</h2>
      <bricks-element-children :element="element"/>
      <p>Text node after nestable children</p>
    </component>
  </script>
}
```

### Nestable Element Items (in panel)

If your nestable element structure is based on items on the same level (such as our Accordion above), then you can add a Repeater (see builder panel in screenshot above) by adding a `repeater` control with the `items` property set to `children`:

```php
public function set_controls() {
  // Array of nestable element.children (@since 1.5)
  $this->controls['_children'] = [
    'type'          => 'repeater',
    'titleProperty' => 'label',
    'items'         => 'children',
  ];
];
```

> **Note**
>
> If you are start using and/or experimenting with the new Nestable Elements API for your custom elements, [we'd love to hear your feedback](https://bricksbuilder.io/contact/). Does this API miss any features, did you encounter any bugs?
