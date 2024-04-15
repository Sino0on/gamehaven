from django import template

from game.models import SiteContent

register = template.Library()


@register.filter(name='multiply')
def multiply(value, arg):
    """Multiplies the value by the arg."""
    return value * arg


@register.simple_tag
def get_or_create_content(original_text):
    # Check if the original text exists in the database
    content, created = SiteContent.objects.get_or_create(original_text=original_text)

    # If it's a new entry, set the current_text to be the same as original_text
    if created:
        content.current_text = original_text
        content.save()

    # Return the current text
    return content.current_text