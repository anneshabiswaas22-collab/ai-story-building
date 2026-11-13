# Build notes

The PNGs, Markdown, JSON, SRT and review HTML can be used directly. Rebuilding is optional. The supplied source scripts use Python 3, Pillow, Inkscape CLI and DejaVu Sans. Font paths are Linux paths and must be adjusted on another system. Run build_package.py, build_learning_assets.py, build_shot_cards.py and build_review_book.py from the project directory. These scripts create documents and static graphics; they do not call Google Flow. Asset generation requires the supplied image prompts and real reference images. No video or audio build script is claimed.

The existing environment supplied the rendering tools. New internet research was not performed for this package.
