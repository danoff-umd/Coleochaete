---
layout: page
title: "Strain Information"
permalink: /strains/
---

Access comprehensive strain IDs, taxonomic lineages, and morphology metadata for our active algae collection. All names given to the strains are strictly to describe what the organism most closely resembles. There is a lot more species diversity than previously expected so genetic data will be necessary in order to properly attribute a name to these organisms. 

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
