# Blog

this is my first serious and very real web application. it's indended as being a web view into my obsidian notes.

## Motivation

The idea evolved. It was originally simply intended as being a web view into my personal notes but it is now intended
to be a fully-blown knowledge base of university courses that i attended to help with the coursework and bridge the
gap between academic validation and actual learning and knowledge.

# Slashes

### Why Django cares

Django follows a convention that most application URLs end with a trailing slash:

```python
path("favorite/", views.favorite)
path("posts/", views.posts)
path("users/", views.users)
```

When `APPEND_SLASH=True`, Django tries to help by redirecting:

```text
/favorite  -> /favorite/
```

for GET requests.

However, for POST requests:

```http
POST /favorite
```

Django can't safely redirect because the request body could be lost, so it raises the error you saw.

# Schema

The top-level container will be a **vault**. It's a themed set of notes inside of which are topics? Or maybe the vautl itself
is the topic? So a better alternative would be chapters? I guess there should be topics inside each vault.

Actually, let's just stick to obsidian terminology instead of overcomplicating it from the start. We'll go with **vaults**,
**Folders**, and **Notes**.

# TODOs

# Questions


