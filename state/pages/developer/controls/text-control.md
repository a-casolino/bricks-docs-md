*Reference for the Bricks Text control, including its options, CSS mapping, and usage in custom elements.*

The text control displays a text input field. You can set the following parameters:

- `spellcheck`: true/false. (Default: false)
- `trigger`: 'keyup'/'enter'. (Default: keyup)
- `inlineEditing`: Set to true to enable

If the control accepts dynamic tags, resolve its value inside `render()` before output. See [Render dynamic text](https://academy.bricksbuilder.io/developer/elements/create-your-own-elements/#render-dynamic-text).

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
    $text = isset( $this->settings['exampleText'] )
      ? $this->render_dynamic_data( $this->settings['exampleText'] )
      : __( 'No text provided.', 'bricks' );

    echo '<div ' . $this->render_attributes( '_root' ) . '>' . esc_html( $text ) . '</div>';
  }
}
```

### Resources

- [https://developer.mozilla.org/en-US/docs/Web/SVG/Element/svg](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/svg)
- [https://css-tricks.com/using-svg/](https://css-tricks.com/using-svg/)