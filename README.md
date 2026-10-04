# davidplanella.org

Hugo source of the blog. Theme: Blowfish (git submodule, pinned to a release).

Build locally with Hugo extended 0.166:

    git clone --recurse-submodules https://github.com/dplanella/blog
    hugo server

Posts are in `content/posts/<slug>/index.md`. English is at the root, Catalan
under `/ca/`.

`tools/ghost-to-hugo.py` is the one-off script that converted the old Ghost
posts.
