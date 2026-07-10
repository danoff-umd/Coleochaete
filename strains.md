---
layout: page
title: "Strain Information"
permalink: /strains/
---

Access comprehensive strain IDs, taxonomic lineages, and morphology metadata for our active algae collection.

## Catalogued Strains

<ul>
  {% for post in site.posts %}
    {% if post.tags contains "Strain information" %}
      <li>
        <strong>
          <a href="{{ post.url | relative_url }}">
            {{ post.title }} ({% if post.strain_id %}{{ post.strain_id }}{% else %}No ID{% endif %})
          </a>
        </strong>
      </li>
    {% endif %}
  {% endfor %}
</ul>
