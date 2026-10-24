# Builder Access & Capabilities

Source: https://academy.bricksbuilder.io/builder/interface/builder-access/

*Control who can access Bricks and which builder capabilities are available for different WordPress roles.*

Bricks gives you full control over who can access the builder, and what actions they're allowed to perform. You can either assign a **predefined capability**, or create your own **custom capability** that allows only the specific permissions you enable for it.

This gives you complete freedom and control to tailor the builder experience to any roles (i.e. content editor, designer, client, etc.) depending on what they should be able to do.

![](https://academy.bricksbuilder.io/assets/bricks-settings-builder-access.png)

## Access levels

There are two ways to manage builder access:

1. Use one of the predefined capabilities: **Full access**, **Edit content**, or **No access**
2. Create your own custom builder capability with detailed permission control

### Predefined capabilities

- **Full access**: Grants access to all features and permissions in the Bricks builder.
- **Edit content**: Limits the user to content editing only. Layout, styling, and structural controls are disabled. More specifically, this includes the following permissions:
  - Access revisions
  - Set component properties (instance)
  - Access content (HTML) settings
  - Edit all elements
  - Edit all Bricks-enabled post types
- **No access**: Blocks access to the Bricks builder entirely.

## Creating a custom capability {#custom}

If you need precise control over the actions a user or role should be able to perform, you can create your very own custom builder capability, following the steps outlines below.

1. Go to **Bricks > Settings > Builder access**
2. Under **Builder capabilities**, click **Add new capability**

![](https://academy.bricksbuilder.io/assets/bricks-builder-access-add-custom-capability.png)

Inside the capability popup, you can:

- Give the capability a name & a description
- Enable exactly the permissions you want to grant

![](https://academy.bricksbuilder.io/assets/bricks-builder-access-permissions.png)

Once created, you can assign this capability to specific users or user roles.

## Assigning capabilities

You can assign any builder capability, whether predefined or custom:

- To a **user role**, under **Bricks > Settings > Builder access > Builder access**

![](https://academy.bricksbuilder.io/assets/bricks-builder-access-custom-capabilities.png)

- To a **specific user**, by editing their WordPress user profile

![](https://academy.bricksbuilder.io/assets/bricks-builder-edit-user-profile.png)

![](https://academy.bricksbuilder.io/assets/bricks-builder-access-user-settings.png)

This gives you flexibility to apply permissions globally or individually.

## Available permissions

When editing a capability, the following permissions are available and grouped by category:

### Post types {#post-types}

Choose which post types can be edited using Bricks.

### General {#general}

- Access breakpoints manager
- Access page settings
- Access template settings
- Access revisions
- Delete revisions
- Access font manager
- Access icon manager
- Access query manager
- Customize builder interface
- Manage builder interface profiles
- Manage global elements (only if legacy Global Elements exist)

### Templates {#templates}

- Create templates
- Edit templates
- Delete templates
- Insert templates
- Access remote templates
- Import/export templates

### Global styles & settings {#styles-setting}

- Access theme styles
- Access color manager
- Access variable manager
- Access class manager
- Create global classes
- Edit global classes
- Assign/unassign global classes
- Delete global classes
- Lock/unlock global classes
- Copy/paste global class styles
- Access pseudos & selectors

### Components {#components}

- Access remote components
- Insert components
- Edit properties (instance)
- Edit components
- Create components
- Delete components
- Import/export components

Remote workflows combine these permissions instead of using one broad access flag:

| Workflow | Required permissions |
| --- | --- |
| Browse a configured remote component library | **Access remote components** |
| Import a remote component | **Access remote components** and **Import/export components** |
| Insert an imported component | **Insert components** |
| Insert a remote template without components | **Access remote templates** and **Insert templates** |
| Insert a remote template with component dependencies | **Access remote templates**, **Insert templates**, **Access remote components**, **Import/export components**, and **Insert components** |
| Save a remote template to My Templates | **Access remote templates** and **Import/export templates** |
| Save a remote template with component dependencies to My Templates | The template import permissions above, plus **Access remote components** and **Import/export components** |

See [Remote Templates](https://academy.bricksbuilder.io/builder/features/remote-templates/) for the corresponding template setup.

### Element editing & styling {#element-edit-style}

- Access content (HTML) settings
- Access style (CSS) settings
- Access query loop builder
- Access element hide
- Access element conditions
- Access element interactions
- Duplicate elements
- Delete elements
- Move elements
- Copy/paste elements
- Copy/paste element styles
- Copy/paste element conditions
- Copy/paste element interactions
- Copy/paste element attributes
- Pin/unpin elements

### Edit elements {#edit-elements}

Controls general editing of existing elements.

_Note: Requires access to content and/or style settings._

### Add elements {#add-elements}

Define which elements can be inserted.

---

# Builder Interface Customiser and Profiles

Source: https://academy.bricksbuilder.io/builder/interface/builder-interface-customiser-profiles/

*Customize the Bricks builder workspace, save reusable interface profiles, and assign layouts to roles or users.*

The Builder Interface Customiser lets you adjust the Bricks builder workspace to match the way you work.

You can add, hide and move toolbar items, dock the Control panel and Structure, place Pinned controls in the bottom dock, and save layouts as profiles for different users or roles.

This changes the builder workspace only. It does not change frontend output, templates, elements, or page data.

https://www.youtube.com/watch?v=iIUmLZQp_CY

## Requirements

Builder interface customization is available in Bricks 2.4.

The Builder interface entry appears when the current user can customize the builder interface or manage builder interface profiles. Administrators with full builder access can use both by default.

Use [Builder access](https://academy.bricksbuilder.io/builder/interface/builder-access/) to grant these permissions to other roles:

- **Customize builder interface**: Lets the user save and reset their own builder interface preferences.
- **Manage builder interface profiles**: Lets the user create, load, rename, overwrite, delete, import, and export builder interface profiles.

Site admins can disable the customiser globally under `Bricks -> Settings -> Builder -> Builder interface` by enabling **Disable builder interface customiser**.

## Open the Builder interface

Open the builder, then use either of these entry points:

- Open the builder settings panel and click **Builder interface**.
- Open the [Command Palette](https://academy.bricksbuilder.io/builder/interface/command-palette/) and choose **Builder interface** from the Builder scope.

![](https://academy.bricksbuilder.io/assets/bricks-builder-interface-popup.webp)

## Workspace layout

The Builder interface popup controls the main workspace areas.

### Control panel and Structure

Use the **Control panel** and **Structure** settings to dock each panel to the **Left**, **Right**, or **Bottom**.

When the Control panel and Structure are assigned to the same side dock, Bricks displays them next to each other instead of stacking both panels in the same area.

![](https://academy.bricksbuilder.io/assets/bricks-builder-interface-control-structure-panels.webp)

### Pinned controls

Pinned controls can stay inside the control panel or move to the bottom dock.

When **Pinned controls** is set to **Bottom**, the popup shows a **Pinned controls layout** section. Use it to set the number of columns and optional column widths. Bricks supports up to six pinned-control columns.

![](https://academy.bricksbuilder.io/assets/bricks-builder-interface-pinned-controls.webp)

### Bottom dock

The bottom dock can contain:

- Control panel
- Structure
- Pinned controls

Items in the bottom dock appear as tabs. You can reorder those tabs while editing the builder interface.

When more than one item is assigned to the bottom dock, the popup shows a **Bottom dock layout** section. Use it to set the number of bottom dock columns and optional CSS widths for each column. The maximum number of columns matches the number of items currently assigned to the bottom dock.

![](https://academy.bricksbuilder.io/assets/bricks-builder-interface-bottom-dock.webp)

## Toolbar layout

The toolbar can be placed on the **Top**, **Right**, **Bottom**, or **Left** edge of the builder.

Each toolbar edge has three groups:

- **Start**
- **Center**
- **End**

Drag toolbar items between these groups to change their order and placement. Bricks keeps the breakpoint controls together as one locked cluster.

### Toolbar items

The **Toolbar items** section contains optional items you can drag into the toolbar. This includes repeatable toolbar dividers and custom **Insert element** shortcuts.

An Insert element shortcut can insert a selected element or component directly from the toolbar.

![](https://academy.bricksbuilder.io/assets/bricks-builder-interface-toolbar-items.webp)

### Hidden items

Drag optional toolbar items into **Hidden items** to remove them from the visible toolbar. Use the restore button on a hidden item to bring it back.

Required toolbar items cannot be hidden. In Bricks 2.4, **Elements**, **Structure**, **Preview**, and **Save** are required.

## Save or reset your layout

Click **Save** to store the current builder interface for your user account.

Click **Reset** to remove your saved builder interface preferences and return to the resolved default layout. The reset keeps pinned control groups where possible, so frequently used pinned groups are not lost just because the workspace layout was reset.

If the popup shows an unsaved-changes message, save before closing the popup if you want to keep the layout.

## Profiles

Builder interface profiles save a complete builder interface layout that can be reused.

In the **Profiles** section, you can:

- **Load** an existing profile into the current popup.
- **Save as** a new profile from the current layout.
- **Overwrite** the selected profile.
- **Rename** the selected profile.
- **Delete** the selected profile.

Profiles are useful when different people need different builder workspaces. For example, a designer might use a wide control panel and visible Structure panel, while a content editor might use fewer toolbar items and a simplified bottom dock.

> **Note**
>
> Bricks applies profiles after personal builder interface preferences. If a setting exists in both places, the assigned profile wins. Use profile assignments when you want a role or user to consistently receive a specific builder workspace.

Saving a profile does not assign it automatically. Assign profiles under Builder access after creating them.

## Assign profiles to roles or users

After creating profiles, assign them under `Bricks -> Settings -> Builder access -> Builder interface profile`.

Each WordPress role can use:

- **Default**
- Any saved builder interface profile

You can override the role assignment for a specific person by editing that user's WordPress profile and selecting a **Builder interface profile**.

![](https://academy.bricksbuilder.io/assets/builder-interface-profiles-user-roles.webp)

If a user has multiple roles with different profile assignments, Bricks uses the first matching role assignment from the user's role list.

Deleting a profile removes any role and user assignments that pointed to that profile.

![](https://academy.bricksbuilder.io/assets/bricks-builder-interface-profiles.webp)

## Import and export

Open the import/export icon in the Builder interface popup to move layouts between sites or browsers.

![](https://academy.bricksbuilder.io/assets/bricks-builder-interface-import-export.webp)

You can export or import:

- Current builder interface settings
- The selected profile
- All profiles

Importing builder interface settings overrides the current builder interface settings. Importing profiles does not import role or user assignments.

When imported profiles conflict with existing profile IDs, Bricks lets you overwrite, import as a copy, or skip each profile. Conflicting profiles are skipped by default until you choose another option.

## Reset another user's preferences

Admins can reset another user's saved builder interface preferences from that user's WordPress profile.

In the user's WordPress profile, find **Builder interface** and click **Reset builder interface**. This removes that user's custom builder interface preferences and restores the default or assigned profile layout on the next builder load.

## Troubleshooting

- **The Builder interface entry is missing:** Check that the user has **Customize builder interface** or **Manage builder interface profiles**, and that **Disable builder interface customiser** is not enabled.
- **A user's saved layout does not appear after reload:** Check whether a builder interface profile is assigned to the user's role or user account. Assigned profiles override personal preferences.
- **A toolbar item will not hide:** Required toolbar items cannot be hidden.
- **A profile is missing after deletion:** Deleting a profile also removes role and user assignments for that profile.
- **Profile assignments did not move during import:** Importing profiles does not import role or user assignments. Assign the profiles again under **Builder access**.

---

# Command Palette

Source: https://academy.bricksbuilder.io/builder/interface/command-palette/

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

---

# Context Menu

Source: https://academy.bricksbuilder.io/builder/interface/context-menu/

*Use the Bricks context menu for quick element actions such as edit, clone, delete, structure moves, and style copy and paste.*

The Bricks context menu gives you quick access to actions for the selected element. It is especially useful for copying, pasting, duplicating, deleting, hiding, wrapping, converting, and saving reusable layout pieces.

To open it, right-click an element on the canvas or in the Structure panel.

https://youtu.be/7HpRF6jRSlc

## How the context menu selects an element

Right-clicking an element makes that element active and opens the Element panel.

The Bricks context menu is hidden in Preview mode. It also does not open from the Elements library panel, because that panel is for inserting new elements, not editing existing ones.

## Action availability

The context menu is dynamic. It changes based on:

- The current user's builder permissions.
- Whether one element or multiple elements are selected.
- Whether the selected element is nestable.
- Whether the selected element is cloneable or deletable.
- Whether the selected element is a Component instance or Component root.
- Whether the selected element is a legacy Global Element.
- Whether the clipboard currently contains Bricks data that can be pasted.

If an action is missing, it is usually because the current selection, permissions, or clipboard state does not support it.

## Main actions

| Action | What it does | Important limits |
| --- | --- | --- |
| Copy | Copies the selected element or selected elements. | Requires copy/paste element permission. |
| Paste | Pastes copied Bricks elements when the clipboard contains element data. | Requires copy/paste element permission. |
| Duplicate | Clones the active element. | Hidden for active Component roots and unavailable for elements marked as not cloneable. |
| Delete | Deletes the active element. In bulk mode, deletes the selected elements. | Hidden for active Component roots and unavailable for elements marked as not deletable. |
| Hide element | Toggles hide settings for builder, frontend, or both. | Requires access to element hide. |
| Insert | Inserts a Container, Block, or Div inside the selected layout element. Hold Cmd/Ctrl to switch to **Insert after**. | Available for nestable elements. |
| Wrap | Wraps the selected element or selected sibling elements in the configured wrapper type (Block by default). Use the adjacent icons to choose another type. Section is offered only for top-level elements. | In bulk mode, selected elements must share the same parent. |
| Unwrap | Removes a selected nestable wrapper and moves its children up to the wrapper's parent. | Requires a nestable element with children. |
| Convert | Converts Section, Container, Block, and Div layout elements to another layout type where allowed. | Only applies to layout elements. |
| Save as Component | Opens the Components workflow for the selected element. | Hidden in bulk mode, while editing Components, or for Component/legacy Global Element selections. Shown but disabled for Template and Filter elements. |
| Save as Template | Saves a nestable element as a Template. | Not available in bulk mode or while editing Components. |
| Edit Component | Opens a Component instance for editing. | Requires Component permissions. |
| Unlink Component | Converts a Component instance into regular local elements after confirmation. | Requires Component permissions. |
| Unlink Global Element | Unlinks a legacy Global Element when one exists. | Requires legacy Global Element access. |

## Copy sub-actions

The Copy row can show extra icons for more specific data:

| Copy icon/action | Copied data |
| --- | --- |
| CSS ID | The element's rendered CSS ID, including `#`. |
| Bricks ID | The internal Bricks element ID. |
| Query ID | The query ID for a selected query loop element. In Component loop contexts, this can include the instance ID. |
| Styles | Element ID styles, or active global class styles if a class is active. |
| Conditions | Element conditions. |
| Interactions | Element interactions. |
| Classes | Assigned global classes. |
| Attributes | Custom attributes. |

These actions are permission-gated. For example, copying attributes requires copy/paste element attributes permission, while copying conditions requires copy/paste element conditions permission.

## Paste sub-actions

The Paste row changes based on the clipboard data. Bricks shows only paste actions that match the current clipboard source.

| Paste action | Behavior |
| --- | --- |
| Styles | Pastes copied element styles or global class styles to the selected target. |
| Conditions | Appends copied conditions to the existing element conditions and generates new condition IDs. |
| Interactions | Appends copied interactions to the existing element interactions and generates new interaction IDs. |
| Attributes | Replaces the target element's copied custom attributes and generates new attribute IDs. |
| Classes | Merges copied global classes into the target element's existing classes without duplicates. |

Pasting styles can target one selected element or multiple selected elements. When multiple elements are selected, Bricks applies the paste operation to the selected elements.

## Bulk editing behavior

The context menu supports bulk editing, but not every action is available for multiple selected elements.

Bulk editing works best for:

- Copying selected elements.
- Deleting selected elements.
- Hiding selected elements.
- Wrapping selected sibling elements with the same parent.
- Pasting shared styles.
- Applying copied classes, conditions, interactions, or attributes where supported.

Bulk editing has important limits:

- Save as Component and Save as Template are not shown in bulk mode.
- Some copy sub-actions are disabled in bulk mode.
- Wrap requires all selected elements to share the same parent.
- Unwrap only works when the selected nestable elements contain children and the selected set does not include those children.

## Insert, wrap, unwrap, and convert

The context menu can create or reshape layout structure without dragging from the Elements panel.

### Insert

Insert adds a Container, Block, or Div inside the selected layout element, as its last child. The default insert type can be controlled by builder settings. Hold Cmd (macOS) or Ctrl (Windows) while the menu is open and the action changes to **Insert after**, which adds the new element after the selection instead.

### Wrap

Wrap places the selected element, or selected sibling elements, inside a new wrapper. Clicking **Wrap** uses the wrapper type selected in builder settings (Block by default). Use the icons next to it to choose another wrapper type. Section is only offered when the selected elements sit at the top level of the page.

Use wrap when you already built content but need an additional layout layer.

### Unwrap

Unwrap removes a selected nestable wrapper and moves its children to the wrapper's parent. It preserves child order as much as the current hierarchy allows.

Use unwrap carefully. It changes structure, not only styling.

### Convert

Convert changes one layout wrapper type into another, such as Container to Block or Div to Container. It is available for Section, Container, Block, and Div when the selected structure can be converted.

Section conversion is restricted to root-level contexts because sections are top-level layout wrappers.

## Components, templates, and legacy Global Elements

Use **Save as Component** when the selected element should become reusable and editable through the Components system.

Use **Save as Template** when the selected nestable element should become a reusable template that can be inserted later.

Legacy [Global Elements](https://academy.bricksbuilder.io/builder/features/global-elements/) can still be unlinked from the context menu when they exist. For new reusable content, use [Components](https://academy.bricksbuilder.io/builder/features/components/) or Templates.

## Permission notes

Context menu actions follow the same Builder Access permission model as the rest of the builder. A user might be able to open the context menu but not see specific actions.

Common permission-gated actions include:

- Copy/paste elements
- Copy/paste styles
- Copy/paste conditions
- Copy/paste interactions
- Copy/paste attributes
- Hide element
- Duplicate elements
- Delete elements
- Create Components
- Edit Components
- Create Templates
- Manage legacy Global Elements

Review [Builder Access](https://academy.bricksbuilder.io/builder/interface/builder-access/) when a user reports that a context-menu action is missing.

## Troubleshooting

- **The Bricks context menu does not open:** Make sure you are not in Preview mode and that you are right-clicking an existing canvas or Structure element.
- **Paste action is missing:** Copy the matching Bricks data first. The paste menu only shows actions that match the clipboard data.
- **Copy/paste behaves differently in Safari:** Safari can be stricter about clipboard access, so perform copy and paste from direct user gestures.
- **Save as Component is missing or disabled:** Check permissions and make sure you are not bulk editing, editing an active Component, selecting a Component or legacy Global Element, or selecting a Template or Filter element.
- **Wrap is missing or disabled:** Confirm the selected elements share the same parent and can be wrapped in the current hierarchy.

---

# Adding & Editing Elements

Source: https://academy.bricksbuilder.io/builder/interface/editing-elements/

*Add elements to the canvas, edit their settings, and understand the main element editing workflow in Bricks.*

Elements are the building blocks of a Bricks layout. This article explains how elements are added, selected, nested, styled, reset, copied, and edited in single-element and bulk-edit workflows.

## Element mental model

A Bricks layout is an element tree. Every element has:

- A type, such as Section, Heading, Image, Button, or Form.
- A unique Bricks ID.
- Optional children if the element can contain other elements.
- A parent, unless it is a root element.
- Settings, which store content, styles, classes, conditions, interactions, custom attributes, and other element-level data.

Root elements sit at the top of the page content. Nested elements sit inside another element. The canvas shows the visual result; the Structure panel shows the actual hierarchy.

## Add an element

Open the Elements panel, then drag an element onto the canvas or into the Structure panel.

Where the element lands depends on the current drop target:

- Drop onto a nestable element to place the new element inside it.
- Drop between siblings to place the new element at that position.
- Drop at root level to create a top-level element.

You can also add layout elements from the [Context Menu](https://academy.bricksbuilder.io/builder/interface/context-menu/) when an existing nestable element is selected.

## Layout elements

The current layout elements are **Section**, **Container**, **Block**, and **Div**.

Use them as structural wrappers:

- **Section**: Common top-level page section.
- **Container**: Common content-width wrapper.
- **Block**: Generic block-level wrapper.
- **Div**: Generic wrapper with fewer layout assumptions.

Not every element can contain children. Elements that can contain children are nestable. Non-nestable elements, such as many content elements, can be moved, styled, copied, or deleted, but they cannot be used as parents.

## Select and edit an element

Click an element on the canvas or in the Structure panel to select it. The panel switches to the selected element and shows its controls.

> **Note**
>
> You can edit text directly on the canvas by clicking on it and typing. Select text portions with your mouse to reveal the text formatting toolbar with styling options such as bold, italic, and links.

The panel header shows the selected element label. You can rename the label to make the Structure panel easier to scan. The label is for builder organization and does not change the HTML tag or frontend text by itself.

The panel can also show quick actions for hide settings, conditions, interactions, Components, and legacy Global Elements depending on the selected element and your permissions.

## Content controls

Content controls affect the element's markup, data, and behavior. Examples include an Image element's image source, a Button element's link, a Heading element's text, or a Form element's fields and actions.

The screenshot below shows Content controls for the Image element:

![Panel: Content (Tab)](https://academy.bricksbuilder.io/assets/bricks-academy-panel-content-tab-1024x576.png)

<figcaption>

Element Image: Content Tab

</figcaption>

Content controls are not only for visible text. They can also control semantic tags, attributes, query settings, form behavior, media sources, links, and dynamic data.

## Style controls

Style controls affect the CSS Bricks generates for the selected element, active class, active selector, active pseudo state, and active breakpoint.

Style controls are commonly grouped into:

- Layout
- Typography
- Background
- Border / Box Shadow
- Gradient / Overlay
- Shape Dividers
- Transform
- CSS

![Panel: Style (Tab)](https://academy.bricksbuilder.io/assets/bricks-academy-panel-style-tab-1024x576.png)

<figcaption>

Element Image: Style Tab

</figcaption>

Before changing styles, check which selector is active at the top of the panel:

- If the element ID is active, styles apply only to that element.
- If a global class is active, styles apply to that class everywhere it is used.
- If a pseudo selector is active, styles apply to that selector state.
- If a breakpoint is active, responsive style values are stored for that breakpoint.

This is the most important styling habit in Bricks: select the target first, then change the control.

## Classes, selectors, and responsive edits

The selector area above the Content/Style tabs controls whether you are styling the element ID, a global class, or a selector/pseudo state.

Use global classes for reusable styling. Use the element ID for one-off styling. Use selectors and pseudo classes when styling states or child selectors.

Responsive edits are controlled by the active breakpoint in the toolbar. A control indicator can show when a control has a value at the active breakpoint or another breakpoint, depending on your builder settings.

## Bulk editing

You can select multiple elements with Cmd/Ctrl or Shift selection. Bulk editing is useful for shared style changes, class assignment, moving, hiding, deleting, and some context-menu actions.

Bulk editing has limits:

- Bricks calculates the settings shared by the selected elements.
- If selected elements have different values, the shared control can appear empty.
- Editing a shared setting applies that change to the selected elements.
- If different element types are selected, Bricks shows only the Style tab.
- Some actions are disabled in bulk mode, such as saving as a Component or Template.
- Bulk wrapping only works when selected elements share the same parent.

Use bulk editing for broad, predictable operations. For content-heavy edits, edit one element type at a time.

## Hide, conditions, and interactions

Element-level hide settings, conditions, and interactions are opened from the element panel header when available.

- **Hide element** can hide an element in the builder, on the frontend, or both.
- **Conditions** control whether the element should render for the current request.
- **Interactions** attach frontend behavior to triggers and actions.

These panels are permission-gated. If you cannot see them, check [Builder Access](https://academy.bricksbuilder.io/builder/interface/builder-access/).

## Components and locked editing states

When you select a Component instance, Bricks shows instance controls and exposed properties instead of treating every nested element as local page content. To edit the Component definition, enter Component editing mode.

Some elements may also be disabled through the Element Manager or unavailable because their element type no longer exists. In those cases, Bricks shows a notice instead of normal controls.

Legacy Global Elements can still appear on existing sites. Bricks marks them as deprecated and recommends Components for new reusable content.

## How To Reset Controls

Controls that have a stored value show a small indicator next to the control label or group label. Hover the indicator to reveal the reset action.

You can reset:

- A single control.
- A control group, such as Typography.
- Element ID styles.
- Active class styles, if you are styling a class and it is not locked.

Resetting style controls removes the stored style values for the current target. It does not remove content such as text, links, form fields, or image selections.

When styling a global class, resetting styles affects that class, not only the selected element.

## Copy & Paste Styles

To copy and paste element styles, right-click an element on the canvas or in the Structure panel to reveal the context menu. Use **Copy Styles**, then select the target element and use **Paste Styles**.

Style paste respects the copied style data and the current target:

- Pasting element styles applies copied style settings to the target element.
- Pasting global class styles applies copied class style settings when a class is the active target.
- Shape dividers, custom CSS, and other complex style controls are handled as style data when supported.

For more copy and paste actions, including classes, conditions, interactions, and attributes, use the [Context Menu](https://academy.bricksbuilder.io/builder/interface/context-menu/).

## Practical editing checklist

Before making a change, confirm:

- The correct element is selected.
- The correct selector is active: element ID, class, or pseudo selector.
- The correct breakpoint is active.
- You are editing Content for markup/data changes or Style for CSS changes.
- You are not accidentally editing a Component definition when you meant to edit an instance.
- You have saved before testing frontend behavior.

---

# Keyboard Shortcuts

Source: https://academy.bricksbuilder.io/builder/interface/keyboard-shortcuts/

*Speed up Bricks workflows with keyboard shortcuts for editing, navigating, saving, and other builder actions.*

Quickly perform the most common in-builder actions through short & simple keyboard shortcuts:

| **Key Combination** | **Description** |
| --- | --- |
| `CMD / CTRL` | Insert element outside active nestable/parent element |
| `CMD / CTRL + S` | Save changes |
| `CMD / CTRL + Shift + S` | Force save all data |
| `CMD / CTRL + K` | Open command palette |
| `CMD / CTRL + .` | Toggle Style Manager |
| `CMD / CTRL + Shift + .` | Toggle Builder Browser |
| `CMD / CTRL + P` | Toggle preview mode |
| `CMD / CTRL + B` | Switch between responsive editing modes |
| `CMD / CTRL + C` | Copy selected element(s), when not editing text or an input and permission allows |
| `CMD / CTRL + V` | Paste copied element(s), when not editing text or an input and permission allows |
| `CMD / CTRL + Z` | Undo your last change |
| `CMD / CTRL + ALT + NUMBER` | Quick Access Bar: Go to tab/control group |
| `1-8` | Switch Style Manager tabs while the Style Manager is open |
| `CMD / CTRL + Shift + Arrow down` | Edit next element (same level) |
| `CMD / CTRL + Shift + Arrow up` | Edit previous element (same level) |
| `CMD / CTRL + Shift + Arrow right` | Edit first child element |
| `CMD / CTRL + Shift + Arrow left` | Edit parent element (container) |
| `CMD / CTRL + Shift + Z` | Redo your last change |
| `CMD / CTRL + Shift + D` | Duplicate selected element |
| `CMD / CTRL + Shift + F` | Focus on element setting search input (in panel) |
| `CMD / CTRL + Shift + L` | Open Builder Browser on the Templates view |
| `CMD / CTRL + Shift + P` | Wrap in the configured wrapper element |
| `CMD / CTRL + Shift + H` | Show history panel |
| `CMD / CTRL + Shift + V` | View on frontend |
| `CMD / CTRL + Shift + C` | Show components panel |
| `CMD / CTRL + Shift + X` | Show structure panel |
| `CMD / CTRL + Shift + E` | Show elements panel (and focus on search) |
| `CMD / CTRL + Delete` | Delete active element (and its children) |
| `CMD / CTRL + ENTER` | Toggle element classes UI |
| `Shift (modifier)` | Hold down "Shift" to:<br />- Adjust element spacing (margin, padding) or container sizing (height, width) on the canvas in steps of 5 (custom units) or 10 (default unit = px)<br />- Directly edit new element |
| `ESC` | Cancel/close popup (templates, documentation, etc.) |
| `ALT/OPTION + T` | Focus on toolbar (logo). TAB through toolbar possible |

---

# Start Editing With Bricks

Source: https://academy.bricksbuilder.io/builder/interface/editing-with-bricks/

*Start editing with Bricks by understanding the builder layout, canvas behavior, and the basic flow for working on a page.*

This article explains how to open the Bricks builder, what each main area of the interface does, and how editing with Bricks relates to rendering the page on the frontend.

## Before you open the builder

Bricks shows builder entry points when the current post can be edited with Bricks:

- The current user has permission to use the builder.
- The post type is enabled for Bricks.
- The post can be edited by the current user.

Bricks checks the license when the builder opens. If the license is not valid, Bricks redirects to the [license screen](https://academy.bricksbuilder.io/builder/license/license-and-updates/) instead of loading the builder.

Go to **Bricks -> Settings** and select the post types you want to edit with Bricks:

![](https://academy.bricksbuilder.io/assets/bricks-settings-post-types.png)

> **Note**
>
> While you can enable Bricks for blog posts, most sites work better when posts are written in the WordPress editor and displayed through a Bricks template. Use Bricks for the layout, and use WordPress for the editorial content.

## Open the builder

You can open the builder from several places in WordPress.

### Posts list

Hover over a supported post, page, or custom post type in the WordPress dashboard and click **Edit with Bricks**:

![](https://academy.bricksbuilder.io/assets/docs-edit-with-bricks-button.png)

### Post edit screen

When editing an existing post or creating a new one, click **Edit with Bricks** in the Bricks editor area:

![](https://academy.bricksbuilder.io/assets/bricks-post-edit-screen-1024x576.png)

### Frontend admin bar

When you are logged in and viewing the page on the frontend, use the WordPress admin bar. The Bricks menu can open the current page, the active header template, the active content template, the active footer template, or the Templates screen when those links apply to the current page.

If the **Edit with Bricks** link is missing, check the current user's builder permissions and make sure the post type is enabled under **Bricks -> Settings**.

## Edit with Bricks vs render with Bricks

Editing with Bricks opens the visual builder. Rendering with Bricks controls which content source the frontend uses.

A post can have WordPress editor content, Bricks data, or both. The **Render with Bricks** / **Render with WordPress** option in the admin bar switches the editor mode for the current post. If a post is set to render with WordPress, its Bricks data remains stored, but the frontend uses the WordPress content instead.

Bricks templates are different. Templates are Bricks documents by definition, so the editor mode toggle does not apply to them.

Use the render mode deliberately:

- Choose **Render with Bricks** when the page itself is built in Bricks.
- Choose **Render with WordPress** when the page should use normal WordPress content, usually with a Bricks template controlling the surrounding layout.
- Do not use the render toggle as a content backup system. It only chooses the frontend render source.

If a page is rendered with Bricks, the post list shows a **- Bricks** status after the title:

![](https://academy.bricksbuilder.io/assets/bricks-post-screen-post-status.png)

<figcaption>

Post status "Bricks" shows you that a page is rendered with Bricks

</figcaption>

## Delete Bricks data

The admin bar and post edit screen can show a **Delete Bricks data** button when this option is enabled in **Bricks -> Settings**.

This removes Bricks-generated data from the current post, including page content, page settings, header/footer data, editor mode, and template type metadata. Treat it as destructive. Use it only when you want the post to stop using its stored Bricks layout data.

## Builder anatomy

The builder is made of four main working areas.

### Toolbar

The toolbar runs across the top of the builder. It gives you access to global builder actions and mode switches, including:

- Style Manager
- Pages panel
- Templates
- Settings
- Command Palette
- Elements and Components
- Breakpoints
- Preview width, height, and scale
- Reload canvas
- Undo and redo
- Preview and save actions

Which buttons you see depends on your permissions and global builder settings. For example, template actions require template permissions, and the breakpoints manager requires breakpoint access.

### Panel

The left panel changes depending on what you are doing. It can show the element library, the selected element controls, page/template settings, revisions, pages, or other manager views.

The panel can be resized and minimized. When an element is selected, the panel shows the element label, element actions, class/selector controls, and the relevant Content and Style controls.

### Canvas

The canvas is the live visual preview of the current page. It renders the Bricks layout in an iframe, so selecting and editing elements feels close to editing the frontend output.

The canvas can be reloaded from the toolbar. Reloading is useful after changing settings that need a fresh render, or when external scripts, query data, or dynamic content affect the preview.

### Structure panel

The Structure panel shows the element tree. It is the safest place to understand nesting, select hard-to-click elements, move elements, and work with deeply nested layouts.

Use the Structure panel whenever the canvas view is visually crowded, an element is hidden, or you need to confirm parent-child relationships.

## First successful edit workflow

Use this workflow when creating or editing a normal page:

1. Enable the page post type under **Bricks -> Settings**.
2. Create or open the page in WordPress.
3. Click **Edit with Bricks**.
4. Open the Elements panel and add a layout element, such as a Section or Container.
5. Add content elements inside the layout.
6. Select an element on the canvas or in the Structure panel.
7. Edit its Content controls for markup and data.
8. Edit its Style controls for design.
9. Switch breakpoints and adjust responsive styles where needed.
10. Save the builder.
11. Preview the page and confirm it is rendered with Bricks.

## Common builder states

### Preview mode

Preview mode hides the normal editing controls so you can inspect the layout. While previewing, builder editing actions such as the custom context menu are disabled.

### Unsaved changes

The builder tracks history and unsaved changes. Use save before leaving the builder, switching important context, or testing frontend-only behavior.

### Unsupported post type

If a post type is not enabled for Bricks, Bricks redirects you back to WordPress admin instead of opening the builder. Enable the post type under **Bricks -> Settings** or use a Bricks template for that content type.

### Missing permissions

Users can have full access, content-editing access, or custom permission sets. Missing permissions can hide toolbar buttons, element categories, manager popups, settings panels, and editing controls. Review [Builder Access](https://academy.bricksbuilder.io/builder/interface/builder-access/) if a user can open the builder but cannot see or edit a specific area.

### Login or license redirects

If the builder detects that the current browser session is no longer logged in, it redirects to the login page. If the license is not valid, Bricks redirects to the [license screen](https://academy.bricksbuilder.io/builder/license/license-and-updates/).

## Troubleshooting checklist

- **No Edit with Bricks button:** Check post type support, user permissions, and whether the current user can edit the post.
- **The page opens in WordPress instead of Bricks:** Confirm the page has Bricks data or switch the admin bar render mode to **Render with Bricks**.
- **Builder opens but controls are missing:** Check builder permissions and whether the selected element is disabled.
- **Canvas looks stale:** Reload the canvas from the toolbar.
- **Page looks different on the frontend:** Save the builder, confirm render mode, and test outside preview mode.

---

# Builder Mode (Custom)

Source: https://academy.bricksbuilder.io/builder/interface/builder-mode/

*Customize the Bricks builder color scheme with custom builder-mode CSS variables.*

Starting with Bricks 1.3.7 you can customize the builder mode (color scheme) to your liking by tweaking a few CSS variables.

You first have to set the "Builder Mode" under Bricks → Settings → Builder to "Custom" and save your settings.

The following new setting called "Builder Mode (Custom)" should now appear:

![Builder Mode: Custom](https://academy.bricksbuilder.io/assets/bricks-setting-builder-mode-custom-1024x721.png)

Below you can find a starter CSS snippet with commonly customized builder CSS variables. Bricks 2.x defines additional variables for classes, components, status colors, muted colors, and the canvas scrollbar, so use this as a starting point and override any extra variables your custom mode needs.

```php
[data-builder-mode=custom] {
  --builder-bg: #f6f4f2;
  --builder-bg-2: #efebe6;
  --builder-bg-3: #e7e1da;
  --builder-bg-4: #dbd2c8;
  --builder-bg-accent: #EED8FD;

  --builder-color: #2e271e;
  --builder-color-description: #76634c;
  --builder-color-accent: #7209B7;
  --builder-color-accent-inverse: #fff;

  --builder-color-knob: #c8baaa;
  --builder-border-color: #d8cec2;
  --builder-placeholder-opacity: .33;

  --builder-color-class: #2b6cb0;
  --builder-bg-class: #d8e8f6;
  --builder-color-component: #6b46c1;
  --builder-bg-component: #eadcf8;
  --builder-color-info: #006c9c;
  --builder-bg-info: #d9f1ff;
  --builder-color-danger: #b42318;
  --builder-bg-danger: #ffe4e2;
  --builder-color-success: #027a48;
  --builder-bg-success: #dcfae6;
  --builder-color-muted: #7a6f63;
  --builder-bg-muted: #e2ddd6;

  --builder-canvas-scrollbar-thumb: #c8baaa;
  --builder-canvas-scrollbar-thumb_hover: #76634c;
  --builder-canvas-scrollbar-track: #efebe6;

  --bricks-tooltip-bg:   #16130f;
  --bricks-tooltip-text: #f6f4f2;
}
```

If you copy the CSS above, paste it into your "Builder Mode (Custom)" setting, and save your settings, your builder should look like this:

![](https://academy.bricksbuilder.io/assets/bricks-screenshot-builder-mode-custom-1024x576.png)

<figcaption>

Bricks builder with a custom color scheme (mode)

</figcaption>

### Resources

- Color palettes: [https://coolors.co/palettes/trending](https://coolors.co/palettes/trending)
- Color palettes: [https://colorhunt.co](https://colorhunt.co)
- Generate color shades & tints: [https://www.colorhexa.com](https://www.colorhexa.com)

Note: In custom builder mode, Code element's background color changes to a light color scheme.

---

# Page Settings

Source: https://academy.bricksbuilder.io/builder/interface/page-settings/

*Use Bricks page settings to control per-page markup, styling, SEO metadata, social sharing output, and custom code.*

Page Settings control output for the page, post, or content template you are currently editing. They are different from global Bricks settings and different from an individual element's controls.

Use Page Settings when a setting should apply to the whole current page, such as body classes, header/footer visibility, page-level scroll snap, SEO metadata, social sharing data, or page-specific code.

## Open Page Settings

Open the builder and click the **Settings** icon in the toolbar. Choose **Page Settings**.

Page Settings are available only when the current user has permission to access them. Some groups can also be hidden by global settings.

Use the **Reset** icon in the panel header to clear all page settings with a single click.

## How Page Settings are applied

Page Settings are stored with the current Bricks document. On the frontend, Bricks reads those settings while rendering the page.

Some settings change markup, such as body classes or disabling the header. Some generate CSS, such as scroll snap and Custom CSS. Some print metadata or scripts into the document head or body. Some settings are visible in the builder immediately, while others should be checked on the frontend.

![](https://academy.bricksbuilder.io/assets/bricks-page-settings.png)

## General settings

The General group contains page-wide output options.

| Setting | What it does |
| --- | --- |
| CSS classes (body) | Adds space-separated classes to the page `<body>` tag. Dynamic data can be used when appropriate. |
| Disable header | Prevents the active Bricks header from rendering on this page. Not shown for header or footer templates. |
| Disable footer | Prevents the active Bricks footer from rendering on this page. Not shown for header or footer templates. |
| Disable lazy load | Disables Bricks lazy loading for the current page. |
| Disable popups | Prevents Bricks popups from rendering on the current page. |
| Page layout | Overrides the page layout inherited from Theme Styles. |
| Page background | Overrides the page background inherited from Theme Styles. |
| Content margin | Overrides the content margin inherited from Theme Styles when available. |

Use these settings for page-specific exceptions. If you need the same behavior on many pages, use global settings, Theme Styles, or templates instead.

## Scroll snap

The Scroll snap group configures page-level CSS scroll snapping.

| Setting | What it does |
| --- | --- |
| Type | Sets the page scroll-snap type on the `html` element. |
| Snapping elements selector | Defines which elements should snap. Defaults to Bricks sections when left empty. |
| Align | Sets the snap alignment of snapping elements. |
| Margin | Sets scroll margin for snapping elements. |
| Padding | Sets scroll padding on the `html` element. |
| Stop | Sets scroll-snap-stop behavior. |

Scroll snap is primarily a frontend behavior. Test it on the frontend, not only in the builder canvas. Layout height, overflow, sticky headers, and browser behavior can affect the result.

If you use a custom selector, make sure the selector matches the elements that should become snap points. If the selector matches nothing, the page can have scroll snap enabled without visible snapping.

## One Page Navigation {#one-page-nav}

If enabled, Bricks adds a vertical dot menu to the right edge of the page in a fixed position, with each dot linking to the page's root element.

![](https://academy.bricksbuilder.io/assets/bricks-one-page-navigation-1024x534.png)

One Page Navigation is shown only where it applies, such as normal pages and content templates. It is not shown for header or footer templates.

The navigation uses the IDs Bricks renders for root elements. Add custom CSS IDs when you need stable, readable anchors or when root elements are generated dynamically.

> **Note**
>
> If a root element is inside a query loop, use dynamic data in the CSS ID, such as a post ID or slug, so every repeated root element has a unique anchor.

![](https://academy.bricksbuilder.io/assets/one-page-navigation-loop-unique-css-id.png)

The One Page Navigation controls style the dot menu and its active state:

- Spacing
- Item width and height
- Item color
- Border
- Box shadow
- Active item width and height
- Active item color
- Active border
- Active box shadow

The active dot changes based on the root element currently in the scroll range.

## SEO

The SEO group controls page-level metadata. This group is hidden when Bricks SEO output is disabled globally.

| Setting | What it does |
| --- | --- |
| Permalink | Updates the post slug. Use lowercase words separated by dashes. |
| Title | Updates the WordPress post title after applying the change. |
| Document title | Sets the frontend SEO title without changing the WordPress post title. |
| Meta description | Prints a page-level meta description. |
| Meta keywords | Prints page-level meta keywords. |
| Meta robots | Prints robots directives such as `noindex` or `nofollow`. |

Use **Save new title/permalink** after changing the post title or permalink in the SEO group. Other page settings are saved through the normal builder save flow.

If you use a dedicated SEO plugin, decide which tool owns the metadata. Avoid setting competing metadata in multiple places.

## Social media

The Social media group controls Open Graph style sharing data for the current URL. This group is hidden when Bricks Open Graph output is disabled globally.

| Setting | Default when empty |
| --- | --- |
| Title | The post/page title. |
| Description | The post/page excerpt. |
| Image | The featured image. |

Use this group when a page needs a social title, description, or image that differs from its normal SEO data.

## Custom Code

The Custom Code group adds page-specific CSS and scripts.

| Setting | Output location |
| --- | --- |
| Custom CSS | Inline CSS in the document `<head>`. Supports breakpoint-specific values. |
| Header scripts | Before the closing `</head>` tag. |
| Body (header) scripts | Immediately after the opening `<body>` tag. |
| Body (footer) scripts | Before the closing `</body>` tag. |

Script fields are shown only to users who are allowed to add unfiltered HTML. Users without that capability see an informational notice instead.

Use page-level code sparingly. Prefer element settings, classes, Theme Styles, global settings, or properly enqueued code when the behavior should be reused across the site.

## Common mistakes

- **Changing SEO title but not applying it:** Use **Save new title/permalink** for title and slug changes.
- **Expecting header/footer disable to affect templates globally:** These settings affect only the current page render.
- **Using duplicate IDs for One Page Navigation:** Give repeated root elements unique IDs, especially inside query loops.
- **Testing scroll snap only in the builder:** Always test on the frontend.
- **Adding scripts without the right capability:** Script fields require permission to add unfiltered HTML.
- **Using page code for reusable behavior:** Page Custom Code is local to the current page. Use global settings or enqueue code for site-wide behavior.

---

# Responsive Editing

Source: https://academy.bricksbuilder.io/builder/interface/responsive-editing/

*Edit Bricks designs responsively across breakpoints and adjust layout, spacing, and element settings for smaller screens.*

What looks great on a large desktop screen usually needs some refinement for smaller devices. This typically involves applying smaller font sizes, margins, paddings, column width/stacking, or hiding certain elements on smaller devices.

Bricks provides the following four breakpoints out-of-the-box:

| **Breakpoint** | **@media query** |
| --- | --- |
| Desktop | Base breakpoint |
| Tablet portrait | &lt; 992px |
| Mobile landscape | &lt; 768px |
| Mobile portrait | &lt; 478px |

Styles set on the base breakpoint are inherited by all other breakpoints.

Once you've finished styling a page on the base breakpoint (desktop), make sure to view & adjust the styling on the other breakpoints too.

## Background video on larger breakpoints only

The Background control includes **Start play at** for background videos. Select the smallest breakpoint where the video should run. Below that width, Bricks stops before assigning the video source, so the desktop video is not downloaded by the native background-video script.

To show an image on smaller screens:

1. Set the background video on the element.
2. Set **Start play at** to the smallest breakpoint that should play it.
3. Set a background image for the smaller breakpoint.

To view & edit the styles for a specific breakpoint simply click on its breakpoint icon located in the center of the builder toolbar. Or via the [keyboard shortcut](https://academy.bricksbuilder.io/builder/interface/keyboard-shortcuts/) "CMD/CTRL + B".

![](https://academy.bricksbuilder.io/assets/bricks-1.5.1-in-builder-breakpoint-mobile-landscape-1024x576.jpg)

<figcaption>

Editing in the "Mobile landscape" breakpoint

</figcaption>

Next to the breakpoint icons are inputs for width ("W"), height ("H"), and scale (%).

## Custom Breakpoints {#custom-breakpoints}

To start using custom breakpoints, you first have to enable them in your WordPress dashboard under `Bricks > Settings > General > Custom breakpoints`:

![](https://academy.bricksbuilder.io/assets/bricks-enable-custom-breakpoints.jpg)

Once enabled, you can access the **breakpoint manager** in the builder by clicking the three-dotted icon in the builder toolbar (next to the first breakpoint icon):

![](https://academy.bricksbuilder.io/assets/bricks-1.5.1-breakpoint-manager-default-breakpoints.jpg)

<figcaption>

Breakpoint Manager (open via the three-dotted icon in the builder toolbar)

</figcaption>

### Editing a breakpoint

Clicking the pencil icon brings up the editing options of the selected breakpoint:

![](https://academy.bricksbuilder.io/assets/bricks-edit-default-breakpoint.jpg)

<figcaption>

Editing the default "Tablet portrait" breakpoint

</figcaption>

You can edit the following breakpoint properties:

| **Property** | **Description** |
| --- | --- |
| Label | Used when hovering over the breakpoint icon in the builder toolbar |
| Width (px) | @media query min-width/max-width value (depending on the base breakpoint) |
| Width (Builder) | Width is used when switching to the breakpoint in the builder |
| Icon | Used as the breakpoint icon in the builder toolbar |
| Base breakpoint | Set breakpoint as base breakpoint |
| *Key* | *Not customizable (used to store & identify breakpoint settings)* |

The most common action is to customize the widths of the default (mobile) breakpoints. The following screenshot shows you the "Tablet portrait" with a custom width of 1023px:

![](https://academy.bricksbuilder.io/assets/bricks-edit-breakpoint-width.jpg)

That means any styles set on the "Tablet portrait" breakpoint will apply to devices with a width of less than 1024px.

### Creating new breakpoints

You can create as many additional custom breakpoints as you want. Although, it is recommended to customize the widths of the default mobile breakpoints to your liking before utilizing more breakpoints.

You should rarely need more than one or two additional breakpoints on top of the default ones.

Clicking the "+" (plus) icon in the breakpoint manager's header launches the breakpoint creator form.

The following screenshot shows how we created a  new breakpoint named "Large" with a width of 1400px:

![](https://academy.bricksbuilder.io/assets/bricks-create-new-breakpoint.jpg)

<figcaption>

Creating a new breakpoint

</figcaption>

Once you click "Create" your newly created breakpoint should appear in the breakpoint manager (alongside a "CUSTOM" label) & in the builder toolbar like this:

![](https://academy.bricksbuilder.io/assets/bricks-custom-breakpoint-large-created.jpg)

<figcaption>

Breakpoint manager with new custom breakpoint

</figcaption>

As we've set the width of this new breakpoint to 1400px, it shows as the first breakpoint, as it is now the largest of our breakpoints. The Desktop (base breakpoint) has a default width of 1279px.

### Pausing a custom breakpoint

You can pause any of your custom breakpoints by toggling the checkbox at the right-hand side of the breakpoint manager:

![](https://academy.bricksbuilder.io/assets/bricks-pause-custom-breakpoint.jpg)

<figcaption>

Pausing custom breakpoint "Large"

</figcaption>

Pausing a custom breakpoint allows you to skip generating the styles for it on the frontend, while still retaining the styles you've set throughout your site without having to delete them one by one. Which, on a full-built-out site, can go into thousands of settings.

### Resetting a default breakpoint

To restore the default values of a default breakpoint, click on the "reset" icon (next to the pencil) icon.

### Resetting all breakpoints

Clicking the "gear" icon in the breakpoint manager header opens up the "Reset: Breakpoints" action. Clicking this button removes all your breakpoint edits (default & custom breakpoints) from the database.

> **Note**
>
> **Breakpoint-specific settings performed on an element or the Theme Styles are not deleted. Please choose desktop or mobile-first at the very beginning.**

![](https://academy.bricksbuilder.io/assets/bricks-reset-all-breakpoints.jpg)

### Understanding the base breakpoint

The base breakpoint doesn't have a @media query. So all styles set on the base breakpoint apply to all screen widths.

That is why, by default, any styles set on the "Desktop" breakpoint are visible on any other breakpoint. Unless you specify a style on a specific breakpoint. Then the breakpoint-specific rule precedes the base breakpoint style.

When editing a breakpoint, you can set it as the "Base breakpoint". Then all styles set on this new base breakpoint are inherited up & down the breakpoint chain.

In the following screenshot, you can see that the "Tablet portrait" breakpoint has been set as the base breakpoint.

The yellow dot, lines, and arrows next to the breakpoint icons should help to visualize the style inheritance:

![](https://academy.bricksbuilder.io/assets/bricks-custom-base-breakpoint.jpg)

<figcaption>

Changed base breakpoint to "Tablet portrait"

</figcaption>

### Mobile-first design {#mobile-first}

Styling in Bricks, by default, happens from the largest breakpoint down to "Tablet portrait" > "Mobile landscape" and "Mobile portrait".

Utilise a so-called `**mobile-first**` design approach by setting the smallest breakpoint as the base breakpoint.

The following screenshot shows the "Mobile portrait" (our smallest breakpoint) set as the base breakpoint. We now use the mobile-first approach. Also indicated by the "MOBILE FIRST" label in the breakpoint manager header:

![](https://academy.bricksbuilder.io/assets/bricks-mobile-first.jpg)

<figcaption>

Mobile-first design in Bricks

</figcaption>

You'll also notice that the order of the breakpoints is reversed and now starts at the smallest breakpoint. You can now start to design your pages starting at the smallest breakpoint.

### Regenerating (Bricks) CSS files

Whenever you customize the width of a default breakpoint, Bricks automatically updates any Bricks CSS files (like frontend.min.css, etc.) that contain media queries for this breakpoint.

If you experience that your breakpoint widths on the front end are not correctly applied, please regenerate your Bricks CSS files by clicking the "Regenerate CSS files" button under `Bricks > Settings > General > Custom breakpoints`.

## Responsive control indicator {#responsive-control-indicator}

In Bricks 1.11.1, we introduced the responsive control indicator which helps you see which controls can have different values at different breakpoints. We provide multiple options for when to show this indicator to suit different preferences. You can adjust these under `Bricks > Settings > Builder > Control panel > Responsive control indicator`:

- **Show if any value exists (Default)**: Displays if a control has any value set across breakpoints.
- **Show if non-base breakpoint value exists**: Shows only if a control’s value differs from the base breakpoint.
- **Show on all responsive controls**: Displays on all responsive controls, regardless of values.
- **Disable**.

![](https://academy.bricksbuilder.io/assets/bricks-responsive-control-indicator.png)

---

# Revisions

Source: https://academy.bricksbuilder.io/builder/interface/revisions/

*Review, restore, and manage Bricks revisions so you can safely recover earlier builder states.*

When you save builder data changes, Bricks creates a revision/snapshot of the relevant Bricks data and page settings (template, page, etc.) using the official WordPress Revisions API.

Bricks also stores autosaves separately. Autosaves are backup copies from the autosave process, while regular revisions are created when Bricks element data or page settings are included in a manual save. After a regular revision is created, Bricks clears the related autosave.

You can browse, preview, and apply your revisions inside the builder by clicking the **Revisions** (clock) icon in the builder toolbar, then going to the "Revisions" tab.

Select any revision in this list to preview it. The canvas should automatically update showing you the selected revision.

Click **Apply** to continue editing the selected revision. Click **Discard** to continue editing your current version.

If your builder capability includes **Delete revisions**, you can delete individual revisions or delete all revisions from the Revisions panel.

![](https://academy.bricksbuilder.io/assets/builder-revisions-1024x576.png)

## Manage the number of Bricks revisions {#bricks_max_revisions_to_keep}

In order to limit the number of Bricks revisions, you may define the constant `BRICKS_MAX_REVISIONS_TO_KEEP` like so (insert this code in the Bricks child theme):

```php
if ( ! defined( 'BRICKS_MAX_REVISIONS_TO_KEEP' ) ) {
    define( 'BRICKS_MAX_REVISIONS_TO_KEEP', 10 );
}
```

By default, Bricks sets the maximum to 100 revisions per post for the Bricks templates and enabled post types.

You may set the following values:

- true: unlimited revisions
- false or 0: do not store any Bricks' revisions
- value above 0: store up to this number of revisions per post. Old revisions are automatically deleted.

---

# Save & Publish

Source: https://academy.bricksbuilder.io/builder/interface/save-publish/

*Understand how saving and publishing work in Bricks, including drafts, updates, and when frontend changes go live.*

Bricks, by default, automatically creates an autosave every 60 seconds when the current builder area has unsaved element changes.

Autosave creates a backup copy of the elements on the canvas. It does not save global data such as components, classes, or variables. Autosaves can be restored under **Manage > History / Revisions** from the builder toolbar.

To adjust or disable the autosave interval go to **Bricks > Settings > Builder** in your WordPress admin area. The default interval is 60 seconds, and the minimum interval is 15 seconds.

Bricks detects unsaved changes and will show you a prompt to help prevent data loss in case you reload the builder by accident.

To manually save your changes click the **Save** (disk) icon at the very right of the builder toolbar. Or use the [keyboard shortcut](https://academy.bricksbuilder.io/builder/interface/keyboard-shortcuts/) CMD/CTRL + S.

**Bricks creates a revision/snapshot** when changed Bricks data or page settings are saved using the standard WordPress Revisions API ([learn more about revisions](https://academy.bricksbuilder.io/builder/interface/revisions/)).

Designing a stunning website or writing compelling content is hard. That's why Bricks celebrates every saved change by displaying a random save message to keep your spirit up :)

You can, of course, customize those save messages via the [bricks/builder/save_messages](https://academy.bricksbuilder.io/developer/hooks/filters/filter-save-messages/) filter.

## Publishing A Page

When an unpublished page (draft) is saved the status does not change by itself. So once your page is ready to be published click the **Publish** (power) icon in the builder toolbar.
