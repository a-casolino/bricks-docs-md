*Control who can access Bricks and which builder capabilities are available for different WordPress roles.*

Bricks gives you full control over who can access the builder, and what actions they're allowed to perform. You can either assign a **predefined capability**, or create your own **custom capability** that allows only the specific permissions you enable for it.

This gives you complete freedom and control to tailor the builder experience to any roles (i.e. content editor, designer, client, etc.) depending on what they should be able to do.

https://youtu.be/5C52ddR5f54

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

Every role except Administrator starts with **No access**. Administrators always have full access, and their setting can't be changed.

## Creating a custom capability {#custom}

If you need precise control over the actions a user or role should be able to perform, you can create your very own custom builder capability, following the steps outlines below.

1. Go to **Bricks > Settings > Builder access**
2. Under **Builder capabilities**, click **Add new capability**

![](https://academy.bricksbuilder.io/assets/bricks-builder-access-add-custom-capability.png)

Inside the capability popup, you can:

- Give the capability a name & a description
- Enable exactly the permissions you want to grant

![](https://academy.bricksbuilder.io/assets/bricks-builder-access-permissions.png)

Close the popup and click **Save Settings**. The new capability is only stored once the settings are saved.

Once created, you can assign this capability to specific users or user roles.

## Assigning capabilities

You can assign any builder capability, whether predefined or custom:

- To a **user role**, under **Bricks > Settings > Builder access > Builder access**

![](https://academy.bricksbuilder.io/assets/bricks-builder-access-custom-capabilities.png)

- To a **specific user**, by editing their WordPress user profile

![](https://academy.bricksbuilder.io/assets/bricks-builder-edit-user-profile.png)

![](https://academy.bricksbuilder.io/assets/bricks-builder-access-user-settings.png)

This gives you flexibility to apply permissions globally or individually.

A capability set on a user's profile overrides the one assigned to their role. The first option in the user's **Builder access** dropdown shows the role's capability marked **(Default)**. Select it to let the user follow their role again.

Builder access works on top of the user's WordPress role. Bricks only opens a page in the builder if the user's role can also edit that page in WordPress. For example, an Editor can edit all pages, while an Author can't edit pages at all, whatever builder capability they have.

## Example: let a client edit text and images {#client-example}

A common setup is a client who keeps names, job titles, and photos up to date without changing the design, in a builder that only shows what she needs. Two settings do this: a builder capability decides what she is allowed to do, and a [builder interface profile](https://academy.bricksbuilder.io/builder/interface/builder-interface-customiser-profiles/) decides what she sees.

1. Create a custom capability, for example "Client editor".
2. Under **Post types**, enable **Pages**.
3. Under **Element editing & styling**, enable **Access content (HTML) settings**. Leave **Access style (CSS) settings** off.
4. Under **Edit elements**, click **Enable all**, so the client can edit the content of every element.
5. Leave everything else off, close the popup, and click **Save Settings**.
6. In the builder, open **Builder interface**. Set **Structure** to **Hidden** and **Element quick access** to **Hide**, remove the toolbar items the client doesn't need, and save the layout as a profile, for example "Client". Both options are available since Bricks 2.5. In earlier versions, minimize the Structure panel with the arrow on its edge instead; the element quick access bar can't be hidden through a profile there.
7. Open the client's WordPress user profile. Under **Builder access**, choose **Client editor**. Under **Builder interface profile**, choose **Client**. Click **Update User**.

![The Bricks section of the client's user profile: Builder access set to Client editor and Builder interface profile set to Client.](https://academy.bricksbuilder.io/assets/bricks-builder-access-user-profile-client.webp)

To give the same setup to every editor instead, choose the capability and the profile for the **Editor** role under **Bricks > Settings > Builder access**.

In the builder, the client sees only the content settings of the selected element. There is nothing to add in the Elements panel, the Structure panel and the element quick access bar are hidden, and the toolbar only shows what the profile keeps.

![The client's builder: a heading selected with only its content settings, no Structure panel or element quick access bar, and a toolbar with only the Bricks logo on the left.](https://academy.bricksbuilder.io/assets/bricks-builder-access-client-builder.webp)

A profile only arranges the workspace. It doesn't restrict anything: a command palette hidden from the toolbar, for example, still opens with its keyboard shortcut. What a user can change is always set by their builder capability.

## Drafts and site versions {#drafts-and-versions}

With [Drafts](https://academy.bricksbuilder.io/builder/interface/drafts/) enabled, users need WordPress permission to edit the page and Bricks access for that page's post type to open its page draft. A page draft can be opened by other users with the same required access; it is not private to its creator.

[Site versions](https://academy.bricksbuilder.io/builder/interface/site-versions/) span multiple pages. Opening or creating them requires Builder access and WordPress permission to edit other users' posts (`edit_others_posts`). Existing Builder permissions still control the actions available inside either kind of draft.

Publishing checks the rights required for all included changes, including page and template settings, shared data, and code execution. Having access to a draft does not grant permission to publish every change someone else added to it.

[Review links](https://academy.bricksbuilder.io/builder/interface/review-links/) provide a separate, view-only preview for people without an editor login. They do not give reviewers Builder access or permission to edit or publish.

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
- Access filter manager (Bricks 2.5)
- Customize builder interface
- Manage builder interface profiles
- Manage global elements (only if legacy Global Elements exist)

**Access filter manager** permits creating, editing, organizing, deleting, importing, and exporting [global filters](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#global-filters). This includes editing shared controls on linked elements. Users without it can select an existing compatible global filter and edit local settings such as the target query and presentation.

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

To keep a user away from global classes, leave the class permissions off. Since Bricks 2.5, this replaces the deprecated **Disable global classes (interface)** builder setting.

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