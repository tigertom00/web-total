from django.template import Library

register = Library()


# Calculate Total timer per user on each jobb
@register.filter
def running_total(username_list):
    return sum(d.timer for d in username_list)
    # return sum([d.get('timer') for d in username_list])
