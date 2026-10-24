*Use the Bricks Command Palette to run common actions, navigate faster, and insert element structures with keyboard-driven workflows.*

Bricks 2.0 introduces the **Command Palette**, a powerful new feature that gives you instant keyboard-driven access to core functionality inside the builder.

https://youtu.be/gOVNlRvsYc8

## How to launch it

Click the command `⌘` icon in the builder toolbar or use the `CMD/CTRL + K` keyboard shortcut to open the Command Palette, which appears as an overlay, allowing you to type and filter commands across four scopes.

## Scope: Builder {#builder}

Navigate to key parts of the builder from a growing list of targets such as classes, variables, templates, theme styles, settings, etc.

![](https://academy.bricksbuilder.io/assets/bricks-2.0-command-palette-scope-builder.png)

## Scope: Post Types {#post-types}

This scope lets you browse the registered post types your builder capability can access, create new posts when your user can edit posts, or duplicate existing posts.

Besides "All" and "Template (Bricks)", a post type gets its own tab only when Bricks is enabled for it under **Bricks > Settings > General > Post types** and your role can access it in the builder. "All" searches every public post type.

To create a post, select the post type tab, type the title, and click "Create". Bricks adds the post as a draft. Click a result to open it in the builder. `CMD/CTRL` + click opens it in a new browser tab. Posts of a type that is not enabled for Bricks open in the WordPress editor in a new tab.

The scope auto-selects the post type that you are currently editing. So if you are editing a Bricks template the "Template (Bricks)" post type will be selected. If you edit a "Page", then "Page" is selected and so on.

![](https://academy.bricksbuilder.io/assets/bricks-2.0-command-palette-scope-post-types.png)

## Scope: Elements {#elements}

The "Elements" scope will dramatically speed up your workflow by allowing you to insert multiple elements with specific structure in a single action.

By mastering the Emmet-like syntax, you can create complex layouts in seconds rather than minutes, making your design process significantly more efficient.

With practice, this feature becomes second nature and an essential part of your Bricks Builder toolkit, especially for quickly creating common page structures and element combinations that you use frequently, which you can also save for instant access to use whenever needed.

![](https://academy.bricksbuilder.io/assets/bricks-2.0-command-palette-scope-elements.png)

### Insert single element

To insert a single element simply type its name, such as "Section", then `ARROW`-navigate to it in the elements list, and insert it by pressing `ENTER` or just click on the element name.

### Insert element structure

Each element starts with an **@** symbol.

The element name that the command bar requires is displayed in square brackets in the results list:

![](https://academy.bricksbuilder.io/assets/bricks-2.0-command-palette-element-name.png)

<figcaption>

Text link element command: `@text-link`

</figcaption>

### Supported operators

Use the following operators to define nested structure, siblings, a multiplier, or to move back up one nesting level.

| Symbol | Meaning |
| --- | --- |
| `@` | Bricks element name (e.g. `@heading`) |
| `>` | Nest inside |
| `+` | Insert element as sibling |
| `*` | How often to insert the element |
| `^` | Move one level up before inserting the next element |

### Element structure example

`@section * 2 > @heading + @text + @button`
This creates the following structure *(two times because of the multiplier: `* 2`)*:

- `Section`
 └ `Container`
   ├ `Heading`
   ├ `Text`
   └ `Button`

Bricks adds the Container inside every Section automatically, so you don't type `@container` after `@section`.

### Quick element insertion

> **Note**
>
> After selecting an element from the search results, its name is added to your query with the `@` prefix, allowing you to quickly build complex queries:

1. Type `@` to activate insertion mode
2. Select an element (e.g., "section")
3. Type `>` for a child element
4. Continue building your structure
5. Insert your element structure
  - Click the "Insert" button that appears next to your query
  - Press `CMD/CTRL + ENTER`

If no element is selected, Bricks adds the structure at the end of the page or template.

### Save element structures

Instead of typing out your favorite structures by hand every time, you can save them by clicking the "Save" button next to the command bar. Your structures are stored in this browser's `localStorage`, so they are local to that browser/profile and are not synced between users or devices.

![](https://academy.bricksbuilder.io/assets/bricks-2.0-command-palette-saved-element-structures.png)

<figcaption>

List of saved element structures

</figcaption>

To insert a saved structure, open the "Select element structure" dropdown in the Elements scope and pick it. To delete a structure, mouseover the structure item in the list, and click the "Delete" icon.

## Scope: Components {#components}

This scope lists the components on your site. Select a component to insert an instance of it, the same way you insert a single element. The scope is available when your role can insert components.

## Keyboard shortcuts

| **Keyboard shortcut** | **Action** |
| --- | --- |
| `CMD/CTRL + K` | Open/close the command palette |
| `ESC` | Close the command palette |
| `TAB > ENTER` (to enter selected scope) | Navigate between search and scopes |
| `#` (as the first character in the search input) | Enter scope “Builder” |
| `/` (as the first character in the search input) | Enter scope “Post Types” |
| `+` or `@` (as the first character in the search input) | Enter scope “Elements” |
| `*` (as the first character in the search input) | Enter scope “Components” |
| `CMD/CTRL + ENTER` | Insert the element structure typed in scope “Elements” |
| `/0-9` (forward slash followed by number) | Navigate to a specific post type |
| `ARROW UP/DOWN` + ENTER | Navigate to a search result and open it |

## Notes

Bricks remembers your last selected scope, even after builder reload (stored in your localStorage).

The "Pages" panel remains available from the builder toolbar. The Command Palette is an additional fast way to browse, create, duplicate, and open posts.

The docs entry is also accessible from the "Builder" scope.