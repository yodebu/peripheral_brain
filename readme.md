# Chris Albon's Peripheral Brain

There is a concept in the field of medcial education that I have always loved: [the peripheral brain](http://en.wiktionary.org/wiki/peripheral_brain). Like many fields, the amount of medical information — from studies to surgical techniques — a medical student or doctor has to know is massive. The most important information becomes part of our long-term memory, but what about the rest? It goes in a peripheral brain: a repository of all the knowledge that is important, but not important enough to keep in your head.

Like medicine, data science has a staggering amount of information — from linear regression to SQL to causal logic. It is frankly why some of us love this field: there is always something new to learn. Taking a lesson from medicine, [ChrisAlbon.com](http://chrisalbon.com) is my peripheral brain on data science and quantitative political science.

Specifically, it is a colleciton of iPython Notebooks covering everything from web scraping in Python to basic mathematics to statistics. This website is static, each ipynb file is "wrapped" in an html template for styling.

**The workflow for adding posts is as follows:**

1. Write a post in an iPython Notebook.
2. Export the ipynb file to basic html.
3. Paste the header and footer in template.partial above and below the notebook's contents (and change the title), respectively.
4. Add the html file and ipynb file to the appropriate folder.
5. Edit index.html to add a link to the html file.

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

### python | regex | rstats etc

- **template.partial** - A partial file containing the header and footer used to wrap the ipython notebooks.

### scripts/

Scripts used the run the site.

- **html/nb_to_html_all.command** - A script for converting all .pynb files in the current directory into their basic template.
- **html/nb_to_html_single.command** - A script for converting a single .pynb file into its basic template.

### js/

Javascript files.

## Credits

- Ian Devlin for creating [HTML5 Bones](http://www.html5bones.com/)
- [Sebastian Raschka](http://sebastianraschka.com/)
- The whole iPython team.
