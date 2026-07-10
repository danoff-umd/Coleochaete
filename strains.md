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
        <strong><a href="{{ post.url | relative_url }}">{{ post.title }}</a></strong> 
        {% if post.strain_id %}
          — <code>Strain: {{ post.strain_id }}</code>
        {% endif %}
      </li>
    {% endif %}
  {% endfor %}
</ul>
