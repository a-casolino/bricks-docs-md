*Reference for the Bricks Gradient control, including its options, CSS mapping, and usage in custom elements.*

The gradient control lets you define an unlimited number of gradients that you can apply to text, background, and as an overlay.

For generated gradients, you can set the CSS selector, adjust the angle between 0 and 360°, and set a color stop for each color. Since Bricks 2.5, the **Custom** type accepts complete gradient values and CSS variable references. See [Custom gradients](https://academy.bricksbuilder.io/builder/styling/gradients-overlays/#custom-gradients) for the Builder workflow.

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