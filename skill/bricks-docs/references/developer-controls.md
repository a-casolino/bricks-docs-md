# Apply Control

Source: https://academy.bricksbuilder.io/developer/controls/apply-control/

*Reference for the Bricks Apply control, including its options, CSS mapping, and usage in custom elements.*

The `apply` control saves your settings. You can set the `reload` control property to **true** in order to trigger a builder reload after the "Apply" button has been clicked. We use it in the builder for settings like the template "Populate Content" or the "SEO" page settings.

```php
$this->controls['apply'] = [
  'group' => 'template-preview',
  'type' => 'apply',
  'reload' => true,
  'label' => esc_html__( 'Apply preview', 'bricks' ),
];
```

---

# Align Items Control (Flexbox)

Source: https://academy.bricksbuilder.io/developer/controls/align-items-control/

*Reference for the Bricks Align Items Control (Flexbox) control, including its options, CSS mapping, and usage in custom elements.*

Use the align-items control to allow users to set the `align-items` CSS property (alignment along the [cross-axis](https://developer.mozilla.org/en-US/docs/Web/CSS/align-items)) of your CSS flexbox layout.

There is also a [`justify-content`](https://academy.bricksbuilder.io/developer/controls/justify-content-control/) control to allow users to set the alignment along the main axis of your CSS flexbox layout:

```php
public function set_controls() {
  $this->controls['alignItems'] = [ // Setting key
    'tab'   => 'content',
    'label' => esc_html__( 'Align items', 'bricks' ),
    'type'  => 'align-items',
    'css'   => [
      [
        'property' => 'align-items',
        'selector' => '.flexbox-wrapper',
      ],
    ],
    // 'isHorizontal' => false,
    // 'exclude' => [
      // 'flex-start',
      // 'center',
      // 'flex-end',
      // 'space-between',
      // 'space-around',
      // 'space-evenly',
    // ],
  ];
}
```

---

# Audio Control

Source: https://academy.bricksbuilder.io/developer/controls/audio-control/

*Reference for the Bricks Audio control, including its options, CSS mapping, and usage in custom elements.*

The audio control lets you select an audio file from the media library. It also gives you various options to show/hide artist and title, choose between a light/dark theme, autoplay the audio file, etc. It has no custom control parameters.

```php
class Prefix_Element_Audio extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['file'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Audio file', 'bricks' ),
      'type' => 'audio',
    ];
  }

  // Render element HTML
  public function render() {
    $settings = $this->settings;

    if ( isset( $settings['file']['url'] ) ) {
      echo wp_audio_shortcode( [
        'src'      => $settings['file']['url'],
        'loop'     => isset( $settings['loop'] ) ? $settings['loop'] : false,
        'autoplay' => isset( $settings['autoplay'] ) ? $settings['autoplay'] : false,
        'preload'  => isset( $settings['preload'] ) ? $settings['preload'] : 'none',
      ] );
    }
  }
}
```

### Resources

[https://codex.wordpress.org/Function_Reference/wp_audio_shortcode](https://codex.wordpress.org/Function_Reference/wp_audio_shortcode)

---

# Background Control

Source: https://academy.bricksbuilder.io/developer/controls/background-control/

*Reference for the Bricks Background control, including its options, CSS mapping, and usage in custom elements.*

The background control lets you set the following background properties:

- Background color
- Background image
- Background video (requires `bricksBackgroundVideoInit` script. See code example below)

There are various settings for the background image and video. You can exclude color/image/video settings via the `exclude` parameter.

As the background control serves most likely as a CSS setting the following example shows you how to set the `css` parameter to apply it to the elements' `.prefix-test-wrapper` HTML.

Adding a background video requires you to load the `bricksBackgroundVideoInit` script and use the `BricksFrontend::get_element_background_video_wrapper()` method to render it.

> **Note**
>
> When you just want to set a background color better use the [color control](https://academy.bricksbuilder.io/developer/controls/color-control/). The background control is handier when using a background image or video on top of the color.

```php
class Prefix_Element_Background extends \Bricks\Element {
  // Required for background video
  public $scripts = ['bricksBackgroundVideoInit'];

  // Set builder controls
  public function set_controls() {
    $this->controls['exampleBackground'] = [ // Setting key
      'tab' => 'content',
      'label' => esc_html__( 'Background', 'bricks' ),
      'type' => 'background',
      'css' => [
        [
          'property' => 'background',
          'selector' => '.prefix-background-wrapper',
        ],
      ],
      'exclude' => [
        // 'color',
        // 'image',
        // 'parallax',
        // 'attachment',
        // 'position',
        // 'positionX',
        // 'positionY',
        // 'repeat',
        // 'size',
        // 'custom',
        // 'videoUrl',
        // 'videoScale',
      ],
      'inline' => true,
      'small' => true,
      'default' => [
        'color' => [
          'rgb' => 'rgba(255, 255, 255, .5)',
          'hex' => '#ffffff',
        ],
      ],
    ];
  }

  // Render element HTML
  public function render() {
    echo '<div class="prefix-background-wrapper">';

    // Background video
    echo BricksFrontend::get_element_background_video_wrapper(
      ['settings' => $settings],
      'exampleBackground' // Setting key
    );

    echo get_bloginfo( 'name' );

    echo '</div>';
  }
}
```

---

# Border Control

Source: https://academy.bricksbuilder.io/developer/controls/border-control/

*Reference for the Bricks Border control, including its options, CSS mapping, and usage in custom elements.*

The border control lets you set the following border properties:

- Border width (top/right/bottom/left)
- Background style (top/right/bottom/left)
- Background color (none/solid/double/dotted/dashed)
- Border radius (top/right/bottom/left)

The example below illustrates how to apply a border via the `css` parameter and how to set border defaults.

```php
class Builder_Element_Prefix_Test extends \Bricks\Element {
  public function set_controls() {
    $this->controls['titleBorder'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Title border', 'bricks' ),
      'type' => 'border',
      'css' => [
        [
          'property' => 'border',
          'selector' => '.prefix-test-title',
        ],
      ],
      'inline' => true,
      'small' => true,
      'default' => [
        'width' => [
          'top' => 1,
          'right' => 0,
          'bottom' => 0,
          'left' => 0,
        ],
        'style' => 'solid',
        'color' => [
          'hex' => '#ffff00',
        ],
        'radius' => [
          'top' => 1,
          'right' => 1,
          'bottom' => 1,
          'left' => 1,
        ],
      ],

    ];
  }
}
```

---

# Box Shadow Control

Source: https://academy.bricksbuilder.io/developer/controls/box-shadow-control/

*Reference for the Bricks Box Shadow control, including its options, CSS mapping, and usage in custom elements.*

The box-shadow control is a CSS control and you can set the following properties:

- Offset X
- Offset Y
- Spread
- Blur
- Color
- Inset

```php
class Prefix_Element_Box_Shadow extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleBoxShadow'] = [
      'tab' => 'content',
      'label' => esc_html__( 'BoxShadow', 'bricks' ),
      'type' => 'box-shadow',
      'css' => [
        [
          'property' => 'box-shadow',
          'selector' => '.prefix-box-shadow-wrapper',
        ],
      ],
      'inline' => true,
      'small' => true,
      'default' => [
        'values' => [
          'offsetX' => 0,
          'offsetY' => 0,
          'blur' => 2,
          'spread' => 0,
        ],
        'color' => [
          'rgb' => 'rgba(0, 0, 0, .1)',
        ],
      ],
    ];
  }

  // Render element HTML
  public function render() {
    echo '<div class="prefix-box-shadow-wrapper">';
    echo get_bloginfo( 'name' );
    echo '</div>';
  }
}
```

### Resources

[https://developer.mozilla.org/en-US/docs/Web/CSS/box-shadow](https://developer.mozilla.org/en-US/docs/Web/CSS/box-shadow)

---

# Checkbox Control

Source: https://academy.bricksbuilder.io/developer/controls/checkbox-control/

*Reference for the Bricks Checkbox control, including its options, CSS mapping, and usage in custom elements.*

The checkbox control is a simple on/off switch. If enabled it outputs a boolean value of `true`. Disabled it returns `false`. You can use it to conditionally show/hide other content settings as we illustrate in the following code example:

```php
class Prefix_Element_Checkbox extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleCheckbox'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Show site title', 'bricks' ),
      'type' => 'checkbox',
      'inline' => true,
      'small' => true,
      'default' => true, // Default: false
    ];
  }

  // Render element HTML
  public function render() {
    // Show site title if setting checkbox 'exampleCheckbox' is checked
    if ( isset( $this->settings['exampleCheckbox'] ) ) {
      echo get_bloginfo( 'name' );
    }
  }
}
```

---

# Code Control

Source: https://academy.bricksbuilder.io/developer/controls/code-control/

*Reference for the Bricks Code control, including its options, CSS mapping, and usage in custom elements.*

The code control embeds a code editor utilizing the amazing CodeMirror library. Users for which you've enabled "**Code Execution**" in the Bricks settings, will be able to execute PHP, HTML, CSS, and JavaScript.

```php
class Prefix_Element_Code extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleHtml'] = [
      'tab' => 'content',
      'label' => esc_html__( 'HTML', 'bricks' ),
      'type' => 'code',
      'mode' => 'php',
      'default' => '<h4>Example H4 HTML title</h4>',
    ];
  }

  // Render element HTML
  public function render() {
    echo isset( $this->settings['exampleHtml'] ) ? $this->settings['exampleHtml'] : esc_html__( 'No HTML provided.', 'bricks' );
  }
}
```

> **Note**
>
> You don't need to define your own element CSS and JS controls. Those are already available when editing the element under the Style tab "CSS" control group.

---

# Color Control

Source: https://academy.bricksbuilder.io/developer/controls/color-control/

*Reference for the Bricks Color control, including its options, CSS mapping, and usage in custom elements.*

The color control is a custom-built color picker that you won't find anywhere else.

It lets you pick and adjust colors in `hex`, `rgba` and `hsl` format. It also includes a global color palette to save any color for later reuse anywhere else on your site.

Define your own default color palette with the `bricks/builder/color_palette` filter.

You can set the CSS `property` to `color` or `background-color` as illustrated in the example below.

```php
class Prefix_Element_Color extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    // Text color applied to '.prefix-element-test-title'
    $this->controls['exampleColor'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Title color', 'bricks' ),
      'type' => 'color',
      'inline' => true,
      'css' => [
        [
          'property' => 'color',
          'selector' => '.prefix-element-test-title',
        ]
      ],
      'default' => [
        'hex' => '#3ce77b',
        'rgb' => 'rgba(60, 231, 123, 0.9)',
      ],
    ];

    // Background color applied to '.prefix-element-test-content'
    $this->controls['exampleBackgroundColor'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Background color', 'bricks' ),
      'type' => 'color',
      'inline' => true,
      'css' => [
        [
          'property' => 'background-color',
          'selector' => '.prefix-element-test-content',
        ]
      ],
      'default' => [
        'hex' => '#1ebea5',
        'rgb' => 'rgba(30, 190, 165, 0.8)',
      ],
    ];
  }

  // Render element HTML
  public function render() {
    echo '<h5 class="prefix-element-test-title">' . get_bloginfo( 'name' ) . '</h5>';
    echo '<p class="prefix-element-test-content">Just some bogus text ..</p>';
  }
}

```

### Color palette filter

Add the following PHP code into the funcions.php file of your [chil](https://docs.bricksbuilder.io/article/71-child-theme)[d theme](https://academy.bricksbuilder.io/developer/guides/child-theme/) to add your own colors to the default color palette (option #1) or replace all default colors with your own choice of colors (option #2).

```php
// functions.php
add_filter( 'bricks/builder/color_palette', function( $colors ) {
  // Option #1: Add individual color
  $colors[] = [
    'hex' => '#3ce77b',
    'rgb' => 'rgba(60, 231, 123, 0.56)',
  ];

  // Option #2: Override entire color palette
  $colors = [
    ['hex' => '#3ce77b'],
    ['hex' => '#f1faee'],
    ['hex' => '#a8dadc'],
    ['hex' => '#457b9d'],
    ['hex' => '#1d3557'],
  ];

  return $colors;
} );
```

> **Note**
>
> If you have saved any custom colors with the builder you need to reset your global settings in order for your new default colors to take effect.

---

# Datepicker Control

Source: https://academy.bricksbuilder.io/developer/controls/datepicker-control/

*Reference for the Bricks Datepicker control, including its options, CSS mapping, and usage in custom elements.*

The datepicker control provides a great interface for selecting a specific date and time and outputting it in the [format of your choice](http://hilios.github.io/jQuery.countdown/documentation.html#directives).

The Datepicker control leverages the Flatpickr library to offer a robust date selection interface. Since Bricks 1.9.8 an `options` property has been added which allows for further customization.

## Properties:

### Property: options (since 1.9.8)

- **Type:** array (associative)
- **Description:** Enables customization of the datepicker by passing an associative array of options defined in the Flatpickr library.
- **Default values:**
  - **enableTime:** Defaults to `true` unless explicitly set through a passed property.
  - **altInput:** Defaults to `true` unless specified otherwise through a passed property.

**Example usage:**

```php
$this->controls['date'] = [
  'tab' => 'content',
  'label' => esc_html__('Date', 'bricks'),
  'type' => 'datepicker',
  'options' => [
    'enableTime' => true,  // Enables time selection.
    'time_24hr' => true,   // Displays time picker in 24-hour mode.
    'noCalendar' => true   // Hides the calendar day selection.
  ]
];
```

In this example, the `options` array is configured to create a time picker that operates in 24-hour format without showing a calendar for day selection. The `enableTime` option is set to true to ensure time can be selected, `time_24hr` is enabled for 24-hour time format, and `noCalendar` is set to true to hide the calendar component. Adjust the `options` array as needed to customize the datepicker to meet different requirements.

For a full list of customizable options available in Flatpickr, please refer to the [Flatpickr Options documentation](https://flatpickr.js.org/options/).

### Property: enableTime

- **Type:** boolean
- **Description:** Determines whether time selection is enabled. Overridden if any settings are passed in the `options` property.
- **Default:** true

### Property: altInput

- **Type:** boolean
- **Description:** Enables an alternative, more user-friendly input style. Overridden if any settings are passed in the `options` property.
- **Default:** true

## Example: Countdown element

```php
// Example: Countdown element
class Prefix_Element_Countdown extends \Bricks\Element {
  public $category = 'general';
  public $name     = 'countdown';
  public $icon     = 'ti-timer';
  public $scripts  = ['bricksCountdown'];

  public function get_label() {
    return esc_html__( 'Countdown', 'bricks' );
  }

  public function set_controls() {
    $this->controls['date'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Date', 'bricks' ),
      'type' => 'datepicker',
      'options' => ['enableTime' => true, 'altInput' => true],
      'default' => '2019-01-01 12:00',
    ];

    $this->controls['format'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Format', 'bricks' ),
      'type' => 'text',
      'default' => '%D days %H hours %M minutes %S seconds.',
      'description' => sprintf(
        '%s <a target="_blank" href="http://hilios.github.io/jQuery.countdown/documentation.html#directives">%s</a>.',
        esc_html__( 'For formatting options see', 'bricks' ),
        esc_html__( 'directives', 'bricks' )
      ),
    ];
  }

  public function render() {
    $this->set_attribute( 'wrapper', 'class', 'countdown-wrapper' );

    $countdown_options = [
      'date' => isset( $this->settings['date'] ) ? $this->settings['date'] : '',
      'format' => isset( $this->settings['format'] ) ? $this->settings['format'] : '',
    ];

    $this->set_attribute( 'wrapper', 'data-bricks-countdown-options', wp_json_encode( $countdown_options ) );

    // Render
    if ( ! isset( $this->settings['date'] ) || ! isset( $this->settings['format'] ) ) {
      return $this->render_element_placeholder( [
        'icon-class' => 'ti-timer',
        'text'       => esc_html__( 'No date/format set.', 'bricks' ),
      ] );
    } else {
      echo '<div ' . $this->render_attributes( 'wrapper' ) . '></div>';
    }
  }
}
```

---

# Dimensions Control

Source: https://academy.bricksbuilder.io/developer/controls/dimensions-control/

*Reference for the Bricks Dimensions control, including its options, CSS mapping, and usage in custom elements.*

The dimensions control is perfect for adding multi-directional CSS properties such as margin and padding (top/right/bottom/left). You can set the directions to anything you want via the `directions` property.

```php
class Prefix_Element_Dimensions extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleDimensions'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Title padding', 'bricks' ),
      'type' => 'dimensions',
      'css' => [
        [
          'property' => 'padding',
          'selector' => '.prefix-element-dimensions-title',
        ]
      ],
      'default' => [
        'top' => '30px',
        'right' => 0,
        'bottom' => '10em',
        'left' => 0,
      ],
      // 'unitless' => false, // false by default
      // Custom directions
      // 'directions' => [
        // 'offsetX' => esc_html__( 'Offset X', 'bricks' ),
        // 'offsetY' => esc_html__( 'Offset Y', 'bricks' ),
        // 'spread'  => esc_html__( 'Spread', 'bricks' ),
        // 'blur'    => esc_html__( 'Offset Y', 'bricks' ),
      // ],
    ];
  }

  // Render element HTML
  public function render() {
    echo '<h5 class="prefix-element-dimensions-title">' . get_bloginfo( 'name' ) . '</h5>';
  }
}
```

---

# Direction Control (Flexbox)

Source: https://academy.bricksbuilder.io/developer/controls/direction-control/

*Reference for the Bricks Direction Control (Flexbox) control, including its options, CSS mapping, and usage in custom elements.*

Use the direction control to allow users to set the `flex-direction` CSS property of your CSS flexbox layout.

```php
public function set_controls() {
  $this->controls['direction'] = [ // Setting key
    'tab'   => 'content',
    'label' => esc_html__( 'Direction', 'bricks' ),
    'type'  => 'direction',
    'css'   => [
      [
        'property' => 'flex-direction',
        'selector' => '.flexbox-wrapper',
        // 'id'       => '', // Leave 'id' empty to apply to .flexbox-wrapper directly (@since 1.5.6)
      ],
    ],
  ];
}
```

---

# Editor Control

Source: https://academy.bricksbuilder.io/developer/controls/editor-control/

*Reference for the Bricks Editor control, including its options, CSS mapping, and usage in custom elements.*

The editor control provides the default WordPress editor. To directly edit content in the builder preview set the `inlineEditing` properties. See the code example below:

```php
class Prefix_Element_Editor extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleEditor'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Text editor', 'bricks' ),
      'type' => 'editor',
      'inlineEditing' => [
        'selector' => '.text-editor', // Mount inline editor to this CSS selector
        'toolbar' => true, // Enable/disable inline editing toolbar
      ],
      'default' => esc_html__( 'Here goes the content ..', 'bricks' ),
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleEditor'] ) ) {
      echo '<div class="text-editor">' . $this->settings['exampleEditor'] . '</div>';
    }
  }
}
```

---

# Element Controls

Source: https://academy.bricksbuilder.io/developer/controls/element-controls/

*Reference for the Bricks Element Controls control, including its options, CSS mapping, and usage in custom elements.*

Element controls allow the user to change the content and appearance of an element. You can define the controls of an element with the set_controls() method in your [element PHP class](https://academy.bricksbuilder.io/developer/elements/create-your-own-elements/).

Example element class with control parameters for control `testColor`:

```php
class Prefix_Element_Test extends \Bricks\Element {
  public function set_controls() {
    $this->controls['testColor'] = [
      'tab' => 'content',
      'group' => 'settings',
      'label' => esc_html__( 'Text color', 'bricks' ),
      'type' => 'color',
      'inline' => true,
      'small' => true,
      'css' => [
        [
          'property' => 'color',
          'selector' => '.content',
          'important' => true, // Optional
        ],
      ],
      'default' => [
        'rgb' => 'rgba(158, 158, 158, .8)',
        'hex' => '#9e9e9e',
      ],
      'pasteStyles' => false,
      'description' => esc_html__( 'Define the content color.', 'bricks' ),
      'required' => ['showText', '!=', ''],
    ];
  }
}
```

The following control parameters are available for all control types. To dive deeper into the arguments of a specific control type select the control from the list at the bottom.

### Universal control arguments

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| tab | string | content | Tab under which to show the control. Accepts: `content` or `style`. |
| group | string |  | Group under which to show the control. By default a control shows ungrouped under the `content` tab. |
| label | string |  | Localized control label. E.g.: `esc_html__( 'Color', 'bricks' ),` |
| type | string |  | Set the control type (see the list below for a list of all available control types). |
| inline | bool | false | Set to true to show control label and input on the same line. |
| small | bool | false | Set to true to show a control input of 60px width. By default inline label and input have equal widths of 50%. |
| css | array |  | Array with CSS rule definitions. Each CSS rule is a separate array and requires a `property` and `selector` parameter. |
| default | string/array |  | Default control value. Either a string or an array (depending on the control type, see control list below for specific control default) |
| pasteStyles | bool | true | Set to true excludes setting from being pasted via the builders' custom right click "Paste Styles". Recommended for all controls that output HTML content instead of CSS. |
| description | string |  | Optional description for controls that need additional explanation or link to a resource. |
| required | array |  | Show control in relation to the setting of another control.<br /><br />Parameter #1: control ID<br /><br />Parameter #2: comparison operator: `=`, `!=`, `>`, `<`, `>=`, `<=`<br /><br />Example: `'required' => ['layout', '=', ['list', 'grid']],`<br /><br />Required condition: Show this control if setting value of control `layout` equals `=` either `list` or `grid`. |

### Controls Types

| Control Type | Output (Content/CSS) |
| --- | --- |
| [apply](https://academy.bricksbuilder.io/developer/controls/apply-control/) | None |
| [align-items](https://academy.bricksbuilder.io/developer/controls/align-items-control/) | CSS |
| [audio](https://academy.bricksbuilder.io/developer/controls/audio-control/) | Content |
| [background](https://academy.bricksbuilder.io/developer/controls/background-control/) | CSS |
| [border](https://academy.bricksbuilder.io/developer/controls/border-control/) | CSS |
| [box-shadow](https://academy.bricksbuilder.io/developer/controls/box-shadow-control/) | CSS |
| [checkbox](https://academy.bricksbuilder.io/developer/controls/checkbox-control/) | Conditional |
| [code](https://academy.bricksbuilder.io/developer/controls/code-control/) | Content |
| [color](https://academy.bricksbuilder.io/developer/controls/color-control/) | CSS |
| [datepicker](https://academy.bricksbuilder.io/developer/controls/datepicker-control/) | Content |
| [dimensions](https://academy.bricksbuilder.io/developer/controls/dimensions-control/) | CSS |
| [direction](https://academy.bricksbuilder.io/developer/controls/direction-control/) | CSS |
| [editor](https://academy.bricksbuilder.io/developer/controls/editor-control/) | Content |
| [filters](https://academy.bricksbuilder.io/developer/controls/filters-control/) | CSS |
| [gradient](https://academy.bricksbuilder.io/developer/controls/gradient-control/) | CSS |
| [icon](https://academy.bricksbuilder.io/developer/controls/icon-control/) | Content |
| [image](https://academy.bricksbuilder.io/developer/controls/image-control/) | Content/CSS |
| [image-gallery](https://academy.bricksbuilder.io/developer/controls/image-gallery-control/) | Content |
| [info](https://academy.bricksbuilder.io/developer/controls/info-control/) | Builder panel only |
| [justify-content](https://academy.bricksbuilder.io/developer/controls/justify-content-control/) | CSS |
| [link](https://academy.bricksbuilder.io/developer/controls/link-control/) | Content |
| [number](https://academy.bricksbuilder.io/developer/controls/number-control/) | Content/CSS |
| [posts](https://academy.bricksbuilder.io/builder/elements/wordpress/posts/) | Content |
| [repeater](https://academy.bricksbuilder.io/developer/controls/repeater-control/) | Content |
| [select](https://academy.bricksbuilder.io/developer/controls/select-control/) | Content/CSS |
| [slider](https://academy.bricksbuilder.io/developer/controls/slider-control/) | Content |
| [svg](https://academy.bricksbuilder.io/developer/controls/svg-control/) | Content |
| [text](https://academy.bricksbuilder.io/developer/controls/text-control/) | Content |
| [textarea](https://academy.bricksbuilder.io/developer/controls/textarea-control/) | Content |
| [text-align](https://academy.bricksbuilder.io/developer/controls/text-align-control/) | CSS |
| [text-decoration](https://academy.bricksbuilder.io/developer/controls/text-decoration-control/) | CSS |
| [text-shadow](https://academy.bricksbuilder.io/developer/controls/text-shadow-control/) | CSS |
| [text-transform](https://academy.bricksbuilder.io/developer/controls/text-transform-control/) | CSS |
| [typography](https://academy.bricksbuilder.io/developer/controls/typography-control/) | CSS |

---

# Filters Control

Source: https://academy.bricksbuilder.io/developer/controls/filters-control/

*Reference for the Bricks Filters control, including its options, CSS mapping, and usage in custom elements.*

The filters control offers the following [CSS filters](https://developer.mozilla.org/en-US/docs/Web/CSS/filter): `blur`, `brightness`, `contrast`, `hue`, `invert`, `opacity`, `saturation`, `sepia`.

```php
class Prefix_Element_Filters extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleFilters'] = [
      'tab' => 'content',
      'label' => esc_html__( 'CSS filters', 'bricks' ),
      'type' => 'filters',
      'inline' => true,
      'css' => [
        [
          'property' => 'filter',
          'selector' => '.css-filter',
        ],
      ],
    ];
  }

  // Render element HTML
  public function render() {
    echo '<div class="css-filter">' . echo get_bloginfo( 'name' ); . '</div>';
  }
}
```

> **Note**
>
> All sections, rows, columns, and elements already have a **CSS Filters** control under the Style tab CSS group.

---

# Gradient Control

Source: https://academy.bricksbuilder.io/developer/controls/gradient-control/

*Reference for the Bricks Gradient control, including its options, CSS mapping, and usage in custom elements.*

The gradient control lets you define an unlimited number of gradients that you can apply to text, background, and as an overlay.

You can set the CSS selector in the control, adjust the angle between 0 and 360°, and set a color stop for each color.

```php
class Prefix_Element_Gradient extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleGradient'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Gradient', 'bricks' ),
      'type' => 'gradient',
      'css' => [
        [
          'property' => 'background-image',
        ],
      ],
    ];
  }

  // Render element HTML
  public function render() {
    echo get_bloginfo( 'name' );
  }
}
```

> **Note**
>
> All sections, rows, columns, and elements already have a **CSS Gradient** control under the Style tab Gradient / Overlay group.

---

# Icon Control

Source: https://academy.bricksbuilder.io/developer/controls/icon-control/

*Reference for the Bricks Icon control, including its options, CSS mapping, and usage in custom elements.*

The icon control lets you select and output icons from the following icon font libraries:

- [Fontawesome 6](https://fontawesome.com/icons?d=gallery&m=free)
- [Ionicons 4](https://ionic.io/ionicons/v4/cheatsheet.html)
- [Themify](https://themify.me/themify-icons)

The user can also select individually uploaded SVG files if you've enabled "**SVG Uploads**" under `Bricks > Settings` in your WordPress dashboard, and custom icon sets since Bricks 2.0.

```php
class Prefix_Element_Icon extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleIcon'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Icon', 'bricks' ),
      'type' => 'icon',
      'default' => [
        'library' => 'themify', // fontawesome/ionicons/themify
        'icon' => 'ti-star',    // Example: Themify icon class
      ],
      'css' => [
        [
          'selector' => '.icon-svg', // Use to target SVG file
        ],
      ],
    ];
  }

  // Render element HTML
  public function render() {
    // Set icon 'class' attribute
    if ( isset( $this->settings['exampleIcon'] ) ) {
      Helpers::render_control_icon( $settings['exampleIcon'], ['test-class', 'test-class-2'] );
    }
  }
}
```

---

# Image Control

Source: https://academy.bricksbuilder.io/developer/controls/image-control/

*Reference for the Bricks Image control, including its options, CSS mapping, and usage in custom elements.*

The image control lets you select a single image from your media library. Once an image has been selected you can choose the image size.

You can either use the returned image `id` and `size` to render an image on your page or as a `background-image` via the CSS control property. See the code example below.

> **Note**
>
> **TIP:** Select the smallest possible image size in which the image still looks crisp. This helps to reduce the loading time of your website and is great for SEO, as loading times are an important ranking factor for search engines.

```php
class Prefix_Element_Image extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleImage'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Image', 'bricks' ),
      'type' => 'image',
      // Use the selected image as a background image
      // 'css' => [
      //   [
      //     'property' => 'background-image',
      //     'selector' => '.bricks-video-overlay-image',
      //   ],
      // ],
    ];
  }

  // Render element HTML
  public function render() {
    // Dump 'exampleImage' settings on the screen
    // var_dump( $this->settings['exampleImage'] );

    if ( isset( $this->settings['exampleImage'] ) ) {
      // Render <img> tag by prodiving image 'id' and 'size'
      //
      echo wp_get_attachment_image(
        $this->settings['exampleImage']['id'],
        $this->settings['exampleImage']['size'],
        false,
        [] // Image attributes
      );
    } else {
      esc_html_e( 'No image selected.', 'bricks' );
    }
  }
}
```

---

# Image Gallery Control

Source: https://academy.bricksbuilder.io/developer/controls/image-gallery-control/

*Reference for the Bricks Image Gallery control, including its options, CSS mapping, and usage in custom elements.*

The image gallery control lets you select multiple images from your media library. Once images have been selected you can choose the image size.

Your selected images are stored in an array, which you have to loop through (see code example below). Use the `id` and `size`  of each image to render it on your page.

> **Note**
>
> **Tip #1:** Hold down the *SHIFT* key in order to select multiple image in your media library.

> **Note**
>
> **Tip #2:** Select the smallest possible image size in which the image still looks crisp. This helps to reduce the loading time of your website and is great for SEO, as loading times are an important ranking factor for search engines.

```php
class Prefix_Element_Image extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleImageGallery'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Image gallery', 'bricks' ),
      'type' => 'image-gallery',
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleImageGallery'] ) ) {
      foreach( $this->settings['exampleImageGallery'] as $index => $image ) {
        echo wp_get_attachment_image(
          $image['id'],
          $image['size'],
          false,
          ['class' => 'css-filter']
        );
      }
    } else {
      esc_html_e( 'No image(s) selected.', 'bricks' );
    }
  }
}
```

---

# Controls

Source: https://academy.bricksbuilder.io/developer/controls/

*Reference the Bricks controls used in custom elements and builder extensions, from layout and typography controls to media, code, query, and repeater controls.*

Bricks controls define how users edit custom element settings inside the builder. This section helps you understand the available control types, the data they store, and when to use each one.

## Common control groups

- [Element Controls](https://academy.bricksbuilder.io/developer/controls/element-controls/) for the overall structure of element settings
- [Content Controls](https://academy.bricksbuilder.io/developer/controls/text-control/) for text, textarea, editor, select, and checkbox inputs
- [Styling Controls](https://academy.bricksbuilder.io/developer/controls/color-control/) for visual styling fields such as color, typography, border, and shadow
- [Media Controls](https://academy.bricksbuilder.io/developer/controls/image-control/) for images, galleries, icons, SVG, and audio
- [Advanced Controls](https://academy.bricksbuilder.io/developer/controls/query-control/) for query, repeater, code, filters, and apply workflows

---

# Info Control

Source: https://academy.bricksbuilder.io/developer/controls/info-control/

*Reference for the Bricks Info control, including its options, CSS mapping, and usage in custom elements.*

The info control does not affect the HTML or CSS on the frontend. It serves as a builder-only helper controls to provide additional information.

Example below: the **Alert** element displays an info control when the *Type* is set to *Custom*.

```php
class Prefix_Element_Info extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['type'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Type', 'bricks' ),
      'type' => 'select',
      'options' => [
        'info' => esc_html__( 'Info', 'bricks' ),
        'success' => esc_html__( 'Success', 'bricks' ),
        'warning' => esc_html__( 'Warning', 'bricks' ),
        'danger' => esc_html__( 'Danger', 'bricks' ),
        'muted' => esc_html__( 'Muted', 'bricks' ),
        'custom' => esc_html__( 'Custom', 'bricks' ),
      ],
      'inline' => true,
      'clearable' => false,
      'pasteStyles' => false,
      'default' => 'info',
    ];

    $this->controls['typeInfo'] = [
      'tab' => 'content',
      'content' => esc_html__( 'Customize alert in STYLE tab.', 'bricks' ),
      'type' => 'info',
      'required' => ['type', '=', 'custom'], // Show info control if 'type' = 'custom'
    ];
  }
}
```

---

# Link Control

Source: https://academy.bricksbuilder.io/developer/controls/link-control/

*Reference for the Bricks Link control, including its options, CSS mapping, and usage in custom elements.*

The link control give you the choice of different link types:

- Internal post/page
- External URL
- Popup (image, video)

```php
class Prefix_Element_Link extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleLink'] = [
      'tab'         => 'content',
      'label'       => esc_html__( 'Link', 'bricks' ),
      'type'        => 'link',
      'pasteStyles' => false,
      'placeholder' => esc_html__( 'http://yoursite.com', 'bricks' ),
      // 'exclude'     => [
      //  'rel',
      //  'newTab',
      // ],
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleLink'] ) ) {
      // Set link attributes by passing attribute key and link settings
      $this->set_link_attributes( 'a', $this->settings['exampleLink'] );

      echo '<a ' . $this->render_attributes( 'a' ) . '>' . get_bloginfo( 'name' ) . '</a>';
    } else {
      esc_html_e( 'No link provided.', 'bricks' );
    }
  }
}
```

---

# Number Control

Source: https://academy.bricksbuilder.io/developer/controls/number-control/

*Reference for the Bricks Number control, including its options, CSS mapping, and usage in custom elements.*

The number control represents a simple number input field. It has the following custom properties:

- units (optional: boolean or array)
- unit (string: `px`, `em`, `rem` etc.)
- min (number)
- step (Default: 1) (Custom: '0.1' etc.)

Use it to render a number to the page or set the `css` control property to target a specific CSS style.

```php
class Prefix_Element_Number extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleNumber'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Number', 'bricks' ),
      'type' => 'number',
      'min' => 0,
      'step' => '0.1', // Default: 1
      'inline' => true,
      'default' => 123,
    ];

    $this->controls['examplePadding'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Padding in px', 'bricks' ),
      'type' => 'number',
      'unit' => 'px',
      'inline' => true,
      'css' => [
        [
          'property' => 'padding',
        ],
      ],
      'default' => 33,
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleNumber'] ) ) {
      echo esc_html__( 'Number: ', 'bricks' ) . $this->settings['exampleNumber'];
    } else {
      esc_html_e( 'No number provided.', 'bricks' );
    }
  }
}
```

---

# Justify Content Control (Flexbox)

Source: https://academy.bricksbuilder.io/developer/controls/justify-content-control/

*Reference for the Bricks Justify Content Control (Flexbox) control, including its options, CSS mapping, and usage in custom elements.*

Use the justify-content control to allow users to set the `justify-content` CSS property (alignment along the [main-axis](https://developer.mozilla.org/en-US/docs/Web/CSS/justify-content)) of your CSS flexbox layout.

There is also a [`align-items`](https://academy.bricksbuilder.io/developer/controls/align-items-control/) control to allow users to set the alignment along the cross axis of your CSS flexbox layout:

```php
public function set_controls() {
  $this->controls['justifyContent'] = [
    'tab'   => 'content',
    'label' => esc_html__( 'Justify content', 'bricks' ),
    'type'  => 'justify-content',
    'css'   => [
      [
        'property' => 'justify-content',
        'selector' => '.flexbox-wrapper',
      ],
    ],
    // 'isHorizontal' => false,
    // 'exclude' => [
      // 'flex-start',
      // 'center',
      // 'flex-end',
      // 'space-between',
      // 'space-around',
      // 'space-evenly',
    // ],
  ];
}
```

---

# Query Control

Source: https://academy.bricksbuilder.io/developer/controls/query-control/

*Reference for the Bricks Query control, including its options, CSS mapping, and usage in custom elements.*

The query control lets you set query arguments to retrieve items of any post type. Use the returned value to set up a custom `WP_Query` to render the matching posts in any way you want.

```php
class Prefix_Element_Posts extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleQueryArgs'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Posts', 'bricks' ),
      'type' => 'query',
      // Default required for query to populate
      'default' => [
        'post_type' => 'post',
      ],
    ];
  }

  // Render element HTML
  public function render() {
    $query_args = $this->settings['exampleQueryArgs'];
    $posts_query = new WP_Query( $query_args );

    // Standard WordPress loop
    if ( $posts_query->have_posts() ) :
      while ( $posts_query->have_posts() ) : $posts_query->the_post();
        // Render post title and thumbnail
        the_title( '<h5>', '</h5>' );
        the_post_thumbnail( 'thumbnail' );
      endwhile;

      wp_reset_postdata();
    else :
     esc_html_e( 'No posts matched your criteria.', 'bricks' );
    endif;
  }
}
```

### Resources

- [https://codex.wordpress.org/Class_Reference/WP_Query#Parameters](https://codex.wordpress.org/Class_Reference/WP_Query#Parameters)

---

# Repeater Control

Source: https://academy.bricksbuilder.io/developer/controls/repeater-control/

*Reference for the Bricks Repeater control, including its options, CSS mapping, and usage in custom elements.*

The repeater control lets you create repeatable fields. Fields can be cloned, deleted, and sorted via Drag & Drop. Use the `fields` argument to set up the field controls.

```php
class Prefix_Element_Posts extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleRepeater'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Repeater', 'bricks' ),
      'type' => 'repeater',
      'titleProperty' => 'title', // Default 'title'
      'default' => [
        [
          'title' => 'Design',
          'description' => 'Here goes the description for repeater item.',
        ],
        [
          'title' => 'Code',
          'description' => 'Here goes the description for repeater item.',
        ],
        [
          'title' => 'Launch',
          'description' => 'Here goes the description for repeater item.',
        ],
      ],
      'placeholder' => esc_html__( 'Title placeholder', 'bricks' ),
      'fields' => [
        'title' => [
          'label' => esc_html__( 'Title', 'bricks' ),
          'type' => 'text',
        ],
        'description' => [
          'label' => esc_html__( 'Description', 'bricks' ),
          'type' => 'textarea',
        ],
      ],
    ];
  }

  // Render element HTML
  public function render() {
    $items = $this->settings['exampleRepeater'];

    if ( count( $items ) ) {
      foreach ( $items as $item ) {
        echo '<h4>' . $item['title'] . '</h4>';
        echo '<p>' . $item['description'] . '</p>';
      }
    } else {
      esc_html_e( 'No items defined.', 'bricks' );
    }
  }
}
```

---

# Select Control

Source: https://academy.bricksbuilder.io/developer/controls/select-control/

*Reference for the Bricks Select control, including its options, CSS mapping, and usage in custom elements.*

The select control lets you select an option from a dropdown. It can be used to render content or CSS styling. Use the options array to populate the dropdown with your own options. The option key should be all lowercase, with no spaces.

```php
class Prefix_Element_Posts extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    // Example content
    $this->controls['exampleSelectTitleTag'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Title tag', 'bricks' ),
      'type' => 'select',
      'options' => [
        'h1' => 'H1',
        'h2' => 'H2',
        'h3' => 'H3',
        'h4' => 'H4',
        'h5' => 'H5',
        'h6' => 'H6',
      ],
      'inline' => true,
      'placeholder' => esc_html__( 'Select tag', 'bricks' ),
      'multiple' => true,
      'searchable' => true,
      'clearable' => true,
      'default' => 'h3',
    ];

    // Example CSS
    $this->controls['exampleSelectTextAlign'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Text align', 'bricks' ),
      'type' => 'select',
      'options' => [
        'right' => esc_html__( 'Right', 'bricks' ),
        'center' => esc_html__( 'Center', 'bricks' ),
        'left' => esc_html__( 'Left', 'bricks' ),
      ],
      'inline' => true,
      'css' => [
        [
          'property' => 'text-align',
          'selector' => '.prefix-title',
        ],
      ],
      'placeholder' => esc_html__( 'Select', 'bricks' ),
      'default' => 'center', // Option key
    ];
  }

  // Render element HTML
  public function render() {
    $title_tag = isset( $this->settings['exampleSelectTitleTag'] ) ? $this->settings['exampleSelectTitleTag'] : 'h5';
    echo '<' . $title_tag . ' class="prefix-title">' . get_bloginfo( 'name' ) . '</' . $title_tag . '>';
  }
}
```

---

# Slider Control

Source: https://academy.bricksbuilder.io/developer/controls/slider-control/

*Reference for the Bricks Slider control, including its options, CSS mapping, and usage in custom elements.*

The slider control shows a draggable range input field. Default units are `px`, `em` and `rem`. You can set the following control parameters:

- units (array with custom units and `min`, `max`, `step` attributes)
- unitless (set to `false` for plain number)

```php
class Prefix_Element_Slider extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleSliderFontSize'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Font size', 'bricks' ),
      'type' => 'slider',
      'css' => [
        [
          'property' => 'font-size',
        ],
      ],
      'units' => [
        'px' => [
          'min' => 1,
          'max' => 50,
          'step' => 1,
        ],
        'em' => [
          'min' => 1,
          'max' => 20,
          'step' => 0.1,
        ],
      ],
      'default' => '30px',
      'description' => esc_html__( 'Slider adjusts font size via CSS.', 'bricks' ),
    ];
  }

  // Render element HTML
  public function render() {
    echo '<h3>' . get_bloginfo( 'name' ) . '</h3>';
  }
}
```

### Resources

- [https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/range](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/range)

---

# SVG Control

Source: https://academy.bricksbuilder.io/developer/controls/svg-control/

*Reference for the Bricks SVG control, including its options, CSS mapping, and usage in custom elements.*

The SVG control lets you select an SVG (Scalable Vector Graphic) file from the media library. The selected SVG returns an array with the following keys:

- `id` (media library item ID)
- `filename`
- `url`

We recommend rendering the SVG inline as shown in the code example below. This way you can easily customize it via CSS.

```php
class Prefix_Element_Svg extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleSvg'] = [
      'tab' => 'content',
      'type' => 'svg',
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleSvg']['url'] ) ) {
      echo file_get_contents( esc_url( $this->settings['exampleSvg']['url'] ) );
    } else {
      esc_html_e( 'No SVG selected.', 'bricks' );
    }
  }
}
```

### Resources

- [https://developer.mozilla.org/en-US/docs/Web/SVG/Element/svg](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/svg)
- [https://css-tricks.com/using-svg/](https://css-tricks.com/using-svg/)

---

# Text Control

Source: https://academy.bricksbuilder.io/developer/controls/text-control/

*Reference for the Bricks Text control, including its options, CSS mapping, and usage in custom elements.*

The text control displays a text input field. You can set the following parameters:

- `spellcheck`: true/false. (Default: false)
- `trigger`: 'keyup'/'enter'. (Default: keyup)
- `inlineEditing`: Set to true to enable

```php
class Prefix_Element_Text extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleText'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Text', 'bricks' ),
      'type' => 'text',
      'spellcheck' => true, // Default: false
      // 'trigger' => 'enter', // Default: 'enter'
      'inlineEditing' => true,
      'default' => 'Here goes your text ..',
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleText'] ) ) {
      echo $this->settings['exampleText'];
    } else {
      esc_html_e( 'No text provided.', 'bricks' );
    }
  }
}
```

### Resources

- [https://developer.mozilla.org/en-US/docs/Web/SVG/Element/svg](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/svg)
- [https://css-tricks.com/using-svg/](https://css-tricks.com/using-svg/)

---

# Text Align Control

Source: https://academy.bricksbuilder.io/developer/controls/text-align-control/

*Reference for the Bricks Text Align control, including its options, CSS mapping, and usage in custom elements.*

Use the **text-align** control to allow users to set the text-align CSS property like so:

```php
public function set_controls() {
  $this->controls['textAlign'] = [ // Setting key
    'tab' => 'content',
    'label' => esc_html__( 'Text align', 'bricks' ),
    'type' => 'text-align',
    'css' => [
      [
        'property' => 'text-align',
        'selector' => '.text-wrapper',
      ],
    ],
  ];
}
```

---

# Text Decoration Control

Source: https://academy.bricksbuilder.io/developer/controls/text-decoration-control/

*Reference for the Bricks Text Decoration control, including its options, CSS mapping, and usage in custom elements.*

Use the **text-decoration** control to allow users to set the text-decoration CSS property like so:

```php
public function set_controls() {
  $this->controls['textDecoration'] = [ // Setting key
    'tab' => 'content',
    'label' => esc_html__( 'Text decoration', 'bricks' ),
    'type' => 'text-decoration',
    'css' => [
      [
        'property' => 'text-decoration',
        'selector' => '.text-wrapper',
      ],
    ],
  ];
}
```

---

# Text Shadow Control

Source: https://academy.bricksbuilder.io/developer/controls/text-shadow-control/

*Reference for the Bricks Text Shadow control, including its options, CSS mapping, and usage in custom elements.*

The text-shadow control displays a popup that lets you set the CSS text-shadow of a specified HTML text element.

```php
class Prefix_Element_Textarea extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleTextShadow'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Text Shadow', 'bricks' ),
      'type' => 'text-shadow',
      'css' => [
        [
          'property' => 'text-shadow',
          'selector' => '.prefix-text',
        ],
      ],
      'inline' => true,
    ];
  }

  // Render element HTML
  public function render() {
    echo '<h3 class="prefix-text">' . get_bloginfo( 'name' ) . '</h3>';
  }
}
```

### Resources

[https://developer.mozilla.org/en-US/docs/Web/CSS/text-shadow](https://developer.mozilla.org/en-US/docs/Web/CSS/text-shadow)

---

# Text Transform Control

Source: https://academy.bricksbuilder.io/developer/controls/text-transform-control/

*Reference for the Bricks Text Transform control, including its options, CSS mapping, and usage in custom elements.*

Use the **text-transform** control to allow users to set the text-transform CSS property like so:

```php
public function set_controls() {
  $this->controls['textTransform'] = [ // Setting key
    'tab' => 'content',
    'label' => esc_html__( 'Text transform', 'bricks' ),
    'type' => 'text-transform',
    'css' => [
      [
        'property' => 'text-transform',
        'selector' => '.text-wrapper',
      ],
    ],
  ];
}
```

---

# Textarea Control

Source: https://academy.bricksbuilder.io/developer/controls/textarea-control/

*Reference for the Bricks Textarea control, including its options, CSS mapping, and usage in custom elements.*

The textarea control displays a textarea input field. You can set the following parameters:

- `rows` (number. Default: 5)
- `readonly` (true/false. Default: false)
- `spellcheck` (true/false. Default: false)
- `inlineEditing` (true to enable)

```php
class Prefix_Element_Textarea extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleTextarea'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Textarea', 'bricks' ),
      'type' => 'textarea',
      // 'readonly' => true, // Default: false
      'rows' => 10, // Default: 5
      'spellcheck' => true, // Default: false
      'inlineEditing' => true,
      'default' => 'Here goes your content ..',
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleTextarea'] ) ) {
      echo $this->settings['exampleTextarea'];
    } else {
      esc_html_e( 'No text provided.', 'bricks' );
    }
  }
}
```

---

# Typography Control

Source: https://academy.bricksbuilder.io/developer/controls/typography-control/

*Reference for the Bricks Typography control, including its options, CSS mapping, and usage in custom elements.*

The typography control provides the following CSS properties:

- color
- font-size
- text-align
- text-transform
- font-family
- font-weight
- font-style
- line-height
- letter-spacing
- text-shadow
- text-decoration

Use the `exclude` parameter to hide specific typography properties. Set `popup` to false to show control inline.

```php
class Prefix_Element_Typography extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleTypography'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Typography', 'bricks' ),
      'type' => 'typography',
      'css' => [
        [
          'property' => 'typography',
          'selector' => '.prefix-typography',
        ],
      ],
      'inline' => true,
      // 'exclude' => [
      //   'font-family',
      //   'font-weight',
      //   'text-align',
      //   'text-transform',
      //   'font-size',
      //   'line-height',
      //   'letter-spacing',
      //   'color',
      //   'text-shadow',
      // ],
      // 'popup' => false, // Default: true
    ];
  }

  // Render element HTML
  public function render() {
    echo '<h3 class="prefix-typography">' . get_bloginfo( 'name' ) . '</h3>';
  }
}
```
