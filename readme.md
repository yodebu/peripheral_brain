# Welcome To The Repo For Chris's Blog

In an attempt to combine the wonders of working in iPython with a personal blog, and following a conversation with Sebastian Raschka about it, I decided the best strategy to take would be to create a static html "wrapper" that would be able to take iPython notebook html export files and make them pretty.

The workflow for blogging is as follows:
1. Write a post in an iPython notebook in the blog's repo.
2. Convert the ipython notebook to basic html.
3. Paste the contents of header.partial and footer.partial above and below the notebook contents.
4. Add the file to html/
5. Edit index.html to include a link

## Repo Structure:

- **index.html** - The site's homepage.
- **readme.md** - This file.

### clean-templates/

This is a folder to place the original material used to create the site that might be useful later.

- **clean-templates/ipython_nb_css_raw.css** - The original css file used to style ipython notebooks. This is kept around just in case as reference.
- **clean-templates/main-template-bare-bones.html** - The bare bones html5 template with incredible notes.
- **clean-templates/main-template-no-comments.html** - The bare bones html5 template with no notes.

### css/

- **css/normalize_legacy.css** - A css file to normalize between browsers.
- **css/normalize.css** - A css file to normalize between browsers.
- **css/notebooks.css** - A css file for styling the notebooks get are pasted in.
- **css/styles.css** - A css file to style the site.

### html/
- **html/template.partial** - A partial file containing the header and footer used to wrap the ipython notebooks.
- **html/test.html** - A test post. Might be outdated.
- **html/convert.command** - A short script for converting ipython notebooks into their basic template.

### js/

Javascript... so who knows.

### notebooks/

This folder contains the raw iPython notebook files.

## Credits

- Ian Devlin for creating [HTML5 Bones](http://www.html5bones.com/)
- [Sebastian Raschka](http://sebastianraschka.com/)
- The whole iPython team.
