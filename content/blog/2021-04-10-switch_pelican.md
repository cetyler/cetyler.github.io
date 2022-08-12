Title: Switch Website to Pelican
Date: 2021-04-10 14:30
Modified: 2021-04-20 19:30
Category: Blog
Tags: website, pelican, jekyll
Author: Christopher
Summary: Switch from Jekyll to Pelican.
Status: published
comment_id: switch-from-jekyll-to-pelican

## Why I Changed

My initial website was done using the default for GitHub Pages using Jekyll.
Jekyll would probably have been fine but I knew that I wanted to use Jupyter
Notebooks.
Also I know Python a lot more than Ruby so I thought it made sense to make the
change sooner rather than waiting until I have problems with different kinds of
content.

## Changing to Pelican

Initially I used
[Justin Naldzin](https://justinnaldzin.github.io/create-a-website-using-github-pages-and-pelican.html)
blog post but it was not up to date however, it was a good start.
I then went to [Pelican](https://blog.getpelican.com/) and used a combo of both
to get up and going.
After getting the theme to work and trying some test pages, I moved the handful
of my posts and was able to get things to work using `make devserver` and
viewing my website locally.
I did had to add in `pelicanconf.py` the option `BIND = ''` so that I could see
my website on my local network as I work on a remote VM.

## Updating My GitHub Page 

First I open `MakeFile` and do the following:

    DELETE_OUTPUT_DIRECTORY = False

I then do a git submodule of my GitHub Page repo to the `output` folder.
For now I am not using any pre-commits to automatically apply the same commit
message to my git submodule at this time.

Finally I run `make publish` to publish my website and go into the `output`
folder and commit that as well.

## Add Jupyter Notebook Support

I wanted to have the ability to write a post using Jupyter Notebooks.
That way if I had any tables/charts/analysis, I can do everything in the
notebook instead of using Markdown or RestructuredText.

I followed the instructions to install
[Pelican Jupyter](https://github.com/danielfrg/pelican-jupyter).

Now all I need to do is work on my post using Jupyter Notebook and when I
publish, the notebook will be generated as a html page.
This enables me to work on a notebook in a separate directory and I just need to
copy to my `content` folder.
 
## Conclusion

I now have my website to the same level as I had using Jekyll.
I was able to pretty easily add Jupyter Notebook support.