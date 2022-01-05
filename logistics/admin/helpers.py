from django.utils.safestring import mark_safe
from django.utils import timezone

import string
import random


def create_copy_button(value, N=10):

    random_string = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=N))
    btn_id = 'copy-helper'+random_string
    return mark_safe(f"""
      <input text="hidden" id="{btn_id}" value="{value}" style="display:none;">
      <span>{value}</span>
      <a href="#" onclick="document.querySelector(\'#{btn_id}\').select(); document.execCommand(\'copy\');">Copy</a>
      """
                     )


def create_filter_button(field_name, value, label, N=10):
    return mark_safe(f"""
      <a href="#" onclick="window.location.search = new URLSearchParams('{field_name}__exact={value}').toString();">
        {label}
      </a>
      """
                     )


def format_date(date):

    TODAY = timezone.now()
    delta = (date - TODAY).days

    if delta > 365:
        return f"{(delta / 365)} years ago"
    elif delta > 30:
        return f"{(delta / 30)} months ago"
    elif delta > 7:
        return f"{(delta / 7)} weeks ago"
    else:
        return date.strftime('%H:%M:%S')
